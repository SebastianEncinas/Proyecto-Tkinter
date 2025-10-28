from PIL import Image, ImageTk
import tkinter as tk 
def home_mi_club():
    home = tk.Tk()
    home.title("Mi Club (Home)")
    home.geometry("600x800")

    
    coleccion_button = tk.Button(home,width=15, height=3, text="Colección", bd=5, bg="violet", fg="white")
    coleccion_button.grid(row=1, column=0, padx=40, pady=20)

    tienda_button = tk.Button(home,width=15, height=3, text="Tienda", bd=5, bg="violet", fg="white")
    tienda_button.grid(row=1, column=1, padx=40, pady=20)

    historial_button = tk.Button(home  ,width=15, height=3, text="Historial", bd=5, bg="violet", fg="white")
    historial_button.grid(row=2, column=0, padx=40, pady=20)

    arenas_button = tk.Button(home, width=15, height=3, text="Arenas", bd=5, bg="violet", fg="white")
    arenas_button.grid(row=2, column=1, padx=40, pady=20)

    imagen = Image.open("Users\Administrator\Desktop\Tkinter-Encinas\imagenes\coleccion-maestrias.png")
    imagen_Tk = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(home, image=imagen_Tk)
    label_imagen.pack()
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
ventana.geometry("300x500")

seccion1 = tk.Frame(ventana, bg="violet", bd=15, relief="groove")
seccion1.pack(pady=70)

etiqueta_label = tk.Label(seccion1, text="BIENVENIDO A CLUB CLASH ROYALE",background="violet", font=("Arial",15), fg="white")
etiqueta_label.pack()

usuario_label = tk.Label(seccion1, text="Usuario",font=("Arial",10), bg="violet", fg="white")
usuario_label.pack()

usuario_entry = tk.Entry(seccion1)
usuario_entry.pack()

contraseña_label = tk.Label(seccion1, text="Contraseña",font=("Arial",10),  bg="violet", fg="white")
contraseña_label.pack()

contraseña_entry = tk.Entry(seccion1, show="")
contraseña_entry.pack()

login_button = tk.Button(seccion1, text="Iniciar Sesion", bd=5, bg="violet", fg="white", command=verificar_credenciales)
login_button.pack(pady=20)

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()