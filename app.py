import requests
import json
from translate import Translator # type: ignore

# Translator
translator = Translator(to_lang='pt')

# Url Api Avatar para buscar personagens
api_url = 'https://last-airbender-api.fly.dev/api/v1/characters'

# Buscando uma reposta através do método GET
response = requests.get(api_url)
#print(json.dumps(response.json(), indent=4))
data = json.loads(json.dumps(response.json()))

# Lista Traduzida :  Nome e Afiliação
print(f'{'Nome'.ljust(25)} | {'Afiliação'.ljust(25)}')
for personagem in data :
    print(f'{translator.translate(personagem.get('name', '')).ljust(25)} | {translator.translate(personagem.get('affiliation', 'Não Possui')).ljust(25)}')
