"""
Module to create a hotel instance in the system
"""

import sys

sys.path.append("/home/jaseco/Documents/MastersDegree_MNA/A01794233_A6.2/")
from MyBooking.reservation import Reservation


class Hotel:
    """Metods and attributes for hotel instance"""

    def __init__(self, name, city, rooms):
        """Initializes a Hotel object"""
        self.name = name
        self.city = city
        self.rooms = rooms

    @staticmethod
    def create_hotel(name, city, rooms):
        """Creates a new hotel instance"""
        if rooms < 0:
            raise ValueError("rooms can't be negative")
        hotel = Hotel(name, city, rooms)
        return hotel

    def delete_hotel(self):
        """Deletes a hotel instance"""
        self.name = None
        self.city = None
        self.rooms = None

    def display_information(self):
        """Returns hotel information"""
        name_inf = "Name: " + self.name
        city_inf = ", City: " + self.city
        rooms_inf = ", Rooms: " + str(self.rooms)
        return name_inf + city_inf + rooms_inf

    def modify_information(self, new_name, new_city, new_rooms):
        """Modifies hotel information"""
        self.name = new_name
        self.city = new_city
        self.rooms = new_rooms

    @staticmethod
    def create_reservation_room(reservation_id, number_persons, date):
        """Create a reservation instance"""
        if number_persons < 0:
            raise ValueError("number_persons can't be negative")
        reservation = Reservation.create_reservation(
            reservation_id, number_persons, date
        )
        return reservation

    @staticmethod
    def cancel_reservation(reservation):
        """Cancel reservation"""
        Reservation.cancel_reservation(reservation)
