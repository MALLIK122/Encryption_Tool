import os
import subprocess

def run_cli():
    script_path = os.path.join("cli", "encrypt_tool_cli.py")
    subprocess.run(["python", script_path])

def run_gui():
    script_path = os.path.join("gui", "encrypt_tool_gui.py")
    subprocess.run(["python", script_path])

if __name__ == "__main__":
    print("🔐 Encryption/Decryption Tool Launcher")
    print("1. Run CLI Tool")
    print("2. Run GUI Tool")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        run_cli()
    elif choice == "2":
        run_gui()
    else:
        print("❌ Invalid choice. Exiting.")
