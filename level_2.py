import customtkinter as ctk
import tkinter.messagebox as messagebox

class LevelTwo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.master = master
        
        self.trace_level = 0.2 
        self.time_left = 30    
        self.timer_running = True
        self.proxy_active = False

        # --- UI ELEMENTS ---
        self.title_label = ctk.CTkLabel(self, text="LEVEL 2: PROXY OVERRIDE", font=("Courier New", 24, "bold"), text_color="#00FF41")
        self.title_label.pack(pady=10)

        self.timer_label = ctk.CTkLabel(self, text=f"TIME REMAINING: {self.time_left}s", font=("Courier New", 18, "bold"), text_color="#FF0000")
        self.timer_label.pack(pady=5)

        self.display_box = ctk.CTkTextbox(self, width=600, height=150, font=("Courier New", 14), text_color="#00FF41", fg_color="#111111")
        self.display_box.pack(pady=10)
        self.display_box.insert("0.0", "Target: Corporate Bank Server\nObjective: Bypass Firewall within 30 seconds!\nWarning: Direct attacks will trigger immediate lockdown.\n\nWaiting for command...\n")
        self.display_box.configure(state="disabled")

        self.trace_bar = ctk.CTkProgressBar(self, width=400, progress_color="red")
        self.trace_bar.set(self.trace_level)
        self.trace_bar.pack(pady=20)

        # --- BUTTONS ---
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack()

        self.btn_proxy = ctk.CTkButton(self.btn_frame, text="1. Setup Proxy", command=self.setup_proxy, width=130)
        self.btn_proxy.grid(row=0, column=0, padx=10)
        
        self.btn_payload = ctk.CTkButton(self.btn_frame, text="2. Inject Payload", command=self.inject_payload, width=130, fg_color="#8B0000")
        self.btn_payload.grid(row=0, column=1, padx=10)

        self.btn_bypass = ctk.CTkButton(self.btn_frame, text="3. Bypass Firewall", command=self.bypass_firewall, width=130, fg_color="#00008B")
        self.btn_bypass.grid(row=0, column=2, padx=10)

        ctk.CTkButton(self.btn_frame, text="Abort", command=self.abort_mission, fg_color="#555555", width=80).grid(row=0, column=3, padx=10)

        self.update_timer()

    # --- GAME LOGIC ---
    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=f"TIME REMAINING: {self.time_left}s")
            
            self.after(1000, self.update_timer) 
        elif self.time_left <= 0 and self.timer_running:
            self.game_over("TIME'S UP! The connection was terminated by host.")

    def setup_proxy(self):
        self.update_log("> Bouncing connection through proxies...")
        self.proxy_active = True
        self.trace_level = max(0, self.trace_level - 0.2) 
        self.trace_bar.set(self.trace_level)
        self.update_log("[+] Proxy active. Trace risk reduced. Safe to inject payload.")

    def inject_payload(self):
        if not self.proxy_active:
            self.update_log("[!] WARNING: Direct injection detected! Massive trace spike.")
            self.trace_level += 0.6
        else:
            self.update_log("> Injecting payload... Firewall weakened.")
            self.trace_level += 0.2
            
        self.trace_bar.set(self.trace_level)
        self.check_status()

    def bypass_firewall(self):
        if self.trace_level < 0.8 and self.proxy_active:
            self.timer_running = False
            self.update_log("\n[SUCCESS] Firewall bypassed. Mainframe accessed!")
            messagebox.showinfo("Mission Success", "Level 2 Cleared! Returning to Main Menu.")
            self.master.show_dashboard()
        else:
            self.update_log("[ERROR] Access Denied! Need active proxy and weakened firewall.")

    def check_status(self):
        if self.trace_level >= 1.0:
            self.game_over("TRACED! Security forces have your location.")

    def game_over(self, reason):
        self.timer_running = False
        self.update_log(f"\n[SYSTEM LOCKDOWN] {reason}")
        self.btn_proxy.configure(state="disabled")
        self.btn_payload.configure(state="disabled")
        self.btn_bypass.configure(state="disabled")

    def abort_mission(self):
        self.timer_running = False 
        self.master.show_dashboard()

    def update_log(self, text):
        self.display_box.configure(state="normal")
        self.display_box.insert("end", text + "\n")
        self.display_box.see("end")
        self.display_box.configure(state="disabled")