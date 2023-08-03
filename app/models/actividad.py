import json

class Actividad:
    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_actividades(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Actividad.de_json(json.dumps(dato)) for dato in datos]

    def __str__(self):
        return f"Actividad {self.id}: {self.nombre}" \
                f"\nDestino ID: {self.destino_id}" \
                f"\nHora de inicio: {self.hora_inicio}"