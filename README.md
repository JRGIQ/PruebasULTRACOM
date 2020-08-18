# PruebasULTRACOM

MANUAL DE FUNCIONAMIENTO

#_______________________________________________________________________________________________________________________________________________________________________________#
* CLASE : Ajedrez.py

Este código simula los movimientos de cada una de las piezas de un ajedrez. 

SUPOSICIONES:

* El peón es la única pieza que no se puede mover libremente, ya que esta solo posee movimientos hacia adelante y dependiendo del color su movimiento puede ser de arriba hacia abajo del tableo o viceversa.
Por lo tanto, se supondrá que la pieza puede moverse hacia adelante y hacia atrás.

FUNCIONAMIENTO:

1-) Al ejecutar el código, este pedirá ingresar el nombre de la pieza en minúsculas.
Posteriormente se podrá escoger la posición de la pieza en el tablero, para esto se tienen dos opciones: Marcar el número cero {0} para escoger una posicion manual o {1} para que se genere automáticamente de una manera aleatoria.
___________________________________________

Ingrese el nombre de la pieza en minúsculas 
 [peon,torre,alfil 
 caballo,rey,reina] : reina
--------------------------------------------

Ingrese {0} para generar una posición manual o {1} para generarla automaticamente de manera aleatoria : 

--------------------------------------------------------------------------------------------------------

2-) Al realizar las acciones mencionadas anteriormente, el programa mostrara una matriz que simula las posiciones del tablero de ajedrez mostrando la posición de la pieza de la siguiente manera
Representada con el número ocho {8}, las posiciones que puede realizar la pieza con el número uno {1}, y las posiciones que la pieza no puede realizar representadas por cero {0}.

___________________________________________
TABLERO DE AJEDREZ
___________________________________________
PIEZA : reina 
 *Posición en el tablero = Fila: 4 ,Columna: 2 
 *Posición de la pieza (8). 
 *Posibles movimientos (1). 
 *Movimientos no posibles (0).
___________________________________________
[[0 1 0 0 1 0 0 0]
 [0 1 0 1 0 0 0 0]
 [1 1 1 0 0 0 0 0]
 [1 8 1 1 1 1 1 1]
 [1 1 1 0 0 0 0 0]
 [0 1 0 1 0 0 0 0]
 [0 1 0 0 1 0 0 0]
 [0 1 0 0 0 1 0 0]]

#______________________________________________________________________________________________________________________________________________________________________________#
#_______________________________________________________________________________________________________________________________________________________________________________#
* CLASE : Objeto_Algebraico.py

Este código realiza algunas funciones matemáticas como: 

- Suma y resta de números enteros, decimales, racionales e irracionales.
- Multiplicación de dos polinomios, estos pueden tener hasta cuatro variables f(x,y,z,w).
- Multiplicación de un polinomio f(x,y,z,w) por un escalar (n).
- Evaluación de un polinomio f(x) en "n" valores para la variable (x).

FUNCIONAMIENTO:

1-) Al ejecutar el código, este ingresara al siguiente menu de selección. 
_________________________________________________
####### MENU ####### :
 
 - Sumar números = '0' 
 
 - Restar números = '1' 
 
 - Multiplicar polinomios = '2' 
 
 - Multiplicar polinomio por un escalar = '3' 
 
 - Evaluar un polinomio = '4'  
_________________________________________________

 *** Elija la operación requerida *** : 
 
 2-) Una vez seleccionada la opción requerida, se ingresa a un menu para cada operación. 
 En caso de no seleccionar una opción del menu, este informara con un mensaje "NO SELECCIONASTE UNA OPCION VALIDA" y volverá a pedir un ingreso.
 
 2.1-) Opción cero {0}: SUMA
 _________________________________________________
### MÓDULO DE SUMA ###
_________________________________________________
***PARA SUMAR LOS NÚMEROS MARQUE CERO {0}***.
***PARA SUMAR LOS NÚMEROS MARQUE CERO {0}***.
***PARA SUMAR LOS NÚMEROS MARQUE CERO {0}***.
_________________________________________________

Digite los valores que se desean sumar = 

- El programa pedirá los números que se desean sumar, cada vez que se ingresa un número el programa preguntará si se quiere ingresar otro.
- En caso de querer ingresar otro número, se debe digitar la letra "s", en caso contrario se digitará la letra "n" y se hará la suma de los números ingresados.

2.2) Opción uno {1}: RESTA

- Esta opción se ejecuta exactamente igual a la OPCION SUMA, con la diferencia que en esta se ingresa el primer número y se le restan los números que se ingresen después.

2.3-) Opción dos {2} : MULTIPICAR POLINOMIOS.

- Una vez se escoja esta opción, se abrirá el siguiente menu:

_________________________________________________
 ###### MÓDULO PARA MULTIPLICAR POLINOMIOS ####### 
 
 Ejemplo: 2x³+4x²+5y²+y = 2*x**3+4*x**2+5y**2+y
_________________________________________________

Ingrese  f(x,y,z,w) = 

- En la casilla "Ingrese f(x,y,z,w), se digitará el primer polinomio de acuerdo al ejemplo dado, se pulsa enter y el programa pedirá el segundo polinomio, se pulsa enter y se mostrara la multiplicación de los polinomios seguido por las variables utilizadas y el dominio de la función.
El resultado se muestra de la siguiente manera:

_________________________________________________
_________________________________________________
 ###### MÓDULO PARA MULTIPLICAR POLINOMIOS ####### 
--------------------------------------------------
 f(x,y,z,w) =  x+y+z+w
--------------------------------------------------
 g(x,y,z,w) =  x+y+z+w
------------------------------------------------------------------------------------------------------------------
 f x g =  Poly(x**2 + 2*x*y + 2*x*z + 2*x*w + y**2 + 2*y*z + 2*y*w + z**2 + 2*z*w + w**2, x, y, z, w, domain='ZZ')
__________________________________________________________________________________________________________________


2.4-) Opcion tres {3} : MULTIPLICACIÓN DE UN POLINOMIO POR UN ESCALAR.

- Una vez se ejecuta este código, al igual que el anterior para multiplicar polinomios, este pedirá primero que se ingrese el polinomio y después que se ingrese el escalar.
- Los resultados se mostrarán en pantalla exactamente igual a la opción {2}, multiplicación de polinomios dada anteriormente.

2.5-) Opción cuatro {4} : EVALUAR UN POLINOMIO.

- Al ejecutar esta opción, el programa pedirá primero ingresar el polinomio en función de la variable "x" de la siguiente manera:
_________________________________________________
 ### MÓDULO PARA EVALUAR POLINOMIOS ### 
 
 Ejemplo f(x): 2x³+4x²+x+1 = 2*x**3+4*x**2+x+1 
_________________________________________________

ingrese el polinomio f(x) = 

- En la opcion Ingrese el polinomio f(x), se pondrá el polinomio que se desea evaluar. Al pulsar ENTER, este pedirá ahora que se ingresen los valores de "x" a evaluar.
En caso de querer otro valor, el programa preguntará si se desea o no de la siguiente manera. 

 *** Desea ingresar otro valor *** 
 
 Si/s - No/n = 
 
 - En caso de querer ingresar otro valor, basta con digitar la letra "s", en caso de no querer digitar la letra "n" y automáticamente se evaluarán los valores ingresados.
 - Los resultados se mostrarán en pantalla de la siguiente manera.
 _________________________________________________
 ### MÓDULO PARA EVALUAR POLINOMIOS ### 
_________________________________________________
f(x) =  2*x**2+x+1
-------------------------------------------------
Valores de 'x' =  [1. 2. 3. 4.]
-------------------------------------------------
Resultado f(xi) =  [ 4. 11. 22. 37.]
_________________________________________________





 
 


