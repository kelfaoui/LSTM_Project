import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk
import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import numpy as np

from customtkinter import CTkButton, CTkImage
from tkinter import PhotoImage

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.frame_index = 0

        self.title("MainWindow")
        self.geometry("900x600")
        self.state("zoomed")

        

        self.refresh()
    
    def remove_all_frames(self):
        """Remove all frames before refreshing the content."""
        for widget in self.winfo_children():
            if isinstance(widget, (tk.Frame, ctk.CTkFrame)):  # Destroy only frames
                widget.destroy()

    def refresh(self):
        self.remove_all_frames()
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#1C3A6B")
        sidebar.pack(fill="y", side="left")

        logo_label = ctk.CTkLabel(sidebar, text="LOGO", text_color="white", font=("Helvetica", 30, "bold"))
        logo_label.pack(pady=(20, 40))

        menu_items = ["PRÉTRAITEMENT", "ENTRAÎNEMENT", "VISUALISATION DES DONNÉES"]
        idx = 0
        images = [Image.open("edit.png"), Image.open("params.png"), Image.open("visu.png")]
     
        for item in menu_items:

            if idx == 0 :
                cmd = self.show_pretraitement
            elif idx == 1 :
                cmd = self.show_training
            else:
                cmd = self.show_visualizations
            icon = CTkImage(light_image=images[idx], size=(20, 20))
            idx = idx + 1
            button = ctk.CTkButton(
                sidebar, text=item, width=200, height=40, anchor="w", corner_radius=10, font=("Helvetica", 16, "bold"), fg_color="#1C3A6B",
                command=cmd, image=icon,
            )
            button.pack(pady=(0, 20), padx=10)
        if self.frame_index == 0:
            main_frame = ctk.CTkFrame(self, fg_color="white")
            main_frame.pack(fill="both", expand=True, padx=20, pady=20)
            title_label = ctk.CTkLabel(main_frame, text="PRÉTRAITEMENT", font=("Helvetica", 28, "bold"))
            title_label.pack(padx=20, pady=20, anchor="w")

            select_label = ctk.CTkLabel(main_frame, text="sélectionner le fichier :", font=("Helvetica", 14))
            select_label.place(x=50, y=60)

            drop_frame = ctk.CTkFrame(main_frame, width=500, height=250, border_color="#d3d3d3", border_width=2, fg_color="white")
            drop_frame.place(x=300, y=60)

            drag_label = ctk.CTkLabel(drop_frame, text="Glisser déposer les fichiers ici", font=("Helvetica", 14))
            drag_label.pack(expand=True)

            browse_button = ctk.CTkButton(drop_frame, text="Browse Files", width=100)
            browse_button.pack(pady=(0, 10))

            columns = ["id-veh", "local_X", "local_Y", "altitude", "longitude"]
            y_positions = [250, 290, 330, 250, 290]
            x_positions = [50, 50, 50, 300, 300]

            for i, col in enumerate(columns):
                checkbox = ctk.CTkCheckBox(main_frame, text=col)
                checkbox.place(x=x_positions[i], y=y_positions[i])

            back_button = ctk.CTkButton(main_frame, text="BACK", width=100, fg_color="#1C3A6B", command=self.destroy)
            back_button.place(x=500, y=400)

            simulate_button = ctk.CTkButton(main_frame, text="SIMULATE", width=100, fg_color="#1C3A6B")
            simulate_button.place(x=650, y=400)

        elif self.frame_index == 1:
            main_frame = ctk.CTkFrame(self, fg_color="white")
            main_frame.pack(fill="both", expand=True, padx=20, pady=20)

            title_label = ctk.CTkLabel(main_frame, text="ENTRAÎNEMENT", font=("Helvetica", 28, "italic"), text_color="black")
            title_label.pack(pady=10)

            # Algo Section Titles
            algo_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
            algo_frame.pack(pady=20, expand=True)

            algo1_label = ctk.CTkLabel(algo_frame, text="Algo 1", font=("Helvetica", 20, "bold"))
            algo1_label.grid(row=0, column=0, padx=100, pady=10)

            algo2_label = ctk.CTkLabel(algo_frame, text="Algo 2", font=("Helvetica", 20, "bold"))
            algo2_label.grid(row=0, column=1, padx=100, pady=10)

            # Checkbox Labels
            algo1_options = [
                "nombre",
                "nombre LSTM",
                "nombre de alpha",
                "autre",
                "autre",
                "autre"
            ]

            algo2_options = [
                "nombre",
                "nombre LSTM",
                "nombre de alpha",
                "autre",
                "autre",
                "autre"
            ]

            # Create Checkboxes for Algo 1 and Algo 2
            for i, option in enumerate(algo1_options):
                checkbox = ctk.CTkCheckBox(algo_frame, text=option + " ℹ")
                checkbox.grid(row=i + 1, column=0, padx=50, pady=10, sticky="w")

            for i, option in enumerate(algo2_options):
                checkbox = ctk.CTkCheckBox(algo_frame, text=option + " ℹ")
                checkbox.grid(row=i + 1, column=1, padx=50, pady=10, sticky="w")

            # Back and Simulate Buttons
            button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
            button_frame.pack(pady=20)

            back_button = ctk.CTkButton(button_frame, text="BACK", width=100, fg_color="#1C3A6B")
            back_button.grid(row=0, column=0, padx=20)

            simulate_button = ctk.CTkButton(button_frame, text="SIMULATE", width=100, fg_color="#1C3A6B")
            simulate_button.grid(row=0, column=1, padx=20)
        else:
            x = np.linspace(0, 60, 100)
            true_latitude = 30 + np.sin(x / 10) * 0.5
            predicted_latitude = 30 + np.sin(x / 10) * 0.5 + np.random.normal(0, 0.05, len(x))
            true_longitude = -97 + np.cos(x / 10) * 0.5
            predicted_longitude = -97 + np.cos(x / 10) * 0.5 + np.random.normal(0, 0.05, len(x))
            main_frame = ctk.CTkFrame(self, fg_color="white")
            main_frame.pack(fill="both", expand=True, padx=20, pady=20)
            title_label = ctk.CTkLabel(main_frame, text="ENTRAÎNEMENT", font=("Helvetica", 28, "italic"), text_color="black")


            fig = Figure(figsize=(6, 4), dpi=100)
            ax1 = fig.add_subplot(211)
            ax2 = fig.add_subplot(212)

            ax1.plot(x, true_latitude, label="True Latitude", color='blue')
            ax1.plot(x, predicted_latitude, label="Predicted Latitude", color='orange')
            ax1.legend()
            ax1.set_title("True Latitude vs Predicted Latitude")

            ax2.plot(x, true_longitude, label="True Longitude", color='blue')
            ax2.plot(x, predicted_longitude, label="Predicted Longitude", color='orange')
            ax2.legend()
            ax2.set_title("True Longitude vs Predicted Longitude")


            canvas = FigureCanvasTkAgg(fig, master=main_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

            button_frame = ctk.CTkFrame(main_frame)
            button_frame.pack(pady=10)

            back_button = ctk.CTkButton(button_frame, text="BACK")
            back_button.pack(side="left", padx=10)

            simulate_button = ctk.CTkButton(button_frame, text="SIMULATE")
            simulate_button.pack(side="right", padx=10)
        
    def show_pretraitement(self):
        self.frame_index = 0
        self.refresh()

    def show_training(self):
        self.frame_index = 1
        self.refresh()
    
    def show_visualizations(self):
        self.frame_index = 2
        self.refresh()



class Launcher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Launcher")
        self.geometry("700x500")
        self.resizable(False, False)

        logo_label = ctk.CTkLabel(self, text="LOGO", font=("Helvetica", 20, "italic"), text_color="gray")
        logo_label.place(x=20, y=20)

        title_label = ctk.CTkLabel(self, text="Prédiction de la congestion routière", font=("Helvetica", 32, "bold"))
        title_label.pack(pady=80)

        start_button = ctk.CTkButton(self, text="START", width=100, height=40, fg_color="#1C3A6B", font=("Helvetica", 18), command=self.open_main_window)
        start_button.pack(pady=20)

        lang_frame = ctk.CTkFrame(self, fg_color="transparent")
        lang_frame.pack(pady=20)

        fr_image = Image.open("france_flag.png").resize((50, 50))
        fr_icon = ImageTk.PhotoImage(fr_image)

        en_image = Image.open("uk_flag.png").resize((50, 50))
        en_icon = ImageTk.PhotoImage(en_image)

        self.fr_button = ctk.CTkButton(lang_frame, image=fr_icon, text="FRANÇAIS", compound="top", width=80, height=80)
        self.fr_button.grid(row=0, column=0, padx=20)

        self.en_button = ctk.CTkButton(lang_frame, image=en_icon, text="ENGLISH", compound="top", width=80, height=80)
        self.en_button.grid(row=0, column=1, padx=20)

        self.fr_icon = fr_icon
        self.en_icon = en_icon

    def open_main_window(self):
        MainWindow(self)
        self.withdraw()


if __name__ == "__main__":
    app = Launcher()
    app.mainloop()
