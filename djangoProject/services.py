"""
import requests


def get_data():
    response = requests.get('https://apps.who.int/gho/athena/api/GHO/MH_12.json?profile=simple&filter=YEAR:2017')
    data = response.json()
    data_list = []
    for i in range(len(data['fact'])):
        if len(data['fact'][i]['dim']) == 6:
            data_list.append(data['fact'][i])
    return data_list
"""
