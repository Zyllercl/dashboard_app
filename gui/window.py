import tkinter as tk

class DashboardWindow:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard APP v0.1")
        self.root.geometry("600x400") # Ancho x Alto
    
    def run(self):
        self.root.mainloop()