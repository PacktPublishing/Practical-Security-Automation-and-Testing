ZAP -port 8090

pytest UserRegistration.py --browser=chrome --proxy=127.0.0.1:8090

timeout /T 30

CURL "http://localhost:8090/JSON/ascan/action/scan/?zapapiformat=JSON&formMethod=GET&url=http://hackazon.webscantest.com&recurse=&inScopeOnly=&scanPolicyName=&method=&postData=&contextId="

 timeout /T 30

Curl “http://localhost:8090/HTML/core/view/alerts” > UserRegisterResult.html