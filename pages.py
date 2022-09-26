import tkinter
import customtkinter as ctk
import csv


class admin_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

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
        self.frame_bottom.rowconfigure(0, weight=1)

        # Text
        self.string_header = tkinter.StringVar(value="Welcome Admin!")
        self.label_header = ctk.CTkLabel(master=self.frame_top, textvariable=self.string_header, width=120,
                                         height=25)
        self.label_header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


        # def delete_data():
        #


        # Quit Button
        self.button_quit = ctk.CTkButton(master=self.frame_bottom, text="Quit",
                                         command=lambda: controller.up_frame(welcome_page))
        self.button_quit.grid(row=2, column=1, padx=10, pady=10)


class user_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

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



        # Check Box
        checkbox_var = tkinter.StringVar(self.frame_middle, "Disagree")

        checkbox = ctk.CTkCheckBox(master=self.frame_middle,
                                   text="I certify on my honour that the above information are "
                                        "correct.",
                                   variable=checkbox_var, onvalue="Agree", offvalue="Disagree")
        checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        def save_data():
            f = open('data.csv', 'a', newline='')
            var = (entry.get(), status_var.get(), checkbox_var.get())
            writer = csv.writer(f)
            writer.writerow(var)
            print("SUBMITTED")
            f.close()

        # Submit Button
        self.button_submit = ctk.CTkButton(master=self.frame_bottom, text="Submit", command=save_data)

        self.button_submit.grid(row=2, column=0, padx=10, pady=10)

        # Quit Button
        self.button_quit = ctk.CTkButton(master=self.frame_bottom, text="Quit",
                                         command=lambda: controller.up_frame(welcome_page))
        self.button_quit.grid(row=2, column=1, padx=10, pady=10)


class welcome_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

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
        self.frame_bottom.rowconfigure(0, weight=1)

        # Text Welcome
        self.string_wlcm = tkinter.StringVar(value="Welcome to the Assessment Management System")
        self.label_wlcm = ctk.CTkLabel(master=self.frame_top, textvariable=self.string_wlcm, width=120,
                                       height=25)
        self.label_wlcm.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Button User
        self.button_user = ctk.CTkButton(master=self.frame_middle, text="User",
                                         command=lambda: controller.up_frame(user_page))
        self.button_user.grid(row=1, column=1, padx=10, pady=10)

        # Button Admin
        self.button_admin = ctk.CTkButton(master=self.frame_middle, text="Admin",
                                          command=lambda: controller.up_frame(admin_page))
        self.button_admin.grid(row=2, column=1, padx=10, pady=10)
