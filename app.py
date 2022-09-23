import tkinter
import customtkinter as ctk
from pages import admin_page, user_page, welcome_page

# Create a button
def button_function():
    print("button pressed")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.geometry("400x400")
        self.title("Home Page")


        container = ctk.CTkFrame(self)
        container.grid(row=0, column=0, sticky="nsew")

        self.id = ctk.StringVar()
        self.id.set("welcome_page")

        self.frames = {}  # Dictionary of frames

        # welcome_page = welcome_page(container, self)
        # admin_page = admin_page(container, self)
        # user_page = user_page(container, self)

        self.pages = [welcome_page, admin_page, user_page] # List of frames

        for F in self.frames:
            frame = F(parent=container, controller=self)  # parent, controller
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[F] = frame

        self.up_frame(welcome_page)

    def up_frame(self, page_name):
        page = self.frames[page_name]
        page.tkraise()


# Generate Window
if __name__ == "__main__":
    app = App()
    app.mainloop()
