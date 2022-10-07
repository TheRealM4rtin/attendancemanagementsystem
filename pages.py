import tkinter
import customtkinter as ctk
import os
from tkcalendar import DateEntry
import pandas as pd


class admin_page(ctk.CTkFrame):
    def __init__(self, *args, parent, controller, **kwargs):
        super().__init__(*args, **kwargs)

        # Horizontal Frames
        self.frame_top = ctk.CTkFrame(self, bg="blue")
        self.frame_middle = ctk.CTkFrame(self, bg="blue")
        self.frame_bottom = ctk.CTkFrame(self, bg="blue")
        # Grid Frames
        self.frame_top.grid(row=0, column=0, sticky="nsew")
        self.frame_middle.grid(row=1, column=0, sticky="nsew")
        self.frame_bottom.grid(row=2, column=0, sticky="nsew")
        # Column config
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(1, weight=1)
        self.frame_middle.columnconfigure(2, weight=1)
        self.frame_bottom.columnconfigure(0, weight=1)
        # Row Config
        self.frame_top.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(1, weight=1)
        self.frame_middle.rowconfigure(2, weight=1)
        self.frame_middle.rowconfigure(3, weight=1)
        self.frame_middle.rowconfigure(4, weight=1)
        self.frame_bottom.rowconfigure(0, weight=1)

        # Text
        self.string_header = tkinter.StringVar(value="Welcome Admin!")
        self.label_header = ctk.CTkLabel(master=self.frame_top, textvariable=self.string_header, width=120,
                                         height=25)
        self.label_header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Button Launch Excel
        self.button_launch_excel = ctk.CTkButton(master=self.frame_middle, text="Launch the Original Excel", width=20,
                                                 height=5, command=lambda: launch_excel())
        self.button_launch_excel.grid(row=0, columnspan=3, padx=10, pady=10)

        def launch_excel():
            os.system('open -a Microsoft\ Excel.app /Users/martin/PycharmProjects/CentriaPythonProjects'
                      '/AttendanceManagement/data.csv')

        # Select Date Label
        self.string_select_date = tkinter.StringVar(value="Or please Select a Date:")
        self.label_select_date = ctk.CTkLabel(master=self.frame_middle, textvariable=self.string_select_date, width=20)
        self.label_select_date.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Label Date Entry
        self.string_date = tkinter.StringVar(value="Begin Date")
        self.label_date = ctk.CTkLabel(master=self.frame_middle, textvariable=self.string_date, width=20, height=5)
        self.label_date.grid(row=2, column=0, padx=3, pady=3)

        # Label Date Entry 2
        self.string_date = tkinter.StringVar(value="End Date")
        self.label_date = ctk.CTkLabel(master=self.frame_middle, textvariable=self.string_date, width=20, height=5)
        self.label_date.grid(row=2, column=1, padx=3, pady=3)

        # Date Entry 1
        self.date_entry = DateEntry(master=self.frame_middle, width=12)
        self.date_entry.grid(row=3, column=0, padx=10, pady=10)

        # Date Entry 2
        self.date_entry2 = DateEntry(master=self.frame_middle, width=12)
        self.date_entry2.grid(row=3, column=1, padx=10, pady=10)

        # Save entry data
        self.button_excel = ctk.CTkButton(master=self.frame_middle, text="Save Data", width=20, height=5,
                                          command=lambda: save())
        self.button_excel.grid(row=4, columnspan=3, padx=20, pady=20)

        # Save function
        def save():
            begin = self.date_entry.get_date()
            end = self.date_entry2.get_date()

            # Print the date and its type
            # print(begin)
            # print(type(begin))

            # Read the csv file
            df = pd.read_csv('data.csv', lineterminator='\n', on_bad_lines='skip', sep=',', header=None)

            # Print type of the date column
            # print(df[3].dtypes)

            # Convert the date column to datetime
            beginstr = begin.strftime('%Y-%m-%d')
            endstr = end.strftime('%Y-%m-%d')

            df = df[(df[3] >= beginstr) & (df[3] <= endstr)]

            # Save the data
            df.to_csv('new.csv', header=False, index=False)

            # Create Top Level Window
            self.popup = tkinter.Toplevel()
            self.popup.title("Done! Your CSV file has been saved!")
            self.popup.geometry("350x150")
            self.popup.columnconfigure(0, weight=1)
            self.popup.rowconfigure(0, weight=1)

            # Label Ask
            self.string_ask = tkinter.StringVar(value="Would you like to open the file?")
            self.label_ask = ctk.CTkLabel(master=self.popup, textvariable=self.string_ask, width=20, height=5)
            self.label_ask.grid(row=0, rowspan=2, column=0, padx=5, pady=5)

            # Button Yes and No
            self.button = ctk.CTkButton(self.popup, text="Yes", width=20, height=5, command=lambda: answer_yes())
            self.button.grid(row=2, column=0, padx=20, pady=10)
            self.button = ctk.CTkButton(self.popup, text="No", width=20, height=5,
                                        command=lambda: self.popup.quit())
            self.button.grid(row=3, column=0, padx=20, pady=10)

            def answer_yes():
                os.system('open -a Microsoft\ Excel.app /Users/martin/PycharmProjects/CentriaPythonProjects'
                          '/AttendanceManagement/new.csv')
                self.popup.quit()  # destroy()

        # Quit Button
        self.button_quit = ctk.CTkButton(master=self.frame_bottom, text="Quit",
                                         command=lambda: controller.up_frame(welcome_page))
        self.button_quit.grid(row=2, column=1, padx=10, pady=10)


class user_page(ctk.CTkFrame):
    def __init__(self, *args, parent, controller, **kwargs):
        super().__init__(*args, **kwargs)

        # Horizontal Frames
        self.frame_top = ctk.CTkFrame(self, bg="blue")
        self.frame_middle = ctk.CTkFrame(self, bg="blue")
        self.frame_bottom = ctk.CTkFrame(self, bg="blue")
        # Grid Frames
        self.frame_top.grid(row=0, column=0, sticky="nsew")
        self.frame_middle.grid(row=1, column=0, sticky="nsew")
        self.frame_bottom.grid(row=2, column=0, sticky="nsew")
        # Column config
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(1, weight=1)
        self.frame_middle.columnconfigure(2, weight=1)
        self.frame_bottom.columnconfigure(0, weight=1)
        # Row Config
        self.frame_top.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(1, weight=1)
        self.frame_middle.rowconfigure(2, weight=1)
        self.frame_middle.rowconfigure(3, weight=1)
        self.frame_middle.rowconfigure(4, weight=1)
        self.frame_middle.rowconfigure(5, weight=1)
        self.frame_bottom.rowconfigure(0, weight=1)

        # Text
        self.string_wlcm = tkinter.StringVar(value="Welcome Student!")
        self.label_wlcm = ctk.CTkLabel(master=self.frame_top, textvariable=self.string_wlcm, width=120,
                                       height=25)
        self.label_wlcm.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Entry Field
        entry = ctk.CTkEntry(master=self.frame_middle,
                             placeholder_text="Name",
                             width=120,
                             height=25,
                             border_width=2,
                             corner_radius=10)
        entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Option Box
        status_var = ctk.StringVar(value="Present")  # set initial value

        combobox = ctk.CTkComboBox(master=self.frame_middle,
                                   values=["Present", "Late", "Absent"],
                                   variable=status_var)
        combobox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Label Date Entry
        self.string_select_date = tkinter.StringVar(value="Please Select a Date")
        self.label_select_date = ctk.CTkLabel(master=self.frame_middle, textvariable=self.string_select_date, width=2)
        self.label_select_date.grid(row=3, column=0, padx=1, pady=1)

        # Entry Date
        self.date_entry = DateEntry(master=self.frame_middle, width=12)
        self.date_entry.grid(row=3, column=1, padx=1, pady=1)

        # Check Box
        checkbox_var = tkinter.StringVar(self.frame_middle, "Disagree")

        checkbox = ctk.CTkCheckBox(master=self.frame_middle,
                                   text="I certify on my honour that the above information are "
                                        "correct.",
                                   variable=checkbox_var, onvalue="Agree", offvalue="Disagree")
        checkbox.grid(row=5, column=0, padx=10, pady=10)

        def save_data():
            var = (entry.get(), status_var.get(), checkbox_var.get(), self.date_entry.get_date())
            dataframe = pd.DataFrame([var], columns=['Name', 'Status', 'Agree', 'Date'])
            dataframe.to_csv('data.csv', header=None, index=False, mode='a')
            print(dataframe)
            print("SUBMITTED")

        # Submit Button
        self.button_submit = ctk.CTkButton(master=self.frame_bottom, text="Submit", command=save_data)

        self.button_submit.grid(row=2, column=0, padx=10, pady=10)

        # Quit Button
        self.button_quit = ctk.CTkButton(master=self.frame_bottom, text="Quit",
                                         command=lambda: controller.up_frame(welcome_page))
        self.button_quit.grid(row=2, column=1, padx=10, pady=10)


class welcome_page(ctk.CTkFrame):
    def __init__(self, *args, parent, controller, **kwargs):
        super().__init__(*args, **kwargs)
        # Controller is the main frame, useful to use the up_frame method
        self.controller = controller

        # self.id = controller.id

        self.frame = ctk.CTkFrame(self, bg="blue")
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)

        # Text Welcome
        self.string_wlcm = tkinter.StringVar(value="Welcome to the Assessment Management System")
        self.label_wlcm = ctk.CTkLabel(master=self.frame, textvariable=self.string_wlcm)
        self.label_wlcm.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        # Button User
        self.button_user = ctk.CTkButton(master=self.frame, text="User",
                                         command=lambda: controller.up_frame(user_page))
        self.button_user.grid(row=2, column=0, padx=10, pady=10)

        # Button Admin
        self.button_admin = ctk.CTkButton(master=self.frame, text="Admin",
                                          command=lambda: controller.up_frame(admin_page))
        self.button_admin.grid(row=3, column=0, padx=10, pady=10)

        # Quit Button
        self.button_quit = ctk.CTkButton(master=self.frame, text="Quit", command=lambda: controller.quit())
        self.button_quit.grid(row=4, column=0, padx=10, pady=10)
