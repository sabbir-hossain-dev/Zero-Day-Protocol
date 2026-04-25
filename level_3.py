import customtkinter as ctk
import tkinter.messagebox as messagebox
import random

class LevelThree(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.master = master
        
        # Hardcore Boss State
        self.trace_level = 0.4    
        self.decrypt_level = 0.0  
        self.time_left = 60       
        self.timer_running = True
        self.current_hex = self.generate_hex()

        # --- UI ELEMENTS (High-Contrast Cyberpunk) ---
        self.title_label = ctk.CTkLabel(self, text="[ ! ] LEVEL 3: ROOT ACCESS [ ! ]", font=("Courier New", 24, "bold"), text_color="#FF4500")
        self.title_label.pack(pady=(15, 5))

        self.timer_label = ctk.CTkLabel(self, text=f">> SYSTEM PURGE IN: {self.time_left}s <<", font=("Courier New", 18, "bold"), text_color="#FF0000")
        self.timer_label.pack(pady=5)

        self.display_box = ctk.CTkTextbox(self, width=640, height=140, font=("Courier New", 14), text_color="#00FF41", fg_color="#0a0a0a", border_color="#FF4500", border_width=1, corner_radius=0)
        self.display_box.pack(pady=10)
        self.display_box.insert("0.0", "Target: DEFENSE MAINFRAME\nObjective: Decrypt Payload to 100% and Execute Root.\nWarning: Military AI Active. Trace increasing rapidly!\n\nWaiting for command...\n")
        self.display_box.configure(state="disabled")

        # --- PROGRESS BARS ---
        self.bars_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bars_frame.pack(pady=5)

        # Trace Bar (Red)
        self.trace_label = ctk.CTkLabel(self.bars_frame, text="ACTIVE TRACE", font=("Courier New", 12, "bold"), text_color="#FF0000")
        self.trace_label.grid(row=0, column=0, padx=10, sticky="w")
        self.trace_bar = ctk.CTkProgressBar(self.bars_frame, width=300, progress_color="#FF0000", fg_color="#330000", border_width=1, border_color="#FF0000", corner_radius=0)
        self.trace_bar.set(self.trace_level)
        self.trace_bar.grid(row=1, column=0, padx=10)

        # Decrypt Bar (Green)
        self.decrypt_label = ctk.CTkLabel(self.bars_frame, text="DECRYPTION STATUS", font=("Courier New", 12, "bold"), text_color="#00FF41")
        self.decrypt_label.grid(row=0, column=1, padx=10, sticky="w")
        self.decrypt_bar = ctk.CTkProgressBar(self.bars_frame, width=300, progress_color="#00FF41", fg_color="#003311", border_width=1, border_color="#00FF41", corner_radius=0)
        self.decrypt_bar.set(self.decrypt_level)
        self.decrypt_bar.grid(row=1, column=1, padx=10)

        # --- BUTTONS FRAME ---
        # FIXED: Removed specific colors from base style to prevent conflicts
        base_btn_style = {
            "font": ("Courier New", 13, "bold"),
            "corner_radius": 0,          
            "border_width": 1,           
            "fg_color": "#0a0a0a",       
            "hover_color": "#003311",    
            "height": 40
        }

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=20)

        # ROW 0
        self.btn_scan = ctk.CTkButton(self.btn_frame, text=">_ SCAN MEMORY", command=self.scan_memory, border_color="#00AAFF", text_color="#00AAFF", width=160, **base_btn_style)
        self.btn_scan.grid(row=0, column=0, padx=5, pady=5)

        self.hex_entry = ctk.CTkEntry(self.btn_frame, placeholder_text="0x0000", font=("Courier New", 14), text_color="#00FF41", fg_color="#111111", border_color="#555555", corner_radius=0, width=140, height=40)
        self.hex_entry.grid(row=0, column=1, padx=5, pady=5)

        self.btn_inject = ctk.CTkButton(self.btn_frame, text=">_ INJECT HEX", command=self.inject_zero_day, border_color="#00FF41", text_color="#00FF41", width=160, **base_btn_style)
        self.btn_inject.grid(row=0, column=2, padx=5, pady=5)

        # ROW 1
        self.btn_stealth = ctk.CTkButton(self.btn_frame, text=">_ OBFUSCATE", command=self.obfuscate, border_color="#aaaaaa", text_color="#aaaaaa", width=160, **base_btn_style)
        self.btn_stealth.grid(row=1, column=0, padx=5, pady=5)

        self.btn_root = ctk.CTkButton(self.btn_frame, text=">_ EXECUTE ROOT", command=self.execute_root, border_color="#FF4500", text_color="#FF4500", fg_color="#1a0000", hover_color="#4d0000", corner_radius=0, border_width=2, width=140, height=40, font=("Courier New", 14, "bold"))
        self.btn_root.grid(row=1, column=1, padx=5, pady=5)

        self.btn_abort = ctk.CTkButton(self.btn_frame, text="[ DISCONNECT ]", command=self.abort_mission, fg_color="transparent", text_color="#555555", hover_color="#111111", corner_radius=0, width=160)
        self.btn_abort.grid(row=1, column=2, padx=5, pady=5)

        self.update_timer()

    # --- GAME LOGIC ---
    def generate_hex(self):
        return f"0x{random.randint(4096, 65535):04X}" # 1000 to FFFF range

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=f">> SYSTEM PURGE IN: {self.time_left}s <<")
            
            # Active AI Threat
            if self.time_left % 2 == 0:
                self.trace_level += 0.04
                self.trace_bar.set(self.trace_level)
                self.check_status()

            self.after(1000, self.update_timer) 
        elif self.time_left <= 0 and self.timer_running:
            self.game_over("TIME'S UP! Mainframe purged your connection.")

    def scan_memory(self):
        self.update_log("\n> Dumping memory registers...")
        self.update_log(f"  {self.generate_hex()}  {self.generate_hex()}  {self.generate_hex()}")
        self.update_log(f"  {self.generate_hex()}  [!] VULN_OFFSET: {self.current_hex}")
        self.update_log("> Input the VULN_OFFSET to inject payload.")

    def obfuscate(self):
        self.update_log("> Deploying smoke-screen. Trace level reduced.")
        self.trace_level = max(0.0, self.trace_level - 0.20)
        self.trace_bar.set(self.trace_level)

    def inject_zero_day(self):
        entered_hex = self.hex_entry.get().strip().upper()

        if entered_hex == self.current_hex:
            self.update_log(f"> Payload accepted at {self.current_hex}. Decrypting...")
            self.decrypt_level += 0.34  
            self.trace_level += 0.15    
            
            if self.decrypt_level > 1.0:
                self.decrypt_level = 1.0
                self.update_log("[+] DECRYPTION AT 100%. READY FOR ROOT EXECUTION.")
            
            self.current_hex = self.generate_hex() 
            self.hex_entry.delete(0, 'end')
        else:
            self.update_log(f"[!] INVALID OFFSET ({entered_hex}). Memory fault triggered!")
            self.trace_level += 0.35 
            
        self.decrypt_bar.set(self.decrypt_level)
        self.trace_bar.set(self.trace_level)
        self.check_status()

    def execute_root(self):
        if self.decrypt_level >= 0.99 and self.trace_level < 1.0:
            self.timer_running = False
            self.update_log("\n[!!! ROOT ACCESS GRANTED !!!]")
            self.update_log("Mainframe is now under your control. Zero-Day Protocol Complete.")
            messagebox.showinfo("VICTORY!", "YOU HAVE CONQUERED THE MAINFRAME!\n\nAll levels cleared successfully.")
            self.master.show_dashboard()
        else:
            self.update_log("[CRITICAL ERROR] Decryption incomplete. Root denied!")
            self.trace_level = 1.0
            self.trace_bar.set(self.trace_level)
            self.check_status()

    def check_status(self):
        if self.trace_level >= 1.0:
            self.game_over("TRACED BY MILITARY AI! Your terminal has been locked.")

    def game_over(self, reason):
        self.timer_running = False
        self.update_log(f"\n[SYSTEM FATAL ERROR] {reason}")
        self.btn_scan.configure(state="disabled")
        self.btn_inject.configure(state="disabled")
        self.btn_stealth.configure(state="disabled")
        self.btn_root.configure(state="disabled")
        self.hex_entry.configure(state="disabled")

    def abort_mission(self):
        self.timer_running = False
        self.master.show_dashboard()

    def update_log(self, text):
        self.display_box.configure(state="normal")
        self.display_box.insert("end", text + "\n")
        self.display_box.see("end")
        self.display_box.configure(state="disabled")