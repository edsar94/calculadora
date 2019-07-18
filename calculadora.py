from tkinter import * #tener en cuenta que en pyton 3 comienza en minuscula


class Calculadora():
    def __init__(self):
        self.num1=0
        self.num2=0
        self.rta=0
        self.operador=""
        
    def sumar(self):
        self.rta=self.num1+self.num2

    def res(self):
        self.rta=self.num1-self.num2

    def mul(self):
        self.rta=self.num1*self.num2

    def div(self):
        self.rta=self.num1/self.num2




class InterfazCalculadora():
    def mostrar(self,var1):
        self.ventana.set(self.ventana.get()+var1)

    def operar(self,var1):
        if var1 in ["+","-","*","/"]:
            self.calculadora.num1 = int(self.ventana.get())
            self.operador=var1
            self.ventana.set("")
        if var1 == "C":
            self.calculadora.num1 = 0
            self.calculadora.num2 = 0
            self.calculadora.rta = 0
            self.operador=var1
            self.ventana.set("")



        if var1 == "=":
            self.calculadora.num2 = int(self.ventana.get())
            if self.operador == "+":
                self.calculadora.sumar()
                
            if self.operador == "-":
                self.calculadora.res()

            if self.operador == "*":
                self.calculadora.mul()
                

            if self.operador == "/":
                self.calculadora.div()

            self.ventana.set(str(self.calculadora.rta))
                
       
            
      
    def __init__(self):
        self.root=Tk()
        self.frame=Frame(self.root)
        self.frame.pack()
        self.root.geometry('800x600')
        self.operador=""
        self.calculadora = Calculadora()
        
        self.frame = Frame(self.root)
        self.frame.configure(background="#3333ff")
        self.frame.pack()

        self.ventana = StringVar()
        self.display = Label(self.frame, textvariable = self.ventana,width=25,height=2, font=("Helvetica",15),justify = "left", bg = "#33ffff")
        self.display.grid(row=0, column= 0,columnspan=4)

        self.boton_uno=Button(self.frame, text=" 1 ", command=lambda:self.mostrar("1"), width=5, height=2)  #1
        self.boton_uno.grid(row=3,column=0)

        self.boton_dos=Button(self.frame, text=" 2 ", command=lambda:self.mostrar("2"), width=5, height=2 )  #2
        self.boton_dos.grid(row=3,column=1)

        self.boton_tres=Button(self.frame, text=" 3 ", command=lambda:self.mostrar("3"), width=5, height=2)  #3
        self.boton_tres.grid(row=3,column=2)

        self.boton_cuatro=Button(self.frame, text=" 4 ", command=lambda:self.mostrar("4"), width=5, height=2)  #4
        self.boton_cuatro.grid(row=2,column=0)

        self.boton_cinco=Button(self.frame, text=" 5 ", command=lambda:self.mostrar("5"), width=5, height=2)  #5
        self.boton_cinco.grid(row=2,column=1)

        self.boton_seis=Button(self.frame, text=" 6 ", command=lambda:self.mostrar("6"), width=5, height=2)  #6
        self.boton_seis.grid(row=2,column=2)

        self.boton_siete=Button(self.frame, text=" 7 ", command=lambda:self.mostrar("7"), width=5, height=2)  #7
        self.boton_siete.grid(row=1,column=0)

        self.boton_ocho=Button(self.frame, text=" 8 ", command=lambda:self.mostrar("8"), width=5, height=2)  #8
        self.boton_ocho.grid(row=1,column=1)

        self.boton_nueve=Button(self.frame, text=" 9 ", command=lambda:self.mostrar("9"), width=5, height=2)  #9
        self.boton_nueve.grid(row=1,column=2)

        self.boton_cero=Button(self.frame, text=" 0 ", command=lambda:self.mostrar("0"), width=5, height=2)  #0
        self.boton_cero.grid(row=4,column=1)

        self.boton_s=Button(self.frame, text=" + ", command=lambda:self.operar("+"), width=5, height=2)  #+
        self.boton_s.grid(row=4,column=3)

        self.boton_r=Button(self.frame, text=" - ", command=lambda:self.operar("-"), width=5, height=2)  #-
        self.boton_r.grid(row=3,column=3)

        self.boton_m=Button(self.frame, text=" * ", command=lambda:self.operar("*"), width=5, height=2)  #*
        self.boton_m.grid(row=2,column=3)

        self.boton_d=Button(self.frame, text=" / ", command=lambda:self.operar("/"), width=5, height=2)  #1
        self.boton_d.grid(row=1,column=3)

        self.boton_igual=Button(self.frame, text=" = ", command=lambda:self.operar("="), width=5, height=2)  #=
        self.boton_igual.grid(row=4,column=2)

        self.boton_borrar=Button(self.frame, text=" C ", command=lambda:self.operar("C"), width=5, height=2,bg= "#b30000" )  
        self.boton_borrar.grid(row=4,column=0)


        self.root.mainloop()


app = InterfazCalculadora()

        




        
