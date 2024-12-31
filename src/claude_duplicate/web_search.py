import requests

def search(query):
    '''Execute web search'''
    response = requests.get(f'https://api.search.com?q={query}')
    return response.json()