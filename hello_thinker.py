import tkinter as tk

# C DAĻA: Funkcija, kas nolasa, pārbauda un izvada datus
def sveicinat():
    vards = varda_ievade.get() # Nolasa tekstu
    
    if vards.strip(): # Ja vārds nav tukšs
        label.config(text=f"Sveiks, {vards}!", fg="darkgreen") # Maina tekstu un krāsu
        root.config(bg="lightyellow") # <--- Tas pats krāsu triks (fons kļūst dzeltens)
        varda_ievade.delete(0, tk.END) # Iztīra lauku
    else:
        label.config(text="Lūdzu, ieraksti vārdu!", fg="red")
        root.config(bg="white") # Atgriež baltu fonu kļūdas gadījumā

# A DAĻA: Galvenais logs
root = tk.Tk()
root.title("Sveicienu programma")
root.geometry("400x300")

# Label - Uzraksts
label = tk.Label(root, text="Kā tevi sauc?", font=("Arial", 14))
label.pack(pady=20)

# C DAĻA: Ievades lauks
varda_ievade = tk.Entry(root, font=("Arial", 12))
varda_ievade.pack(pady=10)

# B DAĻA: Pogas
poga_sveikt = tk.Button(root, text="Sveicināt", command=sveicinat, bg="lightgreen")
poga_sveikt.pack(pady=10)

poga_aizvert = tk.Button(root, text="Aizvērt", command=root.destroy, bg="pink")
poga_aizvert.pack(pady=10)

# Galvenā cilpa
root.mainloop()