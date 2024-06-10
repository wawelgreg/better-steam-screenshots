from tkinter import *
import customtkinter as ct
from customtkinter import filedialog
from PIL import Image

import controller as ctrl
import log_manager as l



class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Better Steam Screenshots")
        self.geometry("600x400")
        self.grid_columnconfigure(0, weight=1)

        ct.set_appearance_mode("dark")

        # Main Frame
        self.frame0 = ct.CTkFrame(master=self, corner_radius=5)
        self.frame0.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        # Image Frame
        self.image_frame = ct.CTkFrame(master=self.frame0)
        self.image_frame.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        logo = ct.CTkImage(Image.open(fr'assets/steam_screenshots_logo.png'), size=(500,125))
        self.image_label = ct.CTkLabel(master=self.image_frame, text="", image=logo)
        self.image_label.grid(row=0, column=0, pady=(5,5))

        # Entry Frame
        self.frame1 = ct.CTkFrame(master=self.frame0, corner_radius=5)
        self.frame1.grid(row=1, column=0, padx=(5,5), pady=(5,5))

        self.key_label = ct.CTkLabel(master=self.frame1, text="Steam API Key:")
        self.key_label.grid(row=0, column=0, padx=10, pady=(5,5), sticky="nsw")

        self.src_label = ct.CTkLabel(master=self.frame1, text="Screenshot Source:")
        self.src_label.grid(row=1, column=0, padx=10, pady=(5,5), sticky="nsw")

        self.dest_label = ct.CTkLabel(master=self.frame1, text="Destination Path:")
        self.dest_label.grid(row=2, column=0, padx=10, pady=(5,5), sticky="nsw")

        t = ct.CTkTextbox(self)
        

        self.key_entry = ct.CTkEntry(corner_radius=5, width=400, master=self.frame1, placeholder_text="Enter Steam API Key")
        self.key_entry.grid(row=0, column=1, padx=10, pady=(5,5), sticky="nsw")

        self.src_entry = ct.CTkEntry(corner_radius=5, width=400, master=self.frame1, placeholder_text="Enter Source Path")
        self.src_entry.grid(row=1, column=1, padx=10, pady=(5,5), sticky="nsw")

        self.dest_entry = ct.CTkEntry(corner_radius=5, width=400, master=self.frame1, placeholder_text="Enter Destination Path")
        self.dest_entry.grid(row=2, column=1, padx=10, pady=(5,5), sticky="nsw")

        # Buttons Frame
        self.buttons_frame = ct.CTkFrame(master=self.frame0, corner_radius=5)
        self.buttons_frame.grid(row=2, column=0, padx=(5,5), pady=(5,5))

        BUTTON_WIDTH = 90

        # Source Selection Frame
        self.selection_buttons_frame = ct.CTkFrame(master=self.buttons_frame, corner_radius=5)
        self.selection_buttons_frame.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        self.src_button = ct.CTkButton(master=self.selection_buttons_frame, text="Choose\nSource", 
                                       width=BUTTON_WIDTH,
                                       command=self.src_button_click) # Prompts file dialog
        self.src_button.grid(row=0, column=0, padx=(5,5), pady=(5,5), sticky="nsw")

        self.dest_button = ct.CTkButton(master=self.selection_buttons_frame, text="Choose\nDestination", 
                                        width=BUTTON_WIDTH,
                                        command=self.dest_button_click) # Prompts file dialog
        self.dest_button.grid(row=0, column=1, padx=(5,5), pady=(5,5), sticky="nsw")

        # Save / Clear Frame
        # self.save_clear_buttons_frame = ct.CTkFrame(master=self.buttons_frame, corner_radius=5)
        # self.save_clear_buttons_frame.grid(row=0, column=1, padx=(5,5), pady=(5,5))

        self.save_button = ct.CTkButton(master=self.selection_buttons_frame, text="Save\nSelections", 
                                        width=BUTTON_WIDTH, fg_color="#246B1D",
                                        command=self.save_button_click)
        self.save_button.grid(row=0, column=2, padx=(5,5), pady=(5,5), sticky="nsw")

        self.clear_button = ct.CTkButton(master=self.selection_buttons_frame, text="Clear\nSelections", 
                                        width=BUTTON_WIDTH, fg_color="#6B1D1D",
                                        command=self.clear_button_click)
        self.clear_button.grid(row=0, column=3, padx=(5,5), pady=(5,5), sticky="nsw")

        # Run / Status Frame
        self.run_button_status_frame = ct.CTkFrame(master=self.buttons_frame, corner_radius=5)
        self.run_button_status_frame.grid(row=1, column=0, padx=(5,5), pady=(5,5))

        self.run_button = ct.CTkButton(master=self.run_button_status_frame, text="Sort my\nimages!", 
                                        width=BUTTON_WIDTH, fg_color="#246B1D",
                                        command=self.run_button_click, border_color="#CCCCCC", border_width=1)
        self.run_button.pack(padx=(5,5), pady=(5,5), side="left")
        # self.run_button.grid(row=0, column=0, padx=(5,5), pady=(5,5), sticky="nsw")

        DEFAULT_STATUS = "Welcome!"

        self.status_label = ct.CTkLabel(master=self.run_button_status_frame, text=DEFAULT_STATUS, width=290,
                                        anchor="w", fg_color="#25404E", corner_radius=8, height=39)
        self.status_label.pack(padx=(5,5), pady=(5,5))


    def update_label_text(self, label_obj: Label, new_text: str):
        label_obj.configure(text=new_text)        


    def set_text(self, e: Entry, text: str):
        e.delete(0, "end")
        e.insert(0, text)


    def src_button_click(self):
        selected_path = filedialog.askdirectory()
        self.set_text(self.src_entry, selected_path)


    def dest_button_click(self):
        selected_path = filedialog.askdirectory()
        self.set_text(self.dest_entry, selected_path)


    def save_button_click(self): # Set config values from corresponding entries
        l.log.info("Save button clicked")
        steam_key = self.key_entry.get()
        src_path = self.src_entry.get()
        dest_path = self.dest_entry.get()

        l.log.info("Saving settings...")
        ctrl.save_settings(steam_key, src_path, dest_path)
        l.log.info("Saving settings done")
        self.update_label_text(self.status_label, "Entries saved!")


    def clear_button_click(self): # Clear all entries
        self.key_entry.delete(0, 'end')
        self.src_entry.delete(0, 'end')
        self.dest_entry.delete(0, 'end')
        self.update_label_text(self.status_label, "Entries cleared, but still saved!")


    def run_button_click(self): # Run sort and storing algorithm
        self.update_label_text(self.status_label, "Sorting images...")
        ctrl.run_sort()
        self.update_label_text(self.status_label, "All images sorted! :)")


    def startup_procedures(self): # Load data file to front-end
        l.log.info("Loading saved settings...")
        temp_dict = ctrl.get_settings()
        self.set_text(self.key_entry, temp_dict["Key"])
        self.set_text(self.src_entry, temp_dict["Src"])
        self.set_text(self.dest_entry, temp_dict["Dest"])
        l.log.info("Loading settings done")



def main():
    l.log.info(">>> Starting front end app... <<<")
    app = App()
    app.startup_procedures()
    app.mainloop()



if __name__ == "__main__":
    main()