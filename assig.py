from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle


class System:
    """ --------------------EMPLOYEE MANAGEMENT SYSTEM--------------------
    -----THIS PROGRAM HELPS YOU TO MINIMIZE YOUR DAILY EFFORT OF MANUALLY WRITING EMPLOYEE'S DETAIL-----"""
    def __init__(self, interface1):
        """ ===============INITIALIZATION OF THE OBJECT===============
        ----------This method generated a window with four buttons, ADD EMPLOYEE, ADD DEPARTMENT, SHOW EMPLOYEE AND EXIT
        """
        self.interface1 = interface1
        self.interface1.geometry('660x300')
        self.interface1.resizable(False, False)
        self.interface1.title('EMPLOYMENT MANAGEMENT SYSTEM')
        self.main_label1 = Label(self.interface1, text='EMPLOYEE MANAGEMENT SYSTEM', font='cambria 16 bold')
        self.main_label1.grid(row=1, column=2)

        self.employ = ttk.Button(self.interface1, text='ADD EMPLOYEE', width=20, command=self.add_employ)
        self.employ.grid(row=2, column=1, padx=10, ipady=20)
        self.depart = ttk.Button(self.interface1, text='ADD DEPARTMENT', width=20, command=self.add_depart)
        self.depart.grid(row=2, column=2, padx=10, ipady=20)
        self.sh = ttk.Button(self.interface1, text='SHOW EMPLOYEE', width=20, command=self.show)
        self.sh.grid(row=2, column=3, padx=10, ipady=20)
        self.exit1 = ttk.Button(self.interface1, text='EXIT', width=20, command=self.interface1.quit)
        self.exit1.grid(row=3, column=3, padx=10, ipady=20, pady=30)

    def add_employ(self):
        """ ===============ADDING EMPLOYEE===============
        ----------add_employ method helps to add employee to our file which is stored in a .txt file named ALLDATA.TXT
        ----------This method creates SEVEN ENTRY BOX, TWO COMBOBOX, THREE BUTTONS and TEN LABELS--------------
        PARAMETERS and LABELS:
        <EMPLOYEE REGISTRATION FORM as big label>
            FIRST NAME: <WHICH ONLY TAKES ALPHABETS AS INPUT>
            MIDDLE NAME: <WHICH ONLY TAKES ALPHABETS AS INPUT>
            LAST NAME: <WHICH ONLY TAKES ALPHABETS AS INPUT>
            EMPLOYEE ID: <WHICH ONLY TAKES NUMERIC VALUES AS INPUT>
            AGE: <WHICH ONLY TAKES NUMERIC VALUES AS INPUT GREATER THAN 17 AND LESS THAN 60>
            GENDER: <WHICH ONLY TAKES THREE VALUES AS INPUT>
            ADDRESS: <WHICH TAKE NUMERIC VALUES AS WELL AS ALPHABETS WITH CHARACTERS>
            CONTACT: <WHICH ONLY TAKES NUMERIC VALUE AS INPUT>
            DEPARTMENT: <CAN BE ADDED AND CHOOSE THE DESIRED DATA>-----------------------------------------
        THREE BUTTONS
        <EXIT>, <RESET> AND <SAVE>"""
        interface2 = Tk()
        self.interface2 = interface2
        self.interface2.geometry('600x575')
        self.interface2.resizable(False, False)
        self.interface2.title('EMPLOYEE REGISTRATION FORM')
        self.main_label2 = Label(self.interface2, text='EMPLOYEE REGISTRATION FORM', font='cambria 16 bold')
        self.main_label2.grid(row=1, column=2)

        self.first_name = Label(self.interface2, text='First Name: ', font='Arial 12 bold', pady=10)
        self.first_name.grid(row=2, column=1)
        self.middle_name = Label(self.interface2, text='Middle Name: ', font='Arial 12 bold', pady=10)
        self.middle_name.grid(row=3, column=1)
        self.last_name = Label(self.interface2, text='Last Name: ', font='Arial 12 bold', pady=10)
        self.last_name.grid(row=4, column=1)
        self.emp_id = Label(self.interface2, text='Employee ID: ', font='Arial 12 bold', pady=10)
        self.emp_id.grid(row=5, column=1)
        self.agel = Label(self.interface2, text='Age: ', font='Arial 12 bold', pady=10)
        self.agel.grid(row=6, column=1)
        self.gender = Label(self.interface2, text='Gender: ', font='Arial 12 bold', pady=10)
        self.gender.grid(row=7, column=1)
        self.contact = Label(self.interface2, text='Contact: ', font='Arial 12 bold', pady=10)
        self.contact.grid(row=8, column=1)
        self.address = Label(self.interface2, text='Address: ', font='Arial 12 bold', pady=10)
        self.address.grid(row=9, column=1)
        self.department = Label(self.interface2, text='Department--Code: ', font='Arial 12 bold', pady=10)
        self.department.grid(row=10, column=1)

        self.e_fname = Entry(self.interface2, width=50)
        self.e_fname.grid(row=2, column=2)
        self.e_mname = Entry(self.interface2, width=50)
        self.e_mname.grid(row=3, column=2)
        self.e_lname = Entry(self.interface2, width=50)
        self.e_lname.grid(row=4, column=2)
        self.e_empid = Entry(self.interface2, width=50)
        self.e_empid.grid(row=5, column=2)
        self.e_age = Entry(self.interface2, width=50)
        self.e_age.grid(row=6, column=2)
        self.e_gen = ttk.Combobox(self.interface2, width=50, state='readonly', values=['Male', 'Female', 'Other'])
        self.e_gen.grid(row=7, column=2)
        self.e_contact = Entry(self.interface2, width=50)
        self.e_contact.grid(row=8, column=2)
        self.e_add = Entry(self.interface2, width=50)
        self.e_add.grid(row=9, column=2)
        self.e_depart = ttk.Combobox(self.interface2, width=50,state='readonly', values=self.get_depart())
        self.e_depart.grid(row=10, column=2)

        self.btn_reset = ttk.Button(self.interface2, text='RESET', command=self.reset_box1)
        self.btn_reset.grid(row=11, column=1, ipady=15, ipadx=15)
        self.btn_save = ttk.Button(self.interface2, text='SAVE', command=self.save)
        self.btn_save.grid(row=11, column=2, ipady=15, ipadx=15)
        self.btn_exit = ttk.Button(self.interface2, text='EXIT', command=self.interface2.destroy)
        self.btn_exit.grid(row=11, column=3, ipady=15, ipadx=15)

    def get_depart(self):
        """ ---------------FETCH THE STORED DATA FOR DEPARMENT---------------------
        This function fetches the data required in the COMBOBOX of DEPARTMENT
        FETCHED DATA are DEPARTMENT NAME and DEPARTMENT CODE."""
        try:
            with open('depart.txt', 'rb') as for_depart:
                fetch_depart = pickle.load(for_depart)
                print(fetch_depart)
                return fetch_depart
        except FileNotFoundError:
            fetch_depart = []
            return fetch_depart
        finally:
            pass

    def save(self):
        """ ---------------SAVES THE EMPLOYEE DATA ON THE FILE---------------------
        This function saves the data in the file name ALLDATA.TXT as list.
         STORES FOLLOWING DATA:
            FIRST NAME
            MIDDLE NAME
            LAST NAME
            EMPLOYEE ID
            AGE
            GENDER
            ADDRESS
            CONTACT
            DEPARTMENT==CODE
        As a DICTIONARY inside LIST."""
        fname = self.e_fname.get().upper()
        mname = self.e_mname.get().upper()
        empid = self.e_empid.get()
        lname = self.e_lname.get().upper()
        gen = self.e_gen.get()
        contact = self.e_contact.get().upper()
        age = self.e_age.get()
        address = self.e_add.get().upper()
        depart = self.e_depart.get()
        global main_data
        main_data = [
            {'ID': empid, 'Name': fname + ' ' + mname + '' + lname, 'Gender': gen, 'Age': age, 'Address': address,
             'Deparment': depart, 'Contact': contact}]
        if fname == ''or lname== ''or empid== ''or gen == ''or contact == ''or age == ''or address == ''or depart == '':
            messagebox.showerror('ERROR', 'BLANK FIELD FOUND')
        elif not fname.isalpha():
            messagebox.showerror('ERROR', 'ONLY USE ALPHABET ON FIRST NAME AND NO IDENTATION.')
        elif not lname.isalpha():
            messagebox.showerror('ERROR', 'ONLY USE ALPHABET ON LAST NAME AND NO IDENTATION.')
        elif not empid.isdigit():
            messagebox.showerror('ERROR', 'ONLY USE NUMBERS ON EMPLOYEE ID.')
        elif not age.isdigit() or int(age) < 18:
            messagebox.showerror('ERROR', 'ONLY USE NUMBER ON AGE AND SHOULD BE 18 ABOVE.')
        elif self.verify_empid():
            messagebox.showerror('ERROR', 'DUPLICATE ENTRY')
        elif not contact.isdigit():
            messagebox.showerror('ERROR', 'ONLY USE NUMERIC ON CONTACT.')
        else:
            try:
                with open('AllData.txt','rb') as file:
                    data = pickle.load(file)
                with open('AllData.txt', 'wb') as file:
                    data.extend(main_data)
                    pickle.dump(data, file)
            except FileNotFoundError:
                with open('AllData.txt', 'wb') as file:
                    data = list()
                    data.extend(main_data)
                    pickle.dump(data, file)
            finally:
                with open('AllData.txt','rb') as file:
                    showdata = pickle.load(file)
                    print(showdata)
                self.reset_box1()
                messagebox.showinfo('CONFIRMATION', 'DATA SAVED SUCCESSFULLY')

    def add_depart(self):
        """=======================ADD DEPARTMENT WINDOWS==================================
        This fucntion creates window with TWO ENTRY BOX, TWO LABEL AND THREE BUTTONS
        TWO LABEL as DEPARTMENT NAME and DEPARTMENT CODE
        TWO ENTRY BOX to save DEPARTMENT NAME and DEPARTMENT CODE
        THREE BUTTONS
        <EXIT>, <RESET> AND <SAVE>"""
        interface3 = Tk()
        self.interface3 = interface3
        self.interface3.geometry('550x200')
        self.interface3.resizable(False, False)
        self.interface3.title('DEPARTMENT ADDITION')
        self.label_x = Label(self.interface3, text='Department Name: ', font="Arial 12 bold")
        self.label_y = Label(self.interface3, text='Department Code: ', font="Arial 12 bold")
        self.Save_Department = ttk.Button(self.interface3, text='Save Department', width=20, command=self.save_d)
        self.reset = ttk.Button(self.interface3, text ="Reset", width=20, command=self.reset_d)
        self.reset.grid(row=10,column=0 , sticky="W",pady=5)
        self.exit = ttk.Button(self.interface3, text="Exit", width=17, command=self.interface3.destroy)
        self.exit.grid(row = 10,column = 3,sticky = 'W')
        self.Save_Department.grid(row=9, column=1, pady=8)
        self.label_x.grid(row=3, column=0, padx=5, pady=8)
        self.label_y.grid(row=7, column=0, padx=5, pady=8)

        self.entry_depart = Entry(self.interface3, width=40)
        self.entry_code = Entry(self.interface3, width=40)
        self.entry_depart.grid(row=3, column=1, padx=5)
        self.entry_code.grid(row=7, column=1, padx=5)


    def save_d(self):
        """=======================SAVE DEPARTMENT DATA==================================
        This function saves DEPARTMENT NAME and DEPARTMENT CODE in file named:DEPART.TXT."""
        if self.entry_depart.get() == '' or self.entry_code.get() == '':
            messagebox.showerror('ERROR', 'BLANK FIELD FOUND')
        elif not self.entry_depart.get().isalpha():
            messagebox.showerror('ERROR', 'USE ALPHABETS IN NAME')
        elif not self.entry_code.get().isdigit():
            messagebox.showerror('ERROR', 'USE NUMBERS IN CODE')
        elif self.verify_departmentid():
            messagebox.showerror('ERROR', 'DUPLICATE ENTRY')
        else:
            single_depart = f'{self.entry_depart.get()}--{str(self.entry_code.get())}'
            sample = single_depart
            try:
                with open('depart.txt', 'rb') as file1:
                    data2 = pickle.load(file1)
                with open('depart.txt', 'wb') as file1:
                    data2.append(sample)
                    pickle.dump(data2, file1)
            except FileNotFoundError:
                with open('depart.txt', 'wb') as file1:
                    data2 = list()
                    data2.append(sample)
                    pickle.dump(data2, file1)
            finally:
                self.reset_d()
                messagebox.showinfo('CONFIRMATION', 'DATA SAVED')

    def reset_d(self):
        """=======================RESET ENTRY BOX FOR DEPARTMENT==================================
        This method clears ENTRY BOX DEPARTMENT NAME and DEPARTMENT CODE."""
        self.entry_depart.delete(0, END)
        self.entry_code.delete(0, END)

    def show(self):
        """-----------------------DISPLAYS SAVED EMPLOYEE DATA----------------------
            This method shows all the data of the registered employee."""
        self.interface4 = Tk()
        self.interface4.geometry('660x300')

        self.interface4.title('DISPLAY EMPLOYEE')
        self.main_label4 = Label(self.interface4, text='EMPLOYEE DETAIL', font='cambria 16 bold')
        self.main_label4.grid(row=1, column=2)
        try:
            with open('AllData.txt', 'rb') as file:
                data = pickle.load(file)
                for i in range(0, len(data)):
                    for k, v in data[i].items():
                        print(k, v)
                        self.show_data1 = Label(self.interface4, text=f'{k}==>{v}')
                        self.show_data1.grid(column=i)
        except FileNotFoundError:
            messagebox.showinfo('FILE MISSING', 'NO DATA FOUND')
        finally:
            pass

    def reset_box1(self):
        """=======================RESET ENTRY BOX FOR EMPLOYEE REGISTRATION==================================
                This method clears  all the ENTRY BOXES in EMPLOYEE REGISTRATION SYSTEM."""
        self.e_fname.delete(0, END)
        self.e_mname.delete(0, END)
        self.e_lname.delete(0, END)
        self.e_empid.delete(0, END)
        self.e_age.delete(0, END)
        self.e_gen.delete(0, END)
        self.e_contact.delete(0, END)
        self.e_add.delete(0, END)
        self.e_depart.delete(0, END)

    def verify_empid(self):
        """=================CHECKS EMPLOYEE ID=============
        THIS METHOD CHECKS FOR DUPLICATE EMPLOYEE ID"""
        try:
            with open('AllData.txt', 'rb') as check:
                data = pickle.load(check)
                for i in range(0, len(data)):
                    for j in data[i].values():
                        print(j)
                        if self.e_empid.get() == j:
                            return True
                        else:
                            return False
        except FileNotFoundError:
            return False
        finally:
            pass

    def verify_departmentid(self):
        """=================CHECKS DEPARTMENT CODE=============
                THIS METHOD CHECKS FOR DUPLICATE DEPARTMENT ID"""
        try:
            with open('depart.txt', 'rb') as check:
                data = pickle.load(check)
                for i in range(0, len(data)):
                    if str(self.entry_code.get()) in data[i]:
                        return True
                    else:
                        return False
        except FileNotFoundError:
            return False
        finally:
            pass


interface = Tk()
gui = System(interface)
interface.mainloop()