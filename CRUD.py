from tkinter import *
import sqlite3 as sq3
from tkinter import messagebox

# --------------------------
#       Funcionalidades
# --------------------------

# Menu

## Menu BBDD
def conectar():
    global con   # declarando a la variable con 'global' hago que la variable pueda ser usada en cualquier parte del código (fuera del for).
    global cur
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    messagebox.showinfo('Status', 'Conectado a la base de datos')  #Crea una ventana dando un mensaje

def salir():
  resp = messagebox.askquestion('Confirmar', '¿Desea salir del programa?')  #askquestion da la opcion en ventana de dar como respuesta un Sí o No (yes or not)
  if resp == 'yes':
    con.close()   # Se desconecta la base de datos
    raiz.destroy()  # Cierra el programa

def licencia():
  # Licencia sacado de CREATIVE COMMONS GNU GPL
  gnu = '''
  Demo de un sistema CRUD en Python para gestión de alumnos.

  Copyright (C) 2022 - Rodrigo Palpa

  Email: rodrigopalpa@economicas.uba.ar

  \n ===================================

  This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
  '''
  messagebox.showinfo('Status', gnu)


def acerca():
  messagebox.showinfo('Acerca de..', 'Creado por Rodrigo Palpa para Codo a Codo 4.0 - BigData')

# --------------------------
#       Funciones CRUD
# --------------------------

def buscar_escuela(actualiza):
  con = sq3.connect('mi_db.db')  # me conecto a la base datos
  cur = con.cursor()    # creo el cursor
  if actualiza == True:   #cuando prendo la aplicacion le voy a pasar que sea falso, entonces trae toda la info de la base de datos
    pass                  # la info lo pide del cursor y lo guarda en 'resultado'
  else:
    cur.execute('SELECT * FROM escuelas')

  resultado = cur.fetchall() # con fetchall entrega toda la informacion que quedó en el cursor
  #print(resultado)

# solo necesito los nombres de la escuela, entonces debo hacer una lista con solo los nombres a partir del cursor antes creado
  retorno = []
  for e in resultado:  #creo un bucle que llame cada escuela
    if actualiza == True:
      pass
    esc = e[1]   #creo la variable tomando el lugar 1
    retorno.append(esc)   #creo la lista completa agregando las escuelas
  
  con.close()
  return retorno

# ---------------------------
#      Intefaz gráfica
# ---------------------------

raiz = Tk() # creo la ventana principal
raiz.title('GUI - Com 22615') # Agrego título a la ventana

# El proceso de incluir objetos en el framework es 1. agregar, 2. otorgar propiedades y 3. activar

# --------- Barra Menu --------
barramenu = Menu(raiz) #Creo la barra menu como objeto Menu (es una clase)
raiz.config(menu = barramenu) # agrego menu a la ventana

# ---- OPcion BBDD en barra menu---
bbddmenu = Menu(barramenu, tearoff= 0)  #Crea la opción y le digo que este dentro de la barra menu
bbddmenu.add_command(label='Conectar', command=conectar)  # add_comand crea las opciones dentro de la pestaña
bbddmenu.add_command(label='Salir', command=salir)
barramenu.add_cascade(label='BBDD', menu=bbddmenu) # crea la opcion de apertura de opciones como cascada y le da el nombre a la pestaña,  a la vez que conectamos con la opcion

# ---------- OPcion limpiar en barra menu-----------

limpiarmenu = Menu(barramenu, tearoff= 0)
limpiarmenu.add_command(label='Limpiar campos')
barramenu.add_cascade(label='Limpiar', menu=limpiarmenu)

# ---------- OPcion Ayuda en barra menu-----------

ayudamenu = Menu(barramenu, tearoff= 0)
ayudamenu.add_command(label='Licencia', command=licencia)
barramenu.add_cascade(label='Ayuda', menu=ayudamenu)

# ---------  Frame Campos ---------------
framecampos = Frame(raiz)  # Crea el frame donde llena los campos
framecampos.pack()

## Declaramos las variables/ campos que se van a agregar

legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()  # variable numeros
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()


## Para visualizacipon de campos-----
legajo_input = Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=2, padx=10, pady=10)

legajo_label = Label(framecampos, text='Legajo:')
legajo_label.grid(row=0, column=1, padx=10, pady=10)
#----
alumno_input = Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=1, column=2, padx=10, pady=10)

alumno_label = Label(framecampos, text='Alumno:')
alumno_label.grid(row=1, column=1, padx=10, pady=10)
#----
email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=2, padx=10, pady=10)

email_label = Label(framecampos, text='Email:')
email_label.grid(row=2, column=1, padx=10, pady=10)
#----
calificacion_input = Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=3, column=2, padx=10, pady=10)

calificacion_label = Label(framecampos, text='Calificación:')
calificacion_label.grid(row=3, column=1, padx=10, pady=10)
#-----
escuelas = buscar_escuela(False)  #esta funcion me devuelve el listado de escuelas. acordarse que
                                 # en la seccion Funciones CRUD cree una funcion que me devolvia la lista de escuelas cuando deba de respuesta False.

#scuela_input = Entry(framecampos, textvariable=escuela)
#escuela_input.grid(row=4, column=2, padx=10, pady=10)
                                                              # famecampos: es donde voy a poner el listado
escuela_option = OptionMenu(framecampos, escuela, *escuelas)  # la info lo guardo en el frame 'escuela' y el listado de opciones lo tengo que sacar de 'escuelas' (la variable creada arriba)
escuela_option.grid(row=4, column=2, padx=10, pady=10)        # 'escuelas' lleva un asterisco para avisar a la funcion que NO sabemos cuantos parametros va a recibir esa variable
                                                              # 'escuelas' es el listado de las escuelas, pero no sabemos cuantas escuelas hay, por eso se agrega el asterisco
escuela_label = Label(framecampos, text='Escuela:')
escuela_label.grid(row=4, column=1, padx=10, pady=10)
#----
localidad_input = Entry(framecampos, textvariable=localidad, state='readonly') #state para ponerlo solo de lectura (no se puede modificar en nuestra aplicacion)
localidad_input.grid(row=5, column=2, padx=10, pady=10)

localidad_label = Label(framecampos, text='Localidad:')
localidad_label.grid(row=5, column=1, padx=10, pady=10)
#-----
provincia_input = Entry(framecampos, textvariable=provincia, state='readonly') #state para ponerlo solo de lectura (no se puede modificar en nuestra aplicacion)
provincia_input.grid(row=6, column=2, padx=10, pady=10)

provincia_label = Label(framecampos, text='Provincia:')
provincia_label.grid(row=6, column=1, padx=10, pady=10)


# -------------- FRAME BOTONES ----------------
# CRUD = Create, Read, Update, Delete

framebotones = Frame(raiz)
framebotones.pack()

boton_crear = Button(framebotones, text='Crear')
boton_crear.grid(row=0, column = 0, padx = 5, pady = 10)

boton_leer = Button(framebotones, text='Leer')
boton_leer.grid(row=0, column = 1, padx = 5, pady = 10)

boton_actualizar = Button(framebotones, text='Actualizar')
boton_actualizar.grid(row=0, column = 2, padx = 5, pady = 10)

boton_borrar = Button(framebotones, text='Borrar')
boton_borrar.grid(row=0, column = 3, padx = 5, pady = 10)


# ------------ FRAME COPY -------------------
framecopy = Frame(raiz)
framecopy.pack()

copy_label = Label(framecopy, text = '2022 | Por Rodrigo Palpa para Codo a Codo - Big Data')
copy_label.grid(row=0, column = 0, padx=10, pady=10)


print(buscar_escuela(False))

# ------- Abre la ventana -------------
raiz.mainloop() #mantiene la ventana siempre abierta. Este código debe estar al final del código para que lea los códigos anteriores