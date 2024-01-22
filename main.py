import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from datetime import datetime
import requests
import json
import time

# Buscando a Grade

def pegar_grade(ra: int, semana: int):
    now = datetime.now()
    tables = pd.read_html(f'https://minhagrade-ufabc.up.railway.app/?ra={ra}')
    #print(f'Total tables: {len(tables)}')

    #Semana 1
    semana_1 = tables[0]

    #Semana 2
    semana_2 = tables[1]

    semana_1
    #segunda = semana_1["Seg"]

    days = {
        "Seg":"Monday",
        "Ter":"Tuesday",
        "Qua":"Wednesday",
        "Qui":"Thursday",
        "Sex":"Friday"
    }

    semana_1.rename(columns=days,inplace=True)
    semana_2.rename(columns=days,inplace=True)

    formatted_date_time = now.strftime('%A')
    dia = str(formatted_date_time)

    if semana == 1 or semana == 2:
        if semana == 1:
            return str(semana_1[dia][0])+"\n"+str(semana_1[dia][1])
        if semana == 2:
            return str(semana_2[dia][0])+"\n"+str(semana_2[dia][1])
    else:
        return "Semana fora do range 1 || 2"


# Buscar no bot do telegram as mensagens que chegam
    
while True:

    key = '6843390780:AAF1ujROv9KLpKUFZEaJ14D9OH8hc6GdnJ0'
    url = f'https://api.telegram.org/bot{key}/getUpdates'
    response = requests.request("GET", url= url)

    data = json.loads(response.text)
    data["result"][0]["message"]["text"]

    data = json.loads(response.text)

    for mensagem in data["result"]:
        aulas_do_dia = pegar_grade(ra= mensagem["message"]["text"], semana= 1)
        
        url = f'https://api.telegram.org/bot{key}/sendMessage'

        params = {
            "chat_id": mensagem["message"]["chat"]["id"],
            "text": aulas_do_dia
        }

        response = requests.request("GET", url= url,params=params)

        data = json.loads(response.text)
        if data["ok"] == True:
            print("Mensagem Enviada =)")
    
    time.sleep(3)