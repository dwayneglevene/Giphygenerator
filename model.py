import requests
def getImageUrlFrom(query,key):
    endpoint =f'https://api.giphy.com/v1/gifs/search?api_key={key}&q={query}&limit=25&offset=0&rating=g&lang=en'
    response = requests.get(endpoint).json()
    return response['data'][0]['images']['fixed_height']['url']