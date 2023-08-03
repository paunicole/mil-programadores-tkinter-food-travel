class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_login(self):
        self.app.cambiar_frame(self.app.vista_login)

    def mostrar_explorar(self):
        self.app.cambiar_frame(self.app.vista_explorar)

    def mostrar_busqueda(self):
        self.app.cambiar_frame(self.app.vista_busqueda)
    
    def mostrar_planificar(self):
        self.app.cambiar_frame(self.app.vista_planificar)
    
    def mostrar_review(self):
        self.app.cambiar_frame(self.app.vista_review)

    def mandar_usuario(self, usuario):
        self.app.vista_planificar.agregar_elementos(usuario)
        self.app.vista_review.recibir_usuario(usuario)