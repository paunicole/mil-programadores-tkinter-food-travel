import json

class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_visitas(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [RutaVisita.de_json(json.dumps(dato)) for dato in datos]

    def __str__(self):
        return f"Ruta de Visita {self.id}: {self.nombre}" \
                f"\nDestinos: {self.destinos}"