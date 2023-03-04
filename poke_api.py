import requests

POKEMON_SEARCH_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    abilities = get_pokemon_info('3')
    pass

def get_pokemon_info(search_term):
    """Get the abilities for the specified pokemon

    Args:
        search_term (str): Name of Pokemon or PokeDex number

    Returns:
        list: List of ability. None if failed
    """

    # clean the search term
    search_term = str(search_term).strip().lower()

    #creating clean url for the search term
    CLEAN_POKEMON_SEARCH_URL = POKEMON_SEARCH_URL + search_term


    print(f'Getting information for {search_term}...', end='')
    resp_msg = requests.get(CLEAN_POKEMON_SEARCH_URL)

    # Check whether the request was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        ability_portion = body_dict['abilities']
        ability_list = [j['ability']['name'] for j in ability_portion]
        return ability_list
    else:
        print("failure")
        print(f"respose code: {resp_msg.status_code} ({resp_msg.reason})")

if __name__ == '__main__':
    main()