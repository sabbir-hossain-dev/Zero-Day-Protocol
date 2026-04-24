import customtkinter as ctk
from level_1 import LevelOne
from level_2 import LevelTwo
from level_3 import LevelThree
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

    def show_level_3(self):
        if self.current_frame is not None:
            self.current_frame.destroy() 
        self.current_frame = LevelThree(self)
        self.current_frame.pack(fill="both", expand=True)    

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent") 
        self.master = master

        # --- Text-based Logo / Title ---
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=(40, 20))
        
        ctk.CTkLabel(title_frame, text="SYS_ADMIN @ LOCALHOST", font=("Courier New", 12), text_color="#555555").pack()
        ctk.CTkLabel(title_frame, text="[ / / / ]", font=("Courier New", 45, "bold"), text_color="#00FF41").pack()
        ctk.CTkLabel(title_frame, text="ZERO-DAY PROTOCOL", font=("Courier New", 35, "bold"), text_color="#00FF41").pack()
        ctk.CTkLabel(title_frame, text=">> UNAUTHORIZED ACCESS DETECTED <<", font=("Courier New", 12, "bold"), text_color="#FF0000").pack(pady=(5,0))

        ctk.CTkLabel(self, text="AVAILABLE EXPLOITS:", font=("Courier New", 14, "underline"), text_color="#aaaaaa").pack(pady=(10, 20))

        # --- Cyberpunk Button Style ---
        btn_style = {
            "font": ("Courier New", 16, "bold"),
            "corner_radius": 0,          
            "border_width": 2,           
            "fg_color": "#0a0a0a",       
            "text_color": "#00FF41",     
            "hover_color": "#003311",    
            "width": 320,
            "height": 45
        }

        self.lvl1_btn = ctk.CTkButton(self, text=">_ EXECUTE: LEVEL 1", command=self.master.show_level_1, border_color="#00FF41", **btn_style)
        self.lvl1_btn.pack(pady=8)

        self.lvl2_btn = ctk.CTkButton(self, text=">_ EXECUTE: LEVEL 2", command=self.master.show_level_2, border_color="#00FF41", **btn_style)
        self.lvl2_btn.pack(pady=8)

        self.lvl3_btn = ctk.CTkButton(self, text=">_ OVERRIDE: ROOT ACCESS", command=self.master.show_level_3, border_color="#FF0000", text_color="#FF0000", fg_color="#1a0000", hover_color="#4d0000", corner_radius=0, border_width=2, width=320, height=45, font=("Courier New", 16, "bold"))
        self.lvl3_btn.pack(pady=8)
        
        self.btn_exit = ctk.CTkButton(self, text="[ DISCONNECT ]", fg_color="transparent", text_color="#555555", hover_color="#111111", command=self.master.destroy, corner_radius=0, width=320)
        self.btn_exit.pack(pady=30)

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()