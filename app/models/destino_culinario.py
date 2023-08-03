import json
class DestinoCulinario:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo,
                 precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    def __str__(self):
        return f"Destino Culinario {self.id}: {self.nombre}" \
                f"\nTipo de Cocina: {self.tipo_cocina}" \
                f"\nIngredientes: {self.ingredientes}" \
                f"\nPrecio Mínimo: {self.precio_minimo}" \
                f"\nPrecio Máximo: {self.precio_maximo}" \
                f"\nPopularidad: {self.popularidad}" \
                f"\nDisponibilidad: {self.disponibilidad}" \
                f"\nID Ubicación: {self.id_ubicacion}, " \
                f"\nImagen: {self.imagen}"
    
    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_locales(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [DestinoCulinario.de_json(json.dumps(dato)) for dato in datos]

