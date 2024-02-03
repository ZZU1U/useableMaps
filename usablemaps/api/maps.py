dates_coords = input().split(', ')
dates_move = input().split(', ')
params = {
    'll': ','.join(dates_coords),
    'spn': ','.join(dates_move),
    'l': 'sat'
}
api_server = "http://static-maps.yandex.ru/1.x/"
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
os.remove(map_file_1)