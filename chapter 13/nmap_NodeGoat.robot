*** Settings ***
Library         Process

*** Test Cases ***
Testing if the website was previously reported XSS
     ${result} =       Run Process        nmap  -p80  --script  http-xssed  nodegoat.kerokuapp.com
     Log               ${result.stdout}
     Should Contain    ${result.stdout}   No previously reported