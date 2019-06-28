from airline.airline import City, CityList, Airplane, Airline, Flight, Passenger
from termcolor import cprint, colored
from datetime import datetime
from base64 import b64encode
import random
import string
import os

city_list = CityList()
airline = Airline()

airplane1 = Airplane('airplane1')
airplane2 = Airplane('airplane2')

airline.add_airplane(airplane1)
airline.add_airplane(airplane2)


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
        handle_add_city()
    elif option == 2:
        handle_list_cities()
    elif option == 3:
        handle_remove_city()
    elif option == 4:
        handle_add_flight()
    elif option == 5:
        airline.list_flights()
    elif option == 6:
        handle_remove_flight()
    elif option == 7:
        handle_reserve_seat()
    elif option == 8:
        handle_detail_flight()

# #region cities


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


def handle_list_cities():
    cprint("Ciudades disponibles:", "blue", attrs=["bold"])
    print_cities()


def handle_remove_city():
    cprint("Remover ciudades", "blue", attrs=["bold"])
    print_cities()
    chosen_city = int(input("Indice de la ciudad que desea eliminar: "))
    chosen_city_obj = city_list.get_cities()[chosen_city - 1]

    city_list.remove_city(chosen_city_obj.name)

# #endregion


def handle_add_flight():
    cprint("Elija la ciudad de partida", "yellow")
    print_cities()
    city_1 = int(input(">: "))
    cprint("Elija la cidad de destino", "yellow")
    city_2 = int(input(">: "))
    cprint("Elija el avión asignado al vuelo")
    for index, airplane in enumerate(airline.airplanes):
        print(index + 1, colored(airplane.id, "magenta"))
    airplane_id = int(input(">: "))
    cprint("Fecha de salida (DD/MM/YYYY HH:mm):", "yellow")
    out_date = input(">: ")
    cprint("Fecha de entrada (DD/MM/YYYY HH:mm):", "yellow")
    arri_date = input(">: ")

    flight = Flight(city_list.get_cities()[city_1-1],
                    city_list.get_cities()[city_2-1],
                    airline.airplanes[airplane_id-1],
                    ''.join(random.choices(
                        string.ascii_uppercase + string.digits, k=4)),
                    datetime.strptime(arri_date, "%d/%m/%Y %H:%M"),
                    datetime.strptime(out_date, "%d/%m/%Y %H:%M"))

    airline.add_flight(flight)

    cprint("Vuelo agregado", "green")


def handle_remove_flight():
    cprint("Lista de vuelos", "blue")
    airline.list_flights()
    cprint("Elija el vuelo a cancelar", "yellow")
    flight_id = input(">: ")

    airline.cancel_flight(flight_id)

    cprint("Vuelo cancelado", "green")


def handle_reserve_seat():
    cprint("Realizar reserva", "blue")

    cprint("Escoja el vuelo", "yellow")
    airline.list_flights()
    flight_code = input(">: ")
    cprint("Ingrese su nombre", "yellow")
    name = input(">: ")
    cprint("Ingrese su número de documento", "yellow")
    document = input(">: ")

    passenger = Passenger(name, document)

    flight = airline.get_flight(flight_code)

    cprint("Asientos", "blue")
    for index, seat in enumerate(flight.plane.seats):
        print(index + 1, seat)

    seat = int(input(">: "))
    chosen_seat = flight.plane.seats[seat - 1]
    seat_info = (chosen_seat.row, chosen_seat.column)

    airline.make_reservation(flight_code, passenger, seat_info)


def handle_detail_flight():
    cprint("Ver detalles de vuelo", "blue")
    airline.list_flights()
    cprint("Ingrese el id del vuelo", "yellow")
    flight_id = input(">: ")
    flight = airline.get_flight(flight_id)

    print(""" 
    -Código de vuelo: {}
    -Ciudad de partida: {}
    -Ciudad de llegada: {}
    -Hora de partida: {}
    -Hora de llegada: {}
    """.format(flight.code, 
                flight.cfrom, 
                flight.cto, 
                flight.departure_date, 
                flight.arrival_date)
    )

    cprint("Sillas disponibles", "blue")
    for index, seat in enumerate(flight.plane.seats):
        if not seat.busy:
            print(index + 1, seat)


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
    8. Ver detalles de vuelo


    """)

    option = int(input("Ingrese una opcion: "))

    if option not in range(0, 9):
        return show_menu()
    return option


if __name__ == '__main__':
    main()
