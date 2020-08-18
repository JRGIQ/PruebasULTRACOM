# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 07:23:52 2020

@author: Jheison René Gutiérrez Gómez. JRGIQ.
"""

import numpy as np
import sympy as sp

class ObjetoAlgebraico():
    
    print("\n"*100)
    
    def __init__(self):
        
        self.__valores=[]          
        
    def __suma(self):
              
        print("_________________________________________________")
        print("### MÓDULO DE SUMA ###")
        print("_________________________________________________")
        print("***PARA SUMAR LOS NÚMEROS MARQUE CERO {0}***.")
        print("***PARA SUMAR LOS NÚMEROS MARQUE CERO {0}***.")
        print("***PARA SUMAR LOS NÚMEROS MARQUE CERO {0}***.")
        print("_________________________________________________")
        n=0    
        
        while n>=0:
             
            self.numero=float(input("Digite los valores que se desean sumar = "))
            print("\n"*100)
            self.Ingresar=str(input(" *** Desea ingresar otro valor *** \n \n Si/s - No/n = "))
            print("\n"*100)
            self.__valores.append(self.numero) 
            n=n+1
                        
            if self.Ingresar=="n":
                
                print("_________________________________________________")
                print("###### MÓDULO SUMA ######")
                print("_________________________________________________") 
                print("Valores ingresados = ",self.__valores)
                print("-------------------------------------------------")
                self.suma=sum(self.__valores)
                print("SUMA = ",self.suma)
                print("_________________________________________________")
                break
        
        
    def __resta(self):
        
        print("_________________________________________________")
        print("### MÓDULO DE RESTA ###")
        print("_________________________________________________")
        print("***PARA RESTAR LOS NÚMEROS MARQUE CERO {0}***.")
        print("***PARA RESTAR LOS NÚMEROS MARQUE CERO {0}***.")
        print("***PARA RESTAR LOS NÚMEROS MARQUE CERO {0}***.")
        print("-------------------------------------------------")
        n=0
        
        while n>=0:
             
            self.numero=float(input("Digite los valores que se desean restar = "))
            print("\n"*100)
            self.__valores.append(self.numero) 
            self.Ingresar=str(input(" *** Desea ingresar otro valor *** \n \n Si/s - No/n = "))
            print("\n"*100) 
            n=n+1
                         
            if self.Ingresar=="n":
               
                print("_________________________________________________")
                print(" ###### MÓDULO DE RESTA ###### ")
                print("_________________________________________________")
                print("Valores ingresados = ",self.__valores)
                print("-------------------------------------------------")              
                self.resta=self.__valores[0]-(sum(self.__valores[1:]))
                print("RESTA = ",self.resta)
                print("_________________________________________________")     
                break
           
            
    def __Mult_Poli(self):
        
        x,y,z,w = sp.symbols('x,y,z,w')            
        print("_________________________________________________")
        print(" ###### MÓDULO PARA MULTIPLICAR POLINOMIOS ####### \n \n Ejemplo: 2x³+4x²+5y²+y = 2*x**3+4*x**2+5y**2+y")        
        print("_________________________________________________")
        self.Poly1=(input("Ingrese  f(x,y,z,w) = "))
        print("-------------------------------------------------")
        self.Poly2=(input("Ingrese  g(x,y,z,w) = ")) 
        print("\n"*100)
        print("_________________________________________________")
        self.P1=sp.Poly(self.Poly1)
        self.P2=sp.Poly(self.Poly2)
        self.Mult=self.P1*self.P2
        print("_________________________________________________")
        print(" ###### MÓDULO PARA MULTIPLICAR POLINOMIOS ####### ") 
        print("-------------------------------------------------")
        print(" f(x,y,z,w) = ",self.Poly1)
        print("-------------------------------------------------")
        print(" g(x,y,z,w) = ", self.Poly2)
        print("-------------------------------------------------")        
        print(" f x g = ", self.Mult)  
        print("_________________________________________________")


    def __Mult_Poli_Escalar(self):
        
        x,y,z,w = sp.symbols('x,y,z,w')                        
        print("_________________________________________________")
        print(" ### MÓDULO PARA MULTIPLICAR POLINOMIOS POR UN ESCALAR ### \n \n Ejemplo: 2x³+4x²+5y²+y = 2*x**3+4*x**2+5y**2+y")        
        print("_________________________________________________")
        self.Poly1=(input("Ingrese  f(x,y,z,w) = ")) 
        print("_________________________________________________")
        self.escalar=float(input("Ingrese el escalar = ")) 
        print("\n"*100)
        print("_________________________________________________")        
        self.P1=sp.Poly(self.Poly1)
        self.Mult=self.P1*self.escalar           
        print("_________________________________________________")
        print(" ### MÓDULO PARA MULTIPLICAR POLINOMIOS POR UN ESCALAR ### ") 
        print("-------------------------------------------------")
        print(" f(x,y,z,w) = ",self.Poly1 ,"\n Escalar = ", self.escalar)
        print("-------------------------------------------------")        
        print(" f x (escalar) = ", self.Mult)  
        print("_________________________________________________")

        
    def f_eval(self):
        
        print("_________________________________________________")
        print(" ### MÓDULO PARA EVALUAR POLINOMIOS ### \n \n Ejemplo f(x): 2x³+4x²+x+1 = 2*x**3+4*x**2+x+1 ")
        print("_________________________________________________")
        self.Poly1=input("ingrese el polinomio f(x) = ")
        print("-------------------------------------------------")        
        self.z=[]
        n=0
        
        while n>=0:
             
            self.xi=float(input("Ingrese el/los valores de 'x' a evaluar = "))
            print("\n"*100)
            self.z.append(self.xi) 
            x=np.array(self.z) 
            self.Ingresar=str(input(" *** Desea ingresar otro valor *** \n \n Si/s - No/n = ")) 
            print("\n"*100) 
            n=n+1
            
            if self.Ingresar=="n":
                
                print("\n"*100)
                print("_________________________________________________")
                print(" ### MÓDULO PARA EVALUAR POLINOMIOS ### ")
                print("_________________________________________________") 
                print("f(x) = ", self.Poly1)
                print("-------------------------------------------------")
                print("Valores de 'x' = " , x) 
                print("-------------------------------------------------")
                self.y=eval(self.Poly1)
                print("Resultado f(xi) = " , self.y)
                print("_________________________________________________")      
                break              
                       
        
    def MENU(self):
        
        print("_________________________________________________")
        print("####### MENU ####### :\n \n - Sumar números = '0' \n \n - Restar números = '1' \n \n - Multiplicar polinomios = '2' \n \n - Multiplicar polinomio por un escalar = '3' \n \n - Evaluar un polinomio = '4'  ")
        print("_________________________________________________")
        self.Operacion=int(input(" *** Elija la operación requerida *** : "))
        print("_________________________________________________")   
        print("\n"*1000)
        
        if self.Operacion==0:
            
            suma1=ObjetoAlgebraico()
            suma1.__suma()
            
        elif self.Operacion==1:
            
            resta1=ObjetoAlgebraico()
            resta1.__resta()
            
        elif self.Operacion==2:
            
            resta1=ObjetoAlgebraico()
            resta1.__Mult_Poli()  
            
        elif self.Operacion==3:
        
            escalar1=ObjetoAlgebraico()
            escalar1.__Mult_Poli_Escalar()
            
        elif self.Operacion==4:
        
            feval=ObjetoAlgebraico()
            feval.f_eval()
            
        else:
            
            print("_________________________________________________")
            print("***NO SE INGRESO UNA OPCIÓN VALIDA****")
            print("***NO SE INGRESO UNA OPCIÓN VALIDA****")
            print("***NO SE INGRESO UNA OPCIÓN VALIDA****")
            print("***NO SE INGRESO UNA OPCIÓN VALIDA****")
            
            retorno=ObjetoAlgebraico()
            retorno.MENU()
            
            
            
operacion1=ObjetoAlgebraico()
operacion1.MENU()        
        
            






            
         
            
            
            
            
            
        
        
        
        