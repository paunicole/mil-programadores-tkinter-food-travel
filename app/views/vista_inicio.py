import customtkinter
from PIL import Image

class VistaInicio(customtkinter.CTkFrame):
    width = 900
    height = 600

    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador


        """WIDGETS"""

        # Carga y crea la imagen de fondo.
        self.bg_image = customtkinter.CTkImage(
            Image.open("app/assets/bg_gradient.jpg"),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)


        """FRAMES"""

        # Crea Frame de inicio
        self.frame_inicio = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_inicio.grid_columnconfigure(0, weight=1)
        self.frame_inicio.grid(row=0, column=0, sticky="nsew", padx=100, columns=3, columnspan=1)

        # Crea Frame para el encabezado
        self.frame_usuario = customtkinter.CTkFrame(self.frame_inicio, corner_radius=0)
        self.frame_usuario.grid_columnconfigure(0, weight=1)
        self.frame_usuario.grid(row=0, column=0, sticky="nsew", columnspan=3) 


        """WIDGETS DEL FRAME ENCABEZADO"""

        # Crea label para mostrar el nombre del usuario que inició sesión.
        self.label_usuario = customtkinter.CTkLabel(self.frame_usuario)
        self.label_usuario.configure(font=customtkinter.CTkFont(size=10, weight="bold"))
        self.label_usuario.grid(row=0, column=0, padx=30, pady=(15, 15), sticky="w")

        # Crea boton para cerrar sesión.
        self.boton_cerrar = customtkinter.CTkButton(self.frame_usuario, command=self.controlador.mostrar_login)
        self.boton_cerrar.configure(text="Cerrar Sesión", width=50)
        self.boton_cerrar.grid(row=0, column=1, padx=(0, 30), pady=(15, 15), sticky="w")


        """WIDGETS DEL FRAME INICIO"""

        # Crea Titulo
        self.label_titulo = customtkinter.CTkLabel(self.frame_inicio)
        self.label_titulo.configure(text="FOOD TRAVEL", font=customtkinter.CTkFont(family="Roboto Condensed", size=20, weight="bold"))
        self.label_titulo.grid(row=1, column=0, padx=30, pady=(30, 15))

        # Crea Boton para navegar a la vista Explorar.
        self.boton1 = customtkinter.CTkButton(self.frame_inicio, command=self.controlador.mostrar_explorar)
        self.boton1.configure(text="Explorar Destinos Culinarios", width=200)
        self.boton1.grid(row=2, column=0, padx=30, pady=(15, 15))

        # Crea Boton para navegar a la vista Búsqueda.
        self.boton2 = customtkinter.CTkButton(self.frame_inicio, command=self.controlador.mostrar_busqueda)
        self.boton2.configure(text="Búsqueda y Filtro", width=200)
        self.boton2.grid(row=3, column=0, padx=30, pady=(15, 15))

        # Crea Boton para navegar a la vista Planificar.
        self.boton3 = customtkinter.CTkButton(self.frame_inicio)
        self.boton3.configure(text="Planificar Visitas", command=self.controlador.mostrar_planificar, width=200)
        self.boton3.grid(row=4, column=0, padx=30, pady=(15, 15))

        # Crea Boton para navegar a la vista Reviews.
        self.boton4 = customtkinter.CTkButton(self.frame_inicio, command=self.controlador.mostrar_review)
        self.boton4.configure(text="Reviews y Calificaciones", width=200)
        self.boton4.grid(row=5, column=0, padx=30, pady=(15, 15))
    
        

    def mostrar_usuario_encabezado(self, usuario):
        """
        Actualiza el contenido de la etiqueta con el nombre del usuario que ha iniciado sesión en la aplicación.
        """
        self.label_usuario.configure(text=usuario.nombre)

        # A traves del controlador de inicio mandamos el usuario a las vistas de Planificar y Reviews porque necesito el id de usuario para ver mi historial de visitas y para escribir una review.
        self.controlador.mandar_usuario(usuario)