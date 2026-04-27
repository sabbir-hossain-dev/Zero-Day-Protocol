import customtkinter as ctk
from level_1 import LevelOne
from level_2 import LevelTwo
from level_3 import LevelThree
from ranking_board import RankingBoard  # Notun import
import tkinter.messagebox as messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class GameApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Zero-Day Protocol")
        self.geometry("700x500")
        self.resizable(False, False)

        # --- PLAYER STATS ---
        self.xp = 0
        self.rank = "Script Kiddie"

        self.current_frame = None 
        self.show_dashboard()

    # --- RANKING LOGIC ---
    def add_xp(self, amount):
        self.xp += amount
        self.check_rank()

    def check_rank(self):
        old_rank = self.rank
        if self.xp >= 1000:
            self.rank = "Zero-Day Legend"
        elif self.xp >= 500:
            self.rank = "SysAdmin Override"
        elif self.xp >= 300:
            self.rank = "Cyber Mercenary"
        elif self.xp >= 100:
            self.rank = "Netrunner"
        else:
            self.rank = "Script Kiddie"
            
        if old_rank != self.rank:
            messagebox.showinfo("RANK UP!", f"System upgrade!\n\nYou have been promoted to: {self.rank}")

    # --- NAVIGATION ---
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

    def show_rankings(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = RankingBoard(self)
        self.current_frame.pack(fill="both", expand=True)


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent") 
        self.master = master

        # --- Text-based Logo / Title ---
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=(25, 10))
        
        ctk.CTkLabel(title_frame, text="SYS_ADMIN @ LOCALHOST", font=("Courier New", 12), text_color="#555555").pack()
        ctk.CTkLabel(title_frame, text="[ / / / ]", font=("Courier New", 45, "bold"), text_color="#00FF41").pack()
        ctk.CTkLabel(title_frame, text="ZERO-DAY PROTOCOL", font=("Courier New", 35, "bold"), text_color="#00FF41").pack()
        
        # --- PLAYER PROFILE DISPLAY ---
        profile_text = f"USER RANK: {self.master.rank} | XP: {self.master.xp}"
        ctk.CTkLabel(title_frame, text=profile_text, font=("Courier New", 14, "bold"), text_color="#00AAFF").pack(pady=(5,0))
        
        ctk.CTkLabel(title_frame, text=">> UNAUTHORIZED ACCESS DETECTED <<", font=("Courier New", 12, "bold"), text_color="#FF0000").pack(pady=(5,0))

        # --- Cyberpunk Button Style ---
        btn_style = {
            "font": ("Courier New", 15, "bold"),
            "corner_radius": 0,          
            "border_width": 2,           
            "fg_color": "#0a0a0a",       
            "text_color": "#00FF41",     
            "hover_color": "#003311",    
            "width": 320,
            "height": 40
        }

        self.lvl1_btn = ctk.CTkButton(self, text=">_ INITIATE: LOCALHOST BREACH", command=self.master.show_level_1, border_color="#00FF41", **btn_style)
        self.lvl1_btn.pack(pady=6)

        self.lvl2_btn = ctk.CTkButton(self, text=">_ DEPLOY: PROXY OVERRIDE", command=self.master.show_level_2, border_color="#00FF41", **btn_style)
        self.lvl2_btn.pack(pady=6)

        self.lvl3_btn = ctk.CTkButton(self, text=">_ OVERRIDE: ROOT ACCESS", command=self.master.show_level_3, border_color="#FF0000", text_color="#FF0000", fg_color="#1a0000", hover_color="#4d0000", corner_radius=0, border_width=2, width=320, height=40, font=("Courier New", 15, "bold"))
        self.lvl3_btn.pack(pady=6)
        
        # --- NEW RANKING BUTTON ---
        self.rank_btn = ctk.CTkButton(self, text=">_ VIEW: GLOBAL RANKINGS", command=self.master.show_rankings, border_color="#00AAFF", text_color="#00AAFF", fg_color="#0a0a0a", hover_color="#001133", corner_radius=0, border_width=2, width=320, height=40, font=("Courier New", 15, "bold"))
        self.rank_btn.pack(pady=6)

        self.btn_exit = ctk.CTkButton(self, text="[ DISCONNECT ]", fg_color="transparent", text_color="#555555", hover_color="#111111", command=self.master.destroy, corner_radius=0, width=320)
        self.btn_exit.pack(pady=15)

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()