import customtkinter as ctk
import pages


# Create the main window taking the properties of ctk object
# Frame object that holds the pages
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.geometry("565x350")
        self.title("Attendance Management System")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Create the container that will hold all the pages
        container = ctk.CTkFrame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # self.id = ctk.StringVar()
        # self.id.set("welcome_page")

        self.frames = {}  # Dictionary of frames

        # List of pages
        self.p = [pages.welcome_page, pages.admin_page, pages.user_page]

        for F in self.p:
            # Create a frame object for each class (pages) in the list
            # Pages linked to the container (parent) and the app object (self)
            frame = F(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)
            # Add the frame to the dictionary
            self.frames[F] = frame
        # Raise the first page (welcome_page)
        self.up_frame(pages.welcome_page)

    # Raise the frame (page)
    def up_frame(self, page_name):
        page = self.frames[page_name]
        page.tkraise()

# Generate Window
if __name__ == "__main__":
    app = App()
    app.mainloop()
