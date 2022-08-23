#Assignment 2

from abstract_railway_employee import AbstractRailwayEmployee
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dispatcher import Dispatcher
from train_driver import TrainDriver


class RailwayManager:
    """Railway Manager class"""
    #Constructor: employees(list of AbstractRailwayEmployee)
    def __init__(self, db_name):
        """Constructor for the RailwayManager class"""
        
        if db_name is None or db_name == "":
            raise ValueError("DB Name cannot be undefined")

        engine = create_engine("sqlite:///" + db_name)
        self._db_session = sessionmaker(bind = engine) 
        self._next_available_id = 1

    #Add employee(employee: AbstractRailwayEmployee)
    def add_employee(self, employee):
        """Add a new employee to the list of employees"""
       
        if self.employee_exists(employee.get_employee_id()):
            raise ValueError("Employee already exists")
        session = self._db_session()
        session.add(employee)
        session.commit()
        session.close()

    def remove_employee_by_id(self, employee_id):
        """Remove an employee from the list of employees"""
        
        session = self._db_session()
        employee = session.query(AbstractRailwayEmployee).filter_by(employee_id=employee_id).first()

        if employee is None:
            session.close()
            raise ValueError("Employee does not exist")

        session.delete(employee)
        session.commit()
        session.close()

    def get_employee(self, employee_id):
        """Get an employee from the list of employees"""

        session = self._db_session()
        employee = session.query(Dispatcher).filter_by(employee_id=employee_id).first()

        if employee is None:
            employee = session.query(TrainDriver).filter_by(employee_id=employee_id).first()

        session.close()

        return employee

    def employee_exists(self, employee_id):
        """Check if an employee exists in the list of employees"""
        
        session = self._db_session()
        employee = session.query(AbstractRailwayEmployee).filter_by(employee_id=employee_id).first()
        session.close()

        if employee is not None:
            return True
        return False
        



    def get_all_employees(self):
        """Get all employees from the list of employees using """
        return self._employees


    def get_all_by_type(self, type):
        """Get all employees of a certain type from the list of employees"""
        # employees = []
        # for e in self._employees:
        #     if e.get_type() == type:
        #         employees.append(e)
        # return employees

        session = self._db_session()
        employees = session.query(type).all()
        if type == Dispatcher.TYPE:
            employees = session.query(Dispatcher).filter(Dispatcher.type == type).all()
        elif type == TrainDriver.TYPE:
            employees = session.query(TrainDriver).filter(TrainDriver.type == type).all()

        else: 
            devices = []

        session.close()
        
 
    

    def update_employee(self, employee):
        """Update an employee in the list of employees using SQL"""
        session = self._db_session()
        session.merge(employee)
        session.commit()
        session.close()

       

        