import tkinter
import customtkinter as ctk
from app import *


class frame_top(ctk.CTkFrame):
    def __init__(self, row, column, sticky):
        ctk.CTkFrame.__init__(self, row, column, sticky)

        # Horizontal Frames
        self.frame_top = ctk.CTkFrame(self, bg="blue")
        self.frame_top.grid(row=row, column=column, sticky=sticky)


class frame_middle(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.frame_middle = ctk.CTkFrame(self, bg="blue")


class frame_bottom(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.frame_bottom = ctk.CTkFrame(self, bg="blue")