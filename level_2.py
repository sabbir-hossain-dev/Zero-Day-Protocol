import customtkinter as ctk
import tkinter.messagebox as messagebox
import random

class LevelTwo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.master = master
        
        # Hardcore Game State
        self.trace_level = 0.2 
        self.time_left = 35    
        self.timer_running = True
        self.proxy_active = False
        self.secure_ip = "10.42.0.1" 

        # --- UI ELEMENTS (Cyberpunk Style) ---
        self.title_label = ctk.CTkLabel(self, text="[ / / / ] LEVEL 2: PROXY CHAIN", font=("Courier New", 22, "bold"), text_color="#00FF41")
        self.title_label.pack(pady=(20, 10))

        self.timer_label = ctk.CTkLabel(self, text=f">> TIME REMAINING: {self.time_left}s <<", font=("Courier New", 16, "bold"), text_color="#FF0000")
        self.timer_label.pack(pady=5)

        self.display_box = ctk.CTkTextbox(self, width=600, height=140, font=("Courier New", 14), text_color="#00FF41", fg_color="#0a0a0a", border_color="#00FF41", border_width=1, corner_radius=0)
        self.display_box.pack(pady=10)
        self.display_box.insert("0.0", "Target: Corporate Bank Server\nWarning: Active Counter-Measures Detected!\nTrace is increasing automatically. Find a secure proxy fast.\n\nWaiting for command...\n")
        self.display_box.configure(state="disabled")

        self.trace_label = ctk.CTkLabel(self, text=">> ACTIVE SYSTEM TRACE <<", font=("Courier New", 12, "bold"), text_color="#FF0000")
        self.trace_label.pack()
        self.trace_bar = ctk.CTkProgressBar(self, width=400, progress_color="#FF0000", fg_color="#330000", border_width=1, border_color="#FF0000", corner_radius=0)
        self.trace_bar.set(self.trace_level)
        self.trace_bar.pack(pady=(0, 20))

        # --- Cyberpunk Button Style ---
        btn_style = {
            "font": ("Courier New", 13, "bold"),
            "corner_radius": 0,          
            "border_width": 1,           
            "fg_color": "#0a0a0a",       
            "text_color": "#00FF41",     
            "hover_color": "#003311",    
            "height": 40
        }

        # --- BUTTONS FRAME ---
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack()

        # 1. Scan Proxies
        self.btn_scan = ctk.CTkButton(self.btn_frame, text=">_ SCAN NODES", command=self.scan_proxies, border_color="#00FF41", width=130, **btn_style)
        self.btn_scan.grid(row=0, column=0, padx=5)

        # 2. Proxy IP Input
        self.ip_entry = ctk.CTkEntry(self.btn_frame, placeholder_text="Node IP...", font=("Courier New", 14), text_color="#00FF41", fg_color="#111111", border_color="#555555", corner_radius=0, width=140, height=40)
        self.ip_entry.grid(row=0, column=1, padx=5)

        # 3. Route Connection (FIXED: Removed **btn_style and added explicit styles)
        self.btn_route = ctk.CTkButton(self.btn_frame, text=">_ ROUTE IP", command=self.route_proxy, border_color="#00AAFF", text_color="#00AAFF", fg_color="#0a0a0a", hover_color="#003311", corner_radius=0, border_width=1, height=40, font=("Courier New", 13, "bold"), width=120)
        self.btn_route.grid(row=0, column=2, padx=5)

        # 4. Breach Firewall 
        self.btn_bypass = ctk.CTkButton(self.btn_frame, text=">_ BREACH", command=self.bypass_firewall, border_color="#FF0000", text_color="#FF0000", fg_color="#1a0000", hover_color="#4d0000", corner_radius=0, border_width=1, width=100, height=40, font=("Courier New", 14, "bold"))
        self.btn_bypass.grid(row=0, column=3, padx=5)

        # Abort Button
        self.btn_abort = ctk.CTkButton(self.btn_frame, text="[X]", command=self.abort_mission, fg_color="transparent", text_color="#555555", hover_color="#111111", corner_radius=0, width=40)
        self.btn_abort.grid(row=0, column=4, padx=5)

        # Start background timer
        self.update_timer()

    # --- GAME LOGIC ---
    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=f">> TIME REMAINING: {self.time_left}s <<")
            
            if self.time_left % 3 == 0 and not self.proxy_active:
                self.trace_level += 0.05
                self.trace_bar.set(self.trace_level)
                self.check_status()

            self.after(1000, self.update_timer) 
        elif self.time_left <= 0 and self.timer_running:
            self.game_over("TIME'S UP! Connection terminated by host.")

    def scan_proxies(self):
        self.update_log("> Scanning for vulnerable proxy nodes...")
        self.update_log(f"> Node 1: 192.168.1.55 (Compromised)")
        self.update_log(f"> Node 2: {self.secure_ip} (Encrypted & Safe)")
        self.update_log(f"> Node 3: 172.16.0.8 (Honeypot Detected)")
        self.update_log("> Enter the safe IP to route your connection.")

    def route_proxy(self):
        entered_ip = self.ip_entry.get().strip()
        
        if entered_ip == self.secure_ip:
            self.update_log(f"> Routing through {entered_ip}...")
            self.proxy_active = True
            self.trace_level = max(0, self.trace_level - 0.4) 
            self.trace_bar.set(self.trace_level)
            self.update_log("[+] Proxy active. Your IP is hidden. Execute breach!")
            self.ip_entry.configure(state="disabled")
        else:
            self.update_log(f"[!] ERROR: Node {entered_ip} is unstable or a trap!")
            self.trace_level += 0.3
            self.trace_bar.set(self.trace_level)
            self.check_status()

    def bypass_firewall(self):
        if self.trace_level < 0.8 and self.proxy_active:
            self.timer_running = False
            self.update_log("\n[SUCCESS] Firewall breached. Mainframe accessed!")
            messagebox.showinfo("Mission Success", "Level 2 Cleared! Returning to Main Menu.")
            self.master.show_dashboard()
        else:
            self.update_log("[ERROR] Access Denied! Need active proxy and low trace.")
            self.trace_level += 0.3
            self.trace_bar.set(self.trace_level)
            self.check_status()

    def check_status(self):
        if self.trace_level >= 1.0:
            self.game_over("TRACED! Security forces have locked your terminal.")

    def game_over(self, reason):
        self.timer_running = False
        self.update_log(f"\n[SYSTEM LOCKDOWN] {reason}")
        self.btn_scan.configure(state="disabled")
        self.btn_route.configure(state="disabled")
        self.btn_bypass.configure(state="disabled")
        self.ip_entry.configure(state="disabled")

    def abort_mission(self):
        self.timer_running = False 
        self.master.show_dashboard()

    def update_log(self, text):
        self.display_box.configure(state="normal")
        self.display_box.insert("end", text + "\n")
        self.display_box.see("end")
        self.display_box.configure(state="disabled")