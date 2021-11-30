import requests


access_token="15034deff220ec38227d187f18f78b62df0fb4fc"
HEADERS = {
        'Authorization': "token %s" % access_token,
        'Content-Type': "application/json",
    }
data =requests.get("http://127.0.0.1:8000/api/user/", headers=HEADERS)
print(data.text)