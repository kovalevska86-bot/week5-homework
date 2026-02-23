import tkinter as tk
from tkinter import messagebox
import logic  # Importējam mūsu loģikas failu

def handle_conversion():
    try:
        # Iegūstam vērtību no Entry un konversijas tipu no Dropdown
        input_value = float(entry.get())
        conversion_type = selected_option.get()
        
        # Izsaucam loģikas funkciju (GUI kods nezina formulas!)
        result = logic.convert(input_value, conversion_type)
        
        # Parādām rezultātu ar 2 decimālzīmēm
        result_label.config(text=f"Rezultāts: {result:.2f}", fg="black")
        
    except ValueError:
        # Ja ievade nav skaitlis, rādām kļūdas paziņojumu logā
        messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu skaitli!")
        result_label.config(text="Nepareiza ievade", fg="red")

# Galvenā loga uzstādījumi
root = tk.Tk()
root.title("Vienību konvertors")
root.geometry("350x300")
root.config(padx=20, pady=20)

# 1. Dropdown izvēlne
tk.Label(root, text="Izvēlies konversijas tipu:").grid(row=0, column=0, sticky="w", pady=5)
options = ["km → mi", "mi → km", "kg → lb", "lb → kg", "L → gal", "gal → L"]
selected_option = tk.StringVar(value=options[0])
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

# 2. Ievades lauks
tk.Label(root, text="Ievadi vērtību:").grid(row=2, column=0, sticky="w", pady=5)
entry = tk.Entry(root)
entry.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)

# 3. Poga "Konvertēt"
convert_button = tk.Button(root, text="Konvertēt", command=handle_conversion, bg="lightblue")
convert_button.grid(row=4, column=0, columnspan=2, sticky="ew", pady=15)

# 4. Rezultāta paziņojums
result_label = tk.Label(root, text="Rezultāts: 0.00", font=("Arial", 12, "bold"))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()