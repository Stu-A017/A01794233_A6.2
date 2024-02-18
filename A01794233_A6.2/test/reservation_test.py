"""
Module to test reservation class
"""

import unittest
import sys

sys.path.append("/home/jaseco/Documents/MastersDegree_MNA/A01794233_A6.2/")
from MyBooking.reservation import Reservation


class ReservationTest(unittest.TestCase):
    """Test metods for reservation class"""

    def setUp(self):
        print("SETUP Called...")
        # Arrange
        self.reservation_id = "111111"
        self.number_persons = 5
        self.date = "02/17/2024"

    def test_create_reservation(self):
        """Test create_reservation method"""
        print("TEST - 1 Called...")

        # Act
        reservation = Reservation.create_reservation(
            self.reservation_id, self.number_persons, self.date
        )

        # Assert
        self.assertEqual(reservation.reservation_id, self.reservation_id)
        self.assertEqual(reservation.number_persons, self.number_persons)
        self.assertEqual(reservation.date, self.date)

    def test_cancel_reservation(self):
        """Test cancel_reservation method"""
        print("TEST - 2 Called...")

        # Arrange
        reservation = Reservation.create_reservation(
            self.reservation_id, self.number_persons, self.date
        )

        # Act
        Reservation.cancel_reservation(reservation)

        # Assert
        self.assertFalse(reservation.active)

    # Exception handler test
    def test_negative_number_persons(self):
        """Test case of a negative number persons"""
        print("TEST - 3 Called...")

        # Act & Assert
        self.assertRaises(
            ValueError,
            Reservation.create_reservation,
            self.reservation_id,
            -1,
            self.date,
        )


if __name__ == "__main__":
    unittest.main()
