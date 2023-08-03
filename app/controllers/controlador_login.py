from models.usuario import Usuario

class ControladorLogin:
    """
    Controlador para la vista de inicio de sesión.
    """

    def __init__(self, app):
        self.app = app
        self.usuarios = Usuario.cargar_usuarios("app/data/usuarios.json")

    def mostrar_inicio(self):
        """
        Cambia la vista actual a la vista de inicio.
        """
        self.app.cambiar_frame(self.app.vista_inicio)

    def validar(self, user, password):
        """
        Valida las credenciales de inicio de sesión ingresadas por el usuario.
        """   
        es_valido = False
        for usuario in self.usuarios:
            if user == usuario.user and password == usuario.password:
                self.app.vista_inicio.mostrar_usuario_encabezado(usuario)
                self.app.cambiar_frame(self.app.vista_inicio)
                es_valido = True
                break
        return es_valido