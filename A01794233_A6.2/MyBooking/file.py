"""
Module to create a txt file with the hotel information
"""

import sys


sys.path.append("/home/jaseco/Documents/MastersDegree_MNA/A01794233_A6.2/")
from MyBooking.hotel import Hotel
from MyBooking.customer import Customer


class File:
    """Metods and attributes for the file information"""

    def __init__(self):
        """Initializes a File object"""
        self.number_file = 1

    @staticmethod
    def create_file(hotel, customer):
        """Creates a file information"""
        with open("hotel_information.txt", "w", encoding="utf-8") as file1:
            file1.write(hotel.display_information() + "\n")
            file1.write(customer.display_customer_information() + "\n")
            file1.close()
