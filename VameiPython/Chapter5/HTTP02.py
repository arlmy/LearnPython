import http.client
import re

conn = http.client.HTTPConnection("www.cnblogs.com")
conn.request("GET", "/vamei")
response = conn.getresponse()

print(response.status, response.reason)
content = response.read(300)

pattern = "<meta (*)>"

for line in content:
	m = re.search(pattern, line)
	if m != None:
		print(m.group(1), m.group(2))


#print(content)