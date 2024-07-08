import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def crear_lista_archivos_ruta(ruta, nivel=0, ignorar_archivos=['Desktop.ini']):
    """Crea una lista recursiva de archivos y directorios, ignorando los especificados.

    Args:
        ruta (str): La ruta del directorio para comenzar la lista.
        nivel (int, optional): El nivel de indentación actual. Defaults to 0.
        ignorar_archivos (list, optional): Una lista de nombres de archivos a ignorar. 
                                            Defaults to ['Desktop'].

    Returns:
        list: Una lista de cadenas que representan los archivos y directorios encontrados.
    """
    lista_archivos = []
    for archivo in os.listdir(ruta):
        if archivo in ignorar_archivos:
            continue  # Ignorar archivos especificados
        archivo_ruta = os.path.join(ruta, archivo)
        if os.path.isdir(archivo_ruta):
            lista_archivos.append("  " * nivel + "**" + archivo + "**/")
            lista_archivos.extend(crear_lista_archivos_ruta(archivo_ruta, nivel + 1, ignorar_archivos))
        else:
            lista_archivos.append("  " * nivel + archivo)
    return lista_archivos

def guardar_lista_en_archivo(lista_archivos, ruta_archivo):
    """Guarda la lista de archivos en un archivo de texto.

    Args:
        lista_archivos (list): La lista de archivos a guardar.
        ruta_archivo (str): La ruta del archivo para guardar la lista.
    """
    with open(ruta_archivo, 'w') as archivo:
        for linea in lista_archivos:
            archivo.write(linea + '\n')

def generar_listado():
    """Solicita al usuario un directorio y genera un listado de archivos en un archivo 'listado.md'.
    """
    ruta = filedialog.askdirectory()
    if ruta:
        lista_archivos = crear_lista_archivos_ruta(ruta)
        ruta_archivo = os.path.join(ruta, 'listado.md')
        guardar_lista_en_archivo(lista_archivos, ruta_archivo)
        messagebox.showinfo("Completado", f"El archivo listado.md ha sido generado en {ruta}")

def crear_interfaz():
    """Crea la interfaz gráfica de usuario para el programa.
    """
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