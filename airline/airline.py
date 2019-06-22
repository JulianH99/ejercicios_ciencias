from airline.structures import Node
from datetime import date
from typing import Dict


class City:
    def __init__(self, name, coordinates):
        """

        :param name:
        :type name: str
        :param coordinates:
        :type coordinates: (int, int)
        """

        self.name = name
        self.coordinates = coordinates


class CityList:
    def __init__(self, cities=None):
        """

        :param cities:
        :type cities: Dict[(City, City), int]
        """
        if cities is None:
            cities = {}
        self.cities = cities

    def add_node(self, city_from, city_to, distance):
        """

        :param city_from:
        :type city_from: City
        :param city_to:
        :type city_to: City
        :param distance:
        :type distance: int
        :return:
        """
        self.cities[(city_from, city_to)] = distance


class Passenger:
    def __init__(self, name, id_number):
        """

        :param name:
        :type name: str
        :param id_number:
        :type id_number: str
        """
        self.name = name
        self.id_number = id_number


class Seat:
    def __init__(self, row, column):
        """

        :param row:
        :type row: int
        :param column:
        :type column: str
        """
        self.row = row
        self.column = column
        self.busy = False
        self.passenger = None

    def make_busy(self):
        self.busy = True

    def un_busy(self):
        self.busy = False

    def set_passenger(self, passenger):
        """

        :param passenger:
        :type passenger: Passenger
        :return:
        """
        self.passenger = passenger


class Airplane:
    def __init__(self, ap_id):
        self.id = ap_id
        self.seats = self.__gen_seats()

    @staticmethod
    def __gen_seats():
        return [Seat(r, c) for r in range(1, 6) for c in ['a', 'b', 'c']]

    def get_seat(self, sea_info):
        """
        returns a seat based on column and row
        :param sea_info:
        :type sea_info: (int, str)
        :return:
        """

        seats = list(filter(lambda s: s.row == sea_info[0] and s.column == sea_info[1], self.seats))

        if not seats:
            return None
        else:
            return seats[0]



class Flight(Node):
    def __init__(self, cfrom, cto, plane, code, arrival_date, departure_date):
        """

        :param cfrom:
        :type cfrom: City
        :param cto:
        :type cto: City
        :param plane:
        :type plane: Airplane
        :param code:
        :type code: str
        :param arrival_date:
        :type arrival_date: date
        :param departure_date:
        :type departure_date: date
        """
        super().__init__()
        self.cfrom = cfrom
        self.cto = cto
        self.plane = plane
        self.code = code
        self.arrival_date = arrival_date
        self.departure_date = departure_date

    def add_passenger(self, passenger, seat_info):
        """

        :param passenger: new passenger in flight
        :type passenger: Passenger
        :param seat_info: seat of the new passenger
        :type seat_info: (int, char)
        :return:
        """
        def map_seat(seat):
            """

            :param seat:
            :type seat: Seat
            :return: Seat
            """
            if seat.row == seat_info[0] and seat.column == seat_info[1]:
                seat.busy = True
                seat.passenger = passenger
            return seat

        self.plane.seats = list(map(map_seat, self.plane.seats))


class Airline:
    def __init__(self):
        self.head_flight: Flight = None

    def add_flight(self, flight):
        """
        Adds a flight to the list
        :param flight:
        :type flight: Flight
        :return: None
        """
        if self.head_flight is None:
            self.head_flight = flight
        else:
            self.__add_flight_on_time(self.head_flight, flight)

    @staticmethod
    def __add_flight_on_time(prev_flight, flight):
        if prev_flight.next is None:
            prev_flight.next = flight
            flight.prev = prev_flight
            return flight
        elif prev_flight.departure_date == flight.departure_date:
            flight.next = prev_flight.next
            prev_flight.next.prev = flight
            flight.prev = prev_flight
            prev_flight.next = flight
            return flight
        else:
            return Airline.__add_flight_on_time(prev_flight.next, flight)

    def cancel_flight(self, f_id):
        """
        Removes a flight from the list
        :param f_id:
        :type f_id: str
        :return: None
        """
        head = self.head_flight
        while head:
            if head.id == f_id:
                break
            else:
                head = head.next

        if head:
            head.prev.next = head.next
            head.next.prev = head.prev

        return head

    def make_reservation(self, f_id, passenger, seat_info):
        """

        :param f_id:
        :type f_id: str
        :param passenger:
        :type passenger: Passenger
        :return: the flight the passenger was assigned to
        :param seat_info: Seat information
        :type seat_info: (int, str)
        :return: updated flight
        :rtype: Flight
        """
        flight = self.head_flight
        while flight:
            if flight.id == f_id:
                seat = flight.plane.get_seat(seat_info)
                if seat and not seat.busy:
                    flight.add_passenger(passenger, seat_info)
                else:
                    return None
            else:
                flight = flight.next
        return flight

    def list_flights(self):
        flight = self.head_flight
        while flight:
            print(flight)
            flight = flight.next

