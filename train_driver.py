#Assignment 2

from abstract_railway_employee import AbstractRailwayEmployee
import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime


"""According to Wikipedia Train driver is a person who drives a train, multiple unit or a locomotive."""
class TrainDriver(AbstractRailwayEmployee):
    """Train Driver class"""


    
    TYPE = "Train Driver"
    train_name = Column(String(100))
    train_id = Column(Integer)
    
    #Constructor: first_name(string), last_name(string), employee_id(int), date_started(date)
    def __init__(self, first_name, last_name, employee_id, date_started, train_name, train_id ):
        super().__init__(first_name, last_name, employee_id, date_started)
        self._train_name = train_name
        self._train_id = train_id


    def get_train_name(self):
        """Returns the name of the train"""
        #if the name is not string, raise error
        if self._train_name != str:
            raise ValueError("Train name must be a string.")
        elif self._train_name is None:
            raise ValueError("Train name must be defined.")
        elif self._train_name == "":
            raise ValueError("Train name cannot be empty.")
        return self._train_name

    def get_train_id(self):
        """Returns the ID of the train"""
        #if the ID is not integer, raise error
        if self._train_id != int:
            raise ValueError("Train ID must be an integer.")
        elif self._train_id is None:
            raise ValueError("Train ID must be defined.")
        elif self._train_id == "":
            raise ValueError("Train ID cannot be empty.")
        #if the ID is string or float, raise error
        elif isinstance(self._train_id, str) or isinstance(self._train_id, float):
            raise ValueError("Train ID must be an integer.")
        return self._train_id

    def get_details(self):
        """Returns the details of the train driver"""
        return "Train ID: " + str(self._train_id) + "\n" + "Train name: " + self._train_name + "\n" + "Name: " + self.get_full_name() + "\n" + "Date started: " + datetime(self._date_started)

    def get_type(self):
        """Returns the type of the train driver"""
        return TrainDriver.TYPE


    # to_dict(self):
    def to_dict(self):
        """Returns all the details of the train driver"""
        return self.get_details() + "\n" + self.get_type()