from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as anm

class ventana(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.V = 0.01
        self.F = 0.01
        self.widget()
        
    def lienzo(self):
        self.fig = plt.figure() #Crea la figura
        self.ax = self.fig.add_subplot(111,xlim=(0,5000),ylim=(-1,1)) #Configura los ejes de la figura
        self.pegamento = FigureCanvasTkAgg(self.fig,self.master) #Sirve para pegar la figura en la ventana
        self.pegamento.get_tk_widget().pack() #Sirve para pegar la figura en la ventana
        self.t = np.arange(0,5,0.001) #arreglo para graficar
        self.line, = self.ax.plot(self.f(self.t))#crear la grafica estatica y le enviamos el arreglo 
        self.ani = anm.FuncAnimation(fig=self.fig,func=self.update_valor,interval=20)

    def update_valor(self,i):
        self.line.set_ydata(self.f(self.t*i))
        return self.line,

    def Graficar(self):
        self.V = float(self.vel.get()) #Obtiene el valor del Entry de la ventana de str a float
        self.F = float(self.frec.get()) #Obtiene el valor del Entry de la ventana de str a float

    def f(self,x): #Función
        y = 2*np.exp(-self.V*x)*np.sin(self.F*x)
        return y

    def menu_ventana(self):
        Button(self.master,text='Salir',command=self.Salir).pack(side='left')
        Button(self.master,text='Graficar',command=self.Graficar).pack()
        self.vel = Entry(self.master,width=12)
        self.vel.pack()
        self.frec = Entry(self.master,width=12)
        self.frec.pack()
        self.vel.insert(0,'0.01')
        self.frec.insert(0,'0.01')
    
    def Salir(self):
        self.master.destroy() #Para salir destruye

    def widget(self):
        self.menu_ventana() #Crea los botones
        self.lienzo() #Crea el lienzo para graficar
        self.master.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600') 
    root.title('Gráfica')
    app = ventana(root)