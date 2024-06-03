from tkinter import *
import customtkinter as ct
from PIL import Image

# class Key_Input(ct.CTk):
#     def __init__(self, master, text_value):
#         super().__init__(master)
#         self.grid_columnconfigure(0, weight=1)

#         entry1 = ct.CTkEntry(text=text_value)

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Better Steam Screenshots")
        self.geometry("600x400")
        self.grid_columnconfigure(0, weight=1)

        # Main Frame
        self.frame0 = ct.CTkFrame(master=self, corner_radius=5)
        self.frame0.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        # Image Frame
        self.image_frame = ct.CTkFrame(master=self.frame0)
        self.image_frame.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        logo = ct.CTkImage(Image.open(fr'better-screenshots/assets/steam_screenshots_logo.png'), size=(500,125))
        self.image_label = ct.CTkLabel(master=self.image_frame, text="", image=logo)
        self.image_label.grid(row=0, column=0, pady=(5,5))

        # Entry Frame
        self.frame1 = ct.CTkFrame(master=self.frame0, corner_radius=5)
        self.frame1.grid(row=1, column=0, padx=(5,5), pady=(5,5))

        self.key_label = ct.CTkLabel(master=self.frame1, text="Steam API Key:")
        self.key_label.grid(row=0, column=0, padx=10, pady=(5,5), sticky="nsw")

        self.dest_label = ct.CTkLabel(master=self.frame1, text="Destination Path:")
        self.dest_label.grid(row=1, column=0, padx=10, pady=(5,5), sticky="nsw")

        self.src_label = ct.CTkLabel(master=self.frame1, text="Screenshot Source:")
        self.src_label.grid(row=2, column=0, padx=10, pady=(5,5), sticky="nsw")

        self.key_entry = ct.CTkEntry(corner_radius=5, width=400, master=self.frame1, placeholder_text="Enter Steam API Key")
        self.key_entry.grid(row=0, column=1, padx=10, pady=(5,5), sticky="nsw")

        self.dest_entry = ct.CTkEntry(corner_radius=5, width=400, master=self.frame1, placeholder_text="Enter Destination Path")
        self.dest_entry.grid(row=1, column=1, padx=10, pady=(5,5), sticky="nsw")

        self.dest_entry = ct.CTkEntry(corner_radius=5, width=400, master=self.frame1, placeholder_text="Enter Destination Path")
        self.dest_entry.grid(row=2, column=1, padx=10, pady=(5,5), sticky="nsw")

        # Buttons Frame
        self.frame2 = ct.CTkFrame(master=self.frame0, corner_radius=5)
        self.frame2.grid(row=2, column=0, padx=(5,5), pady=(5,5))



app = App()
app.mainloop()