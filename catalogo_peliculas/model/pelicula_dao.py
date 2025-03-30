from .conexion_db import ConexionDB 
from tkinter import messagebox
def crear_tabla():
    conexion = ConexionDB()#conexta
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER, 
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''
    
    try:
        conexion.cursor.execute(sql)#crea la tabla peliculas
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creó la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya está creada'
        messagebox.showwarning(titulo, mensaje)
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql ='DROP TABLE peliculas'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borró con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No existe la tabla para borrar'
        messagebox.showerror(titulo, mensaje)   
    
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None#instanciandolo como null directamente si no se pone
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'
    
def guardar(pelicula):
    conexion = ConexionDB()
    sql= f"""INSERT INTO peliculas (nombre, duracion, genero)VALUES('{pelicula.nombre}','{pelicula.duracion}','{pelicula.genero}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar() #deespues de insertar, cierra la conexion
        
    except:
        titulo = 'Conexión al Registro'
        mensaje = 'La tabla peliculas no está creada en la base de datos'
        messagebox.showerror(titulo, mensaje)
    
def listar():
    conexion = ConexionDB()
    lista_peliculas = [] #lista vacia
    sql ='SELECT * FROM PELICULAS'
    
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall() #fetchall() recupera toda la informacion
        conexion.cerrar()
    except:
        titulo = 'Conexión al Registro'
        mensaje = 'Primero debes crear la tabla en la Base de datos'
        messagebox.showerror(titulo, mensaje)
        
    return lista_peliculas #retornamos la lista

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}' 
    WHERE id_pelicula = {id_pelicula}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        titulo = 'Edición de datos'
        mensaje = 'No se a podido editar este registro'
        messagebox.showerror(titulo, f"""{mensaje}. ERROR {e}""")
        
        
def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)