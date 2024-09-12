import tkinter as tk

def create_onglet_competences(notebook):
    global var_competence1, var_competence2
    # Créer le Frame pour l'onglet
    frame_competences = tk.Frame(notebook)
    notebook.add(frame_competences, text="Compétences")

    # Ajouter les cases à cocher
    var_competence1 = tk.BooleanVar()
    var_competence2 = tk.BooleanVar()

    tk.Checkbutton(frame_competences, text="Compétence 1", variable=var_competence1).grid(row=0, column=0)
    tk.Checkbutton(frame_competences, text="Compétence 2", variable=var_competence2).grid(row=1, column=0)
