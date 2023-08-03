import customtkinter

from views.vista_login import VistaLogin
from views.vista_inicio import VistaInicio
from views.vista_explorar import VistaExplorar
from views.vista_busqueda import VistaBusqueda
from views.vista_planificar import VistaPlanificar
from views.vista_review import VistaReview

from controllers.controlador_login import ControladorLogin
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_explorar import ControladorExplorar
from controllers.controlador_busqueda import ControladorBusqueda
from controllers.controlador_planificar import ControladorPlanificar
from controllers.controlador_review import ControladorReview

customtkinter.set_appearance_mode("dark")

class Aplicacion(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Food Travel")
        self.geometry("900x600")
        self.resizable(False, False)

        # Inicializa la aplicación
        self.inicializar()

        # Muestra la pantalla de inicio de sesión al abrir la aplicación.
        self.cambiar_frame(self.vista_login)


    def inicializar(self):
        """
        Inicializa la aplicación creando los controladores y las vistas correspondientes.
        """
        controlador_login = ControladorLogin(self)
        controlador_inicio = ControladorInicio(self)
        controlador_explorar = ControladorExplorar(self)
        controlador_busqueda = ControladorBusqueda(self)
        controlador_planificar = ControladorPlanificar(self)
        controlador_review = ControladorReview(self)

        self.vista_login = VistaLogin(self, controlador_login)
        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_explorar = VistaExplorar(self, controlador_explorar)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)
        self.vista_planificar = VistaPlanificar(self, controlador_planificar)
        self.vista_review = VistaReview(self, controlador_review)

        self.ajustar_frame(self.vista_login)
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_explorar)
        self.ajustar_frame(self.vista_busqueda)
        self.ajustar_frame(self.vista_planificar)
        self.ajustar_frame(self.vista_review)


    def ajustar_frame(self, frame):
        """
        Ajusta el tamaño y la posición del frame dentro de la ventana principal.
        """
        frame.grid(row=0, column=0, sticky="nsew")


    def cambiar_frame(self, frame_destino):
        """
        Cambia el frame actualmente mostrado por el frame de destino.
        """
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()