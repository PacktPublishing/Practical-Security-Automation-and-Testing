*** Settings ***
Suite Teardown    Delete All Sessions
Library           Collections
Library           String
Library           RequestsLibrary
Library           OperatingSystem

*** Variables ***
${url}            http://demo.testfire.net
${SpiderScan}     http://localhost:8090/JSON/spider/action/scan/?zapapiformat=JSON&formMethod=GET&url=${url}&maxChildren=&recurse=&contextName=&subtreeOnly=

*** Test Cases ***
ZAP Spider Scan
    [Tags]    get    skip
    Create Session    ZAP    ${SpiderScan}
    ${resp}=    Get Request    ZAP    /
    Should Be Equal As Strings    ${resp.status_code}    200
    Create Session    ZAP    http://localhost:8090/HTML/core/view/alertsSummary/?zapapiformat=HTML&formMethod=GET&baseurl=
