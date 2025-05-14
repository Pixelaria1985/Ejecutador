import tkinter as tk
import subprocess
import os

# Ruta de instalación de XAMPP
xampp_path = r"C:\xampp"

def iniciar_servidores():
    # Comandos para iniciar Apache y MySQL usando el ejecutable de XAMPP
    apache_cmd = os.path.join(xampp_path, "apache_start.bat")
    mysql_cmd = os.path.join(xampp_path, "mysql_start.bat")

    try:
        subprocess.Popen(apache_cmd, shell=True)
        subprocess.Popen(mysql_cmd, shell=True)
        status_label.config(text="Servidores iniciados.", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Iniciar Servidores XAMPP")
ventana.geometry("300x150")

boton = tk.Button(ventana, text="Iniciar Apache y MySQL", command=iniciar_servidores, height=2, width=25)
boton.pack(pady=20)

status_label = tk.Label(ventana, text="")
status_label.pack()

ventana.mainloop()
