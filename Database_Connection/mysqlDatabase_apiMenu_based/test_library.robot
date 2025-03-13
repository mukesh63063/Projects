*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    library    http://127.0.0.1:5000
Test Setup    Setup Test Data

*** Variables ***
${BOOK_ID}    ${EMPTY}  # Will store the ID of the added book

*** Keywords ***
Setup Test Data
    # Add a test book and capture its ID (assuming the API returns the ID in the response)
    ${data}=    Create Dictionary    title=Test Book    author=Test Author    genre=Fiction
    ${response}=    POST On Session    library    /add_book    json=${data}    expected_status=201
    # Since your current API doesn't return the ID, we'll fetch it from /books
    ${books_response}=    GET On Session    library    /books
    ${books}=    Set Variable    ${books_response.json()}
    ${BOOK_ID}=    Set Variable    ${books[0]['id']}  # Get the first book's ID
    Set Suite Variable    ${BOOK_ID}  # Make it available across tests

*** Test Cases ***
Test Get Available Books
    ${response}=    GET On Session    library    /books
    Should Be Equal As Strings    ${response.status_code}    200
    ${books}=    Set Variable    ${response.json()}
    Should Not Be Empty    ${books}

Test Search Books
    ${response}=    GET On Session    library    /search    params=query=Test
    Should Be Equal As Strings    ${response.status_code}    200
    ${books}=    Set Variable    ${response.json()}
    Should Be True    len(${books}) >= 0

Test Borrow Book
    ${response}=    POST On Session    library    /borrow/${BOOK_ID}
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['message']}    Book borrowed successfully

Test Return Book
    # Ensure the book is borrowed first
    POST On Session    library    /borrow/${BOOK_ID}    expected_status=200
    ${response}=    POST On Session    library    /return/${BOOK_ID}
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['message']}    Book returned successfully

Test Add Book
    ${data}=    Create Dictionary    title=New Book    author=New Author    genre=New Genre
    ${response}=    POST On Session    library    /add_book    json=${data}
    Should Be Equal As Strings    ${response.status_code}    201
    Should Be Equal As Strings    ${response.json()['message']}    Book added successfully

Test Update Book
    ${data}=    Create Dictionary    title=Updated Book    author=Updated Author    genre=Updated Genre
    ${response}=    PUT On Session    library    /update_book/${BOOK_ID}    json=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['message']}    Book updated successfully

Test Remove Book
    ${response}=    DELETE On Session    library    /remove_book/${BOOK_ID}
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['message']}    Book removed successfully

Test Login Success
    ${data}=    Create Dictionary    username=admin    password=admin123
    ${response}=    POST On Session    library    /login    json=${data}
    Should Be Equal As Strings    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()['message']}    Login successful

Test Login Failure
    ${data}=    Create Dictionary    username=wrong    password=wrong
    ${response}=    POST On Session    library    /login    json=${data}    expected_status=400
    Should Be Equal As Strings    ${response.status_code}    400
    Should Be Equal As Strings    ${response.json()['error']}    Invalid username or password