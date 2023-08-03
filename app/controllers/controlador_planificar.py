from models.destino_culinario import DestinoCulinario
from models.ubicacion import Ubicacion
from models.ruta_visita import RutaVisita
from models.ubicacion import Ubicacion
from models.usuario import Usuario

class ControladorPlanificar:
    def __init__(self, app):
        self.usuarios = Usuario.cargar_usuarios("app/data/usuarios.json")
        self.rutas_visitas = RutaVisita.cargar_visitas("app/data/rutas_visitas.json")
        self.destinos = DestinoCulinario.cargar_locales("app/data/destinos_culinarios.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("app/data/ubicaciones.json")
        self.app = app

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def obtener_destinos(self):
        return self.destinos

    def retornar_usuario(self, usuario):
        return usuario

    def obtener_historial_rutas(self, usuario):
        return usuario.historial_rutas

    def obtener_nombre_rutas(self, id_ruta):
        for ruta in self.rutas_visitas:
            if ruta.id == id_ruta:
                return ruta.nombre
    
    def obtener_ubicaciones_de_una_ruta(self, id_ruta):
        lista_nombres = list()
        # Buscamos los destinos de la ruta id_ruta
        destinos = None
        for ruta in self.rutas_visitas:
            if ruta.id == id_ruta:
                destinos = ruta.destinos

        lista_id_ubicaciones = list()
        for id_destino in destinos:
            for destino in self.destinos:
                if destino.id == id_destino:
                    lista_id_ubicaciones.append(destino.id_ubicacion)
                    lista_nombres.append(destino.nombre)

        lista_ubicaciones = list()
        latitudes = list()
        for id_ubicacion in lista_id_ubicaciones:
            for ubicacion in self.ubicaciones:
                if ubicacion.id == id_ubicacion:
                    lista_ubicaciones.append((ubicacion.latitud, ubicacion.longitud))
                    latitudes.append(ubicacion.latitud)

        return lista_ubicaciones, lista_nombres
    
    def obtener_marcadores(self, ubicaciones, destinos):
        for ubicacion, destino in zip(self.ubicaciones, self.destinos):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = {"latitud":ubicacion.latitud, "longitud":ubicacion.longitud, "texto":destino.nombre, "imagen":imagen}
            self.marcadores.append(marcador)
        return self.marcadores
    
    def obtener_ubicacion(self, id_destino):
        
        for destino in self.destinos:
            if destino.id == id_destino:
                id_ubicacion = destino.id_ubicacion
        
        for ubicacion in self.ubicaciones:
            if ubicacion.id == id_ubicacion:
                return ubicacion.latitud, ubicacion.longitud
