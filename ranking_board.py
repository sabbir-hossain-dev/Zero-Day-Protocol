import customtkinter as ctk

class RankingBoard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.master = master

        # --- UI TITLE ---
        ctk.CTkLabel(self, text="[ GLOBAL LEADERBOARD ]", font=("Courier New", 24, "bold"), text_color="#00AAFF").pack(pady=(20, 10))

        # --- RANKING DATA (Dummy + Player) ---
        # Real world-e eta database theke ashe, ekhane amra list use korchi.
        self.leaderboard_data = [
            {"rank": 1, "name": "Neo_Root", "xp": 2500, "status": "Legend"},
            {"rank": 2, "name": "Ghost_In_Shell", "xp": 1800, "status": "Elite"},
            {"rank": 3, "name": "Acid_Burn", "xp": 1200, "status": "Override"},
            {"rank": 4, "name": "Zero_Cool", "xp": 950, "status": "Netrunner"},
            {"rank": 5, "name": "Cereal_Killer", "xp": 600, "status": "Netrunner"},
        ]

        # Player Data adding to the board
        player_entry = {"rank": "??", "name": "YOU (Player)", "xp": self.master.xp, "status": self.master.rank}
        self.leaderboard_data.append(player_entry)

        # --- TABLE HEADER ---
        header_frame = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=0)
        header_frame.pack(fill="x", padx=40, pady=5)
        
        ctk.CTkLabel(header_frame, text="RANK", width=80, font=("Courier New", 12, "bold")).grid(row=0, column=0, padx=10)
        ctk.CTkLabel(header_frame, text="OPERATIVE", width=200, font=("Courier New", 12, "bold")).grid(row=0, column=1, padx=10)
        ctk.CTkLabel(header_frame, text="XP", width=100, font=("Courier New", 12, "bold")).grid(row=0, column=2, padx=10)
        ctk.CTkLabel(header_frame, text="STATUS", width=150, font=("Courier New", 12, "bold")).grid(row=0, column=3, padx=10)

        # --- TABLE ROWS ---
        for i, entry in enumerate(self.leaderboard_data):
            row_color = "#0a0a0a" if entry["name"] != "YOU (Player)" else "#003311"
            text_color = "#00FF41" if entry["name"] != "YOU (Player)" else "#00AAFF"
            
            row_frame = ctk.CTkFrame(self, fg_color=row_color, corner_radius=0)
            row_frame.pack(fill="x", padx=40, pady=2)
            
            ctk.CTkLabel(row_frame, text=f"#{entry['rank']}", width=80, text_color=text_color).grid(row=0, column=0, padx=10)
            ctk.CTkLabel(row_frame, text=entry['name'], width=200, text_color=text_color, anchor="w").grid(row=0, column=1, padx=10)
            ctk.CTkLabel(row_frame, text=str(entry['xp']), width=100, text_color=text_color).grid(row=0, column=2, padx=10)
            ctk.CTkLabel(row_frame, text=entry['status'], width=150, text_color=text_color).grid(row=0, column=3, padx=10)

        # --- BACK BUTTON ---
        self.btn_back = ctk.CTkButton(self, text="[ RETURN TO TERMINAL ]", command=self.master.show_dashboard, 
                                     fg_color="transparent", border_width=1, border_color="#555555", 
                                     hover_color="#111111", corner_radius=0, width=250)
        self.btn_back.pack(pady=30)