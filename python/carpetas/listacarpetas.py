import os
import sys

def listar_archivos_y_carpetas(directorio='.', ignorar=['desktop.ini'], nivel=0):
    contenido = ""
    for raiz, directorios, archivos in os.walk(directorio):
        if nivel == 0:
            try:
                nombre_directorio = os.path.basename(raiz)
                contenido += f"# {nombre_directorio}\n\n"
            except UnicodeEncodeError:
                contenido += "# [Nombre de directorio no imprimible]\n\n"
        
        for directorio in sorted(directorios):
            indentacion = "  " * nivel
            try:
                contenido += f"{indentacion}- **{directorio}/**\n"
                contenido += listar_archivos_y_carpetas(os.path.join(raiz, directorio), ignorar, nivel + 1)
            except UnicodeEncodeError:
                contenido += f"{indentacion}- **[Nombre de directorio no imprimible]/**\n"
        
        for archivo in sorted(archivos):
            if archivo not in ignorar:
                indentacion = "  " * (nivel + 1)
                try:
                    contenido += f"{indentacion}- {archivo}\n"
                except UnicodeEncodeError:
                    contenido += f"{indentacion}- [Nombre de archivo no imprimible]\n"
        
        break  # Solo procesamos el directorio actual en cada llamada recursiva
    
    return contenido

# Configurar la codificación de salida
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Generar y mostrar el listado
listado = listar_archivos_y_carpetas()
print(listado)

# Opcionalmente, guardar el listado en un archivo
with open('listado.md', 'w', encoding='utf-8') as f:
    f.write(listado)