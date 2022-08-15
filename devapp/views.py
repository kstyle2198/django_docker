from lib2to3.refactor import get_fixers_from_package
import aiohttp
from django.shortcuts import render
import time
import requests
import asyncio



def base(request):
    return render(request, 'base.html')


# Synchronous
def dev1(request):    # 약 17~18초 소요됨
    starting_time = time.time()
    pokemon_data = []
    
    for num in range(1, 101):
        url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        res = requests.get(url)
        pokemon = res.json()
        pokemon_data.append([pokemon['name'], pokemon['sprites']['other']['official-artwork']['front_default']])
    
    count = len(pokemon_data)
    total_time = time.time()- starting_time
    
    context = {'data': pokemon_data, 'count': count, 'time': total_time}
    
    return render(request, 'index.html', context)


# Asynchronous
async def dev2(request):     # 약 6~7초 소요
    starting_time = time.time()
    pokemon_data = []
    
    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            async with session.get(url) as res:
                pokemon = await res.json()
                pokemon_data.append([pokemon['name'], pokemon['sprites']['other']['official-artwork']['front_default']])
    count = len(pokemon_data)
    total_time = time.time() - starting_time
    context = {'data': pokemon_data, 'count': count, 'time': total_time}
    return render(request, 'index.html', context)


# asyncio.gather() run coroutines concurrently
async def get_data(session, url):
    async with session.get(url) as res:
        pokemon_data = await res.json()
        return pokemon_data

async def dev3(request):    # 약 1~2초 소요
    starting_time = time.time()
    
    actions =[]
    pokemon_data =[]
    
    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            actions.append(asyncio.ensure_future(get_data(session, url)))
            # print(actions)
        pokemon_res = await asyncio.gather(*actions)
        for pokemon in pokemon_res:
            pokemon_data.append([pokemon['name'], pokemon['sprites']['other']['official-artwork']['front_default']])
            # print(pokemon)
        
    count = len(pokemon_data)
    total_time = time.time() - starting_time
    context = {'data': pokemon_data, 'count': count, 'time': total_time}
    return render(request, 'index.html', context)

