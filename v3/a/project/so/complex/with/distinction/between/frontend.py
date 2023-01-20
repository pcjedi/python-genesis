from backend import complexstuff
import requests

print(requests.get("http://ip.jsontest.com/").json())
print(complexstuff)
