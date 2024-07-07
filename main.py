import tkinter as tk
from tkinter import messagebox
import database  # Importamos nuestro módulo de base de datos

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Registros CRUD")
        self.root.geometry("700x650")  # Aumentamos el tamaño de la ventana
        self.root.configure(bg='#2c3e50')

        # Configurar la cuadrícula principal
        for i in range(8):  # Ajustamos el peso de las filas
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(3):  # Ajustamos el peso de las columnas
            self.root.grid_columnconfigure(i, weight=1)

        # Título
        self.title_label = tk.Label(root, text="Gestión de Registros", font=('Helvetica', 24, 'bold'), fg='#ecf0f1', bg='#2c3e50')
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(20, 30), sticky='nsew')

        # Nombre
        self.nombre_label = tk.Label(root, text="Nombre:", font=('Helvetica', 16), fg='#ecf0f1', bg='#2c3e50')
        self.nombre_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky='e')
        self.nombre_entry = tk.Entry(root, font=('Helvetica', 16))
        self.nombre_entry.grid(row=1, column=1, padx=20, pady=(10, 5), sticky='ew')

        # Edad
        self.edad_label = tk.Label(root, text="Edad:", font=('Helvetica', 16), fg='#ecf0f1', bg='#2c3e50')
        self.edad_label.grid(row=2, column=0, padx=20, pady=5, sticky='e')
        self.edad_entry = tk.Entry(root, font=('Helvetica', 16))
        self.edad_entry.grid(row=2, column=1, padx=20, pady=5, sticky='ew')

        # Email
        self.email_label = tk.Label(root, text="Email:", font=('Helvetica', 16), fg='#ecf0f1', bg='#2c3e50')
        self.email_label.grid(row=3, column=0, padx=20, pady=5, sticky='e')
        self.email_entry = tk.Entry(root, font=('Helvetica', 16))
        self.email_entry.grid(row=3, column=1, padx=20, pady=5, sticky='ew')

        # Botones
        button_font = ('Helvetica', 16)  # Fuente para los botones
        button_width = 10  # Ancho de los botones
        button_padx = 10  # Padding en X para los botones
        button_pady = 5  # Padding en Y para los botones

        self.add_button = tk.Button(root, text="Agregar", font=button_font, width=button_width, bg='#1abc9c', fg='#ecf0f1', command=self.agregar_registro)
        self.add_button.grid(row=4, column=0, padx=button_padx, pady=button_pady, sticky='ew')

        self.update_button = tk.Button(root, text="Modificar", font=button_font, width=button_width, bg='#f39c12', fg='#ecf0f1', command=self.modificar_registro)
        self.update_button.grid(row=4, column=1, padx=button_padx, pady=button_pady, sticky='ew')

        self.delete_button = tk.Button(root, text="Eliminar", font=button_font, width=button_width, bg='#e74c3c', fg='#ecf0f1', command=self.eliminar_registro)
        self.delete_button.grid(row=4, column=2, padx=button_padx, pady=button_pady, sticky='ew')

        # ID
        self.id_label = tk.Label(root, text="ID:", font=('Helvetica', 16), fg='#ecf0f1', bg='#2c3e50')
        self.id_label.grid(row=5, column=0, padx=20, pady=(20, 5), sticky='e')
        self.id_entry = tk.Entry(root, font=('Helvetica', 16))
        self.id_entry.grid(row=5, column=1, padx=20, pady=(20, 5), sticky='ew')

        # Botón de Listar
        self.list_button = tk.Button(root, text="Listar Registros", font=button_font, width=button_width+5, bg='#3498db', fg='#ecf0f1', command=self.listar_registros)
        self.list_button.grid(row=6, column=0, columnspan=3, padx=button_padx, pady=(20, 30), sticky='ew')

        # Área de texto
        self.text_area = tk.Text(root, height=10, width=60, font=('Helvetica', 14))
        self.text_area.grid(row=7, column=0, columnspan=3, padx=20, pady=(0, 20), sticky='nsew')

    def agregar_registro(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        email = self.email_entry.get()
        if nombre and edad and email:
            database.agregar_registro(nombre, edad, email)
            messagebox.showinfo("Información", "Registro agregado correctamente")
            # Limpiar los campos después de agregar
            self.nombre_entry.delete(0, tk.END)
            self.edad_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def modificar_registro(self):
        id_registro = self.id_entry.get()
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        email = self.email_entry.get()
        if id_registro and nombre and edad and email:
            database.modificar_registro(id_registro, nombre, edad, email)
            messagebox.showinfo("Información", "Registro modificado correctamente")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def eliminar_registro(self):
        id_registro = self.id_entry.get()
        if id_registro:
            database.eliminar_registro(id_registro)
            messagebox.showinfo("Información", "Registro eliminado correctamente")
        else:
            messagebox.showerror("Error", "El campo ID es obligatorio")

    def listar_registros(self):
        registros = database.listar_registros()
        self.text_area.delete('1.0', tk.END)
        for registro in registros:
            self.text_area.insert(tk.END, f"ID: {registro[0]}, Nombre: {registro[1]}, Edad: {registro[2]}, Email: {registro[3]}\n")

if __name__ == "__main__":
    database.init_db()  # Inicializamos la base de datos
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
