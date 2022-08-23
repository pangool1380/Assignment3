from flask import Flask, request, jsonify
from abstract_railway_employee import AbstractRailwayEmployee
from railway_manager import RailwayManager
from train_driver import TrainDriver
from dispatcher import Dispatcher
import json

app = Flask(__name__)
railway_manager = RailwayManager("employees.db")
@app.route("/railwaymanager/employees", methods=["POST"])
def add_employee():
    """ Add an employee to the railway manager """
    content = request.json
    try:
        if content["type"] == TrainDriver.TYPE:
            train_driver = TrainDriver(content["first_name"], content["last_name"], content["employee_id"], content["date_started"], content["train_name"], content["train_id"])
            railway_manager.add_employee(train_driver)
        elif content["type"] == Dispatcher.TYPE:
            dispatcher = Dispatcher(content["first_name"], content["last_name"], content["employee_id"], content["date_started"], content["station_name"])
            railway_manager.add_employee(dispatcher)
        else:
            response = app.response_class(
                status = 400,
                response = "Invalid Employee Type"
            )
            return response
        #Add the Train Driver or Dispatcher object to the railway manager
        response = app.response_class(
            status = 200)
        return response
    except ValueError as e:
        response = app.response_class(
            status = 400,
            response = str(e)
        )
        return response

@app.route("/railwaymanager/employees/<employee_id>", methods=["PUT"])
def update_employee(employee_id):
    """ Update an employee's details """

    content = request.json
    try:
        employee = railway_manager.get_employee(employee_id)
        if content["type"] == TrainDriver.TYPE:
            train_driver = TrainDriver(content["first_name"], content["last_name"], content["employee_id"], content["date_started"], content["train_name"], content["train_id"], content["type"])
            railway_manager.update_employee(employee, train_driver)
        elif content["type"] == Dispatcher.TYPE:
            dispatcher = Dispatcher(content["first_name"], content["last_name"], content["employee_id"], content["date_started"], content["station_name"], content["station_id"], content["type"])
            railway_manager.update_employee(employee, dispatcher)
        else:
            response = app.response_class(
                status = 400,
                response = "Invalid Employee Type"
            )
            return response
        #Update the Train Driver or Dispatcher object in the railway manager
        response = app.response_class(
            status = 200)
        return response
    except ValueError as e:
        response = app.response_class(
            status = 400,
            response = str(e)
        )
        return response


@app.route("/railwaymanager/employees/<employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """ Delete an employee from the railway manager """
    try:
        employee = railway_manager.get_employee(employee_id)
        railway_manager.remove_employee_by_id(employee)
        response = app.response_class(
            status = 200)
        return response
    except ValueError as e:
        response = app.response_class(
            status = 400,
            response = str(e)
        )
        return response
    except KeyError as e:
        response = app.response_class(
            status = 404,
            response = str(e)
        )
        return response

@app.route("/railwaymanager/employees/<employee_id>", methods=["GET"])
def get_employee(employee_id):
    """ Get an employee from the railway manager """
    try:
        employee = railway_manager.get_employee(employee_id)
        response = app.response_class(
            status = 200,
            response = employee.to_json()
        )
        return response
    except ValueError as e:
        response = app.response_class(
            status = 400,
            response = str(e)
        )
        return response
    except KeyError as e:
        response = app.response_class(
            status = 404,
            response = str(e)
        )
        return response


@app.route("/railwaymanager/employees/all", methods=["GET"])
def get_all_employees():
    """ Get all employees from the railway manager """
    try:
        employees = railway_manager.get_all_employees()
        response = app.response_class(
            status = 200,
            response = json.dumps(employees)
        )
        return response
    except ValueError as e:
        response = app.response_class(
            status = 400,
            response = str(e)
        )
        return response
    except KeyError as e:
        response = app.response_class(
            status = 404,
            response = str(e)
        )
        return response


@app.route("/railwaymanager/employees/all/<type>", methods=["GET"])
def get_all_employees_by_type(type):
    """ Get all employees of a specific type from the railway manager """
    try:
        employees = railway_manager.get_all_by_type(type)
        response = app.response_class(
            status = 200,
            response = json.dumps(employees)
        )
        return response
    except ValueError as e:
        response = app.response_class(
            status = 400,
            response = str(e)
        )
        return response
    except KeyError as e:
        response = app.response_class(
            status = 404,
            response = str(e)
        )
        return response


if __name__ == "__main__":
    app.run()