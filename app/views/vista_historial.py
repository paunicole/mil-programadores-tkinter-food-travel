import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

class VistaHistorial(customtkinter.CTkFrame):
    def __init__(self, historial_rutas, master=None, controlador=None):
        """
        Crea la vista de la información de un destino.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.historial_rutas = historial_rutas

        self.master.title("Detalles")
        self.master.resizable(False, False)
        self.master.grab_set()


        """WIDGETS"""

        # Crea encabezado
        self.main_label = customtkinter.CTkLabel(
            self,
            text="Mi Historial de Visitas",
            font=customtkinter.CTkFont(family="Roboto Condensed", size=20, weight="bold"),
        )
        self.main_label.grid(row=1, column=0, padx=30, pady=(30, 15), sticky="w")


        """FRAMES"""
        
        # Crea Frame para el historial de visitas
        self.frame_historial = customtkinter.CTkFrame(self, width=200, height=600)
        self.frame_historial.grid_columnconfigure(0, weight=1)
        self.frame_historial.grid(row=2, column=0, padx=(30, 15), pady=(30, 15))

        # Crea Frame para Mapa
        self.frame_mapa = customtkinter.CTkFrame(self, width=550,height=400)
        self.frame_mapa.grid(row=2, column=1, padx=(15, 30), pady=(30, 15))


        """WIDGETS DE LOS FRAMES"""

        # Crea Listbox para listar las visitas
        self.lista_rutas = tk.Listbox(self.frame_historial, width=40, height=25)
        self.lista_rutas.bind('<<ListboxSelect>>', self.trazar_ruta)
        self.lista_rutas.grid()

        # Crea Mapa para ubicar las visitas
        self.mapa = TkinterMapView(self.frame_mapa, width=550, height=400, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.grid()
 

        self.agregar_elementos()
    

    def agregar_elementos(self):
        """
        Agrega los elementos al listbox de la vista de historial.
        """
        for id_ruta in self.historial_rutas:
            ruta_nombre = self.controlador.obtener_nombre_rutas(id_ruta)
            self.lista_rutas.insert(tk.END, ruta_nombre)
    

    def trazar_ruta(self, event):
        """
        Trazar una ruta en el mapa seleccionada en el Listbox.
        """

        # Elimina todos los marcadores del mapa.
        self.mapa.delete_all_marker()

        # Elimina todas las rutas previas del mapa.
        self.mapa.delete_all_path()

        # Obtiene el índice de la ruta seleccionada en el Listbox.
        selected_index = self.lista_rutas.curselection()
        index = int(selected_index[0] + 1)

        # Obtiene la lista de ubicaciones y nombres asociados a la ruta seleccionada.
        lista_ubicaciones, nombres = self.controlador.obtener_ubicaciones_de_una_ruta(index)

        # Traza la ruta en el mapa utilizando las ubicaciones obtenidas.
        path_1 = self.mapa.set_path(lista_ubicaciones)

        # Establece la posición del mapa en la primera ubicación de la ruta.
        self.mapa.set_position(lista_ubicaciones[0][0], lista_ubicaciones[0][1])

        # Agrega marcadores en el mapa con los nombres de los lugares asociados a cada ubicación de la ruta.
        marcadores = zip(lista_ubicaciones, nombres)
        for marcador in marcadores:
            self.mapa.set_marker(marcador[0][0], marcador[0][1], text=marcador[1])


    def obtener_ubicacion_de_una_ruta(self, id_ruta):
        """
        Obtiene la lista de ubicaciones asociadas a una ruta específica.
        """
        lista_ubicaciones = self.controlador.obtener_ubicaciones_de_una_ruta(id_ruta)
        return lista_ubicaciones