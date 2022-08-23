import tkinter as tk
from tkinter import messagebox
import requests

class RemoveEmployeePopup(tk.Frame):
    """Popup frame to Remove an employee """
    def __init__(self, parent, close_callback):
        """Constructor"""

        tk.Frame.__init__(self, parent)
        self._class_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Employee ID:").grid(row=1, column=1)
        self._employee_id = tk.Entry(self)
        self._employee_id.grid(row=1, column=2)
        tk.Button(self, text="Delete", command=self._submit_cb).grid(row=3, column=1)
        tk.Button(self, text="Close", command=self._class_cb).grid(row=3, column=2)


    def _submit_cb(self):
        """Submit Remove Employee"""
        data = {}
        data['employee_id'] = self._employee_id.get()

        response = requests.delete('http://localhost:5000/railwaymanager/employees/' + data['employee_id'])
        if response.status_code == 200:
            self._class_cb()

        else:
            messagebox.showerror("Error", "Remove Employee Request Failed")