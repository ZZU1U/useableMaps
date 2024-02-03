def change_layout_map(layout):
    # по умолчанию у нас будет спутник sat
    # params - атрибут класса, чтобы в функции draw_image отрисововалось с изменениями
    if layout == 'схема':
        params = {
            'll': ','.join(dates_coords),
            'spn': ','.join(dates),
            'l': 'map'
        }
    elif layout == 'спутник':
        params = {
            'll': ','.join(dates_coords),
            'spn': ','.join(dates),
            'l': 'sat'
        }
    elif layout == 'гибрид':
        params = {
            'll': ','.join(dates_coords),
            'spn': ','.join(dates),
            'l': 'skl'
        }
