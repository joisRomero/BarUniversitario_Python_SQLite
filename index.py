from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from datetime import date
from datetime import datetime

import sqlite3

class Bar_Universitario:

    base_datos = "database.db"

    def __init__(self, root):
        self.ventana_principal = root
        self.ventana_principal.title("Bar Universitario")

        self.cuaderno = ttk.Notebook(self.ventana_principal)

        self.pedidos()
        self.estudiantes()
        self.rellenar_menu_disponible()  

        #variable gobal 
        self.total_final = 0
        self.compras = []

        self.cuaderno.grid(column = 0, row = 0, padx = 10, pady = 10)

    def pedidos(self):
        # Pagina Pedidos
        self.pagina_pedidos = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_pedidos, text = "Pedidos")

        # Contenedor Verificaion_de_alumno
        contenedor_verificacion = LabelFrame(self.pagina_pedidos, text = "Verificion de alummno")
        contenedor_verificacion.grid(column = 0, row = 0, padx = 5, pady = 10, sticky = W)

        # Ingresando Dni
        Label(contenedor_verificacion, text = "Ingrese Numero de DNI: ").grid(column = 0, row = 0, padx = 4, pady = 4)
        self.dni_verificacion_pedidos = Entry(contenedor_verificacion)
        self.dni_verificacion_pedidos.focus()
        self.dni_verificacion_pedidos.grid(column = 1, row = 0, padx = 4, pady = 4)
        # Boton buscar alumno
        ttk.Button(contenedor_verificacion, text = "Buscar", command = self.buscar_estudiante_comprar).grid(column = 2, row = 0, padx = 4, pady = 4)

        # Contenedor Pedidos
        contenedor_pedidos = LabelFrame(self.pagina_pedidos, text = "Pedidos")
        contenedor_pedidos.grid(column = 0, row = 1, padx = 5, pady = 10, sticky = W)

        # Datos del estudiante
        Label(contenedor_pedidos, text = "Estudiante:").grid(column = 0, row = 2, padx = 4, pady = 4, sticky = W)
        self.rellenar_nombre = Label(contenedor_pedidos, text = "")
        self.rellenar_nombre.grid(column = 0, row = 2, padx = 4, pady = 4, sticky = E)

        Label(contenedor_pedidos, text = "Credito:").grid(column = 1, row = 2, padx = 4, pady = 4, sticky = E)
        self.rellenar_pedido = Label(contenedor_pedidos, text = "")
        self.rellenar_pedido.grid(column = 5, row = 2, padx = 4, pady = 4, sticky = W)

        # Menu   
        self.menu = ttk.Treeview(contenedor_pedidos, height = 10, columns = 3)
        self.menu.grid(column = 0, row = 3, columnspan = 2, padx = 20, pady = 9)
        self.menu.heading("#0", text = "MENU DISPONIBLE", anchor = CENTER)
        self.menu.heading("#1", text = "PRECIO", anchor = CENTER)
        
        #Menu para comprar
        Label(contenedor_pedidos, text = "Ingrese opción de menú: ").grid(column = 0, row = 4, padx = 4, pady = 4, sticky = E)
        self.estado_opcion_menu = "readonly"
        self.opcion_menu = Entry(contenedor_pedidos, width = 10, state = "readonly")
        self.opcion_menu.grid(column = 1, row = 4, padx = 4, pady = 4, sticky = W)

        Label(contenedor_pedidos, text = "Ingrese cantidad: ").grid(column = 0, row = 5, padx = 4, pady = 4, sticky = E)
        self.ingrese_cantidad = Entry(contenedor_pedidos, width = 10, state = "readonly")
        self.ingrese_cantidad.grid(column = 1, row = 5, padx = 4, pady = 4, sticky = W)

        ttk.Button(contenedor_pedidos, text = "Cargar", command = self.cargar).grid(column = 0, row = 6, padx = 4, pady = 4, columnspan = 3)

        Label(contenedor_pedidos, text = "TOTAL DEL PEDIDO:").grid(column = 0, row = 7, padx = 4, pady = 4)
        self.rellenar_total_pedido = Label(contenedor_pedidos,text = "")
        self.rellenar_total_pedido.grid(column = 0, row = 7, padx = 4, pady = 4, sticky = E)
        ttk.Button(contenedor_pedidos, text = "Comprar", command = self.comprar).grid(column = 1, row = 7, padx = 4, pady = 4, sticky = W)

        Label(contenedor_pedidos, text = "").grid(column = 0, row = 8)
        Label(contenedor_pedidos, text = "Ingrese cantidad a pagar: ").grid(column = 0, row = 9, padx = 4, pady = 4, sticky = E)
        self.cantidad_pagar = Entry(contenedor_pedidos, width = 10, state = "readonly")
        self.cantidad_pagar.grid(column = 1, row = 9, padx = 4, pady = 4, sticky = W)
        ttk.Button(contenedor_pedidos, text = "Aceptar", command = self.aceptar).grid(column = 0, row = 10, padx = 4, pady = 4, columnspan = 3)

    def estudiantes(self):
        #Pagina Estudiantes
        self.pagina_estudiantes = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina_estudiantes, text = "Estudiantes")

        # Cuaderno Registrar y Actualizar
        self.cuaderno_estudiantes = ttk.Notebook(self.pagina_estudiantes)

        self.estudiantes_resgistrar()
        self.estudiantes_actualizar()

        self.cuaderno_estudiantes.grid(column = 0, row = 1, padx = 10, pady = 10)

    def estudiantes_resgistrar(self):
        # Opcion Registrar
        self.pagina_registrar = ttk.Frame(self.cuaderno_estudiantes)
        self.cuaderno_estudiantes.add(self.pagina_registrar, text = "Registrar")

        # Contenedor Registrar_datos
        contenedor_registrar_datos = LabelFrame(self.pagina_registrar, text = "Registrar datos")
        contenedor_registrar_datos.grid(column = 0, row = 1, padx = 10, pady = 10)

        # DNI
        Label(contenedor_registrar_datos, text = "DNI: ").grid(column = 1, row = 2, padx = 4, pady = 4)
        self.registrar_dni = Entry(contenedor_registrar_datos, width = 30)
        self.registrar_dni.focus()
        self.registrar_dni.grid(column = 2, row = 2, padx = 4, pady = 4)
        # Nombre
        Label(contenedor_registrar_datos, text = "Nombres: ").grid(column = 1, row = 3, padx = 4, pady = 4)
        self.registrar_nombre = Entry(contenedor_registrar_datos, width = 30) 
        self.registrar_nombre.grid(column = 2, row = 3, padx = 4, pady = 4)
        # Apellidos
        Label(contenedor_registrar_datos, text = "Apellidos: ").grid(column = 1, row = 4, padx = 4, pady = 4)
        self.registrar_apellidos = Entry(contenedor_registrar_datos, width = 30)
        self.registrar_apellidos.grid(column = 2, row = 4, padx = 4, pady = 4)
        # Ciclo
        Label(contenedor_registrar_datos, text = "Ciclo: ").grid(column = 1, row = 5, padx = 4, pady = 4)
        self.registrar_ciclo = Entry(contenedor_registrar_datos, width = 30)
        self.registrar_ciclo.grid(column = 2, row = 5, padx = 4, pady = 4)
        # Carrera
        Label(contenedor_registrar_datos, text = "Carrera").grid(column = 1, row = 6, padx = 4, pady = 4)
        self.registrar_carrera = ttk.Combobox(contenedor_registrar_datos)
        self.registrar_carrera.grid(column = 2, row = 6, padx = 4, pady = 4, sticky = W)
        self.registrar_carrera['values'] = ("Ing. Informática", "Ing. Electrónica", "Física", "Estadística", "Matemática")
        self.registrar_carrera.current(0)
        # Edad
        Label(contenedor_registrar_datos, text = "Edad").grid(column = 1, row = 7, padx = 4, pady = 4)
        self.registrar_edad = Entry(contenedor_registrar_datos, width = 30)
        self.registrar_edad.grid(column = 2, row = 7, padx = 4, pady = 4)
        # Sexo
        self.seleccion_sexo = StringVar()
        Label(contenedor_registrar_datos, text = "Sexo").grid(column = 1, row = 8, padx = 4, pady = 4)
        sexo_masculino = Radiobutton(contenedor_registrar_datos, text = "Maculino", value = "Maculino", variable = self.seleccion_sexo)
        sexo_masculino.grid(column = 2, row = 8, padx = 4, pady = 4, sticky = W)
        sexo_femenino = Radiobutton(contenedor_registrar_datos, text = "Femenino", value = "Femenino", variable = self.seleccion_sexo)
        sexo_femenino.grid(column = 2, row = 8, padx = 4, pady = 4, sticky = E)
        # Botón guardar
        ttk.Button(contenedor_registrar_datos, text = "Guardar", command = self.guardar_estudiante).grid(column = 2, row = 9, padx = 4, pady = 4)
    
    def estudiantes_actualizar(self):

        # Opcion Actualizar
        self.pagina_actualizar = ttk.Frame(self.cuaderno_estudiantes)
        self.cuaderno_estudiantes.add(self.pagina_actualizar, text = "Actualizar")

        # Contenedor Verificaion_de_alumno
        contenedor_verificacion = LabelFrame(self.pagina_actualizar, text = "Verificion de alummno")
        contenedor_verificacion.grid(column = 0, row = 1, padx = 5, pady = 10, sticky = W)

        # Ingresando Dni
        Label(contenedor_verificacion, text = "Ingrese Numero de DNI: ").grid(column = 0, row = 1, padx = 4, pady = 4)
        self.dni_verificacion_actualizar = Entry(contenedor_verificacion)
        self.dni_verificacion_actualizar.focus()
        self.dni_verificacion_actualizar.grid(column = 1, row = 1, padx = 4, pady = 4)
        # Boton buscar alumno
        ttk.Button(contenedor_verificacion, text = "Buscar", command = self.buscar_estudiante_actualizar).grid(column = 2, row = 1, padx = 4, pady = 4)

        # Contenedor Actualizar_datos_alumno
        contenedor_actualizar_datos = LabelFrame(self.pagina_actualizar, text = "Actualización de datos")
        contenedor_actualizar_datos.grid(column = 0, row = 2, padx = 5, pady = 10, sticky = W)

        # DNI
        Label(contenedor_actualizar_datos, text = "DNI: ").grid(column = 1, row = 2, padx = 4, pady = 4)
        self.actualizar_dni = Entry(contenedor_actualizar_datos, width = 30, state = "readonly")
        self.actualizar_dni.grid(column = 2, row = 2, padx = 4, pady = 4)
        # Nombre
        Label(contenedor_actualizar_datos, text = "Nombres: ").grid(column = 1, row = 3, padx = 4, pady = 4)
        self.actualizar_nombre = Entry(contenedor_actualizar_datos, width = 30, state = "readonly") 
        self.actualizar_nombre.grid(column = 2, row = 3, padx = 4, pady = 4)
        # Apellidos
        Label(contenedor_actualizar_datos, text = "Apellidos: ").grid(column = 1, row = 4, padx = 4, pady = 4)
        self.actualizar_apellidos = Entry(contenedor_actualizar_datos, width = 30, state = "readonly")
        self.actualizar_apellidos.grid(column = 2, row = 4, padx = 4, pady = 4)
        # Ciclo
        Label(contenedor_actualizar_datos, text = "Ciclo: ").grid(column = 1, row = 5, padx = 4, pady = 4)
        self.actualizar_ciclo = Entry(contenedor_actualizar_datos, width = 30, state = "readonly")
        self.actualizar_ciclo.grid(column = 2, row = 5, padx = 4, pady = 4)
        # Carrera
        Label(contenedor_actualizar_datos, text = "Carrera").grid(column = 1, row = 6, padx = 4, pady = 4)
        self.actualizar_carrera = ttk.Combobox(contenedor_actualizar_datos, state = "readonly")
        self.actualizar_carrera.grid(column = 2, row = 6, padx = 4, pady = 4, sticky = W)
        self.actualizar_carrera['values'] = ("Ing. Informática", "Ing. Electrónica", "Física", "Estadística", "Matemática")
        self.actualizar_carrera.current(0)
        # Edad
        Label(contenedor_actualizar_datos, text = "Edad").grid(column = 1, row = 7, padx = 4, pady = 4)
        self.actualizar_edad = Entry(contenedor_actualizar_datos, width = 30, state = "readonly")
        self.actualizar_edad.grid(column = 2, row = 7, padx = 4, pady = 4)
        # Sexo
        self.seleccion_actualizar_sexo = StringVar()
        Label(contenedor_actualizar_datos, text = "Sexo").grid(column = 1, row = 8, padx = 4, pady = 4)
        self.actualizar_sexo_masculino = Radiobutton(contenedor_actualizar_datos, text = "Masculino", value = "Masculino", variable = self.seleccion_actualizar_sexo, state = "disabled")
        self.actualizar_sexo_masculino.grid(column = 2, row = 8, padx = 4, pady = 4, sticky = W)
        self.actualizar_sexo_femenino = Radiobutton(contenedor_actualizar_datos, text = "Femenino", value = "Femenino", variable = self.seleccion_actualizar_sexo, state = "disabled")
        self.actualizar_sexo_femenino.grid(column = 2, row = 8, padx = 4, pady = 4, sticky = E)
        # Credito
        Label(contenedor_actualizar_datos, text = "Credito").grid(column = 1, row = 9, padx = 4, pady = 4)
        self.actualizar_credito = Entry(contenedor_actualizar_datos, width = 30, state = "readonly")
        self.actualizar_credito.grid(column = 2, row = 9, padx = 4, pady = 4)
        # Botón actualizar
        ttk.Button(contenedor_actualizar_datos, text = "Actualizar", command = self.actualizar_estudiante).grid(column = 2, row = 10, padx = 4, pady = 4)

    def consulta(self, query, parametros = ()):
        with sqlite3.connect(self.base_datos) as conn:
           cursor = conn.cursor()
           resultado = cursor.execute(query, parametros)
           conn.commit()
        return resultado
    
    #OPCION HACER PEDIDO
    def validacion_buscar_estudiante(self):
        return len(self.dni_verificacion_pedidos.get()) != 0 or len(self.dni_verificacion_actualizar.get()) != 0

    def buscar_estudiante_dni(self, dni_buscar):
        if self.validacion_buscar_estudiante():
            query = "SELECT dni FROM alumno WHERE dni = ?"
            db_resultado = self.consulta(query, (dni_buscar, ))
            band = 0
            for self.dni in db_resultado:
                band = 0
                if self.dni[0] == int(dni_buscar):
                    band = 1
            return band                    
        else:
            messagebox.showerror('ERROR', 'Ingrese un numero de DNI')
        
    def buscar_estudiante_comprar(self):
        band = self.buscar_estudiante_dni(self.dni_verificacion_pedidos.get())
        if band == 0 or band == 1:
            if band == 1:
                messagebox.showinfo('Mensaje', 'Estudiante encontrado con éxito') 
                self.rellenar_nombre_credito()
                self.opcion_menu["state"] = "normal"
                self.ingrese_cantidad["state"] = "normal"
                self.opcion_menu.focus()
            else:
                messagebox.showinfo('Mensaje', 'Estudiante no registrado')
  
    def rellenar_nombre_credito(self):
        query = "SELECT nombre,apellido,credito FROM alumno WHERE dni = ?"
        db_resultado = self.consulta(query,(self.dni_verificacion_pedidos.get(), ))
        for self.nombre in db_resultado:
            self.rellenar_nombre['text'] = "{} {}".format(self.nombre[0],self.nombre[1])
            self.rellenar_pedido['text'] = "${}0".format(self.nombre[2])

    def rellenar_menu_disponible(self):
        indice = 1
        query = "SELECT * FROM producto"
        db_resultado = self.consulta(query)
        for menu in db_resultado:
            self.menu.insert("",indice, text = "{}. {}".format(indice,menu[1]), values = "${}0".format(menu[2]))
            indice = indice + 1

    def validacion_cargar(self):
        return len(self.opcion_menu.get()) != 0 and len(self.ingrese_cantidad.get()) != 0

    def validacion_opcion_menu(self):
        query = "SELECT MAX(id_producto) FROM producto "
        db_resultado = self.consulta(query)
        for id_mayor in db_resultado:
            if id_mayor[0] >= (int(self.opcion_menu.get())):
                band = 0
            else:
                band = 1
        return band

    def cargar(self):
        if self.validacion_cargar():
            self.opcion_menu.focus()
            if self.validacion_opcion_menu() == 0:
                query = "SELECT precio FROM producto where id_producto = ?"
                db_resultado = self.consulta(query,(self.opcion_menu.get(), ))
                for precio in db_resultado:  
                    total_parcial= (float(precio[0])) * (float(self.ingrese_cantidad.get()))
                    self.total_final = self.total_final + total_parcial 
                self.rellenar_total_pedido['text'] = "${}0".format(self.total_final)
                self.guardar_en_tabla_compra()
                self.limpiar_cargar() 

            else:
                messagebox.showerror('ERROR', 'La "Opción de menú" no corresponde al menú disponible')
                self.limpiar_cargar() 
        else:
            if self.validacion_buscar_estudiante():
                messagebox.showerror('ERROR', 'Complete los campos "Ingrese opción del menú" e "Ingrese cantidad"')
            else:
                messagebox.showerror('ERROR', 'Ingrese un numero de DNI')
    
    def guardar_en_tabla_compra(self):
        self.fecha_compra = date.today()
        query = "INSERT INTO compra (id_compra, dni, id_producto, cantidad, fecha_compra) VALUES (NULL, ?, ?, ?, ?)" 
        parametros = (self.dni_verificacion_pedidos.get(), self.opcion_menu.get(), self.ingrese_cantidad.get(), self.fecha_compra)
        self.consulta(query,parametros)

    def limpiar_cargar(self):
        self.opcion_menu.delete(0, END)
        self.ingrese_cantidad.delete(0, END) 

    def comprar(self):
        self.cantidad_pagar["state"] = "normal"
        self.opcion_menu["state"] = "readonly"
        self.ingrese_cantidad["state"] = "readonly"
    
    def validacion_aceptar(self):
        return len(self.cantidad_pagar.get()) != 0
    
    def aceptar(self):
        self.vuelto = 0.0
        self.dinero_faltante = 0.0
        if self.validacion_aceptar():
            query = "SELECT credito FROM alumno WHERE dni = ?"
            db_resultado = self.consulta(query,(self.dni_verificacion_pedidos.get(), ))

            if self.total_final <= (float(self.cantidad_pagar.get())):
                self.vuelto = (float(self.cantidad_pagar.get())) - self.total_final 
                self.boleta()
                self.rellenar_total_pedido['text'] = "           "
                self.dni_verificacion_pedidos.delete(0, END)
                self.cantidad_pagar.delete(0,END)
                self.cantidad_pagar["state"] = "readonly"
                self.dni_verificacion_pedidos.focus()
            else:
                self.dinero_faltante = self.total_final - (float(self.cantidad_pagar.get()))  
                for credito in db_resultado:
                    if self.dinero_faltante <= credito[0]:
                        self.credito_restante = credito[0] - self.dinero_faltante
                        self.nuevo_credito()
                        self.boleta()
                        self.rellenar_total_pedido['text'] = "           "
                        self.dni_verificacion_pedidos.delete(0, END)
                        self.cantidad_pagar.delete(0,END)
                        self.cantidad_pagar["state"] = "readonly"
                        self.dni_verificacion_pedidos.focus()
                    else:    
                        messagebox.showerror('ERROR', 'Dinero insuficiente')
                        self.cantidad_pagar.delete(0,END)
        else:
            messagebox.showerror('ERROR', 'Complete el campo "Ingrese cantidad a pagar"')
            self.cantidad_pagar.delete(0,END)

    def nuevo_credito(self):
        query = "UPDATE alumno SET credito = ? WHERE dni = ?"
        parametros = (self.credito_restante, self.dni_verificacion_pedidos.get())
        self.consulta(query,parametros)

    def boleta(self):
        self.ventana_factura = Toplevel()
        self.ventana_factura.title("BOLETA")

        Label(self.ventana_factura, text = "BOLETA", font=('Helvetica', 10, 'bold')).grid(row = 0, column = 0, columnspan = 4)
        Label(self.ventana_factura, text = "DNI:", font=('Helvetica', 10, 'bold')).grid(row = 1, column = 0,sticky = W)
        Label(self.ventana_factura, text = "{}".format(self.dni[0])).grid(row = 1, column = 1, sticky = E)

        Label(self.ventana_factura, text = "NOMBRE:", font=('Helvetica', 10, 'bold')).grid(row = 2, column = 0, sticky = W)
        Label(self.ventana_factura, text = "{}".format(self.nombre[0])).grid(row = 2, column = 1, sticky = E) 

        Label(self.ventana_factura, text = "APELLIDO:", font=('Helvetica', 10, 'bold')).grid(row = 3, column = 0, sticky = W)
        Label(self.ventana_factura, text = "{}".format(self.nombre[1])).grid(row = 3, column = 1, sticky = E)
        
        Label(self.ventana_factura, text = "TOTAL $:", font=('Helvetica', 10, 'bold')).grid(row = 5, column = 0, sticky = W)
        Label(self.ventana_factura, text = "{}".format(self.total_final)).grid(row = 5, column = 1, sticky = E)

        Label(self.ventana_factura, text = "PAGA CON $:", font=('Helvetica', 10, 'bold')).grid(row = 6, column = 0, sticky = W)
        Label(self.ventana_factura, text = "{}".format(float(self.cantidad_pagar.get()))).grid(row = 6, column = 1, sticky = E)

        Label(self.ventana_factura, text = "DSCT DEL CRD ESTD:", font=('Helvetica', 10, 'bold')).grid(row = 7, column = 0, sticky = W)
        Label(self.ventana_factura, text = "{}".format(self.dinero_faltante)).grid(row = 7, column = 1, sticky = E)

        Label(self.ventana_factura, text = "VUELTO $:", font=('Helvetica', 10, 'bold')).grid(row = 8, column = 0, sticky = W)
        Label(self.ventana_factura, text = "{}".format(self.vuelto)).grid(row = 8, column = 1, sticky = E)

    #OPCION GUARDAR ESTUDIANTE
    def validacion_guardar_estudiante(self):
        return len(self.registrar_nombre.get()) != 0 and len(self.registrar_apellidos.get()) != 0 and len(self.registrar_dni.get())  != 0 and len(self.registrar_ciclo.get())  != 0 and len(self.registrar_carrera.get())  != 0 and len(self.registrar_edad.get())   != 0 and len(self.seleccion_sexo.get())  != 0 
    
    def limpiar_guardar_estudiantes(self):
        self.registrar_dni.delete(0, END)
        self.registrar_nombre.delete(0, END)
        self.registrar_apellidos.delete(0, END)
        self.registrar_ciclo.delete(0, END)
        self.registrar_edad.delete(0, END)

    def guardar_estudiante(self):
        self.credito = 30
        if self.validacion_guardar_estudiante():
            query = "INSERT INTO alumno VALUES (?,?,?,?,?,?,?,?)"
            parametros = (self.registrar_dni.get(),self.registrar_nombre.get(),self.registrar_apellidos.get(),self.registrar_ciclo.get(),self.registrar_carrera.get(),self.registrar_edad.get(),self.seleccion_sexo.get(),self.credito)
            self.consulta(query,parametros)
            messagebox.showinfo('Mensaje', 'Estudiante guardado con éxito')
            self.limpiar_guardar_estudiantes()
        else:
            messagebox.showerror('ERROR', 'Rellene todos los campos')
    
    #OPCION ACTUALIZAR ESTUDAINTE
    def buscar_estudiante_actualizar(self):
        band = self.buscar_estudiante_dni(self.dni_verificacion_actualizar.get())
        if band == 0 or band == 1:
            if band == 1:
                messagebox.showinfo('Mensaje', 'Estudiante encontrado con éxito') 
                self.habilitar_item()
                self.rellenar_item()
            else:
                messagebox.showinfo('Mensaje', 'Estudiante no registrado')
    
    def habilitar_item(self):
        self.actualizar_dni["state"] = "normal"
        self.actualizar_nombre["state"] = "normal"
        self.actualizar_apellidos["state"] = "normal"
        self.actualizar_ciclo["state"] = "normal"
        self.actualizar_carrera["state"] = "normal"
        self.actualizar_edad["state"] = "normal"
        self.actualizar_sexo_masculino["state"] = "normal"
        self.actualizar_sexo_femenino["state"] = "normal"
        self.actualizar_credito["state"] = "normal"

    def rellenar_item(self):
        query = "SELECT * FROM alumno where dni = ?"
        db_resultado = self.consulta(query, (self.dni_verificacion_actualizar.get(), ))
        for datos in db_resultado:
            self.actualizar_dni["textvariable"] = StringVar(value = datos[0])
            self.actualizar_nombre["textvariable"] = StringVar(value = datos[1])
            self.actualizar_apellidos["textvariable"] = StringVar(value = datos[2])
            self.actualizar_ciclo["textvariable"] = StringVar(value = datos[3])
            indice = self.actualizar_carrera['values'].index(datos[4]) 
            self.actualizar_carrera.current(indice)
            self.actualizar_edad["textvariable"] = StringVar(value = datos[5])
            if str(datos[6]) == "Masculino":
                self.actualizar_sexo_masculino.invoke()
            else:
                self.actualizar_sexo_femenino.invoke()
            self.actualizar_credito["textvariable"] = StringVar(value = datos[7])
             
    def validacion_actualizar_estudiante(self):
        return len(self.actualizar_nombre.get()) != 0 and len(self.actualizar_apellidos.get()) != 0 and len(self.actualizar_dni.get())  != 0 and len(self.actualizar_ciclo.get())  != 0 and len(self.actualizar_carrera.get())  != 0 and len(self.actualizar_edad.get())   != 0 and len( self.seleccion_actualizar_sexo.get())  != 0 
    
    def limpiar_actualizar_estudiante(self):
        self.actualizar_dni.delete(0, END)
        self.actualizar_nombre.delete(0, END)
        self.actualizar_apellidos.delete(0, END)
        self.actualizar_ciclo.delete(0, END)
        self.actualizar_carrera.delete(0, END)
        self.actualizar_edad.delete(0, END)	
        self.actualizar_credito.delete(0, END)
        self.dni_verificacion_actualizar.delete(0, END)
    
    def inhabilitar_item(self):
        self.actualizar_dni["state"] = "readonly"
        self.actualizar_nombre["state"] = "readonly"
        self.actualizar_apellidos["state"] = "readonly"
        self.actualizar_ciclo["state"] = "readonly"
        self.actualizar_carrera["state"] = "readonly"
        self.actualizar_edad["state"] = "readonly"
        self.actualizar_sexo_masculino["state"] = "disabled"
        self.actualizar_sexo_femenino["state"] = "disabled"
        self.actualizar_credito["state"] = "readonly"

    def actualizar_estudiante(self):
        if self.validacion_actualizar_estudiante():
            query = "UPDATE alumno SET dni = ?, nombre = ?, apellido = ?, ciclo = ?, carrera = ?, edad = ?, sexo = ?, credito = ? WHERE dni = ?"
            parametros = (self.actualizar_dni.get(),self.actualizar_nombre.get(),self.actualizar_apellidos.get(),self.actualizar_ciclo.get(),self.actualizar_carrera.get(),self.actualizar_edad.get(),self.seleccion_actualizar_sexo.get(),self.actualizar_credito.get(),self.dni_verificacion_actualizar.get())
            self.consulta(query,parametros)
            messagebox.showinfo('Mensaje', 'Estudiante actualizado con éxito')
            self.limpiar_actualizar_estudiante()
            self.inhabilitar_item()
            self.dni_verificacion_actualizar.focus()
        else:
            messagebox.showerror('ERROR', 'Rellene todos los campos')
        
if __name__ == "__main__":
    root = Tk()
    aplicacion = Bar_Universitario(root)
    root.mainloop()
