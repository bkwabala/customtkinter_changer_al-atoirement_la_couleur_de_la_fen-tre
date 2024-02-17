import customtkinter as ctk
import random

root = ctk.CTk()
root.geometry("400x500")

couleurs = ["white","blue", "cyan","yellow","green",
            "gray","red"]

def suff():
    colors = random.choice(couleurs)
    root.configure(fg_color=colors)


bout = ctk.CTkButton(root, text="Mode",
                     command=suff)
bout.pack(side="bottom", pady=100)

root.mainloop()