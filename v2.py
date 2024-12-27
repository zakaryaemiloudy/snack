from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Menu d'un restaurant")
app.geometry("400x400")

menu_frame = ttk.Frame(app, padding="10")
menu_frame.pack(fill="both", expand=True)

menu_label = ttk.Label(menu_frame, text="Menu", font=("Helvetica", 16, "bold"), padding="5")
menu_label.pack()

menu_tree = ttk.Treeview(menu_frame, columns=("nom", "prix"), show="headings")
menu_tree.pack()

menu_tree.heading("nom", text="nom")
menu_tree.heading("prix", text="prix")
menu_tree.insert("", "end", values=("Pizza", "40.00"))
menu_tree.insert("", "end", values=("Tacos", "49.00"))
menu_tree.insert("", "end", values=("Sandwich", "30.00"))
menu_tree.insert("", "end", values=("Burger", "32.00"))
menu_tree.insert("", "end", values=("Frites", "15.00"))
menu_tree.insert("", "end", values=("Nuggets", "35.00"))
menu_tree.insert("", "end", values=("Soda", "15.00"))
menu_tree.insert("", "end", values=("Limonade", "18.00"))

details_frame = ttk.Frame(app, padding="10")
details_frame.pack(fill="both", expand=True)

details_label = ttk.Label(details_frame, text="Détails de la commande", font=("Helvetica", 10, "bold"), padding="2")
details_label.pack()

details_tree = ttk.Treeview(details_frame, columns=("Item", "Price"), show="headings")
details_tree.pack()

add_button = ttk.Button(app, text="Ajouter", command=lambda: ajout_element(menu_tree, details_tree))
add_button.pack()

remove_button = ttk.Button(app, text="Supprimer", command=lambda: supp_element(details_tree))
remove_button.pack()

calculate_button = ttk.Button(app, text="Calculer", command=lambda: calculate_price(details_tree))
calculate_button.pack()

prix_totale_label = ttk.Label(app, text="Total: 0.00 DH", font=("Helvetica", 16, "bold"), padding="5")
prix_totale_label.pack()

def ajout_element(menu_tree, details_tree):
    element_selectioner = menu_tree.selection()
    if element_selectioner:
        item_name = menu_tree.item(element_selectioner, "values")[0]
        item_price = menu_tree.item(element_selectioner, "values")[1]
        details_tree.insert("", "end", values=(item_name, item_price))

def supp_element(details_tree):
    element_selectioner = details_tree.selection()
    if element_selectioner:
        details_tree.delete(element_selectioner)

def calculate_price(details_tree):
    prix_totale = 0
    for item in details_tree.get_children():
        prix_totale += float(details_tree.item(item, "values")[1])
    prix_totale_label.config(text=f"Total: {prix_totale:.2f} DH")


app.mainloop()

