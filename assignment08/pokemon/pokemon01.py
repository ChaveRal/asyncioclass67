import requests as requests #libraby get api
import time
import random
from pypokemon.pokemon import Pokemon #in folder pokemon

def get_pokemon(url):
    print(f"{time.ctime()} - get {url}")
    resp = requests.get(url)
    pokemon = resp.json()

    return pokemon
    #6-11 get 1 pokemon by url line8

def get_pokemons():
    rand_list=[]
    for i in range(5):
        rand_list.append(random.randint(1,151))

    pokemon_data = []
    for number in rand_list: #random 5 pokemons
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        pokemon_json = get_pokemon(url)
        pokemon_object = Pokemon(pokemon_json) #sent object to pokemon_object
        pokemon_data.append(pokemon_object) #append in list line19
    return pokemon_data
    #create list of 5 pokemons of 151 pokemons 

def main():
    start_time = time.perf_counter() 
    pokemons = get_pokemons() #check if get 5 pokemons
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Synchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

if __name__ == '__main__':
    main()