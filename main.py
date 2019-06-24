from airline.airline import City, CityList
from termcolor import cprint, colored
import os

city_list = CityList()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    city = City(name='Manchester', coordinates=(10, 10))
    city2 = City(name='Otro Manchester', coordinates=(50, 40))
    city3 = City(name='Manchester mas lejos', coordinates=(600, 20))

    city_list.add_node(city, city2, 1000)
    city_list.add_node(city, city3, 2000)
    city_list.add_node(city2, city3, 5000)

    print("Bienvenido al sistema de aerolinea")

    menu = show_menu()
    while menu != 0:
        clear()
        handle_menu(menu)
        menu = show_menu()


def handle_menu(option):
    if option == 1:
        return handle_add_city()
    elif option == 2:
        return handle_list_cities()
    elif option == 3:
        return handle_remove_city()


def print_cities():
    for index, city in enumerate(city_list.get_cities_names()):
        print(index + 1, colored(city, "magenta"))


def handle_add_city():
    cprint("Agregar una ciudad:\n", "blue")
    city_name = input("Nombre de la ciudad: ")
    coordinates_x = int(input("Coordenada x de la ciudad: "))
    coordinates_y = int(input("Coordenada y de la ciudad: "))

    cprint("Esta ciudad se conecta con?:", "yellow")
    cities = city_list.get_cities()
    print_cities()

    chosen_city = int(input("Ciudad (indice):"))
    chosen_city_obj = cities[chosen_city-1]

    distance = input("Ingrese la distancia de la ciudad {} a la ciudad {}: ".format(
        city_name, chosen_city_obj.name))

    new_city = City(city_name, (coordinates_x, coordinates_y))

    city_list.add_node(new_city, chosen_city_obj, distance)

    cprint("La ciudad ha sido agregada exitosamente", "green")

    return True


def handle_list_cities():
    cprint("Ciudades disponibles:", "blue", attrs=["bold"])
    print_cities()

    return True


def handle_remove_city():
    cprint("Remover ciudades", "blue", attrs=["bold"])
    print_cities()
    chosen_city = int(input("Indice de la ciudad que desea eliminar: "))
    chosen_city_obj = city_list.get_cities()[chosen_city - 1]

    city_list.remove_city(chosen_city_obj.name)


def show_menu():
    print("""
    =========
    Ciuades
    =========
    1. Agregar una ciudad
    2. Listar ciudades
    3. Remover ciudad
    
    =========
    Vuelos
    =========
    4. Agregar vuelo
    5. Listar vuelos
    6. Remover vuelos
    7. Reservar un asiento en un vuelo
    """)

    option = int(input("Ingrese una opcion: "))

    if option not in range(0, 8):
        return show_menu()
    return option


if __name__ == '__main__':
    main()
