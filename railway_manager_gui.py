import tkinter as tk
from urllib import response
import requests
from add_dispatcher_popup import AddDispatcherPopup
from add_train_driver_popup import AddTrainDriverPopup
from complete_popup import CompletePopup
from remove_employee_popup import RemoveEmployeePopup


class MainAppController(tk.Frame):
    """ Main Application fot GUI """

    def __init__(self, parent):
        """Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Employees").grid(row=1, column=2)
        self._employees_listbox = tk.Listbox(self)
        self._employees_listbox.grid(row=2, column=1, columnspan=5)

        tk.Button(self, text="Add Dispatcher", command=self._add_dispatcher).grid(row=3, column=1)
        tk.Button(self, text="Add Train Driver", command=self._add_train_driver).grid(row=3, column=2)
        tk.Button(self, text="Complete", command=self._complete).grid(row=3, column=3)
        tk.Button(self, text="Remove", command=self._quit_callback).grid(row=3, column=4)
        tk.Button(self, text="Quit", command=self._delete_employee).grid(row=4, column=2)

        self._update_employees_list()

    def _add_dispatcher(self):
        """ Add Dispatcher Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddDispatcherPopup(self._popup_win, self._close_dispatcher_cb)

    def _close_dispatcher_cb(self):
        """ Close Add Dispatcher Popup """
        self._popup_win.destroy()
        self._update_employees_list()

    def _add_train_driver(self):
        """ Add Train Driver Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddTrainDriverPopup(self._popup_win, self._close_train_driver_cb)


    def _close_train_driver_cb(self):
        """ Close Add Train Driver Popup """
        self._popup_win.destroy()
        self._update_employees_list()

    def _complete(self):
        """ Complete Popup """
        self._popup_win = tk.Toplevel()
        self._popup = CompletePopup(self._popup_win, self._close_complete_cb)


    def _close_complete_cb(self):
        """ Close Complete Popup """
        self._popup_win.destroy()
        self._update_employees_list()


    def _quit_callback(self):
        """"Quit """
        self.quit()


    def _delete_employee(self):
        """Delete an employee """
        self._popup_win = tk.Toplevel()
        self._popup = RemoveEmployeePopup(self._popup_win, self._close_delete_cb)


    def _close_delete_cb(self):
        """ Close Delete Employee Popup """
        self._popup_win.destroy()
        self._update_employees_list()


    def _update_employees_list(self):
        """Update the list of Employees Descriptions"""

        response = requests.get('http://localhost:5000/railwaymanager/employees')
        if response.status_code == 200:
            self._employees_listbox.delete(0, tk.END)
            for employee in response.json():
                self._employees_listbox.insert(tk.END, employee)

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()


   




    
