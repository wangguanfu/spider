import requests

res = requests.get("http://www.taobao.com")
# print(res.text)
print(res.encoding)
print(res.headers)

