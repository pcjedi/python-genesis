from stuff import complexstuff
from stuff.beneath import makeitrain
import requests

print(requests.get("http://ip.jsontest.com/").json())
print(complexstuff)
makeitrain()
