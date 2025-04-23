import customtkinter as ctk
import tkinter.messagebox as messagebox

class LevelOne(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.master = master 
        self.trace_level = 0

        # UI Elements
        self.title_label = ctk.CTkLabel(self, text="LEVEL 1: LOCALHOST BREACH", font=("Courier New", 24, "bold"), text_color="#00FF41")
        self.title_label.pack(pady=20)

        self.display_box = ctk.CTkTextbox(self, width=600, height=150, font=("Courier New", 14), text_color="#00FF41", fg_color="#111111")
        self.display_box.pack(pady=10)
        self.display_box.insert("0.0", "Target: Small Startup Router\nObjective: Get Admin Password\n\nWaiting for command...\n")
        self.display_box.configure(state="disabled")

        self.trace_bar = ctk.CTkProgressBar(self, width=400, progress_color="red")
        self.trace_bar.set(0)
        self.trace_bar.pack(pady=20)

        # Buttons (Decisions)
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack()

        ctk.CTkButton(self.btn_frame, text="1. Nmap Scan", command=self.nmap_scan).grid(row=0, column=0, padx=10)
        ctk.CTkButton(self.btn_frame, text="2. Brute Force", command=self.brute_force, fg_color="#8B0000", hover_color="#600000").grid(row=0, column=1, padx=10)
        
        # Abort Button
        ctk.CTkButton(self.btn_frame, text="Abort Mission", command=self.master.show_dashboard, fg_color="#555555").grid(row=0, column=2, padx=10)

    # --- Game Logic Functions ---
    def nmap_scan(self):
        self.update_log("> Running Nmap... Found Port 22 open.")
        self.trace_level += 0.1
        self.trace_bar.set(self.trace_level)

    def brute_force(self):
        if self.trace_level < 0.1:
            self.update_log("[!] ALERT: Firewall detected! Trace Level critical.")
            self.trace_level = 0.9
            self.trace_bar.set(self.trace_level)
        else:
            self.update_log("[SUCCESS] Password Cracked! Level 1 Complete.")
            messagebox.showinfo("Mission Success", "Level 1 Cleared! Returning to Main Menu.")
            self.master.show_dashboard() 

    def update_log(self, text):
        self.display_box.configure(state="normal")
        self.display_box.insert("end", text + "\n")
        self.display_box.see("end")
        self.display_box.configure(state="disabled")