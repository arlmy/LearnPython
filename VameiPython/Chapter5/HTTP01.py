import http.client

print(dir(http))

print("\n")

print(dir(http.client))

print("\n")

conn = http.client.HTTPConnection("www.bilibili.tv")
conn.request("GET", "/")
response = conn.getresponse()

print(response.status, response.reason)
content = response.read()
print(content)