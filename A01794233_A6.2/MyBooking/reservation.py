"""
Module to create a reservation instance in the system
"""


class Reservation:
    """Metods and attributes for a reservation instance"""

    def __init__(self, reservation_id, number_persons, date):
        """Initializes a reservation object"""
        self.reservation_id = reservation_id
        self.number_persons = number_persons
        self.date = date
        self.active = True

    @staticmethod
    def create_reservation(reservation_id, number_persons, date):
        """Creates a new reservation instance"""
        if number_persons < 0:
            raise ValueError("number_persons can't be negative")
        reservation = Reservation(reservation_id, number_persons, date)
        return reservation

    @staticmethod
    def cancel_reservation(reservation):
        """Cancel a reservation instance"""
        reservation.active = False
