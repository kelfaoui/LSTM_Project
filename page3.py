import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

class Page3:
    def __init__(self, root, language):
        self.root = root
        self.language = language

        self.translations = {
            "fr": {
                "visualization_data": "VISUALISATION DES DONNEES",
                "simulate": "Simuler",
                "back": "Retour",
                "menu": [
                    ("PRÉTRAITEMENT", self.open_page1, "edit.png"),
                    ("ENTRAÎNEMENT", self.open_page2, "params.png"),
                    ("VISUALISATION DES\nDONNÉES", self.open_page3, "visu.png")
                ]
            },
            "en": {
                "visualization_data": "VISUALIZATION DATA",
                "simulate": "Simulate",
                "back": "Back",
                "menu": [
                    ("PREPROCESSING", self.open_page1, "edit.png"),
                    ("TRAINING", self.open_page2, "params.png"),
                    ("DATA VISUALIZATION", self.open_page3, "visu.png")
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
        title_label = ctk.CTkLabel(main_frame, text=self.translations[self.language]["visualization_data"], font=("Arial", 28, "bold"), text_color="black")
        title_label.pack(padx=20, pady=20, anchor="center")
        
        # # Bouton simuler
        # button_next = ctk.CTkButton(main_frame, text=self.translations[self.language]["simulate"], width=100, fg_color="#1C3A6B",command=self.open_page3)
        # button_next.place(relx=0.9, rely=0.95, anchor="center")
        
        # Bouton retour
        button_back = ctk.CTkButton(main_frame, text=self.translations[self.language]["back"], width=100, fg_color="#1C3A6B", command=self.open_page2)
        button_back.place(relx=0.9, rely=0.95, anchor="center")
        

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
            Page3(self.root)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
