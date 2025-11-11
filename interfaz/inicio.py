import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

FONDO_LOGIN = "../img/cancha.jpg"
FONDO_HOME = "./media/fondo_home.jpg"

# Ventana principal
root = tk.Tk()
root.title("Club Atlético Vélez Sarsfield")
root.geometry("1000x600")

# --- VARIABLES GLOBALES ---
usuarios = {"S": {"password": "23", "cuota": "Al día"}} 


# --- FUNCIONES AUXILIARES ---
def cargar_fondo(ruta, tamaño):
    """Carga y ajusta una imagen de fondo si existe."""
    try:
        img = Image.open(ruta)
        img = img.resize(tamaño, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None


def limpiar_pantalla():
    """Elimina todos los widgets actuales de la ventana."""
    for widget in root.winfo_children():
        widget.destroy()


# --- PANTALLA DE LOGIN ---
def mostrar_login():
    limpiar_pantalla()

    global fondo_login_img
    fondo_login_img = cargar_fondo(FONDO_LOGIN, (1000, 600))
    if fondo_login_img:
        tk.Label(root, image=fondo_login_img).place(x=0, y=0, relwidth=1, relheight=1)
    else:
        root.config(bg="#0033A0")

    frame = tk.Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Acceso al Club Vélez Sarsfield",
             font=("Helvetica", 18, "bold"), fg="#0033A0", bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 15))

    tk.Label(frame, text="Usuario:", bg="white").grid(row=1, column=0, padx=5, pady=5)
    usuario_entry = tk.Entry(frame, width=25)
    usuario_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Contraseña:", bg="white").grid(row=2, column=0, padx=5, pady=5)
    contrasena_entry = tk.Entry(frame, show="*", width=25)
    contrasena_entry.grid(row=2, column=1, pady=5)

    def intentar_login():
        user = usuario_entry.get().strip()
        password = contrasena_entry.get().strip()

        if user == "" or password == "":
            messagebox.showerror("Error", "Complete todos los campos requeridos")
        elif user in usuarios and usuarios[user]["password"] == password:
            mostrar_home(user)
        else:
            messagebox.showerror("Error", "Usuario o Contraseña Incorrectos")

    def mostrar_registro():
        limpiar_pantalla()
        mostrar_pantalla_registro()

    tk.Button(frame, text="Ingresar", bg="#0033A0", fg="white", width=15,
              command=intentar_login).grid(row=3, column=0, columnspan=2, pady=(10, 5))

    tk.Label(frame, text="¿No tenés una cuenta?", bg="white").grid(row=4, column=0, columnspan=2, pady=(5, 0))
    tk.Button(frame, text="Registrarse", bg="#00A859", fg="white", width=15,
              command=mostrar_registro).grid(row=5, column=0, columnspan=2, pady=5)


# --- PANTALLA DE REGISTRO ---
def mostrar_pantalla_registro():
    frame = tk.Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Registro de Socio",
             font=("Helvetica", 18, "bold"), fg="#0033A0", bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 15))

    tk.Label(frame, text="Nuevo Usuario:", bg="white").grid(row=1, column=0, padx=5, pady=5)
    nuevo_usuario = tk.Entry(frame, width=25)
    nuevo_usuario.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Contraseña:", bg="white").grid(row=2, column=0, padx=5, pady=5)
    nueva_contra = tk.Entry(frame, show="*", width=25)
    nueva_contra.grid(row=2, column=1, pady=5)

    def registrar_usuario():
        user = nuevo_usuario.get().strip()
        password = nueva_contra.get().strip()

        if user == "" or password == "":
            messagebox.showerror("Error", "Debe completar todos los campos.")
        elif user in usuarios:
            messagebox.showerror("Error", "Ese usuario ya existe.")
        else:
            usuarios[user] = {"password": password, "cuota": "Pendiente"}
            messagebox.showinfo("Éxito", "Registro completado. Ahora podés iniciar sesión.")
            mostrar_login()

    tk.Button(frame, text="Registrar", bg="#00A859", fg="white", width=15,
              command=registrar_usuario).grid(row=3, column=0, columnspan=2, pady=(10, 5))

    tk.Button(frame, text="Volver", bg="#0033A0", fg="white", width=15,
              command=mostrar_login).grid(row=4, column=0, columnspan=2, pady=5)


# --- PANTALLA PRINCIPAL (HOME) ---
def mostrar_home(usuario):
    limpiar_pantalla()

    global fondo_home_img
    fondo_home_img = cargar_fondo(FONDO_HOME, (1000, 600))
    if fondo_home_img:
        tk.Label(root, image=fondo_home_img).place(x=0, y=0, relwidth=1, relheight=1)
    else:
        root.config(bg="#002B5C")

    # Encabezado
    header = tk.Frame(root, bg="#000000", height=60)
    header.pack(fill="x")
    tk.Label(header, text=f"Bienvenido al Club Atlético Vélez Sarsfield, {usuario}",
             font=("Helvetica", 16, "bold"), fg="white", bg="#000000").pack(side="left", padx=20)
    tk.Button(header, text="Cerrar sesión", bg="#0033A0", fg="white",
              command=mostrar_login).pack(side="right", padx=20, pady=10)

    # Cuerpo principal
    frame = tk.Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.55, anchor="center", width=700, height=400)

    # Sección: Información general
    tk.Label(frame, text="Sección de Socios", font=("Helvetica", 18, "bold"),
             fg="#0033A0", bg="white").pack(pady=20)
    tk.Label(frame, text="Aquí podrás consultar tus datos, cuotas y eventos del club.",
             font=("Arial", 12), bg="white", fg="#222").pack(pady=10)

    # --- NUEVAS SECCIONES ---
    info_frame = tk.Frame(frame, bg="#F2F2F2", bd=3, relief="ridge")
    info_frame.pack(pady=10, fill="x", padx=50)

    tk.Label(info_frame, text="Datos del Usuario", bg="#F2F2F2",
             font=("Helvetica", 14, "bold"), fg="#0033A0").pack(pady=5)
    tk.Label(info_frame, text=f"Usuario: {usuario}", bg="#F2F2F2",
             font=("Arial", 12)).pack()
    tk.Label(info_frame, text="Categoría: Socio activo", bg="#F2F2F2",
             font=("Arial", 12)).pack()
    tk.Label(info_frame, text="Antigüedad: 1 año", bg="#F2F2F2",
             font=("Arial", 12)).pack()

    cuota_frame = tk.Frame(frame, bg="#E8F5E9", bd=3, relief="ridge")
    cuota_frame.pack(pady=10, fill="x", padx=50)

    estado_cuota = usuarios[usuario]["cuota"]
    color_estado = "#00A859" if estado_cuota == "Al día" else "#FF0000"

    tk.Label(cuota_frame, text="Estado de Cuota", bg="#E8F5E9",
             font=("Helvetica", 14, "bold"), fg="#0033A0").pack(pady=5)
    tk.Label(cuota_frame, text=f"Estado actual: {estado_cuota}",
             bg="#E8F5E9", fg=color_estado, font=("Arial", 12, "bold")).pack(pady=5)

    # Botón para simular pago
    def pagar_cuota():
        usuarios[usuario]["cuota"] = "Al día"
        messagebox.showinfo("Pago exitoso", "Tu cuota fue actualizada a 'Al día'.")
        mostrar_home(usuario)

    tk.Button(frame, text="Pagar Cuota", bg="#00A859", fg="white",
              width=20, command=pagar_cuota).pack(pady=10)


# --- INICIO ---
root.mainloop()