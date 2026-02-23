import tkinter as tk

root = tk.Tk()
root.title("Skaitītājs")
root.geometry("350x200")

# Stāvokļa glabāšana (State management)
counter_var = tk.IntVar(value=0)

def increment():
    # .get() nolasa pašreizējo vērtību, .set() ieraksta jauno
    counter_var.set(counter_var.get() + 1)

def decrement():
    # Pārbaude: neļaujam iet zem 0
    # Pamatojums: Reālās lietotnēs (piem. iepirkumu grozā) nevar būt -1 prece.
    if counter_var.get() > 0:
        counter_var.set(counter_var.get() - 1)

def reset():
    counter_var.set(0)

# --- GUI izveide ar grid() ---

# Label izmanto textvariable, lai automātiski rādītu counter_var saturu
label = tk.Label(root, textvariable=counter_var, font=("Arial", 60))
# columnspan=3 nozīmē, ka šī šūna aizņem 3 kolonnu platumu
label.grid(row=0, column=0, columnspan=3, pady=20)

# Pogas izvietotas 1. rindā, katra savā kolonnā
btn_minus = tk.Button(root, text="−", command=decrement, width=8, font=("Arial", 14))
btn_minus.grid(row=1, column=0, padx=10, pady=10)

btn_reset = tk.Button(root, text="Reset", command=reset, width=8, font=("Arial", 14))
btn_reset.grid(row=1, column=1, padx=10, pady=10)

btn_plus = tk.Button(root, text="+", command=increment, width=8, font=("Arial", 14))
btn_plus.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()