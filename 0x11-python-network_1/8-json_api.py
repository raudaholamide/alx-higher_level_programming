#!/usr/bin/python3
""" Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ""}

    if len(argv) == 2:
        letter = argv[1]
        values['q'] = letter
        r = requests.post(url, data=values)
    else:
        r = requests.post(url, data=values)
    try:
        json_dic = r.json()
        if json_dic:
            print('[{}] {}'.format(json_dic.get('id'), json_dic.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
