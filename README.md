# 🖥️ Zero-Day Protocol
### A Cybersecurity Simulation Game

![Python](https://img.shields.io/badge/Python-3.x-00FF41?style=flat-square&logo=python&logoColor=white&labelColor=0a0a0a)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-00AA28?style=flat-square&labelColor=0a0a0a)
![Architecture](https://img.shields.io/badge/Architecture-Modular_OOP-0088FF?style=flat-square&labelColor=0a0a0a)
![Type](https://img.shields.io/badge/Type-University_Project-FF4500?style=flat-square&labelColor=0a0a0a)

> **Zero-Day Protocol** is a modern, dark-themed decision-making simulation game built with Python.  
> Designed as a university engineering project, it explores the logical flow of cyber-attacks, resource management, and state-based progression.

---

## 🚀 Overview

The player takes on the role of a **cyber-security specialist** navigating through three increasingly difficult hacking missions. Each level focuses on a different core computing concept — networking, operating system security, and resource optimization — wrapped in an immersive cyberpunk terminal aesthetic.

---

## 🛠️ Technical Stack

| Component | Detail |
|-----------|--------|
| **Language** | Python 3.x |
| **GUI Library** | CustomTkinter (Modern dark-themed UI) |
| **Architecture** | Modular Object-Oriented Programming (OOP) |
| **Core Concepts** | Finite State Machines, Event-Driven Programming, Non-blocking Timers |

---

## 🎮 Game Features & Levels

### 🗂️ Dashboard
A centralized hub for mission selection and system exit. Uses a **Single Page Application (SPA)** pattern — switches `CTkFrame` objects instead of opening multiple windows.

---

### ⚡ Level 1 — Localhost Breach
- **Target:** Small Startup Router
- **Focus:** Basic networking and security vulnerabilities
- **Logic:** Simulate a port scan (Nmap), identify the open SSH port (22), and execute a brute-force attack
- **Risk:** Wrong port entry causes a trace spike — trace ≥ 100% triggers game over

---

### 🔗 Level 2 — Proxy Override
- **Target:** Corporate Bank Server
- **Focus:** Timed operations and anonymity
- **Logic:** 35-second countdown timer, scan proxy nodes, route through the safe IP to hide identity, then breach the firewall
- **Risk:** Trace auto-increases every 3 seconds; entering a wrong or honeypot IP spikes the trace

---

### 💀 Level 3 — Root Access *(Final Boss)*
- **Target:** Defense Mainframe
- **Focus:** Dual-resource management under time pressure
- **Logic:** Scan memory for a randomized `VULN_OFFSET` hex value, inject it to increase the Decrypt bar, use Obfuscate to reduce trace, then execute root when decryption hits 100%
- **Risk:** Military AI actively increases trace every 2 seconds — balance speed vs. stealth to survive

---

## 🏗️ Engineering Highlights

| Pattern | Description |
|---------|-------------|
| **Modular File Structure** | Project split into `main.py` + 3 level modules for scalability and clean code management |
| **SPA Frame-Switching** | Uses `CTkFrame` swapping instead of multiple windows — eliminates state leakage between screens |
| **Finite State Machine (FSM)** | Real-time tracking of `trace_level`, `decrypt_level`, and `timer_running` via class-based state |
| **Non-Blocking Timers** | Tkinter's `after()` method provides async-like countdown behavior without blocking the main UI thread |
| **Risk-Reward Design** | Every player action carries a consequence — wrong moves spike the trace bar, forcing strategic decisions |

---

## 📥 Installation & Usage

**1. Clone the repository or download the source files**

**2. Install dependencies:**
```bash
pip install customtkinter
```

**3. Run the game:**
```bash
python main.py
```

---

## 📂 File Structure

```
zero-day-protocol/
│
├── main.py          # Entry point & Dashboard controller (SPA frame-switching)
├── level_1.py       # Localhost Breach — Nmap scan & brute-force simulation
├── level_2.py       # Proxy Override — countdown timer & proxy routing logic
└── level_3.py       # Root Access [Boss] — hex injection & dual-bar resource management
```

---

## 🎓 Academic Context

Developed as a **Computer Engineering University Project**.  
Demonstrates applied knowledge of: GUI programming, object-oriented design, event-driven architecture, and game state management.

---

*`SYS_ADMIN @ LOCALHOST:~$ _`*