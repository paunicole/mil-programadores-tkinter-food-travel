import tkinter as tk
from tkinter import ttk
import customtkinter
from views.vista_detalles import VistaDetalles

class VistaBusqueda(customtkinter.CTkFrame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador


        """FRAMES"""
        self.frame_busqueda = customtkinter.CTkFrame(self)
        self.frame_tabla = ttk.Frame(self)


        """WIDGETS"""

        # Crea Titulo
        self.label_titulo = customtkinter.CTkLabel(self)

        # Crea Labels
        self.label_tipo = customtkinter.CTkLabel(self.frame_busqueda)
        self.label_ingrediente = customtkinter.CTkLabel(self.frame_busqueda)
        self.label_precio = customtkinter.CTkLabel(self.frame_busqueda)
        self.label_popularidad = customtkinter.CTkLabel(self.frame_busqueda)
        self.label_popularidad_valor = customtkinter.CTkLabel(self.frame_busqueda)

        # Crea Entrys
        valores_tipo = self.obtener_valores_tipo()
        valores_tipo.insert(0, "Seleccione uno..") # Inserta en la posición 0 de la lista el valor "Seleccione uno.."
        self.entry_tipo = customtkinter.CTkComboBox(self.frame_busqueda, values=valores_tipo)
        self.entry_tipo.set("Seleccione uno..") # Valor seleccionado por defecto

        valores_ingrediente = self.obtener_ingredientes()
        valores_ingrediente.insert(0, "Seleccione uno..") # Inserta en la posición 0 de la lista el valor "Seleccione uno.."
        self.entry_ingrediente = customtkinter.CTkComboBox(self.frame_busqueda, values=valores_ingrediente)
        self.entry_ingrediente.set("Seleccione uno..") # Valor seleccionado por defecto

        self.entry_precio_minimo = customtkinter.CTkEntry(self.frame_busqueda)
        self.entry_precio_maximo = customtkinter.CTkEntry(self.frame_busqueda)

        self.entry_popularidad = customtkinter.CTkSlider(self.frame_busqueda, from_=0, to=5, number_of_steps=5, command=self.evento_valor_popularidad)
        self.entry_popularidad.set(0) # Valor por defecto

        # Crea Botones
        self.boton_buscar = customtkinter.CTkButton(self.frame_busqueda, command=self.filtrar_listado)
        self.boton_limpiar = customtkinter.CTkButton(self.frame_busqueda, command=self.limpiar_filtros)
        self.boton_inicio = customtkinter.CTkButton(self, command=self.controlador.regresar_inicio)

        # Crea Tabla
        columnas = ('nombre', 'tipo_cocina', 'ingredientes', 'precio', 'popularidad')
        
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas)
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5, columnspan=6)
        
        self.configurar_tabla()
        self.agregar_scroll()
        self.cargar_tabla()

        # Evento al hacer doble click sobre un registro de la tabla
        self.tabla.bind("<Double-Button-1>", self.mostrar_detalles)


        self.frames_configure()
        self.frames_grid()
    
        self.widgets_configure()
        self.widgets_grid()


    def frames_configure(self):
        """
        Configura los frames dentro de la vista de búsqueda con los tamaños y estilos deseados.
        """
        self.frame_busqueda.configure(width=550, height=400)
        self.frame_tabla.configure(relief="groove", padding=5)
        self.frame_tabla.columnconfigure(0, weight=1)
        self.frame_tabla.rowconfigure(0, weight=1)

    def frames_grid(self):
        """
        Ubica los frames dentro de la vista de búsqueda en la grilla de la interfaz gráfica.
        """
        self.frame_busqueda.grid(row=1, column=0, padx=30, pady=(10, 10))
        self.frame_tabla.grid(row=1, column=1, columnspan=6, sticky=tk.NSEW)


    def widgets_configure(self):
        """
        Configura los widgets de la vista de búsqueda con los textos y atributos deseados.
        """
        # Titulo
        self.label_titulo.configure(text="Búsqueda y Filtro", font=customtkinter.CTkFont(family="Roboto Condensed", size=20, weight="bold"))

        # Labels
        self.label_tipo.configure(text="Tipo de Cocina:", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.label_ingrediente.configure(text="Ingredientes:", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.label_precio.configure(text="Precio:", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.label_popularidad.configure(text="Popularidad:", font=customtkinter.CTkFont(size=10, weight="bold"))
        self.label_popularidad_valor.configure(text=str(self.entry_popularidad.get()))

        # Entry
        self.entry_tipo.configure(width=100)
        self.entry_precio_minimo.configure(width=200, placeholder_text="Mínimo")
        self.entry_precio_maximo.configure(width=200, placeholder_text="Máximo")
        
        # Botones
        self.boton_buscar.configure(text="Buscar", width=200)
        self.boton_limpiar.configure(text="Limpiar", width=200)
        self.boton_inicio.configure(text="Ir a Inicio", width=200)


    def widgets_grid(self):
        """
        Ubica los widgets en la cuadrícula (grid) dentro del frame de la vista de búsqueda.
        """
        # Titulo
        self.label_titulo.grid(row=0, column=0, padx=30, pady=(30, 15))

        # Labels
        self.label_tipo.grid(row=2, column=0, padx=30, pady=(10, 0), sticky='w')
        self.label_ingrediente.grid(row=4, column=0, padx=30, pady=(10, 0), sticky='w')
        self.label_precio.grid(row=6, column=0, padx=30, pady=(10, 0), sticky='w')
        self.label_popularidad.grid(row=9, column=0, padx=30, pady=(10, 0), sticky='w')
        self.label_popularidad_valor.grid(row=11, column=0, padx=30, pady=5, sticky="ew")

        # Entrys
        self.entry_tipo.grid(row=3, column=0, padx=30, pady=(5, 5), sticky='we')
        self.entry_ingrediente.grid(row=5, column=0, padx=30, pady=(5, 5), sticky='we')
        self.entry_precio_minimo.grid(row=7, column=0, padx=30, pady=(5, 5))
        self.entry_precio_maximo.grid(row=8, column=0, padx=30, pady=(5, 5))
        self.entry_popularidad.grid(row=10, column=0, padx=30, pady=5, sticky="ew")

        # Botones
        self.boton_buscar.grid(row=12, column=0, padx=30, pady=(5, 5))
        self.boton_limpiar.grid(row=13, column=0, padx=30, pady=(5, 15))
        self.boton_inicio.grid(row=10, column=0, padx=30, pady=(5, 5))


    def agregar_scroll(self):
        """
        Agrega barras de desplazamiento al widget Treeview para permitir la navegación vertical y horizontal.
        """
        scrollbar_y = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        scrollbar_x = ttk.Scrollbar(self.frame_tabla, orient=tk.HORIZONTAL, command=self.tabla.xview)

        scrollbar_y.grid(row=0, column=6, sticky=tk.NS)
        scrollbar_x.grid(row=1, column=0, columnspan=6, sticky=tk.EW, padx=5)

        self.tabla.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)


    def configurar_tabla(self):
        """
        Configura la apariencia y formato del widget Treeview.
        """

        self.tabla.configure(show='headings', selectmode="browse")

        # Define y nombra los encabezados
        self.tabla.heading('nombre', text='Nombre')
        self.tabla.heading('tipo_cocina', text='Tipo de Cocina')
        self.tabla.heading('ingredientes', text='Ingredientes')
        self.tabla.heading('precio', text='Precio')
        self.tabla.heading('popularidad', text='Popularidad')

        # Ancho de las columnas
        self.tabla.column('nombre', width=120)
        self.tabla.column('tipo_cocina', width=100)
        self.tabla.column('ingredientes', width=100)
        self.tabla.column('precio', width=100)
        self.tabla.column('popularidad', width=90)


    def obtener_valores_tipo(self):
        """
        Obtiene y devuelve una lista de los diferentes tipos de cocina disponibles en los destinos.
        """
        valores_tipo = list()
        for destino in self.controlador.destinos:
            if destino.tipo_cocina not in valores_tipo:
                valores_tipo.append(destino.tipo_cocina)
        return valores_tipo


    def obtener_ingredientes(self):
        """
        Obtiene y devuelve una lista de los diferentes ingredientes utilizados en los destinos culinarios disponibles.
        """
        lista_ingredientes = list()
        for destino in self.controlador.destinos:
            for ingrediente in destino.ingredientes:
                if ingrediente not in lista_ingredientes:
                    lista_ingredientes.append(ingrediente)
        return lista_ingredientes


    def evento_valor_popularidad(self, value):
        """
        Actualiza la etiqueta de la popularidad al cambiar el valor del slider.
        """
        self.label_popularidad_valor.configure(text=str(self.entry_popularidad.get()))


    def cargar_tabla(self, listado=None):
        # Limpia tabla antes de cargar los destinos.
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        
        if listado is None:
            # Carga todos los destinos del archivo JSON.
            for destino in self.controlador.destinos:
                self.tabla.insert('', tk.END,
                                values=(destino.nombre, destino.tipo_cocina, ", ".join(destino.ingredientes), f"${destino.precio_minimo} - ${destino.precio_maximo}", destino.popularidad))
        else:
            # Cargamos los destinos resultantes de la busqueda.
            for destino in listado:
                self.tabla.insert('', tk.END,
                                values=(destino.nombre, destino.tipo_cocina, ", ".join(destino.ingredientes), f"${destino.precio_minimo} - ${destino.precio_maximo}", destino.popularidad))
    

    def filtrar_listado(self):
        """
        Filtra y muestra los destinos en la tabla de acuerdo a los criterios de búsqueda ingresados por el usuario.
        """
        # Obtiene lo valores ingresados.
        tipo = self.entry_tipo.get()
        ingrediente = self.entry_ingrediente.get()
        precio_minimo = self.entry_precio_minimo.get()
        precio_maximo = self.entry_precio_maximo.get()
        popularidad = self.entry_popularidad.get()

        # Muestra por consola los valores ingresados.
        print("buscando: ", tipo)
        print("buscando: ", ingrediente)
        print("buscando: ", precio_minimo)
        print("buscando: ", precio_maximo)
        print("buscando: ", popularidad)
        print("---")

        # Extrae todos los destinos en un conjunto para realizar el filtrado.
        resultado_busqueda = set(self.controlador.destinos)

        # Si se ha seleccionado un tipo de cocina que no sea el valor por defecto "Seleccione uno..".
        if tipo != "Seleccione uno..":
            resultado_tipo = {destino for destino in resultado_busqueda if tipo in destino.tipo_cocina} # Se filtran los destinos que coincidan con el tipo de cocina especificado.
            resultado_busqueda &= resultado_tipo # Intersección entre el conjunto de todos los destinos y el conjunto de los destinos filtrados por tipo_cocina.

        if ingrediente != "Seleccione uno..":
            resultado_ingrediente = {destino for destino in resultado_busqueda if ingrediente in destino.ingredientes}
            resultado_busqueda &= resultado_ingrediente

        if len(precio_minimo):
            resultado_precio_minimo = {destino for destino in resultado_busqueda if int(precio_minimo) <= destino.precio_minimo}
            resultado_busqueda &= resultado_precio_minimo

        if len(precio_maximo):
            resultado_precio_maximo = {destino for destino in resultado_busqueda if int(precio_maximo) >= destino.precio_maximo}
            resultado_busqueda &= resultado_precio_maximo
        
        if popularidad:
            resultado_popularidad = {destino for destino in resultado_busqueda if popularidad == int(destino.popularidad)}
            resultado_busqueda &= resultado_popularidad

        # El conjunto resultado_busqueda contiene los destinos que cumplen con todas las condiciones de búsqueda especificadas por el usuario.
        if resultado_busqueda:
            # Cargamos los destinos filtrados.
            self.cargar_tabla(listado=resultado_busqueda)
        else:
            # Si no hay resultados después del filtrado, eliminamos todas las filas.
            self.tabla.delete(*self.tabla.get_children())


    def limpiar_filtros(self):
        """
        Limpia y restablece todos los filtros de búsqueda a sus valores iniciales.
        """
        # Restablecer el ComboBox de tipo de cocina y el ComboBox de ingredientes
        self.entry_tipo.set("Seleccione uno..")
        self.entry_ingrediente.set("Seleccione uno..")

        # Borrar los valores ingresados en los campos de precio mínimo y máximo
        self.entry_precio_minimo.delete(0, tk.END)
        self.entry_precio_maximo.delete(0, tk.END)

        # Restablecer los placeholders en los campos de precio
        self.entry_precio_minimo.configure(placeholder_text="Mínimo")
        self.entry_precio_maximo.configure(placeholder_text="Máximo")

        # Establecer la popularidad en cero y actualizar su etiqueta de valor
        self.entry_popularidad.set(0)
        self.label_popularidad_valor = customtkinter.CTkLabel(self.frame_busqueda, text=str(self.entry_popularidad.get()))
        self.label_popularidad_valor.grid(row=11, column=0, padx=30, pady=5, sticky="ew")

        # Actualizar la tabla mostrando todos los destinos sin filtros aplicados
        self.cargar_tabla()


    def mostrar_detalles(self, event):
        """
        Muestra los detalles de un destino cuando se hace doble clic en una fila de la tabla.
        """
        print("Doble click")

        # Obtiene el elemento seleccionado.
        selected_item = self.tabla.focus()

        # Obtiene el ID del elemento seleccionado.
        values = self.tabla.item(selected_item, "values")  

        print("Destino seleccionado:", values)

        # Busca el destino seleccionado en la lista de destinos
        destinos = self.controlador.destinos
        for destino in destinos:
            if destino.nombre == values[0]:
                break
        
        # Crea una ventana secundaria para mostrar los detalles del destino.
        toplevel = customtkinter.CTkToplevel(self.master)
        VistaDetalles(destino, toplevel).grid()
