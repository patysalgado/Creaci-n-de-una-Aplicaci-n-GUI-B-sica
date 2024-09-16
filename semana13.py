import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry_dato.get()
    if dato:
        listbox_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un dato.")

# Función para limpiar la lista
def limpiar_lista():
    listbox_datos.delete(0, tk.END)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación de Gestión de Datos")
root.geometry("400x300")

# Etiqueta
label_instrucciones = tk.Label(root, text="Ingrese un dato y haga clic en 'Agregar'")
label_instrucciones.pack(pady=10)

# Campo de texto
entry_dato = tk.Entry(root, width=40)
entry_dato.pack(pady=5)

# Botones
button_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
button_agregar.pack(side=tk.LEFT, padx=20)

button_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
button_limpiar.pack(side=tk.RIGHT, padx=20)

# Lista para mostrar datos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

scrollbar = Scrollbar(frame_lista, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_datos = Listbox(frame_lista, width=50, height=10, yscrollcommand=scrollbar.set)
listbox_datos.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox_datos.yview)

# Ejecutar la aplicación
root.mainloop()
