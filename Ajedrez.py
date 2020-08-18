# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:42:09 2020

@author: Jheison René Gutiérrez Gómez. JRGIQ.
"""

import numpy as np
import random


Tablero=np.zeros([8,8],dtype=int)

print("___________________________________________")
ficha=str(input("Ingrese el nombre de la pieza en minúsculas \n [peon,torre,alfil \n caballo,rey,reina] : "))
print("--------------------------------------------")     
automatico=int(input("Ingrese {0} para generar una posición manual o {1} para generarla automaticamente de manera aleatoria : "))

if automatico==1:  
      
    posicioni=random.randint(0,7)
    posicionj=random.randint(0,7)

if automatico==0:
    print("--------------------------------------------")     
    print("MODO MANUAL")
    print("--------------------------------------------")     
    posicioni=int(input("Ingrese la posición del la fila [0-7] \n Fila :"))
    print("--------------------------------------------")     
    posicionj=int(input("Ingrese la posición del la columna [0-7] \n Columna :"))
#--------------------------------------------------------------------------------------------------------             
Tablero[posicioni,posicionj]=8    
#--------------------------------------------------------------------------------------------------------             
if ficha=="peon" and Tablero[posicioni,posicionj]==Tablero[0,posicionj]==8:
    Tablero[1,posicionj]=1
    
elif ficha=="peon" and Tablero[posicioni,posicionj]==8:
    Tablero[posicioni-1:posicioni+2,posicionj]=1        
    Tablero[posicioni,posicionj]=8    
##--------------------------------------------------------------------------------------------------------                 
if ficha=="torre" and Tablero[posicioni,posicionj]==8:          
    Tablero[0:8,posicionj]=1
    Tablero[posicioni,0:8]=1
    Tablero[posicioni,posicionj]=8
##---------------------------------------------------------------------------------------------------------    
if ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[0,0]==8:
    Tablero[2,1]=1
    Tablero[1,2]=1

elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[7,7]==8:
    Tablero[5,6]=1
    Tablero[6,5]=1

elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[0,7]==8:
    Tablero[1,5]=1
    Tablero[2,6]=1

elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[7,0]==8:
    Tablero[5,1]=1
    Tablero[6,2]=1

elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[0,1]==8:
    Tablero[2,0]=1
    Tablero[2,2]=1
    Tablero[1,3]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[1,0]==8:
    Tablero[0,2]=1
    Tablero[2,2]=1
    Tablero[3,1]=1

elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[0,6]==8:
    Tablero[1,4]=1
    Tablero[2,5]=1
    Tablero[2,7]=1

elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[6,0]==8:
    Tablero[4,1]=1
    Tablero[5,2]=1
    Tablero[7,2]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[1,7]==8:
    Tablero[0,5]=1
    Tablero[2,5]=1
    Tablero[3,6]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[7,1]==8:
    Tablero[5,0]=1
    Tablero[5,2]=1
    Tablero[6,3]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[6,7]==8:
    Tablero[4,6]=1
    Tablero[5,5]=1
    Tablero[7,5]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[7,6]==8:
    Tablero[6,4]=1
    Tablero[5,5]=1
    Tablero[5,7]=1

elif ficha=="caballo" and 8 in Tablero[0,2:6]:
    Tablero[posicioni+2,posicionj+1]=1
    Tablero[posicioni+2,posicionj-1]=1
    Tablero[posicioni+1,posicionj+2]=1
    Tablero[posicioni+1,posicionj-2]=1

elif ficha=="caballo" and 8 in Tablero[7,2:6]:
    Tablero[posicioni-2,posicionj+1]=1
    Tablero[posicioni-2,posicionj-1]=1
    Tablero[posicioni-1,posicionj+2]=1
    Tablero[posicioni-1,posicionj-2]=1   
    
elif ficha=="caballo" and 8 in Tablero[2:6,0]:
    Tablero[posicioni+1,posicionj+2]=1
    Tablero[posicioni-1,posicionj+2]=1
    Tablero[posicioni+2,posicionj+1]=1
    Tablero[posicioni-2,posicionj+1]=1 
    
elif ficha=="caballo" and 8 in Tablero[2:6,7]:
    Tablero[posicioni+1,posicionj-2]=1
    Tablero[posicioni-1,posicionj-2]=1
    Tablero[posicioni+2,posicionj-1]=1
    Tablero[posicioni-2,posicionj-1]=1 
    
elif ficha=="caballo" and 8 in Tablero[2:6,1]:    
    Tablero[posicioni+2,posicionj+1]=1
    Tablero[posicioni+2,posicionj-1]=1
    Tablero[posicioni-2,posicionj+1]=1
    Tablero[posicioni-2,posicionj-1]=1
    Tablero[posicioni-1,posicionj+2]=1
    Tablero[posicioni+1,posicionj+2]=1

elif ficha=="caballo" and 8 in Tablero[2:6,6]:    
    Tablero[posicioni-2,posicionj+1]=1
    Tablero[posicioni-2,posicionj-1]=1
    Tablero[posicioni+2,posicionj+1]=1
    Tablero[posicioni+2,posicionj-1]=1       
    Tablero[posicioni+1,posicionj-2]=1
    Tablero[posicioni-1,posicionj-2]=1  
        
elif ficha=="caballo" and 8 in Tablero[1,2:6]:    
    Tablero[posicioni+1,posicionj+2]=1
    Tablero[posicioni-1,posicionj+2]=1
    Tablero[posicioni+1,posicionj-2]=1
    Tablero[posicioni-1,posicionj-2]=1       
    Tablero[posicioni+2,posicionj-1]=1
    Tablero[posicioni+2,posicionj+1]=1 
    
elif ficha=="caballo" and 8 in Tablero[6,2:6]:
    
    Tablero[posicioni+1,posicionj+2]=1
    Tablero[posicioni-1,posicionj+2]=1
    Tablero[posicioni+1,posicionj-2]=1
    Tablero[posicioni-1,posicionj-2]=1       
    Tablero[posicioni-2,posicionj-1]=1
    Tablero[posicioni-2,posicionj+1]=1 
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[1,1]==8:    
    Tablero[posicioni+2,posicionj+1]=1
    Tablero[posicioni+2,posicionj-1]=1    
    Tablero[posicioni+1,posicionj+2]=1
    Tablero[posicioni-1,posicionj+2]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[6,6]==8:    
    Tablero[posicioni-2,posicionj+1]=1
    Tablero[posicioni-2,posicionj-1]=1    
    Tablero[posicioni+1,posicionj-2]=1
    Tablero[posicioni-1,posicionj-2]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[1,6]==8:    
    Tablero[posicioni+2,posicionj+1]=1
    Tablero[posicioni+2,posicionj-1]=1    
    Tablero[posicioni+1,posicionj-2]=1
    Tablero[posicioni-1,posicionj-2]=1
    
elif ficha=="caballo" and Tablero[posicioni,posicionj]==Tablero[6,1]==8:    
    Tablero[posicioni-2,posicionj+1]=1
    Tablero[posicioni-2,posicionj-1]=1    
    Tablero[posicioni+1,posicionj+2]=1
    Tablero[posicioni-1,posicionj+2]=1
 
elif ficha=="caballo" and Tablero[posicioni,posicionj]==8:            
    Tablero[posicioni-2,posicionj-1]=1
    Tablero[posicioni-2,posicionj+1]=1        
    Tablero[posicioni-1,posicionj-2]=1
    Tablero[posicioni-1,posicionj+2]=1            
    Tablero[posicioni+1,posicionj-2]=1
    Tablero[posicioni+1,posicionj+2]=1        
    Tablero[posicioni+2,posicionj-1]=1
    Tablero[posicioni+2,posicionj+1]=1            
#--------------------------------------------------------------------------------------------------------             
n=1
while ficha=="alfil" and Tablero[posicioni,posicionj]==8:    
    if posicioni+n>7:        
        break
    
    elif posicionj+n>7:        
        break

    Tablero[posicioni+n,posicionj+n]=1           
    n=n+1

n=1    
while ficha=="alfil" and Tablero[posicioni,posicionj]==8:        
    if posicioni-n<0:        
        break
                
    elif posicionj-n<0:        
        break
            
    Tablero[posicioni-n,posicionj-n]=1           
    n=n+1
    
n=1    
while ficha=="alfil" and Tablero[posicioni,posicionj]==8:        
    if posicioni+n>7:        
        break
                
    elif posicionj-n<0:        
        break
            
    Tablero[posicioni+n,posicionj-n]=1           
    n=n+1
    
n=1    
while ficha=="alfil" and Tablero[posicioni,posicionj]==8:    
    if posicioni-n<0:        
        break
                
    elif posicionj+n>7:        
        break
            
    Tablero[posicioni-n,posicionj+n]=1           
    n=n+1    
##---------------------------------------------------------------------------------------------------------    
if ficha=="reina" and Tablero[posicioni,posicionj]==8:    
    Tablero[0:8,posicionj]=1    
    Tablero[posicioni,0:8]=1    
    Tablero[posicioni,posicionj]=8        

n=1
while ficha=="reina" and Tablero[posicioni,posicionj]==8:    
    if posicioni+n>7:        
        break
    
    elif posicionj+n>7:        
        break
    
    Tablero[posicioni+n,posicionj+n]=1           
    n=n+1

n=1    
while ficha=="reina" and Tablero[posicioni,posicionj]==8:    
    if posicioni-n<0:        
        break
    
    elif posicionj-n<0:    
        break
            
    Tablero[posicioni-n,posicionj-n]=1           
    n=n+1
    
n=1    
while ficha=="reina" and Tablero[posicioni,posicionj]==8:    
    if posicioni+n>7:        
        break
                
    elif posicionj-n<0:        
        break
            
    Tablero[posicioni+n,posicionj-n]=1           
    n=n+1
    
n=1    
while ficha=="reina" and Tablero[posicioni,posicionj]==8:    
    if posicioni-n<0:        
        break
                
    elif posicionj+n>7:        
        break
            
    Tablero[posicioni-n,posicionj+n]=1           
    n=n+1    
##---------------------------------------------------------------------------------------------------------    
if ficha=="rey" and Tablero[0,posicionj]==8:    
    Tablero[posicioni+1,posicionj]=1
    
if ficha=="rey" and Tablero[posicioni,0]==8:    
    Tablero[posicioni,posicionj+1]=1
        
if ficha=="rey" and Tablero[posicioni,posicionj]==8:         
    Tablero[posicioni-1:posicioni+2,posicionj]=1
    Tablero[posicioni,posicionj-1:posicionj+2]=1
    Tablero[posicioni,posicionj]=8
    
n=1
while ficha=="rey" and Tablero[posicioni,posicionj]==8:
    if posicioni+n>7:    
        break

    elif posicionj+n>7:        
        break
    
    Tablero[posicioni+1,posicionj+1]=1           
    n=n+1

n=1    
while ficha=="rey" and Tablero[posicioni,posicionj]==8:    
    if posicioni-n<0:        
        break
    
    elif posicionj-n<0:        
        break
            
    Tablero[posicioni-1,posicionj-1]=1           
    n=n+1
    
n=1    
while ficha=="rey" and Tablero[posicioni,posicionj]==8:    
    if posicioni+n>7:        
        break
                
    elif posicionj-n<0:        
        break
            
    Tablero[posicioni+1,posicionj-1]=1           
    n=n+1
    
n=1    
while ficha=="rey" and Tablero[posicioni,posicionj]==8:    
    if posicioni-n<0:        
        break
    
    elif posicionj+n>7:        
        break
    
    Tablero[posicioni-1,posicionj+1]=1           
    n=n+1
##---------------------------------------------------------------------------------------------------------    
if ficha in ["peon","torre","alfil","caballo","rey","reina"]:
     
    
    print("\n"*100)
    print("___________________________________________")
    print("TABLERO DE AJEDREZ")
    print("___________________________________________")
    print("PIEZA :",ficha, "\n *Posición en el tablero =","Fila:",posicioni+1,",Columna:",posicionj+1,"\n *Posición de la pieza (8). \n *Posibles movimientos (1). \n *Movimientos no posibles (0).")
    print("___________________________________________")
    print(Tablero)     
    
else:
    print("--------------------------------------------")    
    print("**NO SE INGRESÓ UNA PIEZA VALIDA**")
    print("--------------------------------------------")    





