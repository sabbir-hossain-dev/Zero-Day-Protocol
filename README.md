# Zero-Day Protocol: A Cyber-Security Simulation Game

**Zero-Day Protocol** is a modern, dark-themed decision-making simulation game built with Python. Designed as a university engineering project, it explores the logical flow of cyber-attacks, resource management, and state-based progression.

## 🚀 Overview
The player takes on the role of a cyber-security specialist navigating through three increasingly difficult levels. Each level focuses on different core computing concepts like networking, operating systems, and resource optimization.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **GUI Library:** `CustomTkinter` (Modern UI/UX)
* **Architecture:** Modular Object-Oriented Programming (OOP)
* **Core Concepts:** Finite State Machines, Event-Driven Programming, Non-blocking Timers.

## 🎮 Game Features & Levels
1.  **Dashboard:** A centralized hub for mission selection and system exit.
2.  **Level 1: Localhost Breach**
    * *Focus:* Basic networking and security vulnerabilities.
    * *Logic:* Port scanning (Nmap) and Brute-force simulation.
3.  **Level 2: Proxy Override**
    * *Focus:* Timed operations and anonymity.
    * *Logic:* Non-blocking countdown timer and proxy-bouncing mechanics to reduce trace levels.
4.  **Level 3: Root Access (The Final Boss)**
    * *Focus:* Dual-resource management.
    * *Logic:* Balancing "Decryption Progress" against "Trace Level" within a strict time limit.

## 🏗️ Engineering Highlights (For Evaluators)
* **Modular File Structure:** The project is split into multiple modules (`main.py`, `level_1.py`, etc.) for scalability and clean code management.
* **Frame-Switching Logic:** Instead of opening multiple windows, the app uses a Single Page Application (SPA) approach by switching `CTkFrame` objects.
* **State Management:** Real-time tracking of player decisions, risk levels, and mission status using class-based states.
* **Threading & Timers:** Utilizes the `after()` method in Tkinter for asynchronous-like timer behavior without blocking the main UI thread.

## 📥 Installation & Usage
1.  **Clone the repository or download the source files.**
2.  **Install dependencies:**
    ```bash
    pip install customtkinter
    ```
3.  **Run the game:**
    ```bash
    python main.py
    ```

## 📂 File Structure
* `main.py`: The entry point and Dashboard controller.
* `level_1.py`: Contains Localhost Breach mechanics.
* `level_2.py`: Contains Proxy Override logic with timer.
* `level_3.py`: Contains the final Root Access decryption challenge.

---
*Developed as a Computer Engineering University Project.*