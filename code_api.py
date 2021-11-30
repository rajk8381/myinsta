import webbrowser
import requests
import json
import base64
import pkce
code_verifier = pkce.generate_code_verifier(length=128)
code_challenge = pkce.get_code_challenge(code_verifier)
client_id="5B42AC92C94C4B0490C265C97ADA0B9F"
client_secret="S02qLhCQEZvjKql5v9x83tevQ1ZS3sh07cmgR5GgElAhXtDV"
redirect_url = 'https://developer.xero.com/'
scope = 'accounting.transactions accounting.contacts'

auth_url = ('https://login.xero.com/identity/connect/authorize?' +
'response_type=code' +
'&client_id=' + client_id +
'&redirect_uri=' + redirect_url +
'&scope=' + scope +
'&code_challenge=' + code_challenge +
'&code_challenge_method=S256' )

res =webbrowser.open(auth_url)

import requests
def resToken(code):
    exchange_url = 'https://identity.xero.com/connect/token'
    response = requests.post(exchange_url,
               headers={
                   'Content-Type': 'application/x-www-form-urlencoded'
               },
               data={
                  'grant_type': 'authorization_code',
                  'client_id' : client_id,
                  'code': code,
                  'redirect_uri': redirect_url,
                  'code_verifier' : code_verifier
    })
    print(response)
    print(response.text)

code =input('Enter Code')
d=resToken(code)

print(d)
