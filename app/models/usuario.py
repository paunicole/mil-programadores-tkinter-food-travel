import json

class Usuario:
    def __init__(self, id, nombre, apellido, historial_rutas, user, password):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
        self.user = user
        self.password = password

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_usuarios(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Usuario.de_json(json.dumps(dato)) for dato in datos]

    def __str__(self):
        return f"Usuario {self.id}: {self.nombre} {self.apellido}" \
                f"\nHistorial de rutas: {self.historial_rutas}" \
                f"\nUsuario: {self.user}" \
                f"\nPassword: {self.password}"