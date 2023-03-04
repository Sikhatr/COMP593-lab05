from poke_api import get_pokemon_info
from pastebin_api import post_new_paste
import sys

def main():
    search_term = get_search_term()
    abilities_list = get_pokemon_info(search_term)

    if abilities_list:
        title, body_text = get_paste_content(abilities_list, search_term)
        paste_url = post_new_paste(title, body_text, '1M')
        print(f"URL of Pokemon Paste: {paste_url}")

def get_search_term():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        search_term = sys.argv[1]
        return search_term
    else:
        print('Error: Missing search term')
        sys.exit(1)

def get_paste_content(abilities_list, search_term):
    title = f'{search_term}\'s Abilities'

    body_text = ''

    for ability in abilities_list:
        body_text += "- " + ability + '\n'

    return title, body_text

if __name__ == '__main__':
    main()
    