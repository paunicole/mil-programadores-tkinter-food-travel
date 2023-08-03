import tkinter as tk
from tkintermapview import TkinterMapView
from tkinter.font import Font
import customtkinter
from views.vista_historial import VistaHistorial
from views.vista_detalles import VistaDetalles

class VistaPlanificar(customtkinter.CTkFrame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de planificar visitas.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        """WIDGETS"""

        # Crea encabezado
        self.label_titulo = customtkinter.CTkLabel(self)
        self.label_titulo.configure(text="Planificar Visitas", font=customtkinter.CTkFont(family="Roboto Condensed", size=20, weight="bold"))
        self.label_titulo.grid(row=0, column=0, padx=30, pady=(30, 15), sticky="w")

        # Crea descripcion
        self.label_descripcion = customtkinter.CTkLabel(self)
        self.label_descripcion.configure(text="Seleccione al menos dos locales para trazar una ruta.", font=customtkinter.CTkFont(family="Open Sans", size=15))
        self.label_descripcion.grid(row=1, column=0, padx=30, pady=(0, 0), columnspan=2, sticky="w")


        """FRAMES"""

        # Crea Frame para los destinos
        self.frame_destinos = customtkinter.CTkFrame(self, width=200, height=600)
        self.frame_destinos.grid_columnconfigure(0, weight=1)
        self.frame_destinos.grid(row=2, column=0, padx=(30, 15), pady=(15, 15))

        # Crea Frame para Mapa
        self.frame_mapa = customtkinter.CTkFrame(self, width=550,height=400)
        self.frame_mapa.grid(row=2, column=1, padx=(15, 30), pady=(15, 15))


        """WIDGETS DE LOS FRAMES"""
        
        # Crea Listbox para listar los destinos
        self.lista_destinos = tk.Listbox(self.frame_destinos, selectmode="multiple", width=40, height=25)
        self.lista_destinos.bind('<<ListboxSelect>>', self.trazar_rutas)
        self.lista_destinos.bind("<Double-Button-1>", self.mostrar_detalles)
        self.lista_destinos.grid()


        # Crea Mapa para ubicar los destinos
        self.mapa = TkinterMapView(self.frame_mapa, width=550, height=400, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.grid()

        
        """BOTONES"""

        # Boton para volver al inicio
        self.boton_inicio = customtkinter.CTkButton(self, command=self.controlador.regresar_inicio)
        self.boton_inicio.configure(text="Ir a Inicio", width=200)
        self.boton_inicio.grid(row=10, column=0, padx=30, pady=(15, 15))

        # Boton para ver historial de visitas
        self.boton_historial = customtkinter.CTkButton(self, command=self.mostrar_historial)
        self.boton_historial.configure(text="Ver historial", width=200)
        self.boton_historial.grid(row=10, column=1, padx=30, pady=(15, 15), sticky="e")


    def agregar_elementos(self, usuario):
        #Agregamos los elementos al listbox
        usuario = self.controlador.retornar_usuario(usuario)

        #Agregamos los elementos a la listbox
        destinos = self.controlador.obtener_destinos()
        for destino in destinos:
            self.lista_destinos.insert(tk.END, destino.nombre)
        
        self.historial_rutas = self.controlador.obtener_historial_rutas(usuario)
    

    def trazar_rutas(self, event):
        """
        Traza las rutas en el mapa según los destinos seleccionados por el usuario en el Listbox.
        """

        # Elimina todos los marcadores previamente trazadas en el mapa.
        self.mapa.delete_all_marker()
        
        # Elimina todas las rutas previamente trazadas en el mapa.
        self.mapa.delete_all_path()

        # Obtener los índices de los elementos seleccionados en el Listbox
        selected_indices = self.lista_destinos.curselection()

        # Obteniene los nombres y ubicaciones de los destinos seleccionados.
        lista_nombres = list()
        lista_ubicaciones = list()
        if selected_indices:
            for index in selected_indices:
                lista_nombres.append(self.lista_destinos.get(index))
                print("Elemento seleccionado:", self.lista_destinos.get(index))
                ubicacion = self.controlador.obtener_ubicacion(index + 1)
                lista_ubicaciones.append(ubicacion)
            print("---")

        # Si hay más de un destino seleccionado, traza una ruta conectando los destinos en el orden seleccionado.
        if len(selected_indices) != 1:
            path_1 = self.mapa.set_path(lista_ubicaciones)
        else:
            # Si hay exactamente un destino seleccionado, simplemente posiciona el mapa en esa ubicación.
            self.mapa.set_position(lista_ubicaciones[0][0], lista_ubicaciones[0][1])

        # Agregar un marcador en el mapa en la ubicación especificada por la latitud y longitud, y se muestra el nombre asociado al marcador mediante la etiqueta text=marcador[1].
        marcadores = zip(lista_ubicaciones, lista_nombres)
        for marcador in marcadores:
            self.mapa.set_marker(marcador[0][0], marcador[0][1], text=marcador[1])
        

    def mostrar_historial(self):
        """
        Abre una ventana secundaria para mostrar el historial de rutas del usuario.
        """
        toplevel = customtkinter.CTkToplevel(self.master)
        self.ventana_secundaria = VistaHistorial(self.historial_rutas, toplevel, self.controlador)
        self.ventana_secundaria.grid()


    def mostrar_detalles(self, event):
        """
        Muestra los detalles del destino seleccionado por el usuario.
        """

        # Obtiene el índice del destino seleccionado.
        indice = self.lista_destinos.curselection()[0]

        # Busca el destino correspondiente al índice seleccionado.
        destinos = self.controlador.destinos
        for destino in destinos:
            if destino.id == (indice + 1):
                break
        
        # Crea una ventana secundaria para mostrar los detalles del destino seleccionado.
        toplevel = customtkinter.CTkToplevel(self.master)
        VistaDetalles(destino, toplevel).grid()
