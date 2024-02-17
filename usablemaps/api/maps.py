import requests


def get_map(dates_coords, zoom):
    params = {
        'll': ','.join(map(str, dates_coords)),
        'spn': ','.join(map(str, [zoom, zoom])),
        'l': 'map'  # sat
    }

    response = requests.get('https://static-maps.yandex.ru/1.x', params=params)

    if not response:
        return None

    return response.content
