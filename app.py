import requests

# Url Api Avatar para buscar personagens
api_url = 'https://last-airbender-api.fly.dev/api/v1/characters'

# Buscando uma reposta através do método GET
response = requests.get(api_url)
print(response.json())