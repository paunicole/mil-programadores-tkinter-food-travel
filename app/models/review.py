import json
class Review:
    def __init__(self, id, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def __str__(self):
        return f"Review {self.id}" \
                f"\nDestino: {self.id_destino}" \
                f"\nUsuario: {self.id_usuario}" \
                f"\nCalificación: {self.calificacion}" \
                f"\nComentario: {self.comentario}" \
                f"\nÁnimo: {self.animo}"
    
    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_review(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Review.de_json(json.dumps(dato)) for dato in datos]