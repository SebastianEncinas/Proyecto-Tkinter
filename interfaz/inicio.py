import tkinter as tk
from PIL import Image, ImageTk




def home_mi_club():
    home = tk.Tk()
    home.title("Mi Club (Home)")
    home.geometry("600x800")
    home.configure(bg="navy")
    # imagen_pil = Image.open("/Img/Clash.jpg")
    # imagen_tk = ImageTk.PhotoImage(imagen_pil)


    home.grid_columnconfigure(0, weight=1)
    home.grid_columnconfigure(1, weight=1)
    home.grid_rowconfigure(0, weight=1)
    home.grid_rowconfigure(1, weight=1)
    home.grid_rowconfigure(2, weight=1)



    # etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
    # etiqueta_imagen.pack()

    coleccion_button = tk.Button(home, width=22, height=8, text="Colección", bd=15, bg="snow", font=("Arial", 18))
    coleccion_button.grid(row=0, column=0, padx=20, pady=40)

    tienda_button = tk.Button(home, width=22, height=8, text="Tienda", bd=15, bg="snow",  font=("Arial", 18))
    tienda_button.grid(row=0, column=1, padx=20, pady=40)

    historial_button = tk.Button(home, width=22, height=8, text="Historial", bd=15, bg="snow", font=("Arial", 18))
    historial_button.grid(row=1, column=0, padx=20, pady=40)

    arenas_button = tk.Button(home, width=22, height=8, text="Arenas", bd=15, bg="snow",  font=("Arial", 18))
    arenas_button.grid(row=1, column=1, padx=20, pady=40)


    home.mainloop()


def verificar_credenciales():
    usuario = usuario_entry.get()
    contraseña = contraseña_entry.get()

    usuario_correcto = "S"
    contraseña_correcta = "23"

    if usuario==usuario_correcto and contraseña == contraseña_correcta:
        ventana.destroy()
        home_mi_club()
    else:
        resultado_label.config(text="Usuario o Contraseña Incorrecta", fg="Red")

ventana = tk.Tk()
ventana.title("Mi Club (Login)")
ventana.geometry("500x700")

seccion1 = tk.Frame(ventana, bg="navy", bd=15, relief="groove")
seccion1.pack(pady=70)

etiqueta_label = tk.Label(seccion1, text="BIENVENIDO AL CLUB VELEZ SARFIELD",background="navy", font=("Arial",15), fg="white")
etiqueta_label.pack(padx=20)

usuario_label = tk.Label(seccion1, text="Usuario",font=("Arial",10), bg="navy", fg="white")
usuario_label.pack()

usuario_entry = tk.Entry(seccion1)
usuario_entry.pack()

contraseña_label = tk.Label(seccion1, text="Contraseña",font=("Arial",10),  bg="navy", fg="white")
contraseña_label.pack()

contraseña_entry = tk.Entry(seccion1, show="")
contraseña_entry.pack()

login_button = tk.Button(seccion1, text="Iniciar Sesion", bd=5, bg="navy", fg="white" ,command=verificar_credenciales)
login_button.pack(pady=20)

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
