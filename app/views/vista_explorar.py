import tkinter as tk
from tkintermapview import TkinterMapView
import customtkinter
from views.vista_detalles import VistaDetalles

class VistaExplorar(customtkinter.CTkFrame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de explorar destinos culinarios.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Crea titulo de la vista
        self.titulo = customtkinter.CTkLabel(
            self,
            text="Explorar Destinos Culinarios",
            font=customtkinter.CTkFont(family="Roboto Condensed", size=20, weight="bold"),
        )

        self.titulo.grid(row=0, column=0, padx=30, pady=(30, 15))

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = customtkinter.CTkButton(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio, width=200
        )
        
        self.boton_inicio.grid(row=2, column=0, padx=30, pady=(15, 15))

        #Mapa
        self.frame_mapa = customtkinter.CTkFrame(self, width=550,height=400)
        self.frame_mapa.grid(row=1,column=1)

        self.mapa = TkinterMapView(self.frame_mapa, width=550, height=400, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.grid()

        #Frame para la lista de destinos
        self.frame_destinos = customtkinter.CTkFrame(self, width=200, height=600)
        self.frame_destinos.grid_columnconfigure(0, weight=1)
        self.frame_destinos.grid(row=1, column=0)

        #Listbox de los destinos
        self.lista_destinos = tk.Listbox(self.frame_destinos, width=40, height=25)
        self.lista_destinos.bind('<<ListboxSelect>>', self.seleccionar_destino)
        self.lista_destinos.grid()

        # Asocia el evento de doble clic a la función seleccionar_juego
        self.lista_destinos.bind("<Double-Button-1>", self.mostrar_detalles)

        #Agregamos los elementos a la listbox
        destinos = self.controlador.obtener_destinos()
        for destino in destinos:
            self.lista_destinos.insert(tk.END, destino.nombre)
        
        #Agregamos los marcadores al mapa
        marcadores = self.controlador.obtener_marcadores()
        for marcador in marcadores:
            self.mapa.set_marker(marcador['latitud'], marcador['longitud'], text=marcador['texto'], image=marcador['imagen']).hide_image(True)
    
    def seleccionar_destino(self, event):
        selection = self.lista_destinos.curselection()
        ubi = self.controlador.seleccionar_local(event, selection)
        self.mapa.set_position(ubi.latitud, ubi.longitud)
    

    def mostrar_detalles(self, event):
        indice = self.lista_destinos.curselection()[0]
        
        destinos = self.controlador.destinos
        for destino in destinos:
            if destino.id == (indice + 1):
                break
        
        toplevel = customtkinter.CTkToplevel(self.master)
        VistaDetalles(destino, toplevel).grid()