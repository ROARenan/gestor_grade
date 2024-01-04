import requests
import json

#Criando e embaralhando o deck
url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
params = {}
header = {}

response = requests.request("GET",url=url,headers = header, params = params)
dados = json.loads(response.text)
print("Resposta:\n", dados)

#Comprando uma carta
url = f'https://www.deckofcardsapi.com/api/deck/{dados["deck_id"]}/draw/?count=1'
params = {}
header = {}

response = requests.request("GET",url=url,headers = header, params = params)
carta = response.text
print(" Resposta:", carta)