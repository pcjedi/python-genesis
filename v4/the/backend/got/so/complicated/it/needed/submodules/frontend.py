import backend
from backend import complexstuff
from backend.beneath import makeitrain
import requests

print(requests.get("http://ip.jsontest.com/").json())
print(complexstuff)
backend.beneath.whoami()
makeitrain(duration=0.01)
backend.beneath.whoami()
print("my name is: ", __name__)
