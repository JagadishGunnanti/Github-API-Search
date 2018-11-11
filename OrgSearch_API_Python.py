#!/usr/bin/env python
import requests
import json
import sys
dynamicurl='https://api.github.com/search/code?q='+sys.argv[1]+'+in:file+org:JagsOrganization'
response=requests.get(dynamicurl, headers={'Authorization': 'TOK:Token'})
print(response)
obj=response.json()
while True:
 for i in range(0,len(obj["items"])):
  with open('output.json', 'a') as f:
   output="Filename:"+""+obj["items"][i]["path"]+"\n"+"Repository URL:"+obj["items"][i]["repository"]["url"]
   print( output, file=f)
   link=response.headers.get('link',None)
 if link is not None:
       url = link
       dynamicurl=url[1:].split(">")[0]
       response=requests.get(dynamicurl, headers={'Authorization': 'TOK:Token'})
       obj=response.json()
 else:
      print("I am done with searching, please check output.json under PWD for search results!")
      break

