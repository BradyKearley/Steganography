import tkinter as tk
from tkinter import filedialog, messagebox
from RSA_Encryption import generate_keys, encrypt, decrypt
from Steganography import encode_image, decode_image

def generate_keys_ui():
    try:
        public_key, private_key = generate_keys()
        n_entry.delete(0, tk.END)
        e_entry.delete(0, tk.END)
        d_entry.delete(0, tk.END)
        n_entry.insert(0, public_key['n'])
        e_entry.insert(0, public_key['e'])
        d_entry.insert(0, private_key['d'])
        with open("private_key.txt", "w") as file:
            file.write(f"n: {private_key['n']}\n")
            file.write(f"d: {private_key['d']}\n")
        with open("public_key.txt", "w") as file:
            file.write(f"n: {public_key['n']}\n")
            file.write(f"e: {public_key['e']}\n")
        messagebox.showinfo("Keys Generated", "Public and Private keys have been generated, saved to files, and displayed.")
    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def load_keys_ui():
    try:
        with open("public_key.txt", "r") as file:
            lines = file.readlines()
            n_entry.delete(0, tk.END)
            e_entry.delete(0, tk.END)
            n_entry.insert(0, int(lines[0].strip().split(": ")[1]))
            e_entry.insert(0, int(lines[1].strip().split(": ")[1]))
        with open("private_key.txt", "r") as file:
            lines = file.readlines()
            d_entry.delete(0, tk.END)
            d_entry.insert(0, int(lines[1].strip().split(": ")[1]))
        messagebox.showinfo("Keys Loaded", "Public and Private keys have been loaded from files.")
    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def save_keys_ui():
    try:
        n = int(n_entry.get())
        e = int(e_entry.get())
        d = int(d_entry.get())
        with open("public_key.txt", "w") as file:
            file.write(f"n: {n}\n")
            file.write(f"e: {e}\n")
        with open("private_key.txt", "w") as file:
            file.write(f"n: {n}\n")
            file.write(f"d: {d}\n")
        messagebox.showinfo("Keys Saved", "Public and Private keys have been saved to files.")
    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def encrypt_image():
    try:
        message = message_entry.get()
        n = int(n_entry.get())
        e = int(e_entry.get())
        public_key = {'n': n, 'e': e}
        encrypted_data = encrypt(message, public_key)
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.*")])
        if output_path:
            encode_image(image_path.get(), encrypted_data, output_path)
            messagebox.showinfo("Success", "Image encrypted and saved successfully!")
    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def decrypt_image():
    try:
        n = int(n_entry.get())
        d = int(d_entry.get())
        private_key = {'n': n, 'd': d}
        decoded_encrypted_data = decode_image(image_path.get())
        decrypted_message = decrypt(decoded_encrypted_data, private_key)
        messagebox.showinfo("Decrypted Message", str(decrypted_message))
    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def select_image():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("All Files", "*.*"),
        ]
    )
    if file_path:
        image_path.set(file_path)

app = tk.Tk()
app.title("Image Encryption and Decryption")
app.configure(bg="#f0f0f0")

image_path = tk.StringVar()

# Layout
tk.Label(app, text="Select Image:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=image_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_image, bg="#4CAF50", fg="white").grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Message:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Entry(app, width=50)
message_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

tk.Label(app, text="n:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
n_entry = tk.Entry(app, width=50)
n_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

tk.Label(app, text="e:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10)
e_entry = tk.Entry(app, width=50)
e_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

tk.Label(app, text="d:", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10)
d_entry = tk.Entry(app, width=50)
d_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

# Buttons
button_frame = tk.Frame(app, bg="#f0f0f0")
button_frame.grid(row=5, column=0, columnspan=3, pady=10)

tk.Button(button_frame, text="Generate Keys", command=generate_keys_ui, bg="#2196F3", fg="white").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Load Keys", command=load_keys_ui, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Save Keys", command=save_keys_ui, bg="#2196F3", fg="white").grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Encrypt Image", command=encrypt_image, bg="#FF9800", fg="white").grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Decrypt Image", command=decrypt_image, bg="#FF9800", fg="white").grid(row=0, column=4, padx=5)

app.mainloop()