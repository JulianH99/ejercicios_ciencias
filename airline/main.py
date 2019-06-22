from airline.airline import *

city = City(name='Manchester', coordinates=(10, 10))
city2 = City(name='Otro Manchester', coordinates=(50, 40))
city3 = City(name='Manchester mas lejos', coordinates=(600, 20))


city_list = CityList()

city_list.add_node(city, city2, 1000)
city_list.add_node(city, city3, 2000)
city_list.add_node(city2, city3, 5000)

if __name__ == '__main__':
    pass
