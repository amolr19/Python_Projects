from tkinter import Tk, Label, Entry, Button, Text, messagebox
from text_encryption_app.backend.encryption import encrypt_aes, decrypt_aes, generate_aes_key


class EncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("Text Encryption and Decryption")
        self.aes_key = generate_aes_key()

        self.label = Label(master, text="Enter Text:")
        self.label.grid(row=0, column=0)

        self.text_entry = Entry(master)
        self.text_entry.grid(row=0, column=1)

        self.enc_button = Button(master, text="Encrypt (AES)", command=self.encrypt)
        self.enc_button.grid(row=1, column=0)

        self.dec_button = Button(master, text="Decrypt (AES)", command=self.decrypt)
        self.dec_button.grid(row=1, column=1)

        self.output_text = Text(master, height=5, width=50)
        self.output_text.grid(row=2, columnspan=2)

    def encrypt(self):
        plaintext = self.text_entry.get()

        try:
            ciphertext = encrypt_aes(plaintext, self.aes_key)
            self.output_text.delete(1.0, "end")
            self.output_text.insert("end", f"AES Encrypted:\n{ciphertext}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        ciphertext = self.text_entry.get()

        try:
            plaintext = decrypt_aes(ciphertext, self.aes_key)
            self.output_text.delete(1.0, "end")
            self.output_text.insert("end", f"AES Decrypted:\n{plaintext}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = Tk()
    app = EncryptionApp(root)
    root.geometry("500x300")
    root.mainloop()
