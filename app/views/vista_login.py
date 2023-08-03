import tkinter as tk
from tkinter.font import Font
import customtkinter
from PIL import Image

class VistaLogin(customtkinter.CTkFrame):
    width = 900
    height = 600

    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio de sesión.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador


        """IMAGEN DE FONDO"""

        # Cargar y crea la imagen de fondo
        self.bg_image = customtkinter.CTkImage(
            Image.open("app/assets/bg_gradient.jpg"),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)


        """FRAMES"""
        self.frame_login = customtkinter.CTkFrame(self)
        

        """WIDGETS"""
        self.label_titulo = customtkinter.CTkLabel(self.frame_login)
        self.entry_usuario = customtkinter.CTkEntry(self.frame_login)
        self.entry_contrasena = customtkinter.CTkEntry(self.frame_login)
        self.label_mensaje = customtkinter.CTkLabel(self.frame_login)


        """BOTON"""
        self.boton_entrar = customtkinter.CTkButton(self.frame_login, command=self.evento_login)
        

        self.frames_configure()
        self.frames_grid()

        self.widgets_configure()
        self.widgets_grid()


    def frames_configure(self):
        """
        Configura los frames dentro de la vista de login.
        """
        self.frame_login.configure(corner_radius=10)


    def frames_grid(self):
        """
        Ubica los frames dentro de la vista de login en la grilla de la interfaz gráfica.
        """
        self.frame_login.grid(row=0, column=0, sticky="ns")


    def widgets_configure(self):
        """
        Configura los widgets de la vista de login con los textos y atributos deseados.
        """
        self.label_titulo.configure(text="Inicio Sesión", font=customtkinter.CTkFont(family="Roboto Condensed", size=20, weight="bold"))
        self.entry_usuario.configure(width=200, placeholder_text="nombre de usuario")
        self.entry_contrasena.configure(width=200, show="*", placeholder_text="contraseña")
        self.boton_entrar.configure(text="Entrar", width=200)
        self.label_mensaje.configure(text="", font=customtkinter.CTkFont(size=10, weight="bold"))
        

    def widgets_grid(self):
        """
        Ubica los widgets en la cuadrícula (grid) dentro del frame de la vista de login.
        """
        self.label_titulo.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.entry_usuario.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.entry_contrasena.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.boton_entrar.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.label_mensaje.grid(row=4, column=0, padx=30, pady=(150, 15))

    def evento_login(self):
        """
        Realiza la acción de inicio de sesión cuando el usuario presiona el botón de login.
        """

        # Obtiene el nombre de usuario y la contraseña ingresados por el usuario en los campos de entrada.
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contrasena.get()

        # Muestro los datos por la consola
        print(
            "Presionó Login - nombre de usuario:", usuario,
            "contraseña:", contraseña,
        )

        # verifica si los campos de entrada de usuario y contraseña no están vacíos.
        if len(usuario) > 0 and len(contraseña) > 0:
            # Intenta validar las credenciales utilizando el método "validar" del controlador.
            validar = self.controlador.validar(usuario, contraseña)

            # Si las credenciales son válidas, se limpian los campos de entrada y se redirige al usuario a la vista de inicio.
            if validar:
                # Limpia los campos de entrada.
                self.entry_usuario.delete(0, tk.END)
                self.entry_contrasena.delete(0, tk.END)

                self.entry_usuario.configure(placeholder_text="nombre de usuario")
                self.entry_contrasena.configure(placeholder_text="contraseña")

                # Redirige al usuario a la vista de inicio.
                self.controlador.mostrar_inicio()
            else:
                # Si las credenciales no son válidas, se muestra un mensaje de error en la etiqueta.
                self.label_mensaje.configure(text="Usuario o contraseña incorrectos")
        else:
            # Si algún campo de entrada está vacío, se muestra un mensaje de error solicitando completar todos los campos.
            self.label_mensaje.configure(text="Rellene todos los campos")