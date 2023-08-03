import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox

class VistaReview(customtkinter.CTkFrame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de reviews y calificaciones.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Crea titulo de la vista
        self.main_label = customtkinter.CTkLabel(
            self,
            text="Reviews y Calificaciones",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        # Frame para la lista de destinos
        self.destinos_frame = customtkinter.CTkFrame(self, height=400)
        self.destinos_frame.grid_columnconfigure(0, weight=1)
        self.destinos_frame.grid(row=1, column=0)

        #Listbox de los destinos
        self.lista_destinos = tk.Listbox(self.destinos_frame, width=40, height=25)
        self.lista_destinos.bind('<<ListboxSelect>>', self.seleccionar_elemento)
        self.lista_destinos.grid()

        #Cargo los destinos a la listbox
        self.cargar_destinos()

        #Frame paras las reviews
        self.reviews_frame = customtkinter.CTkScrollableFrame(self, width=550, height=400)
        self.reviews_frame.grid(row=1, column=1, sticky="nsew", columns=3, rowspan=10, pady=(0, 20))

        #Obtengo los reviews
        reviews = self.controlador.obtener_reviews()

        #Cargo la estrella
        self.estrella = ImageTk.PhotoImage(Image.open("app/views/images/star.png").resize((25, 25)))
        self.like = ImageTk.PhotoImage(Image.open("app/views/images/like.png").resize((25, 25)))
        self.dislike = ImageTk.PhotoImage(Image.open("app/views/images/dislike.png").resize((25, 25)))

        #Muestro Todos las reviews
        i=0   
        for review in reviews:
            #Destino label
            self.label_destino_nombre = customtkinter.CTkLabel(
                self.reviews_frame,
                text="Destino: "+review.id_destino,
                font=customtkinter.CTkFont(family="Open Sans", size=15, weight="bold")
            )
            self.label_destino_nombre.grid(row=i, column=1)
            #Usuario label
            self.label_usuario = customtkinter.CTkLabel(
                self.reviews_frame,
                text="Usuario: "+review.id_usuario,
                font=customtkinter.CTkFont(family="Open Sans", size=13)
            )
            self.label_usuario.grid(row=i+1, column= 0)
            #Calificacion label
            self.label_calificacion = customtkinter.CTkLabel(
                self.reviews_frame,
                text=f"Calificacion: {review.calificacion}",
                font=customtkinter.CTkFont(family="Open Sans", size=13)
            )
            self.label_calificacion.grid(row=i+2, column=0)
            self.frame_estrellas = customtkinter.CTkFrame(self.reviews_frame)
            self.frame_estrellas.grid(row=i+2, column=1)
            for j in range(0, review.calificacion):
                self.imagen_estrella = customtkinter.CTkLabel(self.frame_estrellas, text="",image=self.estrella)
                self.imagen_estrella.grid(row=0, column=j)
            self.imagen_animo = customtkinter.CTkLabel(self.reviews_frame, text="", image=self.like if (review.animo=="Positivo") else self.dislike)
            self.imagen_animo.grid(row=i+2, column=1, padx=(350,0))
            #Label de review
            self.label_review = customtkinter.CTkLabel(
                self.reviews_frame,
                text=review.comentario,
                font=customtkinter.CTkFont(family="Open Sans", size=13),
                wraplength=420
            )
            self.label_review.grid(row=i+3, column=1)
            self.label_espacio  = customtkinter.CTkLabel(self.reviews_frame, text="-------------------------------------------------------------------------------")
            self.label_espacio.grid(row=i+4, column=1)
            i+=5            

        # Crea el botón para crear una review lo agrega a la vista
        self.boton_crear_review = customtkinter.CTkButton(
            self, text="Crear Review", command=self.crear_review, width=200
        )
        self.boton_crear_review.grid(row=2, column=0, padx=30, pady=(15, 15))

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = customtkinter.CTkButton(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio, width=200
        )
        self.boton_inicio.grid(row=3, column=0, padx=30, pady=(15, 15))

    def cargar_destinos(self):
        destinos = self.controlador.obtener_destinos()
        for destino in destinos:
            self.lista_destinos.insert(tk.END, destino.nombre)

    #Mostramos las reviews del local seleccionado
    def seleccionar_elemento(self, event):
        select = self.lista_destinos.curselection()
        id = self.controlador.seleccionar_local(event, select)
        
        #Genero Ventana con reviews
        self.ventana_seleccion = customtkinter.CTkToplevel()
        self.ventana_seleccion.title("Reviews")
        self.ventana_seleccion.resizable(False, False)

        #Establezo grab
        self.ventana_seleccion.grab_set()

        rev = self.controlador.obtener_reviews_seleccionada(id)  
        nombre_destino = self.controlador.obtener_nombre_destino(id)

        #Label con titulo
        self.titulo_nueva_ventana = customtkinter.CTkLabel(
            self.ventana_seleccion,
            text="Reviews de "+nombre_destino,
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.titulo_nueva_ventana.grid(row=0, column=0, padx=30, pady=(30, 30))

        #Frame paras las reviews
        reviews_frame = customtkinter.CTkScrollableFrame(self.ventana_seleccion, width=550, height=400)
        reviews_frame.grid(row=1, column=0, sticky="nsew", padx=30)      
        
        if len(rev) > 0:         
            i = 0
            #Muestro Todos las reviews
            for review in rev:
                #Usuario label
                label_usuario = customtkinter.CTkLabel(
                    reviews_frame,
                    text="Usuario: "+review.id_usuario,
                    font=customtkinter.CTkFont(family="Open Sans", size=13)
                )
                label_usuario.grid(row=i+0, column= 0)
                #Calificacion label
                label_calificacion = customtkinter.CTkLabel(
                    reviews_frame,
                    text=f"Calificacion: {review.calificacion}",
                    font=customtkinter.CTkFont(family="Open Sans", size=13)
                )
                label_calificacion.grid(row=i+1, column=0)
                frame_estrellas = customtkinter.CTkFrame(reviews_frame)
                frame_estrellas.grid(row=i+1, column=1)
                for j in range(0, review.calificacion):
                    imagen_estrella = customtkinter.CTkLabel(frame_estrellas, text="",image=self.estrella)
                    imagen_estrella.grid(row=0, column=j)
                imagen_animo = customtkinter.CTkLabel(reviews_frame, text="", image=self.like if (review.animo=="Positivo") else self.dislike)
                imagen_animo.grid(row=i+1, column=1, padx=(350,0))
                #Label de review
                label_review = customtkinter.CTkLabel(
                    reviews_frame,
                    text=review.comentario,
                    font=customtkinter.CTkFont(family="Open Sans", size=13),
                    wraplength=420
                )
                label_review.grid(row=i+2, column=1)
                label_espacio = customtkinter.CTkLabel(reviews_frame, text="-------------------------------------------------------------------------------")
                label_espacio.grid(row=i+3, column=1)
                i += 4
        else:
            label_review = customtkinter.CTkLabel(
                    reviews_frame,
                    text="No existen reviews del destino seleccionado",
                    font=customtkinter.CTkFont(family="Open Sans", size=15)
                )
            label_review.grid(row=0, column=0)

        button_close = customtkinter.CTkButton(self.ventana_seleccion, text="Volver", command=lambda: self.ventana_seleccion.destroy())
        button_close.grid(row=2, column=0, pady=(30, 30), padx=(30, 30), sticky="w")


    #Creamos metodo para crear nuevas reviews
    def crear_review(self):

        def send_data():
            print("CALIFIACION", calificacion.get())
            if destino.get() and calificacion.get() and comentario.get() and animo.get():
                try:
                    if int(calificacion.get()) <= 5 and int(calificacion.get()) >= 1:
                        review = [destino.get(), self.user.id, int(calificacion.get()), comentario.get(), animo.get()]
                        self.controlador.preparar_review(review)
                        CTkMessagebox(title="Guardado", message="Review guardada con éxito.", icon="check", option_1="Gracias")
                        self.ventana_crear.destroy()
                    else:
                        CTkMessagebox(title="Error", message="Coloque correctamente la calificación", icon="cancel")
                except ValueError:
                    CTkMessagebox(title="Error", message="Coloque correctamente la calificación", icon="cancel")               
            else:
                CTkMessagebox(title="Error", message="Debe rellenar todos los campos!!!", icon="cancel")
        
        #Genero nueva ventana para el formulario
        self.ventana_crear = customtkinter.CTkToplevel()
        self.ventana_crear.title("Crear Review")
        self.ventana_crear.resizable(False, False)
        self.ventana_crear.grab_set()

        formulario_frame = customtkinter.CTkFrame(self.ventana_crear, width=350, height=300)
        formulario_frame.grid(row=0, column=0, padx=30, pady=(20, 20))

        #Labels del formulario
        label_destino = customtkinter.CTkLabel(formulario_frame, text="Destino")
        label_destino.grid(row=0, column=0, padx=10, pady=(15, 5), sticky="e")

        label_calificacion = customtkinter.CTkLabel(formulario_frame, text="Calificación (1 al 5)")
        label_calificacion.grid(row=1, column=0, padx=10, pady=(5, 5), sticky="e")

        label_comentario = customtkinter.CTkLabel(formulario_frame, text="Comentario")
        label_comentario.grid(row=3, column=0, padx=10, pady=(5, 5), sticky="e")

        label_animo = customtkinter.CTkLabel(formulario_frame, text="Ánimo")
        label_animo.grid(row=4, column=0, padx=10, pady=(5, 5), sticky="e")

        #Variables del formulario
        destino = customtkinter.StringVar()
        calificacion = customtkinter.StringVar()
        comentario = customtkinter.StringVar()
        animo = customtkinter.StringVar()

        destinos = self.controlador.obtener_nombres_destinos()

        #Entrys del formulario
        entry_destino = customtkinter.CTkComboBox(formulario_frame, state="readonly", values=[*destinos], variable=destino)
        entry_destino.grid(row=0, column=1, padx=10, pady=(5, 5), sticky="we")
        
        entry_calificacion = customtkinter.CTkEntry(formulario_frame, textvariable=calificacion)
        entry_calificacion.grid(row=1, column=1, padx=10, pady=(5, 5), sticky="we")

        entry_comentario = customtkinter.CTkEntry(formulario_frame, textvariable=comentario, width=200)
        entry_comentario.grid(row=3, column=1, padx=10, pady=(5, 5), sticky="we")

        entry_animo1 = customtkinter.CTkRadioButton(formulario_frame, text="Positivo", value="Positivo", variable=animo)
        entry_animo1.grid(row=4, column=1, padx=10, pady=(5, 5), sticky="w")
        entry_animo2 = customtkinter.CTkRadioButton(formulario_frame, text="Negativo", value="Negativo", variable=animo)
        entry_animo2.grid(row=5, column=1, padx=10, pady=(0, 5), sticky="w")

        button_submit = customtkinter.CTkButton(formulario_frame, text="Confirmar", width=100, command=send_data)
        button_submit.grid(row=6, column=0, padx=(15, 15), pady=(15, 15), columnspan=2, sticky="e")

        button_close = customtkinter.CTkButton(self.ventana_crear, text="Volver", width=100, command=lambda: self.ventana_crear.destroy())
        button_close.grid(row=1, column=0, padx=(30, 30), pady=(20, 30), sticky="w")

    def recibir_usuario(self, usuario):
        self.user = usuario
