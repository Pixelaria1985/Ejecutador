import tkinter as tk
import subprocess
import os
import sys

# Ruta de instalación de XAMPP
xampp_path = r"C:\xampp"

# Obtener la ruta del ejecutable 'pepe.exe' (en la misma carpeta que este script)
def obtener_ruta_local(nombre_archivo):
    if getattr(sys, 'frozen', False):
        # Si el script está convertido en .exe
        carpeta_base = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    else:
        # Si se ejecuta como script .py
        carpeta_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(carpeta_base, nombre_archivo)

def iniciar_y_ejecutar_pepe():
    try:
        # Iniciar Apache y MySQL
        subprocess.Popen(os.path.join(xampp_path, "apache_start.bat"), shell=True)
        subprocess.Popen(os.path.join(xampp_path, "mysql_start.bat"), shell=True)

        # Ejecutar _NOMBRE_DEL_EJECUTABLE_.exe después de un breve retraso el cual esta en una carpeta llamada dist
        pepe_ruta = obtener_ruta_local("dist/_NOMBRE_DEL_EJECUTABLE_.exe")
        ventana.after(3000, lambda: subprocess.Popen(pepe_ruta, shell=True))

        status_label.config(text="Servidores iniciados y 'pepe.exe' ejecutado", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

# Crear interfaz
ventana = tk.Tk()
ventana.title("Iniciar XAMPP y Ejecutar Pepe")
ventana.geometry("320x150")

boton = tk.Button(ventana, text="Iniciar y Ejecutar Pepe", command=iniciar_y_ejecutar_pepe, height=2, width=30)
boton.pack(pady=20)

status_label = tk.Label(ventana, text="")
status_label.pack()

ventana.mainloop()
