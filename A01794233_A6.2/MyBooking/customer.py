"""
Module to create a customer instance in the system
"""


class Customer:
    """Metods and attributes for customer instance"""

    def __init__(self, name, email, type_of_room):
        """Initializes a Customer object"""
        self.name = name
        self.email = email
        self.type_of_room = type_of_room

    @staticmethod
    def create_customer(name, email, type_of_room):
        """Creates a new customer instance"""
        if "@" not in email:
            raise ValueError("email has to contain @ symbol")
        customer = Customer(name, email, type_of_room)
        return customer

    @staticmethod
    def delete_customer(customer):
        """Deletes a customer instance"""
        customer.name = None
        customer.email = None
        customer.type_of_room = None

    def display_customer_information(self):
        """Returns hotel information"""
        return (
            "Name: "
            + self.name
            + ", email: "
            + self.email
            + ", type of room: "
            + self.type_of_room
        )

    def modify_customer_information(self, name, email, type_of_room):
        """Modifies customer information"""
        if "@" not in email:
            raise ValueError("email has to contain @ symbol")
        self.name = name
        self.email = email
        self.type_of_room = type_of_room
