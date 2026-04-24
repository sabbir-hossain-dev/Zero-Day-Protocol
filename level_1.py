import customtkinter as ctk
import tkinter.messagebox as messagebox

class LevelOne(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.master = master 
        self.trace_level = 0.0

        # --- UI ELEMENTS (Cyberpunk Style) ---
        self.title_label = ctk.CTkLabel(self, text="[ / / / ] LEVEL 1: LOCALHOST BREACH", font=("Courier New", 22, "bold"), text_color="#00FF41")
        self.title_label.pack(pady=(20, 10))

        self.display_box = ctk.CTkTextbox(self, width=600, height=150, font=("Courier New", 14), text_color="#00FF41", fg_color="#0a0a0a", border_color="#00FF41", border_width=1, corner_radius=0)
        self.display_box.pack(pady=10)
        self.display_box.insert("0.0", "Target: Small Startup Router\nObjective: Scan Network, Find Open Port, and Execute Brute Force.\n\nWaiting for command...\n")
        self.display_box.configure(state="disabled")

        self.trace_label = ctk.CTkLabel(self, text=">> SYSTEM TRACE RISK <<", font=("Courier New", 12, "bold"), text_color="#FF0000")
        self.trace_label.pack()
        self.trace_bar = ctk.CTkProgressBar(self, width=400, progress_color="#FF0000", fg_color="#330000", border_width=1, border_color="#FF0000", corner_radius=0)
        self.trace_bar.set(self.trace_level)
        self.trace_bar.pack(pady=(0, 20))

        # --- Cyberpunk Style Dictionary ---
        btn_style = {
            "font": ("Courier New", 14, "bold"),
            "corner_radius": 0,          
            "border_width": 1,           
            "fg_color": "#0a0a0a",       
            "text_color": "#00FF41",     
            "hover_color": "#003311",    
            "height": 40
        }

        # Buttons Frame
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack()

        # Nmap Button
        self.btn_nmap = ctk.CTkButton(self.btn_frame, text=">_ NMAP SCAN", command=self.nmap_scan, border_color="#00FF41", width=140, **btn_style)
        self.btn_nmap.grid(row=0, column=0, padx=10)

        # NEW: Port Input Box
        self.port_entry = ctk.CTkEntry(self.btn_frame, placeholder_text="Target Port (e.g. 80)", font=("Courier New", 14), text_color="#00FF41", fg_color="#111111", border_color="#555555", corner_radius=0, width=180, height=40)
        self.port_entry.grid(row=0, column=1, padx=10)

        # Brute Force Button 
        self.btn_brute = ctk.CTkButton(self.btn_frame, text=">_ BRUTE FORCE", command=self.brute_force, border_color="#FF0000", text_color="#FF0000", fg_color="#1a0000", hover_color="#4d0000", corner_radius=0, border_width=1, width=140, height=40, font=("Courier New", 14, "bold"))
        self.btn_brute.grid(row=0, column=2, padx=10)
        
        # Abort Button 
        self.btn_abort = ctk.CTkButton(self.btn_frame, text="[ ABORT ]", command=self.master.show_dashboard, fg_color="transparent", text_color="#555555", hover_color="#111111", corner_radius=0, width=100)
        self.btn_abort.grid(row=0, column=3, padx=10)

    # --- Game Logic Functions ---
    def nmap_scan(self):
        self.update_log("> Initiating Stealth Scan...")
        self.update_log("> PORT STATE SERVICE")
        self.update_log("> 22/tcp open  ssh")
        self.update_log("> 80/tcp closed http")
        self.update_log("> Vulnerability detected on SSH port.")
        
        self.trace_level += 0.2
        self.trace_bar.set(self.trace_level)
        self.check_status()

    def brute_force(self):
        target_port = self.port_entry.get().strip()

        if target_port == "":
            self.update_log("[!] ERROR: Target port cannot be empty!")
            return

        if target_port == "22":
            self.update_log(f"> Initiating dictionary attack on Port {target_port}...")
            if self.trace_level < 0.8:
                self.update_log("\n[SUCCESS] Admin credentials acquired! Level 1 Complete.")
                messagebox.showinfo("Mission Success", "Level 1 Cleared! Returning to Main Menu.")
                self.master.show_dashboard() 
            else:
                self.update_log("[!] Trace level too high! Connection dropped.")
                self.game_over("BANNED BY FIREWALL")
        else:
            self.update_log(f"> Attempting brute force on Port {target_port}...")
            self.update_log("[!] FAILED: Port closed or heavily guarded. Trace spike!")
            self.trace_level += 0.4  # ভুল পোর্টে অ্যাটাক করলে ট্রেস অনেক বাড়বে
            self.trace_bar.set(self.trace_level)
            self.check_status()

    def check_status(self):
        if self.trace_level >= 1.0:
            self.game_over("TRACED! Local authorities have been alerted.")

    def game_over(self, reason):
        self.update_log(f"\n[SYSTEM LOCKDOWN] {reason}")
        self.btn_nmap.configure(state="disabled")
        self.btn_brute.configure(state="disabled")
        self.port_entry.configure(state="disabled")

    def update_log(self, text):
        self.display_box.configure(state="normal")
        self.display_box.insert("end", text + "\n")
        self.display_box.see("end")
        self.display_box.configure(state="disabled")