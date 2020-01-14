from urllib.request import Request, urlopen

req = Request('http://www.google.co.kr')
response = urlopen(req)
print(response.status)
