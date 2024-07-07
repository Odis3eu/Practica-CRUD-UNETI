import sqlite3

def init_db():
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        edad INTEGER NOT NULL,
                        email TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def agregar_registro(nombre, edad, email):
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registros (nombre, edad, email) VALUES (?, ?, ?)", (nombre, edad, email))
    conn.commit()
    conn.close()

def modificar_registro(id_registro, nombre, edad, email):
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE registros SET nombre = ?, edad = ?, email = ? WHERE id = ?", (nombre, edad, email, id_registro))
    conn.commit()
    conn.close()

def eliminar_registro(id_registro):
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registros WHERE id = ?", (id_registro,))
    conn.commit()
    conn.close()

def listar_registros():
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros")
    registros = cursor.fetchall()
    conn.close()
    return registros
