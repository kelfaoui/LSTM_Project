import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkImage
from PIL import Image, ImageTk
from PIL import Image

class Page2:
    def __init__(self, root, language):
        self.root = root
        self.language = language

        self.columns_dict = {
            "Encoder decoder model": ["encoder_lstm_cells", "decoder_lstm_cells", "epochs", "batch_size", "validation_split"],

            "Simple LSTM model": ["lstm_layers", "lstm_cells", "epochs", "batch_size", "validation_split"]
        }
         # Dictionnaire de traductions
        self.translations = {
            "fr": {
                "training": "ENTRAÎNEMENT",
                "choose_algo": "Choisir un algorithme :",
                "select_args": "Sélectionner les arguments :",
                "simulate": "Simuler",
                "back": "Retour",
                "menu": [
                    ("PRÉTRAITEMENT", self.open_page1, "edit.png"),
                    ("ENTRAÎNEMENT", self.open_page2, "params.png"),
                    ("VISUALISATION DES\nDONNÉES", self.open_page3, "visu.png")
                ],
                "columns": {
                    "Encoder decoder model": ["Nb neurones encodeur", "Nb neurones décodeur", "Nb epochs", "Batch size", "Learning rate"],
                    "Simple LSTM model": ["Nb CONV1D neurones encodeur", "Nb LSTM neurones encodeur", "Nb CONV1D neurones décodeur", "Nb LSTM neurones décodeur", "Nb epochs", "Batch size", "Learning rate"]
                },
                "infos": {
                    "Encoder decoder model": ["a faire, par defaut =64", "a faire, par defaut =64", "a faire, par defaut =50", "a faire, par defaut =64", "a faire, par defaut =0.1"],
                    "Simple LSTM model": ["a faire, par defaut =1", "a faire, par defaut =64", "a faire, par deafut =50", "a faire, par deafaut =64", "a faire, par defaut =0.1"]
                }
            },
            "en": {
                "training": "TRAINING",
                "choose_algo": "Choose an algorithm:",
                "select_args": "Select arguments:",
                "simulate": "Simulate",
                "back": "Back",
                "menu": [
                    ("PREPROCESSING", self.open_page1, "edit.png"),
                    ("TRAINING", self.open_page2, "params.png"),
                    ("DATA VISUALIZATION", self.open_page3, "visu.png")
                ],
                "columns": {
                    "Encoder decoder model": ["encoder_lstm_cells", "decoder_lstm_cells", "epochs", "Batch size", "validation_split"],
                    "Simple LSTM model": ["Nb CONV1D encoder neurons", "Nb LSTM encoder neurons", "Nb CONV1D decoder neurons", "Nb LSTM decoder neurons", "Nb epochs", "Batch size", "Learning rate"]
                },
                "infos": {
                    "Encoder decoder model": ["a faire, default =64", "a faire, default =64", "a faire, default =50", "a faire, default =64", "a faire, default =0.1"],
                    "Simple LSTM model": ["a faire, default =1", "a faire, default =64", "a faire, default =50", "a faire, default =64", "a faire, default =0.1"]
                }
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
        title_label = ctk.CTkLabel(main_frame, text=self.translations[self.language]["training"], font=("Arial", 28, "bold"), text_color="black")
        title_label.pack(padx=20, pady=20, anchor="center")
         # Liste déroulante pour choisir l'algorithme
        algo_frame = ctk.CTkFrame(main_frame, fg_color="white", width=500)
        algo_frame.pack(fill="x", padx=20, pady=20)
        algo_label = ctk.CTkLabel(algo_frame, text=self.translations[self.language]["choose_algo"], font=("Arial", 16, "bold"), text_color="black")
        algo_label.pack(pady=5, side="left")
        self.algo_dropdown = ctk.CTkComboBox(algo_frame, values=["Encoder decoder model", "Simple LSTM model"], width=175)
        self.algo_dropdown.pack(padx=(10,0), pady=5, side="left")
        
        selection_label = ctk.CTkLabel(main_frame, text=self.translations[self.language]["select_args"], font=("Arial", 16, "bold"), text_color="black")
        selection_label.pack(padx=20, pady=5, anchor="w")
        
            # CHECHBOX
            
        self.checkbox_frame = ctk.CTkFrame(main_frame, fg_color="white")
        self.checkbox_frame.pack(padx=20, pady=10, anchor="w")
        

        image_path = "info.png"  
        image = Image.open(image_path)  
        image = image.resize((15, 15))  
        self.info_image = ImageTk.PhotoImage(image)  

       # Fonction pour afficher un tooltip au survol
        def show_tooltip(event, text):
            if not hasattr(self, 'tooltip_window') or not self.tooltip_window.winfo_exists():
                x, y = event.x_root, event.y_root
                tooltip_window = tk.Toplevel(self.root)
                tooltip_window.wm_overrideredirect(True)
                tooltip_window.wm_geometry(f"+{x+30}+{y-10}")

                label = tk.Label(tooltip_window, text=text, background="#f0f0f0")
                label.pack(padx=10, pady=5)
                
                # Enregistrer la fenêtre tooltip dans un attribut pour pouvoir la gérer
                self.tooltip_window = tooltip_window

        # Fonction pour supprimer le tooltip lorsque la souris quitte l'icône
        def hide_tooltip(event):
            if hasattr(self, 'tooltip_window') and self.tooltip_window.winfo_exists():
                self.tooltip_window.destroy()
                del self.tooltip_window
              
        # Fonction pour mettre à jour les checkboxes en fonction de l'algorithme choisi
        def update_checkboxes(event=None):
            for widget in self.checkbox_frame.winfo_children():
                widget.destroy()

            # Récupérer l'algorithme sélectionné
            selected_algo = self.algo_dropdown.get()
            print(f"Algorithme sélectionné : {selected_algo}")
            columns = self.columns_dict.get(selected_algo, [])
            # Ajouter les checkboxes pour chaque colonne sur deux colonnes
            for i, column in enumerate(columns):
                row = i // 2 
                column_index = i % 2 
                # Saisie
                entry = self.float_entry()
                entry_label = ctk.CTkLabel(self.checkbox_frame, text=column, font=("Arial", 12), text_color="black")
                info_icon = ctk.CTkLabel(self.checkbox_frame, image=self.info_image, text="")

                if column_index == 1:
                    # Placement pour la deuxième colonne
                    entry.grid(row=row, column=column_index+2, pady=5, padx=(100, 10), sticky="w")
                    entry_label.grid(row=row, column=column_index+3, pady=5, padx=10, sticky="w")
                    info_icon.grid(row=row, column=column_index+4, padx=5, pady=5, sticky="w")
                else:
                    # Placement pour la première colonne
                    entry.grid(row=row, column=column_index, pady=5, padx=10, sticky="w")
                    entry_label.grid(row=row, column=column_index+1, pady=5, padx=10, sticky="w")
                    info_icon.grid(row=row, column=column_index+2, padx=5, pady=5, sticky="w")
                # Associer le survol de l'icône à l'affichage du tooltip
                info_icon.bind("<Enter>", lambda e, text=self.translations[self.language]["infos"].get(selected_algo, [])[i]: show_tooltip(e, text))
                info_icon.bind("<Leave>", hide_tooltip)
            

        # Appeler update_checkboxes à chaque changement de sélection de l'algorithme
        self.algo_dropdown.configure(command=update_checkboxes)
        update_checkboxes()
        
        # Bouton simuler
        button_next = ctk.CTkButton(main_frame, text=self.translations[self.language]["simulate"], width=100, fg_color="#1C3A6B",command=self.open_page3)
        button_next.place(relx=0.9, rely=0.95, anchor="center")
        
        # Bouton retour
        button_back = ctk.CTkButton(main_frame, text=self.translations[self.language]["back"], width=100, fg_color="#1C3A6B", command=self.open_page1)
        button_back.place(relx=0.75, rely=0.95, anchor="center")
    
    # Button customisé pour accepter uniquement les nombres
    def float_entry(self):
        def validate_float(new_text):
            if new_text in ["", ".", "-"]:
                return True
            try:
                float(new_text)
                return True
            except:
                return False
        
        vcmd = (self.root.register(validate_float), '%P')
        
        entry = ctk.CTkEntry(
                self.checkbox_frame,
                width=50,
                fg_color="white",
                text_color="black",
                validate="key",  
                validatecommand=vcmd
            )
            
        entry.configure(
                placeholder_text="0-9",
                justify="center",
                font=("Arial", 12)
            )
        
        return entry

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
            Page2(self.root)

    def open_page3(self):
        from page3 import Page3
        if not isinstance(self, Page3):
            self.clear_window()
            Page3(self.root, language=self.language)
            
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
