import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime

DB_NAME = "club.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tablas():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
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
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS cuotas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        socio_id INTEGER,
        estado TEXT,
        fecha_vencimiento TEXT,
        periodo TEXT,
        FOREIGN KEY(socio_id) REFERENCES socios(id)
    )
    """)

    conn.commit()
    conn.close()

# =======================
# NUEVA FUNCIÓN MODIFICADA
# =======================
def insertar_socio(socio):
    conn = conectar()
    c = conn.cursor()

    try:
        c.execute("""
            INSERT INTO socios (
                nombre_completo, edad, tipo_identificacion, identificacion,
                nacionalidad, usuario, contrasena, fecha_inscripcion, estado
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            socio.nombre_completo, socio.edad, socio.tipo_identificacion,
            socio.identificacion, socio.nacionalidad,
            socio.usuario, socio.contrasena,
            socio.fecha_inscripcion, socio.estado
        ))
        conn.commit()

        socio_id = c.lastrowid
        conn.close()
        return socio_id

    except sqlite3.IntegrityError:
        # Usuario duplicado
        conn.close()
        return None


def obtener_socio_por_credenciales(usuario, contrasena):
    conn = conectar()
    c = conn.cursor()
    c.execute("""
        SELECT id, nombre_completo, edad, tipo_identificacion,
               identificacion, nacionalidad, usuario, contrasena,
               fecha_inscripcion, estado
        FROM socios
        WHERE usuario = ? AND contrasena = ?
    """, (usuario, contrasena))
    row = c.fetchone()
    conn.close()
    return row

def insertar_cuota_inicial(socio_id):
    conn = conectar()
    c = conn.cursor()
    c.execute("""
        INSERT INTO cuotas (socio_id, estado, fecha_vencimiento, periodo)
        VALUES (?, ?, ?, ?)
    """, (socio_id, "Pendiente", "2025-12-01", "2025-11"))
    conn.commit()
    conn.close()


class Socio:
    def __init__(self, nombre_completo, edad, tipo_identificacion,
                 identificacion, nacionalidad, usuario, contrasena,
                 estado):

        self.nombre_completo = nombre_completo
        self.edad = edad
        self.tipo_identificacion = tipo_identificacion
        self.identificacion = identificacion
        self.nacionalidad = nacionalidad
        self.usuario = usuario
        self.contrasena = contrasena
        self.estado = estado
        self.fecha_inscripcion = datetime.today().strftime("%Y-%m-%d")


# =======================
# Tkinter
# =======================

FONDO_LOGIN = "../img/cancha.jpg"
FONDO_HOME = "./media/fondo_home.jpg"

root = tk.Tk()
root.title("Club Atlético Vélez Sarsfield")
root.geometry("1000x600")
root.configure(bg="navy")


def cargar_fondo(ruta, tamaño):
    try:
        img = Image.open(ruta)
        img = img.resize(tamaño, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None

def limpiar_pantalla():
    for w in root.winfo_children():
        w.destroy()



# =======================
# LOGIN
# =======================
def mostrar_login():
    limpiar_pantalla()

    global fondo_login_img
    fondo_login_img = cargar_fondo(FONDO_LOGIN, (1000, 600))
    if fondo_login_img:
        tk.Label(root, image=fondo_login_img).place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Acceso al Club Vélez Sarsfield",
             font=("Helvetica", 18, "bold"), fg="#0033A0", bg="white").grid(row=0, column=0, columnspan=2, pady=15)

    tk.Label(frame, text="Usuario:", bg="white").grid(row=1, column=0, padx=5, pady=5)
    usuario_entry = tk.Entry(frame, width=25)
    usuario_entry.grid(row=1, column=1)

    tk.Label(frame, text="Contraseña:", bg="white").grid(row=2, column=0, padx=5, pady=5)
    contrasena_entry = tk.Entry(frame, show="*", width=25)
    contrasena_entry.grid(row=2, column=1)

    def intentar_login():
        user = usuario_entry.get()
        pwd = contrasena_entry.get()

        socio = obtener_socio_por_credenciales(user, pwd)

        if socio:
            mostrar_home(socio)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(frame, text="Ingresar", bg="#0033A0", fg="white",
              width=15, command=intentar_login).grid(row=3, column=0, columnspan=2, pady=10)

    tk.Button(frame, text="Registrarse", bg="#00A859", fg="white",
              width=15, command=mostrar_registro).grid(row=4, column=0, columnspan=2)



# =======================
# REGISTRO
# =======================
def mostrar_registro():
    limpiar_pantalla()

    frame = tk.Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Registro de Socio",
             font=("Helvetica", 18, "bold"), fg="#0033A0", bg="white").grid(row=0, column=0, columnspan=2, pady=10)

    campos = [
        "Nombre completo",
        "Edad",
        "Tipo identificación",
        "N° Identificación",
        "Nacionalidad",
        "Usuario",
        "Contraseña"
    ]

    entries = {}
    row = 1
    for campo in campos:
        tk.Label(frame, text=campo + ":", bg="white").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        ent = tk.Entry(frame, width=25)
        ent.grid(row=row, column=1, pady=5)
        entries[campo] = ent
        row += 1

    def registrar():
        try:
            socio = Socio(
                entries["Nombre completo"].get(),
                int(entries["Edad"].get()),
                entries["Tipo identificación"].get(),
                entries["N° Identificación"].get(),
                entries["Nacionalidad"].get(),
                entries["Usuario"].get(),
                entries["Contraseña"].get(),
                "Activo"
            )
        except:
            messagebox.showerror("Error", "Datos inválidos")
            return

        socio_id = insertar_socio(socio)

        if socio_id is None:
            messagebox.showerror("Error", "Este usuario ya está registrado.\nIngrese otro nombre de usuario.")
            return

        insertar_cuota_inicial(socio_id)

        messagebox.showinfo("Éxito", "Socio registrado correctamente")
        mostrar_login()

    tk.Button(frame, text="Registrar", bg="#00A859", fg="white",
              width=15, command=registrar).grid(row=row, column=0, columnspan=2, pady=10)

    tk.Button(frame, text="Volver", bg="#0033A0", fg="white",
              width=15, command=mostrar_login).grid(row=row+1, column=0, columnspan=2, pady=5)



# =======================
# HOME
# =======================
def mostrar_home(socio):
    limpiar_pantalla()

    global fondo_home_img
    fondo_home_img = cargar_fondo(FONDO_HOME, (1000, 600))
    if fondo_home_img:
        tk.Label(root, image=fondo_home_img).place(x=0, y=0, relwidth=1, relheight=1)

    header = tk.Frame(root, bg="black", height=60)
    header.pack(fill="x")

    tk.Label(header, text=f"Bienvenido, {socio[1]}",
             fg="white", bg="black", font=("Helvetica", 18, "bold")).pack(side="left", padx=25)

    tk.Button(header, text="Cerrar sesión", bg="#0033A0", fg="white",
              font=("Arial", 11, "bold"),
              command=mostrar_login, cursor="hand2").pack(side="right", padx=20)

    sombra = tk.Frame(root, bg="medium blue", width=420, height=420)
    sombra.place(relx=0.5, rely=0.55, anchor="center", x=4, y=4) 

    card = tk.Frame(root, bg="white", bd=0, width=420, height=420)
    card.place(relx=0.5, rely=0.55, anchor="center")

    tk.Label(card, text="Datos del Socio",
             font=("Helvetica", 20, "bold"),
             fg="#0033A0", bg="white").pack(pady=(25, 5))

    tk.Frame(card, bg="#0033A0", height=2, width=260).pack(pady=(0, 20))

    datos = [
        ("Nombre", socio[1]),
        ("Edad", socio[2]),
        ("Tipo identificación", socio[3]),
        ("Identificación", socio[4]),
        ("Nacionalidad", socio[5]),
        ("Usuario", socio[6]),
        ("Estado", socio[9]),
        ("Fecha de inscripción", socio[8]),
    ]

    for etiqueta, valor in datos:
        fila = tk.Frame(card, bg="white")
        fila.pack(anchor="w", padx=30, pady=6)

        tk.Label(fila, text=f"{etiqueta}:",
                 font=("Arial", 12, "bold"),
                 fg="#0033A0", bg="white").pack(side="left")

        tk.Label(fila, text=f" {valor}",
                 font=("Arial", 12),
                 bg="white").pack(side="left")


crear_tablas()
mostrar_login()
root.mainloop()
