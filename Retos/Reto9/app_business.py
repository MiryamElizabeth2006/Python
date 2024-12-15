from Retos.Reto9.laptop_business import Laptop_Business
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

#Para crear una pantalla de vista
class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = [r"C:\\Users\\mirya\\OneDrive\Escritorio\\KRAKEDEV\\CURSO-KRAKEDEV-ELIZABETH _NONO\\MODULO-6-KRAKEDEV\\EjerciciosPOO\\clase1\\img\\laptop1.png", 
                         r"C:\\Users\\mirya\\OneDrive\\Escritorio\\KRAKEDEV\\CURSO-KRAKEDEV-ELIZABETH _NONO\\MODULO-6-KRAKEDEV\\EjerciciosPOO\\clase1\\img\\laptop2.png",
                         r"C:\\Users\\mirya\\OneDrive\\Escritorio\\KRAKEDEV\\CURSO-KRAKEDEV-ELIZABETH _NONO\\MODULO-6-KRAKEDEV\\EjerciciosPOO\\clase1\\img\\laptop3.png",
                         r"C:\\Users\\mirya\\OneDrive\\Escritorio\\KRAKEDEV\\CURSO-KRAKEDEV-ELIZABETH _NONO\\MODULO-6-KRAKEDEV\\EjerciciosPOO\\clase1\\img\\laptop4.png", 
                         r"C:\\Users\\mirya\\OneDrive\\Escritorio\\KRAKEDEV\\CURSO-KRAKEDEV-ELIZABETH _NONO\\MODULO-6-KRAKEDEV\\EjerciciosPOO\\clase1\\img\\laptop5.png"
                         ]

        root.title("Ingresar Datos Laptop Bussines")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text="Costo").grid(row=4, column=0)
        self.costo = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.costo).grid(row=4, column=1)

        ttk.Label(self.root, text="Almacenamiento").grid(row=5, column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=5, column=1)

        ttk.Label(self.root, text="Duración de Bateria").grid(row=6, column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=6, column=1)

        ttk.Button(self.root, text="Agregar Laptop Business", command=self.agregar_laptop).grid(row=7, column=0, columnspan=2)


        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=8, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200 )
        self.canva.grid(row=1, column=3, rowspan=6)

    def agregar_laptop_business(self):
        nueva_laptop = Laptop_Business(
            self.marca.get(), 
            self.procesador.get(), 
            self.memoria.get(), 
            self.costo.get(), 
            self.almacenamiento.get(), 
            self.duracion_bateria.get()
            )
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")

        self.mostrar_imagen_aleatorios()

    def mostrar_imagen_aleatorios(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW, image = photo)
        self.canva.image = photo

pass

root = tk.Tk()

app = App(root)
root.mainloop()

