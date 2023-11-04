import json 
import requests 
import sys

if len(sys.argv) != 2:
   sys.exit()

response = requests.get("http://universities.hipolabs.com/search?country=United+States&name=" + sys.argv[1])
#print(json.dumps(response.json(), indent = 3))
college = response.json()
for i in college:     
    print("University Name: ", i["name"])
    print("University Website: ", i["web_pages"])
    print("University County: ", i["country"])


