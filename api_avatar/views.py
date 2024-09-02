from django.shortcuts import render
import requests

def index(request):
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

    response = requests.get(api_url).json()

    lista=[]
    for dict in response:
        for item in dict:
            
            chave = dict[item]

            if isinstance(dict[item], str):
                linha=f'{item} : {(chave)}'

            if isinstance(dict[item], list):
                chave = ''.join([i for i in chave]) + ','
                chave = chave[:-1]
                linha=f'{item} : {(chave)}'

            lista.append(linha)
        lista.append("")

    return render(request, 'index.html', {'dados':response})
