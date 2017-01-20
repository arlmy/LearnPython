import http.client
import re

conn = http.client.HTTPConnection("www.cnblogs.com")
conn.request("GET", "/vamei")
response = conn.getresponse()

print(response.status, response.reason)
content = response.read()

content = content.split("\r\n")




print(content)