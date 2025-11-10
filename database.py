# database.py
import sqlite3
from sqlite3 import Connection
from typing import List, Tuple

DB_NAME = "club.db"

def conectar() -> Connection:
    conn = sqlite3.connect(DB_NAME)
    return conn

def crear_tablas():
    conn = conectar()
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS clubes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        ubicacion TEXT,
        presidente TEXT,
        fecha_fundacion TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS socios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_completo TEXT,
        edad INTEGER,
        tipo_identificacion TEXT,
        identificacion TEXT,
        nacionalidad TEXT,
        usuario TEXT UNIQUE,
        contrasena TEXT,
        fecha_inscripcion TEXT,
        estado TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS cuotas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        socio_id INTEGER,
        estado TEXT,
        fecha_vencimiento TEXT,
        periodo TEXT,
        FOREIGN KEY (socio_id) REFERENCES socios(id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS administradores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        contrasena TEXT
    )
    ''')

    # Crear un admin por defecto si no existe
    c.execute("SELECT COUNT(*) FROM administradores")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO administradores (nombre, usuario, contrasena) VALUES (?, ?, ?)",
                  ("Administrador por defecto", "Admin", "ArianaTeAmo"))

    conn.commit()
    conn.close()

# ==== Funciones de ayuda (CRUD básicos) ====

# Administradores
def get_admin_by_credentials(usuario: str, contrasena: str):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT id, nombre, usuario FROM administradores WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
    row = c.fetchone()
    conn.close()
    return row

def create_admin(nombre: str, usuario: str, contrasena: str):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO administradores (nombre, usuario, contrasena) VALUES (?, ?, ?)", (nombre, usuario, contrasena))
    conn.commit()
    conn.close()

# Socios
def insertar_socio(datos: Tuple):
    conn = conectar()
    c = conn.cursor()
    c.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, usuario, contrasena, fecha_inscripcion, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, datos)
    conn.commit()
    uid = c.lastrowid
    conn.close()
    return uid

def obtener_todos_los_socios() -> List[Tuple]:
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT id, nombre_completo, usuario, fecha_inscripcion, estado FROM socios")
    rows = c.fetchall()
    conn.close()
    return rows

def obtener_socio_por_usuario(usuario: str):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT id, nombre_completo, usuario FROM socios WHERE usuario = ? AND contrasena = ?", (usuario, usuario))  # placeholder (no usado)
    conn.close()
    return None

def obtener_socio_por_credenciales(usuario: str, contrasena: str):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT id, nombre_completo, usuario FROM socios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
    row = c.fetchone()
    conn.close()
    return row

# Clubes
def insertar_club(datos: Tuple):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO clubes (nombre, descripcion, ubicacion, presidente, fecha_fundacion) VALUES (?, ?, ?, ?, ?)", datos)
    conn.commit()
    uid = c.lastrowid
    conn.close()
    return uid

def listar_clubes() -> List[Tuple]:
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT id, nombre, descripcion, ubicacion, presidente, fecha_fundacion FROM clubes")
    rows = c.fetchall()
    conn.close()
    return rows

# Cuotas
def insertar_cuota(datos: Tuple):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO cuotas (socio_id, estado, fecha_vencimiento, periodo) VALUES (?, ?, ?, ?)", datos)
    conn.commit()
    uid = c.lastrowid
    conn.close()
    return uid

def listar_cuotas() -> List[Tuple]:
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT cuotas.id, cuotas.socio_id, socios.usuario, cuotas.estado, cuotas.fecha_vencimiento, cuotas.periodo FROM cuotas LEFT JOIN socios ON cuotas.socio_id = socios.id")
    rows = c.fetchall()
    conn.close()
    return rows