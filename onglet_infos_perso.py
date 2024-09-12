import tkinter as tk

def create_onglet_infos_perso(notebook):
    global entry_nom, entry_prenom
    # Créer le Frame pour l'onglet
    frame_infos_personnelles = tk.Frame(notebook)
    notebook.add(frame_infos_personnelles, text="Informations personnelles")

    # Ajouter les champs de texte
    tk.Label(frame_infos_personnelles, text="Nom :").grid(row=0, column=0)
    entry_nom = tk.Entry(frame_infos_personnelles)
    entry_nom.grid(row=0, column=1)

    tk.Label(frame_infos_personnelles, text="Prénom :").grid(row=1, column=0)
    entry_prenom = tk.Entry(frame_infos_personnelles)
    entry_prenom.grid(row=1, column=1)
