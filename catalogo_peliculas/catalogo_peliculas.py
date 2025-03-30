#Usando Tkinter
import tkinter as tk 
from client.gui_app import Frame, barra_menu
def main():#Video 95
    root = tk.Tk();#Esto es una clase que genera la interfaz
    root.title("Catalogo de Películas David")
    root.iconbitmap('img/cp-logo.ico')
    #root.iconbitmap('catalogo_peliculas/img/cp-logo.ico')
    root.resizable(0,0)#Maximizar se quita
    barra_menu(root)
    app = Frame(root = root)
    
    app.mainloop()#para que no se cierre la pantalla

if __name__ == '__main__':
    main()