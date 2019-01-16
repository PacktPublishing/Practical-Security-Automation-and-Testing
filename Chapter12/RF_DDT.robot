*** Settings ***
Library           Collections
Library           CSVLibrary
Library           SeleniumLibrary
Library           OperatingSystem
Library           String
Library           Collections

*** Test Cases ***
SignIn_DDT
    Open Browser    http://nodegoat.herokuapp.com/login
    @{data}=    read csv file to list    sqli.csv
    Log    ${data}
    :FOR    ${x}    IN    @{data}
    \    Log    ${x}
    \    Input Text    id=userName    ${x[${0}]}
    \    Input Text    id=password    ${x[${1}]}
    \    Click Button    xpath=//button[@type='submit']
    \    Log    ${x[${0}]}
    \    Log    ${x[${1}]}
    Close Browser
