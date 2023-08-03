import json
from models.destino_culinario import DestinoCulinario
from models.review import Review
from models.usuario import Usuario

class ControladorReview:
    def __init__(self, app):
        self.app = app
        self.destinos = DestinoCulinario.cargar_locales("app/data/destinos_culinarios.json")
        self.reviews = Review.cargar_review("app/data/reviews.json")
        self.usuarios = Usuario.cargar_usuarios("app/data/usuarios.json")
        self.reviews_seleccionadas = []
        self.user = None

    def obtener_destinos(self):
        return self.destinos
    
    def obtener_reviews(self):
        for review in self.reviews:
            for destino in self.destinos:
                if(destino.id == review.id_destino):
                    review.id_destino = destino.nombre
                    break
            for usuario in self.usuarios:
                if(usuario.id == review.id_usuario):
                    review.id_usuario = usuario.nombre
        return self.reviews

    def seleccionar_local(self, event, select):
        destino = self.destinos[select[0]]  
        return destino.id

    def obtener_nombre_destino(self,id):
        for destino in self.destinos:
            if(destino.id == id):
                return destino.nombre

    def obtener_reviews_seleccionada(self, id):
        self.reviews_seleccionadas=[]
        nombre_destino = self.obtener_nombre_destino(id)
        for review in self.reviews:
            if review.id_destino == nombre_destino:
                self.reviews_seleccionadas.append(review)
        return self.reviews_seleccionadas

    def obtener_nombres_destinos(self):
        lista = []
        for destino in self.destinos:
            lista.append(destino.nombre)
        return lista
    
    def preparar_review(self, review_formulario):
        id_review = len(self.reviews) + 1
        for destino in self.destinos:
            if(review_formulario[0] == destino.nombre):
                id_destino = destino.id
                break
        
        review = {"id":id_review, "id_destino":id_destino, "id_usuario":review_formulario[1], "calificacion": review_formulario[2], "comentario": review_formulario[3], "animo":review_formulario[4]}
        self.cargar_review(review)

    def cargar_review(self, review):
        with open('app/data/reviews.json', 'r+') as f:
            data = json.load(f)
            data.append(review)
            f.seek(0)
            json.dump(data, f, indent=4)


    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)