import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import customtkinter
import os
from PIL import Image
import main

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.scanner = main.Scanner()



        self.title("image_example.py")
        self.geometry("700x450")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example", 
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.frame_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark", ],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        # Create home frame

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Duplicates Detector",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.home_frame_label.grid(row=0, column=0, padx=20, pady=20)
        
        # Disk Utilization frame
        self.diskutil_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.diskutil_frame.grid_columnconfigure(0, weight=1)

        # Home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_frame.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        # self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        # self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            # destroy the previous frame if it exists
            self.home_frame.grid_forget()
            # create a new frame
            self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.home_frame.grid_columnconfigure(0, weight=1)
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Duplicates Detector",
                                                                compound="center", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.home_frame_label.grid(row=0, column=0, padx=20, pady=20)
            self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Find Duplicates", command=self.home_frame_button_event)
            self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
            

        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def frame_button_event(self):
        self.select_frame_by_name("home")
    
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def home_frame_button_event(self):
        # use tkinter library to open a file dialog box to select a folder to scan
        folder = tk.filedialog.askdirectory()
        # call the find_duplicates function from Scanner\main.py
        self.dups = self.scanner.find_duplicates(folder)

        files=[]
        for i in self.dups:
            files.append(self.dups[i])

        if files:
            self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Remove Duplicates", command=self.remove_home_frame_button_event)
            self.home_frame_button_2.grid(row=1, column=0, padx=20, pady=0)
            # create a box to display the duplicate files  in .grid(row=2, column=0, padx=20, pady=10)
            # overwrite the previous label if it exists with the new label
            
            self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Duplicates Found",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.home_frame_label.grid(row=2, column=0, padx=20, pady=20)

            self.scrollable_frame = customtkinter.CTkScrollableFrame(self.home_frame, label_text="List of Duplicates", height=500)
            self.scrollable_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
            self.scrollable_frame.grid_columnconfigure((0,1), weight=1)
            self.variables=[]
            for i in range(len(files)):
                size = os.path.getsize(files[i][0])
                self.variables.append(tk.IntVar(value=0))
                for j in range(len(files[i])):
                    switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=files[i][j], variable=self.variables[i])
                    switch.grid(row=i, column=0, padx=10, pady=20)
                    switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=size)
                    switch2.grid(row=i, column=1, padx=10, pady=20)
                    
        else:
            self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="No Duplicates Found",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.home_frame_label.grid(row=2, column=0, padx=20, pady=20)
            

    def remove_home_frame_button_event(self):

        # use tkinter library to open a file dialog box to select a folder to scan
        # call the find_duplicates function from Scanner\main.py
        ans=self.check_marked()
        if self.scanner.remove_duplicates(ans):
            self.scrollable_frame.grid_forget()
            self.home_frame_label.grid_forget()
            self.home_frame_button_2.grid_forget()

            self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Find Duplicates", command=self.home_frame_button_event)
            self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Duplicates Deleted",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.home_frame_label.grid(row=2, column=0, padx=20, pady=20)   


    def check_marked(self):
        keys=list(self.dups.keys())
        ans={}
        for x in range(len(self.variables)):
            value=self.variables[x].get()
            if value!=0:
                ans[keys[x]]=self.dups[keys[x]]
        return ans
                

        

if __name__ == "__main__":
    app = App()
    app.mainloop()


