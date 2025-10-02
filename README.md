🔐 Encryption/Decryption Tool

📌 Overview

This project provides a simple Encryption/Decryption Tool with two versions:
CLI Version (Command-line)
GUI Version (Tkinter)

It supports:
Caesar Cipher (basic shift cipher for demo)
Fernet Encryption (secure symmetric encryption)
Now it also includes a Launcher Script (run_tool.py) to choose between CLI or GUI without navigating folders.

📂 Project Structure
encryption-tool/
│── README.md               # Documentation  
│── requirements.txt        # Dependencies  
│── run_tool.py             # Launcher (choose CLI or GUI)  
│
├── cli/                    # Command-line version  
│   └── encrypt_tool_cli.py  
│
├── gui/                    # Tkinter GUI version  
│   └── encrypt_tool_gui.py  
│
├── data/                   # Sample data (optional)  
│   └── sample.txt  
│
└── keys/                   # Fernet key storage (auto-generated)  
    └── keyfile.key  

🔧 Installation

Install dependencies:
pip install -r requirements.txt


Tkinter is included with Python by default (no extra install needed).

▶️ Usage
Launcher (Recommended)
Run the tool from the root folder:
python run_tool.py

You’ll see:

🔐 Encryption/Decryption Tool Launcher
1. Run CLI Tool
2. Run GUI Tool
Enter choice (1/2):


Enter 1 → starts the CLI tool
Enter 2 → starts the GUI tool

Run CLI Tool directly
cd cli
python encrypt_tool_cli.py

Run GUI Tool directly
cd gui
python encrypt_tool_gui.py

📊 Example (CLI)
🔐 Encryption/Decryption CLI Tool
Choose method (caesar/fernet): caesar
Do you want to (encrypt/decrypt)? encrypt
Enter text: hello
Enter shift value: 3
Result: khoor

🚀 Features

Text encryption & decryption (Caesar + Fernet)
File encryption/decryption (GUI only for now)
Auto key generation & storage in keys/keyfile.key
Easy-to-use GUI with Tkinter
Simple Launcher Script

✅ Dependencies

cryptography
tkinter (comes with Python)

Install all with:
pip install -r requirements.txt

👨‍💻 Author
Mallikarjun K S
