import requests


def map_zoom(dates_coords, dates_move):
    dates = [dates_move, dates_move]
    params = {
        'll': ','.join(dates_coords),
        'spn': ','.join(dates),
        'l': 'sat'
    }
    response = requests.get(api_server, params=params)
    # elif PgDown убавляем
    dates = [dates_move - zoom_map / 111, dates_move]
    params = {
        'll': ','.join(dates_coords),
        'spn': ','.join(dates),
        'l': 'sat'
    }
    response = requests.get(api_server, params=params)
    if response:
        pass
    else:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file_1 = "map.png"
    with open(map_file_1, "wb") as file:
        file.write(response.content)
