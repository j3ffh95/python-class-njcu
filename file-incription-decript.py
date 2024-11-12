import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Step 1: Generate Key using a password


def generate_key(password, salt=None):
    if not salt:
        salt = os.urandom(16)  # A random salt if not provided
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())  # Derive a key from the password
    return key, salt

# Step 2: Encrypt the file and store IV and Salt in the file


def encrypt_file(input_file, output_file, password):
    key, salt = generate_key(password)
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv),
                    backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f_in:
        file_data = f_in.read()

    encrypted_data = encryptor.update(file_data) + encryptor.finalize()

    # Write the salt and IV at the beginning of the encrypted file
    with open(output_file, 'wb') as f_out:
        f_out.write(salt + iv + encrypted_data)

# Step 3: Decrypt the file by reading IV and Salt from the file


def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f_in:
        salt = f_in.read(16)  # Read the salt (first 16 bytes)
        iv = f_in.read(16)  # Read the IV (next 16 bytes)
        encrypted_data = f_in.read()  # The rest is the encrypted content

    key, _ = generate_key(password, salt)  # Regenerate the key using the salt

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv),
                    backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    with open(output_file, 'wb') as f_out:
        f_out.write(decrypted_data)

# GUI for encryption and decryption


def encrypt_gui():
    file_path = filedialog.askopenfilename(title="Select a file to encrypt")
    if file_path:
        password = "your-secure-password"  # In practice, prompt the user for a password
        encrypted_file = filedialog.asksaveasfilename(
            defaultextension=".enc", title="Save encrypted file as")
        if encrypted_file:
            encrypt_file(file_path, encrypted_file, password)
            messagebox.showinfo("Success", "File encrypted successfully!")


def decrypt_gui():
    file_path = filedialog.askopenfilename(title="Select an encrypted file")
    if file_path:
        password = "your-secure-password"  # In practice, prompt the user for a password
        decrypted_file = filedialog.asksaveasfilename(
            defaultextension=".txt", title="Save decrypted file as")
        if decrypted_file:
            decrypt_file(file_path, decrypted_file, password)
            messagebox.showinfo("Success", "File decrypted successfully!")

# GUI Setup


def main():
    root = Tk()
    root.title("File Encryption & Decryption Tool")

    Label(root, text="File Encryption and Decryption Tool",
          font=("Helvetica", 14)).pack(pady=10)

    Button(root, text="Encrypt File", command=encrypt_gui, width=30).pack(pady=5)
    Button(root, text="Decrypt File", command=decrypt_gui, width=30).pack(pady=5)

    root.geometry("400x200")
    root.mainloop()


if __name__ == "__main__":
    main()
