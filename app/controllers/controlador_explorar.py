from models.destino_culinario import DestinoCulinario
from models.ubicacion import Ubicacion
from PIL import Image, ImageTk

class ControladorExplorar:
    def __init__(self, app):
        self.destinos = DestinoCulinario.cargar_locales("app/data/destinos_culinarios.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("app/data/ubicaciones.json")
        self.imagenes = []
        self.marcadores = []
        self.app = app

        self.obtener_imagenes()
        self.obtener_marcadores()

    def obtener_destinos(self):
        return self.destinos

    def obtener_imagenes(self):
        for destino in self.destinos:
            imagen = ImageTk.PhotoImage(Image.open(f"app/views/images/{destino.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def obtener_marcadores(self):
        for ubicacion, destino in zip(self.ubicaciones, self.destinos):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = {"latitud":ubicacion.latitud, "longitud":ubicacion.longitud, "texto":destino.nombre, "imagen":imagen}
            self.marcadores.append(marcador)
        return self.marcadores

    def seleccionar_local(self, event, selection):
        # Obtiene el local seleccionado
        local_seleccionado = self.destinos[selection[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        # Busca la ubicación correspondiente al local seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == local_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        # Centra el mapa en la ubicación seleccionada
        return ubicacion_seleccionada

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
