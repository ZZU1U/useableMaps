import requests


def search_toponym(name_toponym):
    api_server = 'http://geocode-maps.yandex.ru/1.x/'
    params = {
        'geocode': name_toponym,
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'format': 'json'
    }
    response = requests.get(api_server, params=params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        coords = toponym_coodrinates.split(' ')
        # координаты метки, метка должно быть атрибутом класса
        pt[0], pt[1] = coords[0], coords[1]
        # спозиционировать карту на его центральную точку
        dates_coord[0], dates_coord[1] = coords[0], coords[1]
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")


def draw_image_with_pt():
    # c меткой, когда нажатие на кнопку сброса не было
    # pt - атрибут класса
    # добавила параметр метки
    params = {
        'll': ','.join(dates_coords),
        'spn': ','.join(dates),
        'l': 'sat',
        'pt': ','.join(pt)
    }
    # dates_coord, dates - атрибут класса
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


def draw_image_without_pt():
    # без метки, когда нажатие на кнопку сброса не было
    # pt - атрибут класса
    # добавила параметр метки
    params = {
        'll': ','.join(dates_coords),
        'spn': ','.join(dates),
        'l': 'sat',
    }
    # dates_coord, dates - атрибут класса
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

# при нажатии на кнопку вызывать метод draw_image_without_pt
