import sys
import json
import numpy as np

def load_data(filepath):
	data = json.load(open(filepath))
	coordinates = [] 
	seats_count = []
	#извлечение координат (coordinates) и количества мест (seats_count) из data
	for i in range(len(data['features'])):
		coordinates.append(data['features'][i]['geometry']['coordinates'])
		seats_count.append(data['features'][i]['properties']['Attributes']
		   				   ['SeatsCount'])
	return data, coordinates, seats_count

#создание списка с дистанцией между координатами каждого бара и пользовательскими (longitude, latitude) 
def bars_with_distance(longitude, latitude, coordinates):
	list_with_distance = []
	#расчет эвклидова расстояния (т.к. расстояния не болшие, кривизна поверхности не учитывается)
	for coordinates_for_i in coordinates:
		dist_for_i = ((float(coordinates_for_i[0]) - longitude) ** 2 +
				      (float(coordinates_for_i[1]) - latitude) ** 2) ** 0.5
		list_with_distance.append(dist_for_i)
	return list_with_distance

#создает список идексов с искомым значением
def get_index(sought_value, list_of_values):
	searched_values = np.array([sought_value])
	list_of_values = np.array([list_of_values])
	return np.where((list_of_values==searched_values))[1]

def get_closest(data, longitude, latitude):
	list_with_distance = bars_with_distance(longitude, latitude, coordinates)
	print(
		json.dumps(
			data['features'][list_with_distance.index( 
							 min(list_with_distance))],
			sort_keys=True,
			indent=4,
			ensure_ascii=False
		)
	)
	print('Данные закончились')

def get_biggest_bar(data):
	list_with_index_max = get_index(max(seats_count), seats_count)
	#итерирует список индексов с максимальным значением и выводит по одному
	#на экран информацию по бару по соответствующему индексу
	for index_max_for_i in list_with_index_max:
		print('По вашим запросы найдено {} бар кафе с кол-м мест - {}'
		   	  .format(len(list_with_index_max), max(seats_count)))
		input('Для поочеоедного вывода нажмите "enter"')
		print(
			json.dumps(
				(data['features'][index_max_for_i]),
				sort_keys=True,
				indent=4,
				ensure_ascii=False
				)
			)
		print('Данные закончились')

def get_smallest_bar(data):
	list_with_index_min = get_index(min(seats_count), seats_count)
	#итерирует список индексов с минимальным значением и выводит по одному
	#на экран информацию по бару по соответствующему индексу
	for index_min_for_i in list_with_index_min:
		print('По вашим запросы найдено {} бар кафе с кол-м мест - {}'
		 	  .format(len(list_with_index_min), min(seats_count)))
		input('Для поочередного вывода нажмите "enter"')
		print(
			json.dumps(
				(data['features'][index_min_for_i]),
				sort_keys=True,
				indent=4,
				ensure_ascii=False
				)
			)
		print('Данные закончились')


if __name__ ==  '__main__':
	filepath = input('Введите полный путь до базы данных: ')
	data, coordinates, seats_count = load_data(filepath)
	
	#Jбщение с пользователем и запись его выбора 
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

	#фильт неверных числа
	if choice == 0 or choice > 3 or choice < 0:
		sys.exit(1)
	
	#запись с клавиатуры координат пользователя
	#вывод всей информации по блажайшему бару
	if choice == 1:
		try:
			longitude = float(input('Введите долготу: '))
			latitude = float(input('Введите широту: '))
		except:
			print('Неверные значения.')
			sys.exit(1)
		get_closest(data, longitude, latitude)
	
	#вывод самого маленького бара
	if choice == 2:
		get_smallest_bar(data)
	
	#вывод самого большого бара
	if choice == 3:
		get_biggest_bar(data)
