import requests
import logging


def get_map(dates_coords, zoom):
    params = {
        'll': ','.join(map(str, dates_coords)),
        'z': zoom,
        'l': 'map'  # sat
    }

    response = requests.get('https://static-maps.yandex.ru/1.x', params=params)

    if not response:
        logging.error(response.url)
        logging.error(response.status_code)
        return None

    return response.content
