#Assignment 2

from sqlalchemy import Column, String, Integer, DateTime
import datetime

class AbstractRailwayEmployee:
    """ Static methods """

    BOOLEAN_TRUE = 1
    __tablename__ = "employees"
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    date_started = Column(DateTime)
    type =  Column(String(6))

    def __init__(self, first_name, last_name, employee_id, date_started):
        self._first_name = first_name
        self._last_name = last_name
        self._employee_id = employee_id
        self._date_started = date_started



   

    def get_first_name(self):
        """ Returns the first name of the employee """
        return self._first_name

    def get_last_name(self):
        """ Returns the last name of the employee """
        return self._last_name

    def get_full_name(self):
        """ Returns the full name of the employee """
        return self._first_name + " " + self._last_name

    def get_date_started(self):
        """ Returns the date the employee started working """
        return self._date_started

    #get_details(string)
    def get_details(self):
        """ Returns the details of the employee """
        return "Employee ID: " + str(self._employee_id) + "\n" + "Name: " + self.get_full_name() + "\n" + "Date started: " + datetime(self._date_started)

  
    def get_type(self):
        """ Returns the type of the employee(Dispatcher ot Train Driver) """
        return "Dispatcher" or "Train Driver"

      
        

    #to_dict method(dict)
    def to_dict(self):
        """ Returns a dictionary of the employee """
        return {
            "first_name": self._first_name,
            "last_name": self._last_name,
            "employee_id": self._employee_id,
            "date_started": self._date_started
        }
