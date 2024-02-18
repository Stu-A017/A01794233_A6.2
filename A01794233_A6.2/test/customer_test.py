"""
Module to test customer class
"""

import unittest
import sys

sys.path.append("/home/jaseco/Documents/MastersDegree_MNA/A01794233_A6.2/")
from MyBooking.customer import Customer


class CustomerTest(unittest.TestCase):
    """Test metods for customer class"""

    def setUp(self):
        print("SETUP Called...")
        # Arrange
        self.name = "AA, BB"
        self.email = "aa@bb.com"
        self.type_of_room = "X"

    def test_create_customer(self):
        """Test create_customer method"""
        print("TEST - 1 Called...")

        # Act
        customer = Customer.create_customer(self.name, self.email, self.type_of_room)

        # Assert
        self.assertEqual(customer.name, self.name)
        self.assertEqual(customer.email, self.email)
        self.assertEqual(customer.type_of_room, self.type_of_room)

    def test_delete_customer(self):
        """Test delete_customer method"""
        print("TEST - 2 Called...")

        # Arrange
        customer = Customer.create_customer(self.name, self.email, self.type_of_room)

        # Act
        Customer.delete_customer(customer)

        # Assert
        self.assertIsNone(customer.name)
        self.assertIsNone(customer.email)
        self.assertIsNone(customer.type_of_room)

    def test_display_customer_information(self):
        """Test display_customer_information method"""
        print("TEST - 3 Called...")

        # Arrange
        customer = Customer.create_customer(self.name, self.email, self.type_of_room)
        message = "Name: AA, BB, email: aa@bb.com, type of room: X"

        # Act && Assert
        self.assertEqual(customer.display_customer_information(), message)

    def test_modify_customer_information(self):
        """Test modify_customer_information method"""
        print("TEST - 4 Called...")

        # Arrange
        customer = Customer.create_customer(self.name, self.email, self.type_of_room)
        new_name = "NN, CC"
        new_email = "mm@yahoo.com"
        new_type_of_room = "V"

        # Act
        customer.modify_customer_information(new_name, new_email, new_type_of_room)

        # Assert
        self.assertEqual(customer.name, new_name)
        self.assertEqual(customer.email, new_email)
        self.assertEqual(customer.type_of_room, new_type_of_room)

    # Exception handler test
    def test_should_contain_at_value(self):
        """Test @ value in email"""
        print("TEST - 5 Called...")

        # Act & Assert
        self.assertRaises(
            ValueError,
            Customer.create_customer,
            self.name,
            "123456",
            "Z",
        )

    # Exception handler test
    def test_should_contain_at_value_in_modify(self):
        """Test @ value in email in modify method"""
        print("TEST - 6 Called...")

        # Arrange
        customer = Customer.create_customer(self.name, self.email, self.type_of_room)
        new_name = "NN, CC"
        new_email = "mmyahoo.com"
        new_type_of_room = "V"

        # Act & Assert
        self.assertRaises(
            ValueError,
            customer.modify_customer_information,
            new_name,
            new_email,
            new_type_of_room,
        )


if __name__ == "__main__":
    unittest.main()
