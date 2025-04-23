import customtkinter as ctk
import tkinter.messagebox as messagebox

class LevelThree(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.master = master
        
        # Hard Difficulty
        self.trace_level = 0.3    
        self.decrypt_level = 0.0  
        self.time_left = 40       
        self.timer_running = True

        # --- UI ELEMENTS ---
        self.title_label = ctk.CTkLabel(self, text="LEVEL 3: ROOT ACCESS", font=("Courier New", 26, "bold"), text_color="#FF4500")
        self.title_label.pack(pady=10)

        self.timer_label = ctk.CTkLabel(self, text=f"SYSTEM PURGE IN: {self.time_left}s", font=("Courier New", 18, "bold"), text_color="#FF0000")
        self.timer_label.pack(pady=5)

        self.display_box = ctk.CTkTextbox(self, width=600, height=120, font=("Courier New", 14), text_color="#00FF41", fg_color="#111111")
        self.display_box.pack(pady=10)
        self.display_box.insert("0.0", "Target: Defense Mainframe\nObjective: Decrypt Payload to 100% and Execute Root.\nWarning: Active Counter-Measures Detected!\n")
        self.display_box.configure(state="disabled")

        # Trace Bar (Red)
        self.trace_label = ctk.CTkLabel(self, text="TRACE LEVEL", font=("Arial", 10, "bold"), text_color="red")
        self.trace_label.pack()
        self.trace_bar = ctk.CTkProgressBar(self, width=400, progress_color="red")
        self.trace_bar.set(self.trace_level)
        self.trace_bar.pack(pady=(0, 10))

        # Decrypt Bar (Green)
        self.decrypt_label = ctk.CTkLabel(self, text="DECRYPTION PROGRESS", font=("Arial", 10, "bold"), text_color="#00FF41")
        self.decrypt_label.pack()
        self.decrypt_bar = ctk.CTkProgressBar(self, width=400, progress_color="#00FF41")
        self.decrypt_bar.set(self.decrypt_level)
        self.decrypt_bar.pack(pady=(0, 20))

        # --- BUTTONS ---
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack()

        self.btn_stealth = ctk.CTkButton(self.btn_frame, text="1. Obfuscate (Hide)", command=self.obfuscate, width=130, fg_color="#333333")
        self.btn_stealth.grid(row=0, column=0, padx=10)
        
        self.btn_inject = ctk.CTkButton(self.btn_frame, text="2. Inject Zero-Day", command=self.inject_zero_day, width=130, fg_color="#8B0000")
        self.btn_inject.grid(row=0, column=1, padx=10)

        self.btn_root = ctk.CTkButton(self.btn_frame, text="3. EXECUTE ROOT", command=self.execute_root, width=130, fg_color="#FF4500", text_color="black")
        self.btn_root.grid(row=0, column=2, padx=10)

        ctk.CTkButton(self.btn_frame, text="Abort", command=self.abort_mission, fg_color="#555555", width=80).grid(row=0, column=3, padx=10)

        self.update_timer()

    # --- GAME LOGIC ---
    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=f"SYSTEM PURGE IN: {self.time_left}s")
            self.after(1000, self.update_timer) 
        elif self.time_left <= 0 and self.timer_running:
            self.game_over("TIME'S UP! Mainframe purged your connection.")

    def obfuscate(self):
        self.update_log("> Deploying smoke-screen. Trace level reduced.")
        self.trace_level = max(0.0, self.trace_level - 0.25)
        self.trace_bar.set(self.trace_level)

    def inject_zero_day(self):
        self.update_log("> Injecting payload... Decryption rising! (Trace Spike!)")
        self.decrypt_level += 0.35  
        self.trace_level += 0.30    
        
        if self.decrypt_level > 1.0:
            self.decrypt_level = 1.0
            
        self.decrypt_bar.set(self.decrypt_level)
        self.trace_bar.set(self.trace_level)
        self.check_status()

    def execute_root(self):
        if self.decrypt_level >= 0.99:
            self.timer_running = False
            self.update_log("\n[!!! ROOT ACCESS GRANTED !!!]")
            self.update_log("Mainframe is now under your control.")
            messagebox.showinfo("VICTORY!", "YOU HAVE CONQUERED THE ZERO-DAY PROTOCOL!\n\nAll levels cleared.")
            self.master.show_dashboard()
        else:
            self.update_log("[CRITICAL ERROR] Decryption incomplete. Alarms triggered!")
            self.trace_level = 1.0
            self.trace_bar.set(self.trace_level)
            self.check_status()

    def check_status(self):
        if self.trace_level >= 1.0:
            self.game_over("TRACED BY MILITARY AI! Your IP is logged.")

    def game_over(self, reason):
        self.timer_running = False
        self.update_log(f"\n[SYSTEM LOCKDOWN] {reason}")
        self.btn_stealth.configure(state="disabled")
        self.btn_inject.configure(state="disabled")
        self.btn_root.configure(state="disabled")

    def abort_mission(self):
        self.timer_running = False
        self.master.show_dashboard()

    def update_log(self, text):
        self.display_box.configure(state="normal")
        self.display_box.insert("end", text + "\n")
        self.display_box.see("end")
        self.display_box.configure(state="disabled")