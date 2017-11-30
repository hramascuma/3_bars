import sys
import json
import numpy as np


def load_data(filepath):
    try:
        json_content = json.load(open(filepath))
    except FileNotFoundError:
    	print('Не найден файл')
    	sys.exit(1)

    coordinates = [] 
    seats_count = []
    #извлечение координат (coordinates) и количества мест (seats_count) из json_content
    for i in range(len(json_content['features'])):
        coordinates.append(json_content['features'][i]['geometry']
                                       ['coordinates'])
        seats_count.append(json_content['features'][i]['properties']
                                       ['Attributes']['SeatsCount'])
    return json_content, coordinates, seats_count

#создание списка с дистанцией между координатами каждого бара и пользовательскими (longitude, latitude) 
def bars_with_distance(longitude, latitude, coordinates):
    list_with_distance = []
    #расчет эвклидова расстояния (т.к. расстояния не болшие, кривизна поверхности не учитывается)
    for coordinates_for_each in coordinates:
        dist_for_each = ((float(coordinates_for_each[0]) - longitude) ** 2 +
                         (float(coordinates_for_each[1]) - latitude) ** 2) ** 0.5
        list_with_distance.append(dist_for_each)
    return list_with_distance

#создает список идексов с искомым значением
def get_index(sought_value, list_of_values):
    searched_values = np.array([sought_value])
    list_of_values = np.array([list_of_values])
    return np.where((list_of_values==searched_values))[1]


def get_closest(json_content, longitude, latitude):
    list_with_distance = bars_with_distance(longitude, latitude, coordinates)
    print(
        json.dumps(
            json_content['features'][list_with_distance.index( 
                                     min(list_with_distance))],
			sort_keys=True,
			indent=4,
			ensure_ascii=False
		)
	)
    print('Данные закончились')


def get_biggest_bar(json_content):
    list_with_index_max = get_index(max(seats_count), seats_count)
    #итерирует список индексов с максимальным значением и выводит по одному
    #на экран информацию по бару по соответствующему индексу
    for index_max_for_each in list_with_index_max:
        print('По вашим запросы найдено {} бар кафе с количеством мест - {}'
           	  .format(len(list_with_index_max), max(seats_count)))
        input('Для поочеоедного вывода нажмите "enter"')
        print(
            json.dumps(
                (json_content['features'][index_max_for_each]),
                sort_keys=True,
                indent=4,
                ensure_ascii=False
                )
            )
        print('Данные закончились')


def get_smallest_bar(json_content):
    list_with_index_min = get_index(min(seats_count), seats_count)
    #итерирует список индексов с минимальным значением и выводит по одному
    #на экран информацию по бару по соответствующему индексу
    for index_min_for_each in list_with_index_min:
        print('По вашим запросы найдено {} бар кафе с количеством мест - {}'
              .format(len(list_with_index_min), min(seats_count)))
        input('Для поочередного вывода нажмите "enter"')
        print(
            json.dumps(
                (json_content['features'][index_min_for_each]),
                sort_keys=True,
                indent=4,
                ensure_ascii=False
                )
            )
        print('Данные закончились')


def get_choice():
    #Общение с пользователем и запись его выбора 
    #для дальнешего принятия решения программы.
    #Фильтр введенных символов.
    try:
        choice = int(input("""
1 - вывести ближайший бар
2 - вывести самый маленький бар
3 - вывести самый большой бар
0/Ctrl+C - выход из программы
Ваш выбор: """))
    except KeyboardInterrupt: 
         sys.exit(1)
    except ValueError:
        print('Неверное значение')
        sys.exit(1)
    return choice

def get_my_coordinates():
    try:
        longitude = float(input('Введите долготу: '))
        latitude = float(input('Введите широту: '))
    except ValueError:
        print('Неверные значения.')
        sys.exit(1)
    return longitude, latitude

if __name__ ==  '__main__':
    filepath = input('Введите полный путь до базы данных: ')
    json_content, coordinates, seats_count = load_data(filepath)
    choice = get_choice()
    #фильт неверных числа
    if choice == 0 or choice > 3 or choice < 0:
        sys.exit(1)
    #запись с клавиатуры координат пользователя
    #вывод всей информации по блажайшему бару
    if choice == 1:
        longitude, latitude = get_my_coordinates()
        get_closest(json_content, longitude, latitude)
    #вывод самого маленького бара
    if choice == 2:
        get_smallest_bar(json_content)
    #вывод самого большого бара
    if choice == 3:
        get_biggest_bar(json_content)
