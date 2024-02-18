"""
Module to test hotel class
"""

import unittest
import sys

sys.path.append("/home/jaseco/Documents/MastersDegree_MNA/A01794233_A6.2/")
from MyBooking.hotel import Hotel


class CustomerTest(unittest.TestCase):
    """Test metods for hotel class"""

    def setUp(self):
        print("SETUP Called...")
        # Arrange
        self.name = "Hotel"
        self.city = "City"
        self.rooms = 5

        self.reservation_id = "22222"
        self.number_persons = 7
        self.date = "03/15/2024"

    def test_create_hotel(self):
        """Test create_hotel method"""
        print("TEST - 1 Called...")

        # Act
        hotel = Hotel.create_hotel(self.name, self.city, self.rooms)

        # Assert
        self.assertEqual(hotel.name, self.name)
        self.assertEqual(hotel.city, self.city)
        self.assertEqual(hotel.rooms, self.rooms)

    def test_delete_hotel(self):
        """Test delete_hotel method"""
        print("TEST - 2 Called...")

        # Arrange
        hotel = Hotel(self.name, self.city, self.rooms)

        # Act
        hotel.delete_hotel()

        # Assert
        self.assertIsNone(hotel.name)
        self.assertIsNone(hotel.city)
        self.assertIsNone(hotel.rooms)

    def test_display_information(self):
        """Test display_information method"""
        print("TEST - 3 Called...")

        # Arrange
        message = "Name: Hotel, City: City, Rooms: 5"
        hotel = Hotel(self.name, self.city, self.rooms)
        print(hotel.display_information())

        # Act && Assert
        self.assertEqual(hotel.display_information(), message)

    def test_modify_information(self):
        """Test modify_information method"""
        print("TEST - 4 Called...")

        # Arrange
        hotel = Hotel(self.name, self.city, self.rooms)
        new_name = "HH, VV"
        new_city = "ZZ"
        new_rooms = 9

        # Act
        hotel.modify_information(new_name, new_city, new_rooms)

        # Assert
        self.assertEqual(hotel.name, new_name)
        self.assertEqual(hotel.city, new_city)
        self.assertEqual(hotel.rooms, new_rooms)

    def test_create_reservation_room(self):
        """Test create_reservation_room method"""
        print("TEST - 4 Called...")

        # Act
        reservation = Hotel.create_reservation_room(
            self.reservation_id, self.number_persons, self.date
        )

        # Assert
        self.assertEqual(reservation.reservation_id, self.reservation_id)
        self.assertEqual(reservation.number_persons, self.number_persons)
        self.assertEqual(reservation.date, self.date)

    def test_cancel_reservation(self):
        """Test cancel_reservation"""
        print("TEST - 4 Called...")

        # Arrange
        reservation = Hotel.create_reservation_room(
            self.reservation_id, self.number_persons, self.date
        )

        # Act
        Hotel.cancel_reservation(reservation)

        # Assert
        self.assertFalse(reservation.active)

    # Exception handler test
    def test_negative_rooms(self):
        """Test negative rooms"""
        print("TEST - 5 Called...")

        # Act & Assert
        self.assertRaises(
            ValueError,
            Hotel.create_hotel,
            self.name,
            self.city,
            -1,
        )

    # Exception handler test
    def test_create_reservation_room_with_negative_values(self):
        """Test create_reservation with negative values"""
        print("TEST - 6 Called...")

        # Act & Assert
        self.assertRaises(
            ValueError,
            Hotel.create_reservation_room,
            self.reservation_id,
            -1,
            self.date,
        )


if __name__ == "__main__":
    unittest.main()
