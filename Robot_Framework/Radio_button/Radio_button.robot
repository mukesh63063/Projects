*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Varify Radio Button
        Open Browser    ${url}      ${browser}
        Maximize Browser Window
        Sleep   2s
        Click Element   //input[@value='radio1']
        Sleep   2s
        Click Element   //select[@id='dropdown-class-example']
        Sleep   2s
        Click Element   //input[@id='name']
        Input Text  //input[@id='name']     Shubham
        Sleep   2s
        Click Button    //input[@id='confirmbtn']
        Sleep   3s
        Close Browser
