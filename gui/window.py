import tkinter as tk
from tkinter import ttk

class DashboardWindow:
    
    def __init__(self):
        self.root = tk.Tk()                     # Crear Ventana
        self.root.title("Dashboard APP v0.1")   # Titulo de la APP
        self.root.geometry("800x500")           # Ancho x Alto

        self.build_ui()                         # Llama a la construcción de la interfaz
    
    def build_ui(self):
        # Construcción y organización de todos los widgets dentro de la ventana

        label = ttk.Label(self.root, text="BIENVENIDO AL DASHBOARD APP", font=("Arial", 18))
        label.pack(pady=20)

    def run(self):
        self.root.mainloop()                    # Inicia el Loop de eventos de Tkinter