import tkinter as tk
import customtkinter
import os
from PIL import Image
import scan
from convert import convert_bytes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.scanner = scan.Scanner()
        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
        # self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "../assets/icon.png")), size=(26, 26))

        self.title("Disk Space Manager")
        self.geometry("700x500")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Disk Space Manager",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Duplicate Detection",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.select_home)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.diskutil_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Disk Utilization (By Drive)",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.select_diskutil)
        self.diskutil_button.grid(row=2, column=0, sticky="ew")

        self.diskfutil_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Disk Utilization (By File Type)",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.select_diskfutil)
        self.diskfutil_button.grid(row=3, column=0, sticky="ew")


        self.large_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Large Files Detection",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.select_large)
        self.large_button.grid(row=4, column=0, sticky="ew")
        
        self.infreq_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Infrequent Files",
                                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                        anchor="w", command=self.select_infreq)
        self.infreq_button.grid(row=5, column=0, sticky="ew")




        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.select_settings)
        self.settings_button.grid(row=7, column=0, sticky="ew")
        


        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark", ],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        

        # Create home frame

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Duplicates Detector",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.home_frame_label.grid(row=0, column=0, padx=20, pady=20)
        
        # create diskutil frame
        self.diskutil_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create diskfutil frame
        self.diskfutil_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create large frame
        self.large_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")    

        # create infreq frame
        self.infreq_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create settings frame
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent") 

        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.diskutil_button.configure(fg_color=("gray75", "gray25") if name == "diskutil" else "transparent")
        self.large_button.configure(fg_color=("gray75", "gray25") if name == "large" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")
        self.diskfutil_button.configure(fg_color=("gray75", "gray25") if name == "diskfutil" else "transparent")
        self.infreq_button.configure(fg_color=("gray75", "gray25") if name == "infreq" else "transparent")


        # show selected frame
        if name == "home":
            self.home_frame.grid_forget()
        
            self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.home_frame.grid_columnconfigure(0, weight=1)
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Duplicates Detector",
                                                                compound="center", font=customtkinter.CTkFont(size=25, weight="bold"))
            self.home_frame_label.grid(row=0, column=0, padx=20, pady=10)
            self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Find Duplicates", command=self.home_frame_button_event)
            self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
            

        else:
            self.home_frame.grid_forget()
        if name == "diskutil":
            self.diskutil_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.diskutil_frame.grid_columnconfigure(0, weight=1)
            
            self.diskutil_frame.grid(row=0, column=1, sticky="nsew")
            self.diskutil_frame_label = customtkinter.CTkLabel(self.diskutil_frame, text="Disk Utilization By Drive",
                                                                compound="center", font=customtkinter.CTkFont(size=25, weight="bold"))
            self.diskutil_frame_label.grid(row=0, column=0, padx=20, pady=10)
            
            self.util_frame_button_1 = customtkinter.CTkButton(self.diskutil_frame, text="Get Disk Utilization", command=self.diskutil_frame_button_event)
            self.util_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        else:
            self.diskutil_frame.grid_forget()

        if name == "diskfutil":
            self.diskfutil_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.diskfutil_frame.grid_columnconfigure(0, weight=1)
            
            self.diskfutil_frame.grid(row=0, column=1, sticky="nsew")
            self.diskfutil_frame_label = customtkinter.CTkLabel(self.diskfutil_frame, text="Disk Utilization By File Type",
                                                                compound="center", font=customtkinter.CTkFont(size=25, weight="bold"))
            self.diskfutil_frame_label.grid(row=0, column=0, padx=20, pady=10)
            
            self.util_frame_button_1 = customtkinter.CTkButton(self.diskfutil_frame, text="Get Disk Utilization", command=self.diskfutil_frame_button_event)
            self.util_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        else:
            self.diskfutil_frame.grid_forget()

        if name == "large":
            self.large_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.large_frame.grid_columnconfigure(0, weight=1)

            self.large_frame.grid(row=0, column=1, sticky="nsew")
            self.large_frame_label = customtkinter.CTkLabel(self.large_frame, text="Files Larger than {} MB".format(self.scanner.file_size_limit),
                                                                compound="center", font=customtkinter.CTkFont(size=25, weight="bold"))
            self.large_frame_label.grid(row=0, column=0, padx=20, pady=10)
            
            self.large_frame_button_1 = customtkinter.CTkButton(self.large_frame, text="List Files", command=self.large_frame_button_event)
            self.large_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        else:
            self.large_frame.grid_forget()
        
        if name == "infreq":
            self.infreq_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.infreq_frame.grid_columnconfigure(0, weight=1)

            self.infreq_frame.grid(row=0, column=1, sticky="nsew")
            self.infreq_frame_label = customtkinter.CTkLabel(self.infreq_frame, text="Infrequent Files",
                                                                compound="center", font=customtkinter.CTkFont(size=25, weight="bold"))
            self.infreq_frame_label.grid(row=0, column=0, padx=20, pady=10)

            self.infreq_frame_button_1 = customtkinter.CTkButton(self.infreq_frame, text="Get Infrequent Files", command=self.infreq_frame_button_event)
            self.infreq_frame_button_1.grid(row=1, column=0, padx=20, pady=10)



        else:
            self.infreq_frame.grid_forget()


        if name=="settings":
            self.settings_frame=customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.settings_frame.grid_columnconfigure(2, weight=1)

            self.settings_frame.grid(row=0, column=1, sticky="nsew")
            self.settings_frame_label=customtkinter.CTkLabel(self.settings_frame, text="Settings Menu",compound="center", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.settings_frame_label.grid(row=0, column=0, padx=20, pady=20)

            self.hashfunc_label = customtkinter.CTkLabel(self.settings_frame, text="Hash Function", justify="left", font=customtkinter.CTkFont(size=20, weight="bold"), anchor='w',compound="left")
            self.hashfunc_label.grid(row=1, column=0, padx=20, pady=(20,5), sticky="nsew")
            
            selected_var=customtkinter.StringVar(value=self.scanner.hashalgo)
            self.hashfunc_menu = customtkinter.CTkOptionMenu(self.settings_frame, values=["md5", "blake2b", "sha1", "sha256", "sha512", "sha3_256", "sha3_512", "shake_128", "shake_256", "xxh64", "xxh128", "xxh3_64", "xxh3_128"],
                                                                command=self.change_hashfunc_event, variable=selected_var )
            self.hashfunc_menu.grid(row=2, column=0, padx=20, pady=(5,20), sticky="nsew")

            
            self.large_file_size_limit_label = customtkinter.CTkLabel(self.settings_frame, text="Large File Size Limit (MB)" , font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", compound="left")
            self.large_file_size_limit_label.grid(row=3, column=0, padx=20, pady=(20,5), sticky="nsew")
            self.large_file_size_limit = customtkinter.CTkEntry(self.settings_frame, placeholder_text=">100 MB", justify="center")
            self.large_file_size_limit.grid(row=4, column=0, padx=20, pady=(5,20), sticky="nsew")
            #button to save size limit
            self.large_file_size_limit_button = customtkinter.CTkButton(self.settings_frame, text="Save", command=self.set_large_file_size_limit)
            self.large_file_size_limit_button.grid(row=4, column=1, padx=(0,20), pady=(5,20), sticky="nsew")

            self.infreq_file_time_limit_label = customtkinter.CTkLabel(self.settings_frame, text="Infrequent File Time Limit (Days)" , font=customtkinter.CTkFont(size=20, weight="bold"), anchor="w", compound="left")
            self.infreq_file_time_limit_label.grid(row=5, column=0, padx=20, pady=(20,5), sticky="nsew")
            self.infreq_file_time_limit = customtkinter.CTkEntry(self.settings_frame, placeholder_text=">30 Days", justify="center")
            self.infreq_file_time_limit.grid(row=6, column=0, padx=20, pady=(5,20), sticky="nsew")
            #button to save time limit
            self.infreq_file_time_limit_button = customtkinter.CTkButton(self.settings_frame, text="Save", command=self.set_freq_file_time_limit)
            self.infreq_file_time_limit_button.grid(row=6, column=1, padx=(0,20), pady=(5,20), sticky="nsew")



        else:
            self.settings_frame=customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.settings_frame.grid_forget()

    def select_home(self):
        self.select_frame_by_name("home")

    def select_settings(self):
        self.select_frame_by_name("settings")

    def change_hashfunc_event(self, new_hashfunc):
        self.scanner.hashalgo = new_hashfunc
    
    def set_large_file_size_limit(self):
        size_limit = self.large_file_size_limit.get()
        if size_limit and size_limit.isdigit():
            self.scanner.file_size_limit = int(size_limit)
            self.large_file_size_limit_saved_label = customtkinter.CTkLabel(self.settings_frame, text="Saved!", fg_color="green", compound="center", corner_radius=10 , width=100 )
            self.large_file_size_limit_saved_label.grid(row=5, column=1, padx=20, pady=(5,20), sticky="nsew")
            self.after(2000, lambda: self.large_file_size_limit_saved_label.grid_forget())
        else:
            self.large_file_size_limit_saved_label = customtkinter.CTkLabel(self.settings_frame, text="Invalid Size Limit", fg_color="red", compound="center", corner_radius=10 , width=100 )
            self.large_file_size_limit_saved_label.grid(row=5, column=1, padx=20, pady=(5,20), sticky="nsew")
            self.after(2000, lambda: self.large_file_size_limit_saved_label.grid_forget())        

    def set_freq_file_time_limit(self):
        time_limit = self.infreq_file_time_limit.get()
        if time_limit and time_limit.isdigit():
            self.scanner.time_limit = int(time_limit)
            self.infreq_file_time_limit_saved_label = customtkinter.CTkLabel(self.settings_frame, text="Saved!", fg_color="green", compound="center", corner_radius=10 , width=100 )
            self.infreq_file_time_limit_saved_label.grid(row=7, column=1, padx=20, pady=(5,20), sticky="nsew")
            self.after(2000, lambda: self.infreq_file_time_limit_saved_label.grid_forget())
        else:
            self.infreq_file_time_limit_saved_label = customtkinter.CTkLabel(self.settings_frame, text="Invalid Time Limit", fg_color="red", compound="center", corner_radius=10 , width=100 )
            self.infreq_file_time_limit_saved_label.grid(row=7, column=1, padx=20, pady=(5,20), sticky="nsew")
            self.after(2000, lambda: self.infreq_file_time_limit_saved_label.grid_forget())

    def select_diskutil(self):
        self.select_frame_by_name("diskutil")

    def select_diskfutil(self):
        self.select_frame_by_name("diskfutil")

    def select_large(self):
        self.select_frame_by_name("large")

    def select_infreq(self):
        self.select_frame_by_name("infreq")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def home_frame_button_event(self):
        
        folder = tk.filedialog.askdirectory()
        self.dups = self.scanner.find_duplicates(folder)
        
        files=[]
        for i in self.dups:
            if len(self.dups[i])>1:
                files.append(self.dups[i])
        if files:
            self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Remove Duplicates", command=self.remove_home_frame_button_event)
            self.home_frame_button_2.grid(row=1, column=0, padx=20, pady=0)
            
            self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Duplicates Found",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.home_frame_label.grid(row=2, column=0, padx=20, pady=10)

            # set height of scrollable frame to 80% of window height
            
            self.scrollable_frame = customtkinter.CTkScrollableFrame(self.home_frame, label_text="Duplicates", height=250)
            self.scrollable_frame.grid(row=3, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.scrollable_frame.grid_columnconfigure(0, weight=2)
            self.scrollable_frame.grid_columnconfigure((1,2), weight=1)

            self.variables=[]
            
            switch = customtkinter.CTkLabel(master=self.scrollable_frame, text="File Path", fg_color="grey")
            switch.grid(row=0, column=0,sticky="nsew")
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="File size", fg_color="grey")
            switch2.grid(row=0, column=1, sticky="nsew")
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="Number of Duplicates", fg_color="grey")
            switch2.grid(row=0, column=2, sticky="nsew")
            switch2._label.configure(wraplength=150)
            for i in range(1,len(files)+1):
                size = convert_bytes(len(files[i-1])*os.path.getsize(files[i-1][0]))
                self.variables.append(tk.IntVar(value=0))
            
                switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=files[i-1][0], variable=self.variables[i-1])
                switch.grid(row=i, column=0, padx=10, pady=20, sticky="nsew")
                switch._text_label.configure(wraplength=300)
                switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=size)
                switch2.grid(row=i, column=1, padx=10, pady=20, sticky="nsew")
                switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=len(files[i-1]))
                switch2.grid(row=i, column=2, padx=10, pady=20, sticky="nsew")
                
        else:
            self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="No Duplicates Found",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.home_frame_label.grid(row=2, column=0, padx=20, pady=20)
            

    def remove_home_frame_button_event(self):

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

    def diskutil_frame_button_event(self):
        ans=self.scanner.find_disk_utilization()
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.diskutil_frame, label_text="Disk Utilization")
        self.scrollable_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=2)
        self.scrollable_frame.grid_columnconfigure((1,2), weight=1)
        switch = customtkinter.CTkLabel(master=self.scrollable_frame, text="Drive Name", fg_color="grey")
        switch.grid(row=0, column=0,sticky="nsew")
        switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="Free Space (GB)", fg_color="grey")
        switch2.grid(row=0, column=1, sticky="nsew")
        switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="Total Size (GB)", fg_color="grey")
        switch2.grid(row=0, column=2,sticky="nsew")
        for i in range(1,len(ans[0])+1):
            switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[0][i-1])
            switch.grid(row=i, column=0, padx=10, pady=20)
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[1][i-1])
            switch2.grid(row=i, column=1, padx=10, pady=20)
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[2][i-1])
            switch2.grid(row=i, column=2, padx=10, pady=20)

    
    def diskfutil_frame_button_event(self):
        folder = tk.filedialog.askdirectory()
        ans= self.scanner.find_file_usage(folder)
    
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.diskfutil_frame, label_text="Disk Utilization By File Type", height=300) 
        self.scrollable_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure((0,1,2), weight=1)

        switch = customtkinter.CTkLabel(master=self.scrollable_frame, text="File Type", fg_color="grey")
        switch.grid(row=0, column=0,sticky="nsew")
        switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="File size (Bytes)", fg_color="grey")
        switch2.grid(row=0, column=1, sticky="nsew")
        switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="Number of Files", fg_color="grey")
        switch2.grid(row=0, column=2,sticky="nsew")

        for i in range(1,len(ans)+1):
            switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[i-1][0])
            switch.grid(row=i, column=0, padx=10, pady=20)
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[i-1][1])
            switch2.grid(row=i, column=1, padx=10, pady=20)
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[i-1][2])
            switch2.grid(row=i, column=2, padx=10, pady=20)

    def large_frame_button_event(self):
        folder = tk.filedialog.askdirectory()
        ans=self.scanner.find_large_files(folder)
        self.large=ans
        # print(ans)
        if ans:
            # button for deleting large files
            self.large_frame_button_2 = customtkinter.CTkButton(self.large_frame, text="Delete Large Files", command=self.remove_large_frame_button_event)
            self.large_frame_button_2.grid(row=1, column=0, padx=20, pady=0)


            self.scrollable_frame = customtkinter.CTkScrollableFrame(self.large_frame, label_text="Large Files", height=300)
            self.scrollable_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
            self.scrollable_frame.grid_columnconfigure((0,1), weight=1)
    
            self.variables=[]
            switch = customtkinter.CTkLabel(master=self.scrollable_frame, text="File Path", fg_color="grey")
            switch.grid(row=0, column=0,sticky="nsew")
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="File size (Bytes)", fg_color="grey")
            switch2.grid(row=0, column=1, sticky="nsew")

            for i in range(1,len(ans)+1):
                self.variables.append(tk.IntVar(value=0))
                switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=ans[i-1][0], variable=self.variables[i-1])
                switch.grid(row=i, column=0, padx=10, pady=20, sticky="nsew")
                switch._text_label.configure(wraplength=360)
                switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[i-1][1])
                switch2.grid(row=i, column=1, padx=10, pady=20, sticky="nsew")
        else:
            self.home_frame_label = customtkinter.CTkLabel(self.large_frame, text="No Large Files Found",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))

            self.home_frame_label.grid(row=2, column=0, padx=20, pady=20)

    def remove_large_frame_button_event(self):
        ans=[]
        for x in range(len(self.variables)):
            value=self.variables[x].get()
            if value!=0:
                ans.append(self.large[x][0])  
        if self.scanner.delete_infrequent_files(ans):
            self.scrollable_frame.grid_forget()
            self.large_frame_label.grid_forget()
            self.large_frame_button_2.grid_forget()

            self.large_frame_button_1 = customtkinter.CTkButton(self.large_frame, text="List Files", command=self.large_frame_button_event)
            self.large_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.large_frame_label = customtkinter.CTkLabel(self.large_frame, text="Large Files Deleted",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.large_frame_label.grid(row=2, column=0, padx=20, pady=20)
                
    def infreq_frame_button_event(self):
        folder = tk.filedialog.askdirectory()
        ans=self.scanner.show_infrequent_files(folder)
        self.infreq=ans
        if ans:
            self.infreq_frame_button_2 = customtkinter.CTkButton(self.infreq_frame, text="Delete Infrequent Files", command=self.remove_infreq_frame_button_event)
            self.infreq_frame_button_2.grid(row=1, column=0, padx=20, pady=0)


            self.scrollable_frame = customtkinter.CTkScrollableFrame(self.infreq_frame, label_text="Infrequent Files", height=300)
            self.scrollable_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
            self.scrollable_frame.grid_columnconfigure(0, weight=2)
            self.scrollable_frame.grid_columnconfigure((1,2), weight=1)
            self.variables=[]
            switch = customtkinter.CTkLabel(master=self.scrollable_frame, text="File Path", fg_color="grey")
            switch.grid(row=0, column=0,sticky="nsew")
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="File size", fg_color="grey")
            switch2.grid(row=0, column=1, sticky="nsew")
            switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text="Last Accessed on", fg_color="grey")
            switch2.grid(row=0, column=2,sticky="nsew")
            for i in range(1,len(ans)):
                self.variables.append(tk.IntVar(value=0))
                switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=ans[i-1][0], variable=self.variables[i-1])
                switch.grid(row=i, column=0, padx=10, pady=20, sticky="nsew")
                switch._text_label.configure(wraplength=250)
                switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[i-1][1])
                switch2.grid(row=i, column=1, padx=10, pady=20, sticky="nsew")
                switch2 = customtkinter.CTkLabel(master=self.scrollable_frame, text=ans[i-1][2])
                switch2.grid(row=i, column=2, padx=10, pady=20, sticky="nsew")

        else:
            self.home_frame_label = customtkinter.CTkLabel(self.infreq_frame, text="No Infrequent Files Found",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.home_frame_label.grid(row=2, column=0, padx=20, pady=20)        

    def remove_infreq_frame_button_event(self):
        ans=[]
        for x in range(len(self.variables)):
            value=self.variables[x].get()
            if value!=0:
                ans.append(self.infreq[x][0])  
        if self.scanner.delete_infrequent_files(ans):
            self.scrollable_frame.grid_forget()
            self.infreq_frame_label.grid_forget()
            self.infreq_frame_button_2.grid_forget()

            self.infreq_frame_button_1 = customtkinter.CTkButton(self.infreq_frame, text="Get Infrequent Files", command=self.infreq_frame_button_event)
            self.infreq_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.infreq_frame_label = customtkinter.CTkLabel(self.infreq_frame, text="Infrequent Files Deleted",
                                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.infreq_frame_label.grid(row=2, column=0, padx=20, pady=20)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()


