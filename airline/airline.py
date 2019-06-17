from structures import Node, DoubleLinkedList
from datetime import date


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
        self.flights = DoubleLinkedList()

    def add_flight(self, flight):
        """
        Adds a flight to the list
        :param flight:
        :type flight: Flight
        :return: None
        """
        self.flights.append(flight)

    def cancel_flight(self, f_id):
        """
        Removes a flight from the list
        :param f_id:
        :type f_id: str
        :return: None
        """
        return self.flights.remove(f_id, self.flights.head)

    def make_reservation(self, f_id, passenger):
        """

        :param f_id:
        :type f_id: str
        :param passenger:
        :type passenger: Passenger
        :return: the flight the passenger was assigned to
        :rtype: Flight
        """
        flight = self.flights.head
        while flight:
            if flight.id == f_id:
                flight.add_passenger(passenger)
            else:
                flight = flight.next
        return flight

