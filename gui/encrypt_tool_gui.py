# (GUI code will be same as provided earlier)
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.fernet import Fernet
import os

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def generate_key():
    key = Fernet.generate_key()
    os.makedirs("../keys", exist_ok=True)
    with open("../keys/keyfile.key", "wb") as f:
        f.write(key)
    messagebox.showinfo("Key Generated", "Key saved in ../keys/keyfile.key")

def load_key():
    if not os.path.exists("../keys/keyfile.key"):
        generate_key()
    with open("../keys/keyfile.key", "rb") as f:
        return f.read()

def fernet_encrypt_text(text):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

def fernet_decrypt_text(token):
    try:
        key = load_key()
        f = Fernet(key)
        return f.decrypt(token.encode()).decode()
    except Exception:
        return "❌ Invalid token or wrong key!"

class EncryptGUI:
    def __init__(self, root):
        self.root = root
        root.title("🔐 Simple Encryption Tool")
        root.geometry("600x400")

        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)

        self.text_tab = ttk.Frame(notebook)
        notebook.add(self.text_tab, text="Text Encrypt/Decrypt")

        self.input_text = tk.Text(self.text_tab, height=5, width=60)
        self.input_text.pack(pady=10)

        self.shift_val = tk.IntVar(value=3)
        self.method = tk.StringVar(value="Fernet")
        method_menu = ttk.Combobox(self.text_tab, textvariable=self.method, values=["Fernet", "Caesar"])
        method_menu.pack(pady=5)

        ttk.Label(self.text_tab, text="Shift (for Caesar):").pack()
        tk.Entry(self.text_tab, textvariable=self.shift_val, width=5).pack()

        btn_frame = ttk.Frame(self.text_tab)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Encrypt", command=self.encrypt_text).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Decrypt", command=self.decrypt_text).grid(row=0, column=1, padx=5)

        self.output_text = tk.Text(self.text_tab, height=5, width=60, state="disabled")
        self.output_text.pack(pady=10)

    def encrypt_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if self.method.get() == "Fernet":
            result = fernet_encrypt_text(text)
        else:
            result = caesar_encrypt(text, self.shift_val.get())
        self.show_output(result)

    def decrypt_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if self.method.get() == "Fernet":
            result = fernet_decrypt_text(text)
        else:
            result = caesar_decrypt(text, self.shift_val.get())
        self.show_output(result)

    def show_output(self, result):
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptGUI(root)
    root.mainloop()
