#Assignment 2

from abstract_railway_employee import AbstractRailwayEmployee
import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime



"""According to Wikipedia, Dispatcher is a communications worker who receives and transmits information to coordinate operations of other personnel and vehicles carrying out a service"""
class Dispatcher(AbstractRailwayEmployee):
    """Dispatcher class"""
    TYPE = "Dispatcher"

    station_name = Column(String(100))
    station_id = Column(Integer)


    #Constructor: first_name(string), last_name(string), employee_id(int), date_started(date)
    def __init__(self, first_name, last_name, employee_id, date_started, station_name, station_id ):
        super().__init__(first_name, last_name, employee_id, date_started)
        self._station_name = station_name
        self._station_id = station_id

    def get_station_name(self):
        """Returns the name of the station"""
        #if the name is not string, raise error
        if self._station_name != str:
            raise ValueError("Station name must be a string.")
        elif self._station_name is None:
            raise ValueError("Station name must be defined.")
        elif self._station_name == "":
            raise ValueError("Station name cannot be empty.")
        return self._station_name

    def get_station_id(self):
        """Returns the ID of the station"""
        #if the ID is not integer, raise error
        if self._station_id != int:
            raise ValueError("Station ID must be an integer.")
        elif self._station_id is None:
            raise ValueError("Station ID must be defined.")
        elif self._station_id == "":
            raise ValueError("Station ID cannot be empty.")
        #if the ID is string or float, raise error
        elif isinstance(self._station_id, str) or isinstance(self._station_id, float):
            raise ValueError("Station ID must be an integer.")

        return self._station_id

    def get_details(self):
        """Returns the details of the dispatcher"""
        return "Station ID: " + str(self._station_id) + "\n" + "Station name: " + self._station_name + "\n" + "Name: " + self.get_full_name() + "\n" + "Date started: " + datetime(self._date_started)

    def get_type(self):
        """Returns the type of the dispatcher"""
        return Dispatcher.TYPE

    def get_all_details(self):
        """Returns all the details of the dispatcher"""
        return self.get_details() + "\n" + self.get_type()

    def to_dict(self):
        """Returns all the details of the dispatcher"""
        return self.get_details() + "\n" + self.get_type()