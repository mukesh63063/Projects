*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
Verify Login Page
    Open Browser        ${url}      ${browser}
    Maximize Browser Window
    Sleep   5s  # Wait for page to load
    Input Text    //input[@name='username']    Admin@123
    Sleep   5s
    Close Browser
