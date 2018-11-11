#!/usr/bin/env python
import requests
import json
import sys
from requests.auth import HTTPBasicAuth
import getpass
pwd = getpass.getpass('Password:')
dynamicurl='https://api.github.com/users'
response=requests.get(dynamicurl,auth=HTTPBasicAuth(sys.argv[1],pwd))
print(response)
obj=response.json()
while True:
 for i in range(0,len(obj)):
  with open('output.json', 'a') as f:
   output="loginID:"+str(obj[i]["id"])
   print( output, file=f)
   link=response.headers.get('link',None)
 if link is not None:
       url = link
       dynamicurl=url[1:].split(">")[0]
       print (dynamicurl)
       response=requests.get(dynamicurl,auth=HTTPBasicAuth(sys.argv[1],pwd))
       obj=response.json()
 else:
      print("Check the list of users in output.json under PWD!")
      break

