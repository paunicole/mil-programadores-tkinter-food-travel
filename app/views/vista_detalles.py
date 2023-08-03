import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from models.ubicacion import Ubicacion
from models.actividad import Actividad
from datetime import datetime

class VistaDetalles(customtkinter.CTkFrame):
    def __init__(self, destino, master=None, controlador=None):
        """
        Crea la vista de la información de un destino.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        self.master.title("Detalles")
        self.master.resizable(False, False)
        self.master.grab_set()

        self.ubicaciones = Ubicacion.cargar_ubicaciones("app/data/ubicaciones.json")
        self.actividades = Actividad.cargar_actividades("app/data/actividades.json")

        # Obtiene la ubicación del destino que se desea mostrar.
        for ubicacion in self.ubicaciones:
            if ubicacion.id == destino.id_ubicacion:
                break
        
        # Obtiene un listado de todas las actividades asociadas al destino que se desea mostrar.
        lista_actividades = list()
        for actividad in self.actividades:
            if actividad.destino_id == destino.id:
                lista_actividades.append(actividad)

        # Muestra los detalles del destino y las actividades asociadas en la ventana secundaria.
        self.mostrar_detalles(destino, ubicacion, lista_actividades)

        # Crea un botón "Volver" para cerrar la ventana secundaria.
        boton_cerrar = customtkinter.CTkButton(self, text="Volver", command=lambda: self.master.destroy()) 
        boton_cerrar.configure(width=100)          
        boton_cerrar.grid(row=9, column=1, padx=30, pady=(5, 20), sticky="e")


    def mostrar_detalles(self, destino, ubicacion, actividades):
        
        # Crea etiquetas para mostrar información del destino.
        label_encabezado = customtkinter.CTkLabel(self)
        imagen = ImageTk.PhotoImage(Image.open(f"app/views/images/{destino.imagen}").resize((200, 200)))
        label_imagen = customtkinter.CTkLabel(self, image=imagen)
        label_ubicacion = customtkinter.CTkLabel(self)
        label_tipo = customtkinter.CTkLabel(self)
        label_ingredientes = customtkinter.CTkLabel(self)
        label_precio = customtkinter.CTkLabel(self)
        label_popularidad = customtkinter.CTkLabel(self)
        label_actividades = customtkinter.CTkLabel(self)


        # Configura el texto de las etiquetas.
        label_encabezado.configure(text=destino.nombre)
        label_imagen.configure(text='')
        label_ubicacion.configure(text=f"Dirección: {ubicacion.direccion}")
        label_tipo.configure(text=f"Cocina: {destino.tipo_cocina}")
        ingredientes = ", ".join(destino.ingredientes)
        label_ingredientes.configure(text=f"Ingredientes: {ingredientes}")
        label_precio.configure(text=f"Precio: Desde ${destino.precio_minimo} hasta ${destino.precio_maximo}")
        label_popularidad.configure(text=f"Popularidad: {destino.popularidad}")
        label_actividades.configure(text="Actividades")


        # Configura la fuente de las etiquetas.
        label_encabezado.configure(font=customtkinter.CTkFont(family="Roboto Condensed", size=30, weight="bold"))
        label_ubicacion.configure(font=customtkinter.CTkFont(family="Open Sans", size=15, weight="bold"))
        label_tipo.configure(font=customtkinter.CTkFont(family="Open Sans", size=15, weight="bold"))
        label_ingredientes.configure(font=customtkinter.CTkFont(family="Open Sans", size=15, weight="bold"))
        label_precio.configure(font=customtkinter.CTkFont(family="Open Sans", size=15, weight="bold"))
        label_popularidad.configure(font=customtkinter.CTkFont(family="Open Sans", size=15, weight="bold"))
        label_actividades.configure(font=customtkinter.CTkFont(family="Roboto Condensed", size=20, weight="bold"))


        # Posiciona las etiquetas en la ventana secundaria.
        label_encabezado.grid(row=1, column=0, padx=30, pady=(30, 15), columnspan=2)
        label_imagen.grid(row=2, column=0, padx=30, pady=(30, 5), rowspan=5)
        label_ubicacion.grid(row=2, column=1, padx=(5, 30), pady=(1, 1), sticky="w")        
        label_tipo.grid(row=3, column=1, padx=(5, 30), pady=(1, 1), sticky="w")
        label_ingredientes.grid(row=4, column=1, padx=(5, 30), pady=(1, 1), sticky="w")
        label_precio.grid(row=5, column=1, padx=(5, 30), pady=(1, 1), sticky="w")
        label_popularidad.grid(row=6, column=1, padx=(5, 30), pady=(2, 2), sticky="w")
        label_actividades.grid(row=7, column=0, padx=30, pady=(30, 5), sticky="w")


        # Frame con barra de desplazamiento para las actividades.
        self.frame_actividades = customtkinter.CTkScrollableFrame(self, width=550, height=100)
        self.frame_actividades.grid(row=8, column=0, columnspan=2, padx=30, pady=(10, 10))


        # Si existen actividades: Se recorre la lista de actividades y se muestran los nombres y horarios de cada actividad.
        if actividades:
            i = 0   
            for actividad in actividades:
                
                # Crea labels
                label_evento = customtkinter.CTkLabel(self.frame_actividades)
                label_horario = customtkinter.CTkLabel(self.frame_actividades)
                label_separador = customtkinter.CTkLabel(self.frame_actividades)
                

                # Define Texto de labels
                label_evento.configure(text="Evento: "+actividad.nombre)
                
                fecha_hora_obj = datetime.fromisoformat(actividad.hora_inicio) # Convertir la cadena a objeto datetime
                fecha = fecha_hora_obj.strftime("%d/%m/%Y")                    # Obtener la fecha en formato DD/MM/AAAA
                hora = fecha_hora_obj.strftime("%H:%M")                        # Obtener la hora en formato HH/MM

                label_horario.configure(text=f"Horario: {fecha} {hora} hs.")
                label_separador.configure(text="-----------------------------------------------------------------------------------------")


                # Define fuente del texto de labels
                label_evento.configure(font=customtkinter.CTkFont(family="Open Sans", size=15, weight="bold"))
                label_horario.configure(font=customtkinter.CTkFont(family="Open Sans", size=13))


                # Posiciona labels
                label_evento.grid(row=i, column=0)
                label_horario.grid(row=i+1, column=0)
                label_separador.grid(row=i+2, column=0)

                i += 3 

        else:
            # Si no hay actividades: Se muestra un mensaje indicando que no se registraron actividades.
            label_vacio = customtkinter.CTkLabel(self.frame_actividades)
            label_vacio.configure(text="No se registraron actividades.", font=customtkinter.CTkFont(family="Open Sans", size=15))
            label_vacio.grid(row=0, column=0)