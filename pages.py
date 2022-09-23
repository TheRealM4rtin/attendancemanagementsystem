import tkinter
import customtkinter as ctk


class admin_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        # Horizontal Frames
        self.frame_top = ctk.CTkFrame(self, bg="blue")
        self.frame_middle = ctk.CTkFrame(self, bg="blue")
        # self.frame_bottom = customtkinter.CTkFrame(self, bg="blue")
        # Grid Frames
        self.frame_top.grid(row=0, column=0, sticky="nsew")
        self.frame_middle.grid(row=1, column=0, sticky="nsew")
        # self.frame_bottom.grid(row=2, column=0, sticky="nsew")
        # Column config
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(1, weight=1)
        self.frame_middle.columnconfigure(2, weight=1)
        # Row Config
        self.frame_top.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(1, weight=1)
        self.frame_middle.rowconfigure(2, weight=1)

        # Text admin
        self.string_wlcm = tkinter.StringVar(value="Welcome A D M I N")
        self.label_wlcm = ctk.CTkLabel(master=self.frame_top, textvariable=self.string_wlcm, width=120,
                                                  height=25)
        self.label_wlcm.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

class user_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        # Horizontal Frames
        self.frame_top = ctk.CTkFrame(self, bg="blue")
        self.frame_middle = ctk.CTkFrame(self, bg="blue")
        # self.frame_bottom = customtkinter.CTkFrame(self, bg="blue")
        # Grid Frames
        self.frame_top.grid(row=0, column=0, sticky="nsew")
        self.frame_middle.grid(row=1, column=0, sticky="nsew")
        # self.frame_bottom.grid(row=2, column=0, sticky="nsew")
        # Column config
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(1, weight=1)
        self.frame_middle.columnconfigure(2, weight=1)
        # Row Config
        self.frame_top.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(1, weight=1)
        self.frame_middle.rowconfigure(2, weight=1)

        # Text admin
        self.string_wlcm = tkinter.StringVar(value="Welcome User")
        self.label_wlcm = ctk.CTkLabel(master=self.frame_top, textvariable=self.string_wlcm, width=120,
                                                  height=25)
        self.label_wlcm.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

class welcome_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        # Horizontal Frames
        self.frame_top = ctk.CTkFrame(self, bg="blue")
        self.frame_middle = ctk.CTkFrame(self, bg="blue")
        # self.frame_bottom = customtkinter.CTkFrame(self, bg="blue")
        # Grid Frames
        self.frame_top.grid(row=0, column=0, sticky="nsew")
        self.frame_middle.grid(row=1, column=0, sticky="nsew")
        # self.frame_bottom.grid(row=2, column=0, sticky="nsew")
        # Column config
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(0, weight=1)
        self.frame_middle.columnconfigure(1, weight=1)
        self.frame_middle.columnconfigure(2, weight=1)
        # Row Config
        self.frame_top.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(0, weight=1)
        self.frame_middle.rowconfigure(1, weight=1)
        self.frame_middle.rowconfigure(2, weight=1)

        # Text Welcome
        self.string_wlcm = tkinter.StringVar(value="Welcome to the Assessment Management System")
        self.label_wlcm = ctk.CTkLabel(master=self.frame_top, textvariable=self.string_wlcm, width=120,
                                                  height=25)
        self.label_wlcm.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # Button User
        self.button_user = ctk.CTkButton(master=self.frame_middle, text="User", command=lambda: controller.up_frame(user_page))
        self.button_user.grid(row=1, column=1, padx=10, pady=10)
        # Button Admin
        self.button_admin = ctk.CTkButton(master=self.frame_middle, text="Admin",
                                                     command=lambda: controller.up_frame(admin_page))
        self.button_admin.grid(row=2, column=1, padx=10, pady=10)
