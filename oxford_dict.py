import json
import requests

"""
app_id="39fac4d8"
app_key="c59826077db901e9b29154ca197fc8a2"
endpoint="entries"
language="en-us"
word=input("Give me some word ")
url=f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{language}/{word.lower()}"


r = requests.get(url,headers={"app_id":app_id, "app_key":app_key})
response=json.dumps(r.json())

res=json.loads(response)

print(res)

"""


response = Unirest.get ("https://wordsapiv1.p.mashape.com/words/soliloquy",
  headers={
    "X-Mashape-Key": "23bcc34235mshe98798926db6241p1561edjsn1df043ebd77b",
    "Accept": "application/json"
  }
)

