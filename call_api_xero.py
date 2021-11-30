import requests
import base64
import webbrowser

client_id="5B42AC92C94C4B0490C265C97ADA0B9F"
client_secret="S02qLhCQEZvjKql5v9x83tevQ1ZS3sh07cmgR5GgElAhXtDV"
redirect_url = 'https://developer.xero.com/'
scope = 'accounting.transactions accounting.contacts'
#
# base_64_id_secret =base64.b64encode(bytes(client_id +':'+ client_secret,'utf-8'))
tokenb4 = f"{client_id}:{client_secret}"
basic_token = base64.urlsafe_b64encode(tokenb4.encode()).decode()
auth_url = ('https://login.xero.com/identity/connect/authorize?' +
    'response_type=code' +
    '&client_id=' + client_id +
    '&redirect_uri=' + redirect_url +
    '&scope=' + scope +
    '&state=123' )

print(auth_url)
ddd =dir(auth_url)
print(ddd)
def get_xero_tenant_id(access_token):
    HEADERS = {
        'Authorization': "Bearer %s" % access_token,
        'Accept': "application/json",
        'Content-Type': "application/json",
    }
    data = requests.get("https://api.xero.com/connections",
                        headers=HEADERS)
    print(data.json())
def getAuthToken(authcode):
    exchange_url = 'https://identity.xero.com/connect/token'
    response = requests.post(exchange_url,
                   headers={"Authorization": "Basic %s" % basic_token,
                            'Content-Type': 'application/x-www-form-urlencoded'
                            },
                   data={
                      'grant_type': 'authorization_code',
                      'client_id' : client_id,
                      'code': authcode,
                      'redirect_uri': redirect_url,

    })
    data =response.json()
    access_token=data.get('access_token')
    return access_token

def getCode(auth_link):
    start_number = auth_link.find('code=') + len('code=')
    end_number = auth_link.find('&scope=')
    authcode = auth_link[start_number:end_number]
    return authcode

def getInvoice(access_token,xero_tenant_id):
    HEADERS={
        'Authorization':"Bearer %s" %access_token,
        'xero-tenant-id':xero_tenant_id,
        'Accept':"application/json",
        'Content-Type':"application/json",
    }
    data =requests.get("https://api.xero.com/api.xro/2.0/Invoices",
        headers=HEADERS)

    return data.json()
webbrowser.open(auth_url)


auth_link =input("Enter Link:")
authcode =getCode(auth_link)
if authcode:
    access_token =getAuthToken(authcode)
    if access_token:
        tenantId="55c2e380-1ca9-4e8c-9e9c-7e7538b6d0d3"
        invoice_data =getInvoice(access_token, tenantId)
        print(invoice_data)










