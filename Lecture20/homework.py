import json

import requests

character_url = 'https://rickandmortyapi.com/api/character'
episode_url = 'https://rickandmortyapi.com/api/episode'

char_dict = requests.get(character_url).json()
ep_dict = requests.get(episode_url).json()

def display_characters(dct):
    for data in dct['results']:
        # print(f'{data["name"]} - List of episodes: {data["episode"]}')
        print(data['name'])
        for ep in data['episode']:
            print(f'  {ep}')
        # print('\n')

new_dct = {}
# value_lst = []

def turn_character_into_dict(char_dct, ep_dct):
    for data in char_dct['results']:
        value_lst = []
        for ep in data['episode']:
            for ep1 in ep_dct['results']:
                if ep == ep1['url']:
                    value_lst.append(ep1['name'])
        new_dct[data['name']] = value_lst
    for key, value in new_dct.items():
        print(f'{key}: {value}')

    with open('characters.json', 'w') as json_file:
        json.dump(new_dct, json_file, indent=4)
        # for ep_title in char_dct['results']:
        #     for ep_title1 in ep_dct['results']:
        #         if ep_title['episode'] == ep_title1['url']:
        #             new_dct[data['name']].append(ep_title1['name'])
        # for i in new_dct.items():
        #     print(i)




# display_characters(char_dict)
turn_character_into_dict(char_dict,ep_dict)