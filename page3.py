import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from customtkinter import CTkImage
from PIL import Image
import page1
import page2
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class Page3:
    def __init__(self, root, language):
        global selected_algorithm
        self.root = root
        self.language = language
        self.selected_algo = page1.selected_algorithm
        self.name_file = page1.name_file
        self.val = page2.all_rows
        print(f"Nom du fichier page 3 : {self.name_file}")
        print(f"Algorithme utilisé page 3 : {self.selected_algo}")
        self.translations = {
            "fr": {
                "visualization_data": "VISUALISATION DES DONNEES",
                "simulate": "Simuler",
                "back": "Retour",
                "menu": [
                    ("PRÉTRAITEMENT", self.open_page1, "edit.png"),
                    ("ENTRAÎNEMENT", self.open_page2, "params.png"),
                    ("RESULTAT", self.open_page3, "result.png"),
                    ("VISUALISATION DES\nDONNÉES", self.open_page4, "visu.png")
                ]
            },
            "en": {
                "visualization_data": "VISUALIZATION DATA",
                "simulate": "Simulate",
                "back": "Back",
                "menu": [
                    ("PREPROCESSING", self.open_page1, "edit.png"),
                    ("TRAINING", self.open_page2, "params.png"),
                    ("RESULT", self.open_page3, "result.png"),
                    ("DATA VISUALIZATION", self.open_page4, "visu.png")
                ]
            }
        }
        self.create_sidebar()
        self.create_widgets()

    # Barre latérale (Menu de navigation)
    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self.root, width=300, corner_radius=0, fg_color="#1C3A6B")
        sidebar.pack(side="left", fill="y")

        # Logo
        logo = ctk.CTkImage(light_image=Image.open("logo_LSTM.png"), size=(200, 200))
        label_logo = ctk.CTkLabel(sidebar, image=logo, text="")
        label_logo.pack(pady=(10, 20))

        # Boutons de navigation
        
        for text, command, icon_path in self.translations[self.language]["menu"]:
            icon = CTkImage(light_image=Image.open(icon_path), size=(20, 20))
            button = ctk.CTkButton(
                sidebar, text=text, width=200, height=40, anchor="w",
                corner_radius=10, font=("Arial", 16, "bold"), fg_color="#1C3A6B",
                command=command, image=icon
            )
            button.pack(pady=15, padx=10)

    def create_widgets(self):            
        # FRAME PRINCIPAL
        main_frame = ctk.CTkFrame(self.root, fg_color="white")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Titre
        title_label = ctk.CTkLabel(main_frame, text="Resultat", font=("Arial", 28, "bold"), text_color="black")
        title_label.pack(padx=20, pady=(20, 10), anchor="center")
        
        # Sous-titre
        subtitle_label = ctk.CTkLabel(main_frame, text="RMSE ET les COURBE D’apprentissage", font=("Arial", 18, "italic"), text_color="black")
        subtitle_label.pack(anchor="center")
        
        # FRAME DES GRAPHIQUES
        self.graph_frame = ctk.CTkFrame(main_frame, fg_color="white")
        self.graph_frame.pack(pady=10, padx=10, anchor="center")
        
        # Ajouter le graphique
        self.create_plot()
        
          # Types de graphes avec taille ajustée
        types_label = ctk.CTkLabel(main_frame, text="Types de graphes :", font=("Arial", 16, "bold"), text_color="black", width=180)
        types_label.pack(anchor="w", padx=20)
        
        graph_options = ["graphe par trajectoire", "graphe avec tous les points"]
        graph_listbox = ctk.CTkComboBox(main_frame, values=graph_options, width=250)
        graph_listbox.pack(padx=20, anchor="w", pady=10)
        
        # BOUTONS déplacés plus bas
        button_frame = ctk.CTkFrame(main_frame, fg_color="white")
        button_frame.pack(pady=50)
        
        bouton_afficher = ctk.CTkButton(button_frame, text="afficher le graphe", width=200, fg_color="#1C3A6B", command=self.afficher_graphe)
        bouton_afficher.pack(side="left", padx=20)
        #bouton_afficher.place(relx=0.75, rely=0.95, anchor="center")

        bouton_csv = ctk.CTkButton(button_frame, text="télécharger csv", width=200, fg_color="#1C3A6B", command=self.telecharger_csv)
        bouton_csv.pack(side="left", padx=20)
        #bouton_csv.place(relx=0.55, rely=0.75, anchor="center")

        bouton_afficher_csv = ctk.CTkButton(button_frame, text="afficher le graphe + csv", width=200, fg_color="#1C3A6B", command=self.afficher_graphe_csv)
        bouton_afficher_csv.pack(side="left", padx=10)
        #bouton_afficher_csv.place(relx=0.75, rely=0.95, anchor="center")

        # Bouton retour
        ctk.CTkButton(main_frame, text=self.translations[self.language]["back"], width=100, fg_color="#1C3A6B", command=self.open_page2).place(relx=0.9, rely=0.95, anchor="center")
    
    def create_plot(self):
        self.fig, self.axs = plt.subplots(2, 1, figsize=(4, 3))
        x = np.linspace(0, 100, 100)
        y1_true = np.sin(x / 10) + 0.2
        y1_pred = y1_true + np.random.normal(0, 0.02, len(x))
        y2_true = np.cos(x / 10) + 0.5
        y2_pred = y2_true + np.random.normal(0, 0.02, len(x))
        
        self.axs[0].plot(x, y1_true, label="True Latitude")
        self.axs[0].plot(x, y1_pred, label="Predicted Latitude", linestyle="--")
        self.axs[0].legend()
        
        self.axs[1].plot(x, y2_true, label="True Longitude")
        self.axs[1].plot(x, y2_pred, label="Predicted Longitude", linestyle="--")
        self.axs[1].legend()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
    
    def afficher_graphe(self):
        print("Afficher le graphe")
    
    def telecharger_csv(self):
        print("Télécharger le fichier CSV")
    
    def afficher_graphe_csv(self):
        print("Afficher le graphe et télécharger le CSV")
    
    def retour(self):
        print("Retour à la page précédente")
        
    def ouvrir_fenetre_courbe(self):
        curve_window = tk.Toplevel(self.root)
        curve_window.title("Courbes")
        curve_window.geometry("600x400")

    def telecharger_csv(self):
        # Ouvre le gestionnaire de fichier pour choisir où sauvegarder le fichier CSV
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        
        if file_path:
            # Sauvegarde les données dans un fichier CSV
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Ajoute un en-tête des pour les colonnes
                writer.writerow(["Colonne 1", "Colonne 2", "Colonne 3"])
                # Écrit les données 
                for row in self.val:
                    writer.writerow(row)
            print(f"Fichier CSV sauvegardé sous {file_path}")


    def open_main_window(self):
        from main_window import MainWindow
        self.clear_window()
        MainWindow(self.root)

    def open_page1(self):
        from page1 import Page1
        if not isinstance(self, Page1):
            self.clear_window()
            Page1(self.root, language=self.language) 

    def open_page2(self):
        from page2 import Page2
        if not isinstance(self, Page2):
            self.clear_window()
            Page2(self.root, language=self.language)

    def open_page3(self):
        from page3 import Page3
        if not isinstance(self, Page3):
            self.clear_window()
            Page3(self.root, language=self.language)

    def open_page4(self):
        from page4 import Page4
        if not isinstance(self, Page4):
            self.clear_window()
            Page4(self.root, language=self.language)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
