import tkinter as tk

def create_onglet_infos_formation(notebook):
    global entry_date_entree, entry_date_fin, entry_rythme
    # Créer le Frame pour l'onglet
    frame_infos_formation = tk.Frame(notebook)
    notebook.add(frame_infos_formation, text="Informations Formation")

    # Ajouter les champs de texte pour la formation
    tk.Label(frame_infos_formation, text="Date d'entrée :").grid(row=0, column=0)
    entry_date_entree = tk.Entry(frame_infos_formation)
    entry_date_entree.grid(row=0, column=1)

    tk.Label(frame_infos_formation, text="Date de fin :").grid(row=1, column=0)
    entry_date_fin = tk.Entry(frame_infos_formation)
    entry_date_fin.grid(row=1, column=1)

    tk.Label(frame_infos_formation, text="Rythme hebdomadaire :").grid(row=2, column=0)
    entry_rythme = tk.Entry(frame_infos_formation)
    entry_rythme.grid(row=2, column=1)
import tkinter as tk

def create_onglet_infos_formation(notebook):
    # Créer le Frame pour l'onglet
    frame_infos_formation = tk.Frame(notebook)
    notebook.add(frame_infos_formation, text="Informations Formation")

    # Ajouter les champs de texte pour la formation
    tk.Label(frame_infos_formation, text="Date d'entrée :").grid(row=0, column=0)
    entry_date_entree = tk.Entry(frame_infos_formation)
    entry_date_entree.grid(row=0, column=1)

    tk.Label(frame_infos_formation, text="Date de fin :").grid(row=1, column=0)
    entry_date_fin = tk.Entry(frame_infos_formation)
    entry_date_fin.grid(row=1, column=1)

    tk.Label(frame_infos_formation, text="Rythme hebdomadaire :").grid(row=2, column=0)
    entry_rythme = tk.Entry(frame_infos_formation)
    entry_rythme.grid(row=2, column=1)

    # Retourner les widgets nécessaires
    return entry_date_entree, entry_date_fin, entry_rythme
