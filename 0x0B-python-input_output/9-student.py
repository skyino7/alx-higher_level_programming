#!/usr/bin/python3
"""Module"""


class Student:
    """
    Class
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age

        Args:
            first_name (str): Student First Name
            last_name (str): Student Last Name
            age (int): Student Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance

        Returns:
            dict: Dictionary represents the student instance
        """
        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

        return student_dict
