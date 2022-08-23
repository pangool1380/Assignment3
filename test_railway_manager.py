#Assignment 2
import unittest
import datetime
from railway_manager import RailwayManager
from abstract_railway_employee import AbstractRailwayEmployee

#Test for the RailwayManager Class

class TestRailwayManager(unittest.TestCase):
    """TestRailwayManager class"""
    def setUp(self):
        """Set up"""
        self.rm = RailwayManager("test.sqlite")
        self.employee1 = AbstractRailwayEmployee("John", "Doe", 1, datetime.date(2018, 1, 1))

    
    
    def tearDown(self):
        """ Tear Down"""
        #tearDown method should delete the test sqlite database
        self.rm.remove_employee_by_id(1)
        self.rm.remove_employee_by_id(2)
        self.rm.remove_employee_by_id(3)
        self.rm.remove_employee_by_id(4)
        
        
        

    def logPoint(self, msg):
        """Log point"""
        print(msg)

    def test_add_employee_success(self):
        """Test add employee success"""
        self.logPoint("Test add employee success")
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_employee(1).get_employee_id(), 1)


    def test_add_employee_failure(self):
        """Test add employee failure"""
        self.logPoint("Test add employee failure")
        self.rm.add_employee(self.employee1)
        self.assertRaises(ValueError)


    def test_remove_employee_success(self):
        """Test remove employee success"""
        self.logPoint("Test remove employee success")
        self.rm.add_employee(self.employee1)
        self.rm.remove_employee_by_id(1)
        self.assertEqual(self.rm.get_all_employees(), [])


    def test_remove_employee_failure(self):
        """Test remove employee failure"""
        self.logPoint("Test remove employee failure")
        self.rm.add_employee(self.employee1)
        self.rm.remove_employee_by_id(1)
        self.assertRaises(ValueError)


    def test_get_employee(self):
        """Test get employee"""
        self.logPoint("Test get employee")
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_employee(1).get_employee(), 1)


    def test_employee_exists(self):
        """Test employee exists"""
        self.logPoint("Test employee exists")
        self.rm.add_employee(self.employee1)
        self.assertTrue(self.rm.employee_exists(1))

    def test_get_all_employees(self):
        """Test get all employees"""
        self.logPoint("Test get all employees")
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_all_employees(), [self.employee1])

    
    def test_get_all_by_type(self):
        """Test get_all_by_type method"""
        self.rm.add_employee(self.employee1)
        self.assertEqual(self.rm.get_all_by_type("Dispatcher"), [self.employee1])
         


    def test_update_employee(self):
        """Test update_employee method"""
        self.rm.add_employee(self.employee1)
        self.rm.update_employee(self.employee1)
        self.assertEqual(self.rm.get_all_employees(), [self.employee1])


if __name__ == "__main__":
    unittest.main()

