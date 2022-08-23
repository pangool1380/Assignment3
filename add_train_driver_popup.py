import tkinter as tk
from tkinter import messagebox
import requests

class AddTrainDriverPopup(tk.Frame):
    """Popup Frame to Add a Train Driver as an employee """
    def __init__(self, parent, close_callback):
        """Constructor"""
        tk.Frame.__init__(self, parent)
        self._class_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="First Name:").grid(row=1, column=1)
        self._first_name = tk.Entry(self)
        self._first_name.grid(row=1, column=2)
        tk.Label(self, text="Last Name:").grid(row=2, column=1)
        self._last_name = tk.Entry(self)
        self._last_name.grid(row=2, column=2)
        tk.Label(self, text ="Employee ID:").grid(row=3, column=1)
        self._employee_id = tk.Entry(self)
        self._employee_id.grid(row=3, column=2)
        self._date_started = tk.Entry(self)
        self._date_started.grid(row=4, column=2)
        tk.Label(self, text = "Train Name:").grid(row=5, column=1)
        self._train_name = tk.Entry(self)
        self._train_name.grid(row=5, column=2)
        tk.Label(self, text = "Train ID:").grid(row=6, column=1)
        self._train_id = tk.Entry(self)
        self._train_id.grid(row=6, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=11, column=1)
        tk.Button(self, text="Close", command=self._class_cb).grid(row=11, column=2)

    def _submit_cb(self):
        """Submit Add Train Driver """
        data = {}
        data['first_name'] = self._first_name.get()
        data['last_name'] = self._last_name.get()
        data['employee_id']= self._employee_id.get()
        data['date_started'] = self._date_started.get()
        data['train_name'] = self._train_name.get()
        data['train_id'] = self._train_id.get()

        response = requests.post('http://localhost:5000/railwaymanager/employees', json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Employee Added")
            self._class_cb()

        else:
            messagebox.showerror("Error", "Employee Not Added")
            self._class_cb()

