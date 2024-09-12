import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from docx import Document
from onglet_infos_perso import create_onglet_infos_perso
from onglet_competences import create_onglet_competences
from onglet_infos_formation import create_onglet_infos_formation

# Fonction pour générer le document Word
def generer_document():
    # Utiliser les variables globales pour accéder aux entrées des onglets
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_entree = entry_date_entree.get()
    date_fin = entry_date_fin.get()
    rythme = entry_rythme.get()

    competence1 = var_competence1.get()
    competence2 = var_competence2.get()

    if not nom or not prenom or not date_entree or not date_fin or not rythme:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
        return

    # Génération du document Word
    doc = Document()
    doc.add_heading('Informations sur la Formation', 0)
    doc.add_paragraph(f"Nom : {nom}")
    doc.add_paragraph(f"Prénom : {prenom}")
    doc.add_paragraph(f"Date d'entrée : {date_entree}")
    doc.add_paragraph(f"Date de fin : {date_fin}")
    doc.add_paragraph(f"Rythme hebdomadaire : {rythme}")
    
    doc.add_heading('Compétences', level=1)
    if competence1:
        doc.add_paragraph("Compétence 1 : Apprise")
    if competence2:
        doc.add_paragraph("Compétence 2 : Apprise")

    doc.save('formulaire_formation.docx')
    messagebox.showinfo("Succès", "Le document a été généré avec succès.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Document Word - Formation")

# Création du Notebook pour les onglets
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, padx=10, pady=10)

# Appel aux fonctions pour ajouter les onglets et récupérer les widgets
entry_nom, entry_prenom = create_onglet_infos_perso(notebook)
var_competence1, var_competence2 = create_onglet_competences(notebook)
entry_date_entree, entry_date_fin, entry_rythme = create_onglet_infos_formation(notebook)

# Bouton pour générer le document
btn_generer = tk.Button(root, text="Générer le document", command=generer_document)
btn_generer.grid(row=1, column=0, padx=10, pady=10)

# Lancer l'application
root.mainloop()
