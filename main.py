import tkinter as tk
import subprocess
import os
import webbrowser

# Ruta de instalación de XAMPP
xampp_path = r"C:\xampp"

def iniciar_y_abrir_web():
    try:
        # Ejecutar Apache y MySQL
        subprocess.Popen(os.path.join(xampp_path, "apache_start.bat"), shell=True)
        subprocess.Popen(os.path.join(xampp_path, "mysql_start.bat"), shell=True)

        # Abrir navegador después de un pequeño retraso
        ventana.after(3000, lambda: webbrowser.open("http://localhost/App-fichaje/"))

        status_label.config(text="Servidores iniciados y navegador abierto", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

# Crear ventana
ventana = tk.Tk()
ventana.title("Iniciar XAMPP y Abrir App")
ventana.geometry("320x150")

# Botón
boton = tk.Button(ventana, text="Iniciar y Abrir App", command=iniciar_y_abrir_web, height=2, width=30)
boton.pack(pady=20)

# Etiqueta de estado
status_label = tk.Label(ventana, text="")
status_label.pack()

ventana.mainloop()
