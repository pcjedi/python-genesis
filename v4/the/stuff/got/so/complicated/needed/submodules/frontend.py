from backend import complexstuff
from backend.beneath import makeitrain
import requests

print(requests.get("http://ip.jsontest.com/").json())
print(complexstuff)
makeitrain()
