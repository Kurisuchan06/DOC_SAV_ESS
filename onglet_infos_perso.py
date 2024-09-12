import tkinter as tk

def create_onglet_infos_perso(notebook):
    # Créer le Frame pour l'onglet
    frame_infos_personnelles = tk.Frame(notebook)
    notebook.add(frame_infos_personnelles, text="Informations personnelles")

    # Ajouter les champs de texte pour Nom et Prénom
    tk.Label(frame_infos_personnelles, text="Nom :").grid(row=0, column=0)
    entry_nom = tk.Entry(frame_infos_personnelles)
    entry_nom.grid(row=0, column=1)

    tk.Label(frame_infos_personnelles, text="Prénom :").grid(row=1, column=0)
    entry_prenom = tk.Entry(frame_infos_personnelles)
    entry_prenom.grid(row=1, column=1)

    # Ajouter le champ de texte pour l'Adresse
    tk.Label(frame_infos_personnelles, text="Adresse :").grid(row=2, column=0)
    entry_adresse = tk.Entry(frame_infos_personnelles)
    entry_adresse.grid(row=2, column=1)

    # Ajouter le champ de texte pour le Numéro de téléphone
    tk.Label(frame_infos_personnelles, text="Numéro de téléphone :").grid(row=3, column=0)
    entry_telephone = tk.Entry(frame_infos_personnelles)
    entry_telephone.grid(row=3, column=1)

    # Ajouter le champ de texte pour l'Email
    tk.Label(frame_infos_personnelles, text="Email :").grid(row=4, column=0)
    entry_email = tk.Entry(frame_infos_personnelles)
    entry_email.grid(row=4, column=1)

    # Retourner les widgets nécessaires pour l'accès depuis main.py
    return entry_nom, entry_prenom, entry_adresse, entry_telephone, entry_email
