import tkinter as tk
from tkinter import messagebox
from storage import load_list, save_list
from utils import calc_line_total, calc_grand_total, count_units

def update_total():
    """Atjauno apakšējo informāciju par kopsummu."""
    total_price = calc_grand_total(items)
    total_units = count_units(items)
    total_label.config(text=f"Kopā: {total_price:.2f} EUR ({total_units} vienības)")

def refresh_listbox():
    """Pārzīmē sarakstu."""
    listbox.delete(0, tk.END)
    for item in items:
        line_total = calc_line_total(item)
        listbox.insert(tk.END, f"{item['name']} × {item['qty']} — {item['price']:.2f} EUR — {line_total:.2f} EUR")
    update_total()

def add_item():
    name = name_entry.get().strip()
    try:
        if not name:
            raise ValueError("Nosaukums nevar būt tukšs")
        qty = int(qty_entry.get())
        price = float(price_entry.get())
        
        if qty <= 0 or price <= 0:
            raise ValueError("Skaitļiem jābūt pozitīviem")

        items.append({"name": name, "qty": qty, "price": price})
        save_list(items)
        refresh_listbox()
        
        # Iztīra laukus pēc pievienošanas
        name_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        name_entry.focus() # Novieto kursoru atpakaļ uz nosaukumu
        
    except ValueError as e:
        messagebox.showerror("Kļūda", f"Nepareiza ievade: {e}")

def delete_selected():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Uzmanību", "Lūdzu, izvēlieties produktu no saraksta!")
        return
    
    index = selection[0]
    items.pop(index)
    save_list(items)
    refresh_listbox()

# === GUI Uzstādījumi ===
items = load_list()
root = tk.Tk()
root.title("Iepirkumu saraksts v2.0")
root.geometry("450x550")
root.padx = 20

# Ievades lauki ar Grid
tk.Label(root, text="Produkts:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, columnspan=2, sticky="ew", padx=5)

tk.Label(root, text="Daudzums:").grid(row=1, column=0, sticky="w", pady=5)
qty_entry = tk.Entry(root, width=10)
qty_entry.grid(row=1, column=1, sticky="w", padx=5)

tk.Label(root, text="Cena:").grid(row=1, column=2, sticky="w", pady=5)
price_entry = tk.Entry(root, width=10)
price_entry.grid(row=1, column=2, sticky="e", padx=5)

# Pievienošanas poga
add_btn = tk.Button(root, text="Pievienot sarakstam", command=add_item, bg="#4CAF50", fg="white")
add_btn.grid(row=2, column=0, columnspan=3, sticky="ew", pady=10)

# Saraksta attēlošana (Listbox ar Scrollbar)
listbox_frame = tk.Frame(root)
listbox_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, height=10, width=50, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Dzēšanas poga
delete_btn = tk.Button(root, text="Dzēst izvēlēto", command=delete_selected, bg="#f44336", fg="white")
delete_btn.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

# Kopsummas Label
total_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
total_label.grid(row=5, column=0, columnspan=3, pady=10)



refresh_listbox() # Ielādē datus startējot
root.mainloop()