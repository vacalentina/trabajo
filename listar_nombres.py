import os

carpeta = r"C:\Users\Valentina\Downloads\oxxo\OneDrive_2025-07-17 (3)\metalico"  # Cambia esto por la ruta real

# Lista todos los archivos (no carpetas) en la ruta especificada
nombres_archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]

# Imprimir los nombres
for nombre in nombres_archivos:
    print(nombre)
