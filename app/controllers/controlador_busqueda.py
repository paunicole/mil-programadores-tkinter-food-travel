from models.destino_culinario import DestinoCulinario

class ControladorBusqueda:
    def __init__(self, app):
        self.destinos = DestinoCulinario.cargar_locales("app/data/destinos_culinarios.json")
        self.app = app

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)