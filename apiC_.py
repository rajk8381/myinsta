import requests
import base64
def getAccessToken():
    client_id="00C4E70E059849CE9F1EF373C277A3D4"
    client_secret="fFFC8VzSFOIn1RzgmA3SCwbuPS6AXOU80FwvKij8_q-ea_0d"
    redirect_url = 'https://developer.xero.com/'
    scope = 'offline_access accounting.contacts'








# getAccessToken()

def getInvoice():
    HEADERS={
        'Authorization':"Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFDQUY4RTY2NzcyRDZEQzAyOEQ2NzI2RkQwMjYxNTgxNTcwRUZDMTkiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJISy1PWm5jdGJjQW8xbkp2MENZVmdWY09fQmsifQ.eyJuYmYiOjE2Mzc1Njc2NzAsImV4cCI6MTYzNzU2OTQ3MCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS54ZXJvLmNvbSIsImF1ZCI6Imh0dHBzOi8vaWRlbnRpdHkueGVyby5jb20vcmVzb3VyY2VzIiwiY2xpZW50X2lkIjoiNUI0MkFDOTJDOTRDNEIwNDkwQzI2NUM5N0FEQTBCOUYiLCJzdWIiOiJmYzdhYTViMjFiN2M1MzI1ODAxYzhlMjZhZDdiY2VjYyIsImF1dGhfdGltZSI6MTYzNzU2NzY1NCwieGVyb191c2VyaWQiOiIyNDQ2MjRjYy1kNTRkLTQ2ODctYjkyZi1mNzA0MDViYWZjZTEiLCJnbG9iYWxfc2Vzc2lvbl9pZCI6ImJhNjZmYjRmODZlYjQ4YmZhZDQ1NGQ0NDE0Nzc4Zjg0IiwianRpIjoiYzQyN2EwMjAzMzZkNGM1ODVkODRhOGQyNmVlMzRmYTgiLCJhdXRoZW50aWNhdGlvbl9ldmVudF9pZCI6ImMxNWIyYmM3LTUzOTktNDI3MC1iZWQ0LTkzMDRiOWJhMDY2MiIsInNjb3BlIjpbImFjY291bnRpbmcuc2V0dGluZ3MiLCJhY2NvdW50aW5nLnRyYW5zYWN0aW9ucyIsImFjY291bnRpbmcuY29udGFjdHMiLCJvZmZsaW5lX2FjY2VzcyJdfQ.QQNWFX5AKaOCUnAlhwGEcc8yzwtYik8yGqimYGQCl_jlv317U-7JCCcuxEw6o2rHTYK1f_gxExp7RLDfDeU_EntV-aNZhx33vNmeJaTVr1uurW835A4vB2cyHo14vJfFLqn2832B8bQ9-TV5neHtzjosbD5rDF8PhiAsUHFKs7XFLYftzcZEK9uYTcBpUrcSJ8__Ou334zar2wipxtTngA-M8toKlr8zgYwltO6104HQMA-AyFTK7tLC_Kt3AVLTp7bCA2bh-TxzGgV3-4jxyEXIG6tIxjb4pUeBzSn9HNw-w75aD_cVeYvkNjf35B8J7kycPhEpeWzuZJlq17Wbig",
        'xero-tenant-id':"43c87924-ee80-4d6f-bff4-03b89a8f1bc5",
        'Accept':"application/json",
        'Content-Type':"application/json",
    }
    data =requests.get("https://api.xero.com/api.xro/2.0/Invoices",
        headers=HEADERS)
    print(data.text)

client_id="00C4E70E059849CE9F1EF373C277A3D4"
client_secret="fFFC8VzSFOIn1RzgmA3SCwbuPS6AXOU80FwvKij8_q-ea_0d"
redirect_url = 'https://developer.xero.com/'
scope = 'offline_access accounting.contacts'
import requests
exchange_url = 'https://identity.xero.com/connect/token'
response = requests.post(exchange_url,
           headers={
               'Content-Type': 'application/x-www-form-urlencoded'
           },
           data={
              'grant_type': 'authorization_code',
              'client_id' : client_id,
              'redirect_uri': redirect_url,
              })

print(response)

