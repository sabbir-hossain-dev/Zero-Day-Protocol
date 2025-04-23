import customtkinter as ctk
from level_1 import LevelOne
from level_2 import LevelTwo
import tkinter.messagebox as messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class GameApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Zero-Day Protocol")
        self.geometry("700x500")
        self.resizable(False, False)

        self.current_frame = None 
        self.show_dashboard()

    def show_dashboard(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            
        self.current_frame = DashboardFrame(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_level_1(self):
        if self.current_frame is not None:
            self.current_frame.destroy() 
            
        self.current_frame = LevelOne(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_level_2(self):
        if self.current_frame is not None:
            self.current_frame.destroy() 
            
        self.current_frame = LevelTwo(self)
        self.current_frame.pack(fill="both", expand=True)

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent") 
        self.master = master

        ctk.CTkLabel(self, text="ZERO-DAY PROTOCOL", font=("Courier New", 32, "bold"), text_color="#00FF41").pack(pady=(60, 10))
        ctk.CTkLabel(self, text="Select Mission", font=("Courier New", 14)).pack(pady=(0, 30))

        # Level 1 Button 
        self.lvl1_btn = ctk.CTkButton(self, text="START LEVEL 1", command=self.master.show_level_1, width=300, height=50)
        self.lvl1_btn.pack(pady=10)

        # Level 2 Button
        self.lvl2_btn = ctk.CTkButton(self, text="START LEVEL 2", command=self.master.show_level_2, width=300, height=50)
        self.lvl2_btn.pack(pady=10)
        
        # Exit Button
        self.btn_exit = ctk.CTkButton(self, text="Exit System", fg_color="#8B0000", hover_color="#600000", command=self.master.destroy)
        self.btn_exit.pack(pady=20)

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()