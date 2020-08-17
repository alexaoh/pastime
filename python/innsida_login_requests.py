import requests
from bs4 import BeautifulSoup as bs

url = "https://innsida.ntnu.no"

session = requests.Session()
request = session.get(url)
new_url = request.url
content = bs(request.content, "html.parser")


data = {
    'feidename': '123', 
    'password': '123'
}

auth_req = session.post(new_url, data)
content = bs(auth_req.content,"html.parser")
action = content.find("form")["action"]

SAMLResponse = content.find("input", {"name":"SAMLResponse"})["value"]
RelayState = content.find("input", {"name": "RelayState"})["value"]

auth_data = {
    'SAMLResponse': SAMLResponse,
    'RelayState': RelayState
}

# need to press submit button? 

final_req = session.post(action, auth_data) # Need several of these, since NTNU uses many GET-requests after login!
#print(bs(final_req.content, "html.parser"))

with open('Failed.html', 'w') as file:
    file.write(bs(final_req.content, "html.parser").prettify())

print("done")
