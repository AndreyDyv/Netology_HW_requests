import requests

def find_smartest_hero(heroes_list):

    intelligence_dict = {}
    url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(url=url + '/all.json')

    for hero in response.json():
        if hero['name'] in heroes_list:
            intelligence_dict[hero['name']] = hero['powerstats']['intelligence']

    max_intelligence = max(intelligence_dict.values())
    smartest_hero_dict = {k: v for k, v in intelligence_dict.items() if v == max_intelligence}

    return print(f"Показатели intelligence героев: {intelligence_dict}.\n" 
                 f"Самый высокий показатель intelligence у героя {smartest_hero_dict}")

if __name__ == '__main__':

    heroes_list = ['Thanos', 'Hulk', 'Captain America']
    find_smartest_hero(heroes_list)
