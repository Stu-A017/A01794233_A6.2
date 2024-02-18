"""
Module to test file class
"""

import unittest
import sys
import os

sys.path.append("/home/jaseco/Documents/MastersDegree_MNA/A01794233_A6.2/")
from MyBooking.file import File
from MyBooking.hotel import Hotel
from MyBooking.customer import Customer


class FileTest(unittest.TestCase):
    """Test metods for File class"""

    def setUp(self):
        print("SETUP Called...")
        # Arrange
        self.hotel = Hotel.create_hotel("Hotel", "City", 5)
        self.customer = Customer.create_customer("AA, BB", "aa@bb.com", "X")
        self.path = "/home/jaseco/Documents/MastersDegree_MNA/A01794233_A6.2/test/hotel_information.txt"

    def test_create_file(self):
        """Test create_file method"""
        print("TEST - 1 Called...")

        # Act
        File.create_file(self.hotel, self.customer)

        # Assert
        self.assertTrue(os.path.isfile(self.path))


if __name__ == "__main__":
    unittest.main()
