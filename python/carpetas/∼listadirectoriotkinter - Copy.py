import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def crear_lista_archivos_ruta(ruta, nivel=0):
    lista_archivos = []
    for archivo in os.listdir(ruta):
        archivo_ruta = os.path.join(ruta, archivo)
        if os.path.isdir(archivo_ruta):
            lista_archivos.append("  " * nivel + "**" + archivo + "**/")
            lista_archivos.extend(crear_lista_archivos_ruta(archivo_ruta, nivel + 1))
        else:
            lista_archivos.append("  " * nivel + archivo)
    return lista_archivos

def guardar_lista_en_archivo(lista_archivos, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        for linea in lista_archivos:
            archivo.write(linea + '\n')

def generar_listado():
    ruta = filedialog.askdirectory()
    if ruta:
        lista_archivos = crear_lista_archivos_ruta(ruta)
        ruta_archivo = os.path.join(ruta, 'listado.md')
        guardar_lista_en_archivo(lista_archivos, ruta_archivo)
        messagebox.showinfo("Completado", f"El archivo listado.md ha sido generado en {ruta}")

def crear_interfaz():
    root = tk.Tk()
    root.title("Generador de Listado de Archivos")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    label = tk.Label(frame, text="Seleccione el directorio y genere el listado:")
    label.pack(pady=10)

    boton = tk.Button(frame, text="Seleccionar Directorio y Generar Listado", command=generar_listado)
    boton.pack(pady=10)

    root.mainloop()

# Ejecutar la interfaz
crear_interfaz()
