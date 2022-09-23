import tkinter
import customtkinter as ctk
from app import *

# Leave session button
class QuitButton(ctk.CTkButton):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.button_admin = ctk.CTkButton(master=self.pages.framemiddle, text="Quit",
                                          command=lambda: controller.up_frame(welcome_page))
        self.button_admin.grid(row=2, column=1, padx=10, pady=10)


# Enter button
class EnterButton(ctk.CTkButton):
    def __int__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.button_admin = ctk.CTkButton(master=self.pages.frame_middle, text="Click to Enter",
                                          command=lambda: controller.up_frame(admin_page))
        self.button_admin.grid(row=2, column=1, padx=10, pady=10)