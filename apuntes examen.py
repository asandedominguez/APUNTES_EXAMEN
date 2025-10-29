#Valor abosluto de un número:
n = float(input("Dame un nº: "))
valor = n if n >= 0 else -n
print("El valor absoluto es:", valor)

#Pasar el numero de una lista a letras (Ej: 59=cincuenta y nueva)
#En vez de usar "elif" se podría usar if, útil para evitar confusiones en otros ejerdcicios
n = int(input("Dime un número entre 1 y 99:"))
p = ["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
s = ["","once","doce","trece","catorce","quize","dieciseis","diecisiete","dieciocho","dicinueve"]
f = ["","","veinte","trenta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
if n > 0 and n < 11:
    print(p[n])
elif n >= 11 and n < 20:
    r = n-10
    print(s[r])
elif n >=20 and n < 100:
    r1 =  n//10
    r2 = n%10
    print(f[r1], "y", p[r2])

#DNI predicción
l = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
DNI = int(input("Dime los dígitos de tu DNI"))
let = DNI%23
print("Tu DNI es", DNI,l[let])

#Imprimir valores entre 2 números
i = 10
while i <=20:
    print(i)
    i+=1
#ALTERNATIVA:
n = int(input("Dame un numero: "))
l = int(input("Dame un límite: "))
for i in range (n,l+1):
    print(i)

#De Farenheit a celsius:
v = int(input("Dame la temperatura en Ferenheit:"))
t = 5/9 * (v - 32)
print("La temperatura en Celsius es:", t,"º")
#TABLA:
i = 0
for i in range (0,121,10):
    v = 5/9 * (i-32)
    print("Grados Farenheit:", i, "|" "Grados celisus:", v)
#Si se necesita hacer una cuenta la variable siempre tendra que tener un valor

#NUMEROS PARES entre 2 numeros:
n1 = int(input("Dame el 1º número: "))
n2 = int(input("Dame el 2º número: "))
if n1 > n2:
    for i in range (n2,n1+1):
        if i % 2==0:
            print(i)
elif n2 > n1:
    for i in range (n1,n2+1):
        if i % 2==0:
            print(i)

#NUMEROS TRIANGULARES:
n = int(input("Dime un número: "))
r = int(input("Dime el rango: "))
for i in range (1,r +1):
    rest = i * (i+1)//2
    print(i, "-", rest)

#FACTORIAL:
n = int(input("Cuantos número quieres: "))
for i in range (1,n+1):
    p = int(input("Dame el número: "))
    fact = 1
    for r in range (fact, p+1):
        fact = fact*r
        print(fact)

#Lineas de domino SIN REPETIR
n = int(input("Cuantos número quieres?: "))
for i in range (0,n+1):
    for r in range (i, n+1):
        i = i+0
        print(i,"-",r)

#Calcular CANTIDAD de numeros positivos, negativos y ceros que hay en un grupo de 10 números:
ceros = 0
positivo = 0
negativo = 0
for i in range (10):
    num = int(input("Dame 10 números: "))
    if num == 0:
        ceros = ceros + 1
    elif num >= 1:
        positivo = positivo + 1
    elif num <= -1:
        negativo = negativo+ 1
print("As introducido", ceros, "ceros")
print("As introducido", positivo, "números positivos")
print("As introducido", negativo, "números negatvos")

#Area de un triangulo VALIDANDO que no haya numeros negativos:
b = int(input("Dame la base: "))
a = int(input("Dame la altura: "))
if a and b >= 0:
    result = b*a
    print("El área es:",result)
elif b and a <= 0:
    while b and a<= 0:
        pregunta1 = int(input("Dame una base positiva: "))
        pregunta2 = int(input("Dame la altura positiva: "))
        if pregunta1 >=0 and pregunta2 >=0:
            result = pregunta1*pregunta2
            print("El área es:",result)
            break
elif b <= 0:
    while b <= 0 and a >=0:
        pregunta1 = int(input("Dame una base positiva: "))
        if pregunta1 >=0:
            result = pregunta1*a
            print("El área es:",result)
            break
elif a <= 0:
    while a <= 0 and b >=0:
        pregunta2 = int(input("Dame una altura positiva: "))
        if pregunta2 >=0:
            result= b*pregunta2
            print("El área es:",result)
            break

#TABLA DE MULTIPLICAR:
n = int(input("Dame un número: "))
while n > 0:
    for i in range (1,11):
        i = i * n
        print(i)
    n = int(input("Dame un número: "))
    if n == 0:
        break

#Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa e obteña o número deles que ganan entre 1000 e 1750 €, ámbolos dous incluídos e, a porcentaxe de traballadores que ganan menos de 1000 €. Tendo en conta que non se coñece con antelación o numero de traballadores da empresa e non se admiten os soldos negativos (utiliza como condición de fin un soldo 0).
n = 1
i = 0
t = 0
sueld = 1
while n > 0:
    sueld = int(input("Cuanto cobras: "))
    if sueld >= 1000 and sueld <= 1750:
        i = i + 1
        print("Cobran entre 1000€ y 1750€ un total de:",i,"tabajadores")
    if sueld < 0 or sueld > 1750:
        print("ERROR")
    elif sueld == 0:
        break
    if sueld <= 1000 and sueld > 0:
        t = t + 1
        calc = (t*100)/(i+1)
        print("El porcentaje de los que cobra menos de 1000€ es del",calc,"%")

#PIRAMIDE:
n = int(input("Dame un número: "))
for i in range (1, n+1):
    print(" " * (n - i) + "* " * i)

#PEDIR NÚMEROS Y CALCULAR SUMA, SI SE DA LA CONDICIÓN DE SALIDA MOSTRAR LA SUMA DE LOS NÚMEROS QUE SE HAYAN INTRODUCIDO SIN LLEGAR AL LÍMITE:
suma = 0
for i in range (10):
    n = int(input("Dame un número: "))
    if n == 999:
        break
    suma+=n
print(suma)

#AÑADIR VALORES=
#variable = {}

#DAR VALORES A UNA LISTA
asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
notas = {}
for asignatura in asignaturas:
    nota = int(input(f"¿Que sacaste en {asignatura}?: "))
    notas[asignatura] = nota
for asignatura in asignaturas:
    print(f"Sacaste un {notas[asignatura]} en {asignatura}")

#NUEVA LISTA=
#lista_nueva = []
#lista_nueva.append(valores que queremos que tenga)

#ORDENAR DE MENOR A MAYOR
#lista.sort()

#PRINT SIN []
#*variable#

#RANGO QUE QUEREMOS ABARCAR
#lista[principio:fin:saltos]

#SEPARACIÓN QUE QUEREMOS PARA LOS VALORES
#sep="/" (o , . * ...)

#ORDEN DE MENOR A MAYOR:
numeros = []
for numero in range (8):
    loteria = int(input("Dime los número ganadores: "))
    numeros.append(loteria)
numeros.sort()
print("El numero de la lotería ordenado es :")
print(*numeros[0:8], sep="/")

#ORDEN INVERSO
#lista[::-1]
lista = [1,2,3,4,5,6,7,8,9,10]
print(*lista[::-1], sep =",")

#Escribir un programa que almacene as asignaturas dun curso (por exemplo Matemáticas, Física, Química, Historia e Língua) nunha lista, pregunte o usuario a nota que sacou en cada asignatura e elimine da lista as asignaturas aprobadas. O fin, o programa debe mostrar por pantalla as asignaturas que o usuario ten que repetir.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = {}
for asignatura in asignaturas:
    nota = int(input(f"¿Qué sacaste en {asignatura}?: "))
    notas[asignatura] = nota
print("Tienes que repetir: ")
for asignatura in asignaturas:
    if notas[asignatura] <5:
        print (asignatura)

#Dar valor a una lista:
#len(lista)
#En el ejemplo a=0, b=1 ... z=26

#Posiciones MULTIPLOS DE 3
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
sin = []
for letra in range(len(letras)):
    if (letra + 1) % 3!= 0:
        sin.append(letras[letra])
print(sin)

#PALINDROMO:
palabra = input("Dime una palabra: ")
if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#CONTAR CUENTAS VECES ESTA UN VALOR=
#lista.count(valor)

#CONTAR vocales (valor específico en una lista):
vocales = ["a","e","i","o","u"]
palabras = input("Dime una palabra: ")
for vocal in vocales:
    numero = palabras.count(vocal)
    print(f"{vocal} aparece {numero} veces")

#VALOR MAYOR Y MENOR DE UNA LISTA:
prezos = [50, 75, 46, 22, 80, 65, 8]
print(f"El precio mas bajo es: {min(prezos)}")
print(f"El precio mas alto es: {max(prezos)}")

#PRODUCTO ESCALAR:
vector = [1,2,3]
vecto = [-1,0,2]
lista = [vector[0]*vecto[0]+vector[1]*vecto[1]+vector[2]*vecto[2]]
print(lista)

#PRODUCTO MATRICES.
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
vector3 = [-1, 0]
vector4 = [0, 1]
vector5 = [1, 1]
lista = [
    [vector1[0]*vector3[0] + vector1[1]*vector4[0] + vector1[2]*vector5[0],
     vector1[0]*vector3[1] + vector1[1]*vector4[1] + vector1[2]*vector5[1]],
    [vector2[0]*vector3[0] + vector2[1]*vector4[0] + vector2[2]*vector5[0],
     vector2[0]*vector3[1] + vector2[1]*vector4[1] + vector2[2]*vector5[1]]
]
print("El producto de A x B es:", lista)

#MEDIA Y DESVIACIÓN TÍPICA:
calculo = 0
lista = []
for n in range (5):
    numero = int(input("Dame los números: "))
    lista.append(numero)
    calculo=(numero+calculo)
media = calculo/5
desviacion = 0
for numero in lista:
    desviacion += (numero-media)**2
c = (desviacion/5)**0.5
print("la media es: ",media)
print("La desviación típica es:", desviacion)
print(lista,sep=",")

#LONGITUD TEXTO:
frase = str(input(f"Ingrese una oracion: "))
print(f"La longitud de la frase es: {len(frase)}")

#in significa dentro de

#MOSTRAR CARACTER POR CARACTER:
frase = str("Python")
letras = list(frase)
for letra in letras:
    print(letra)

#CONVERTIR VARIABLE A LISTA
#list(variable)

#INVERTIR TEXTO:
frase = str("Python para todos")
letras = list(frase)
print(*letras[::-1])

#ELIMINAR ESPACIOS:
frase = str("Guido Van Rossum creou Python")
letras = frase.replace(" ","")
print(*letras,sep="")

#CONTAR VOCALES Y CONSONANTES:
frase = str("Python Python Python")
letras = frase.replace(" ","")
vocales = 0
consonantes = 0
for vocal in letras:
    if vocal in "aeiou":
        vocales+=1
    if vocal in "bcdfghjkmlnñpqrstvwxyzBCDFGHJKMLNÑPQRSTVWXYZ":
        consonantes += 1
print(f"La frase tiene {vocales} vocales")
print(f"La frase tiene {consonantes} vocales")

#DIVIDIR TEXTO Y LUEGO CONCATENAR:
frase = str("www.phytonparatodos.com")
cadena = frase
primer = cadena[:10]
segund = frase[10:]
suma = primer+segund
print(primer,segund)
print(suma)

#TRANFORMAR A MAYUSCULAS Y MINUSCULAS:
frase = str("phytoneros")
print(frase)
mayus = frase.upper()
print(mayus)
minus = mayus.lower()
print(minus)

#COMPARAR:
frase = str("phyton")
oracion = str("javascript")
if frase == oracion:
    print("son iguales")
else:
    print("son diferentes")

#SUSTITUIR:
frase = str("jeve jeve jeve")
java = frase.replace("e","a")
print(frase)
print(java)

#Tenta escribir un método, que dado un obxecto da clase str conte diferentes tipos de caracteres. En particular, o método deberá imprimir o número de letras, díxitos e espazos en branco da cadea. Tenta facer un programa que escriba o cálculo da cadea: «Ola, son alumno de DAM1, e son programador desde o 2025».
letras = 0
blanco = 0
frase = str("Ola, son alumno de DAM1, e son programador desde o 2025")
print(f"La frase tiene {len(frase)} dígitos")
for letra in frase:
    if letra in "abcdefghijkmlnñopqrstuvwxyzABCDEFGHIJKMLNÑOPQRSTUVWXYZ":
        letras+=1
print(f"La frase tiene {letras} letras")
for letra in frase:
    if letra in " ":
        blanco+=1
print(f"La frase tiene {blanco} espacios en blanco")

#FUNCION:
#def nombre_de_la_función (variable_que_vamos_a_usar):
    #codigo
#nombre_de_la_función(variables_que_vamos_a_usar)

#IMPRIMIR 2 PRIMEROS CARACTERES, 3 ULTIMOS, IMPRIMIR CADA 2 CARACTERES, IMPRIMIR DEL DERECHO Y PEGADO DEL REVES
caracteres = str(input("Dame una cadena de carcateres: "))
def operacion(caracteres):
    list(caracteres)
    print(caracteres[:2])
    print(caracteres[-3:])
    print(caracteres[::2])
    print(caracteres+caracteres[::-1])
operacion(caracteres)

#REEMPLAZAR POR UN CARACTER, SEPARAR PALABRAS CON UN CARACTER, REEMPLAZAR LOS DÍGITOS POR UN CARCATER Y INSERTAR CADA 3 DIGITOS:
cadena = str(input("Dame una cadena: "))
caracter = str(input("Dame un carcater: "))
def cadena_caracter(cadena,caracter):
    print(cadena.replace(" ",caracter))
    print(cadena.replace("",caracter))
    nueva_cadena = caracter
    for tres in cadena:
        if tres in cadena:
            nueva_cadena += caracter
    print(nueva_cadena)
    cuatro = ""
    simbolo = 1
    for tres in cadena:
        if tres in cadena:
            if simbolo % 3 == 0:
                cuatro += tres
                cuatro += caracter
            else:
                cuatro += tres
            simbolo += 1
    if cuatro:
        print(cuatro)
cadena_caracter(cadena,caracter)

#código anterior con CANTIDAD MÁXIMA Y MÍNIMA de reemplazos:
cadena = str(input("Dame una cadena: "))
caracter = str(input("Dame un carcater: "))
maximo = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter(cadena,caracter,maximo):
    print(cadena.replace(" ",caracter,maximo))
cadena_caracter(cadena,caracter,maximo)

cadena2 = str(input("Dame una cadena: "))
caracter2 = str(input("Dame un caracter: "))
maximo2 = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter2(cadena2,caracter2,maximo2):
    print(cadena2.replace("",caracter2,maximo2))
cadena_caracter2(cadena2,caracter2,maximo2)

cadena3 = str(input("Dame una cadena: "))
caracter3 = str(input("Dame un carcater: "))
maximo3 = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter3(cadena3,caracter3,maximo3):
    nueva_cadena = ""
    contador = 0
    for tres in cadena3:
        nueva_cadena += tres
        if contador < maximo3:
            nueva_cadena += caracter3
            contador += 1
    print(cadena3,caracter3,maximo3)
cadena_caracter3(cadena3,caracter3,maximo3)

cadena4 = str(input("Dame una cadena: "))
caracter4 = str(input("Dame un carcater: "))
maximo4 = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter4(cadena4,caracter4,maximo4):
    cuatro = ""
    simbolo = 1
    contador = 0
    for tres in cadena4:
        cuatro += tres
        if simbolo % 3 == 0 and contador < maximo4:
            cuatro += caracter4
            contador += 1
        simbolo += 1
    if cuatro:
        print(cuatro)
cadena_caracter4(cadena4,caracter4,maximo4)

#separaciones de MILES:
numero = input("Dame un numero: ")
puntos = "."
def punto_1(numero,puntos):
    numero = str(numero)
    numero = numero[::-1]
    punto=""
    calc=1
    for rest in numero:
        if rest in numero:
            if calc % 3 == 0:
                punto += rest
                punto += puntos
            else:
                punto += rest
            calc += 1
    if punto:
        print(punto[::-1])
punto_1(numero,puntos)

#DIVIDIR CADENA EN UNA LISTA QUE SEPARA CADA VALOR
#cadena.split()

#SIGLAS, PRIMERA LETRA DE CADA PALABRA DE LA CADENA EN MAYÚSCULA, PALABRA QUE EMPIECEN POR A (cierto carcater)
palabra = str(input("Dame una palabra: "))
def sigla(palabra):
    palabra = palabra.split()
    division = ""
    for palabras in palabra:
        division = division + palabras[0]
    print(division)
sigla(palabra)

palabra2 = str(input("Dame una palabra: "))
def sigla2(palabra2):
    palabra2 = palabra2.split()
    division2 = ""
    for palabra1 in palabra2:
        division2 += palabra1[0].upper() + palabra1[1:].lower() + " "
    print(division2)
sigla2(palabra2)

palabra3 = str(input("Dame una palabra: "))
def sigla3(palabra3):
    palabra3 = palabra3.split()
    division3 = ""
    for palabra2 in palabra3:
        if palabra2[0].lower() == "a":
            division3 += palabra2 + " "
    print(division3)
sigla3(palabra3)

#UNIR CON UN ESPACIO (UNIR)
# " ".join(variable)

#IMPRIMIR SOLO CONSONANTES, VOCALES, SUSTITUIR POR LA SIGUIENTES VOCALL:
palabra = input(str("Dime una palabra: "))
def consonantes (palabra):
    lista = ("bcdfghjkmlnñpqrstvwxyzBCDFGHIJKMLNÑPQRSTVWXYZ")
    conso = ""
    for consonante in palabra:
        if consonante in lista:
            conso += consonante
    print(conso)
consonantes(palabra)

palabra2 = input(str("Dame una palabra: "))
def vocal (palabra2):
    lista = "aeiouAEIOU"
    voca = ""
    for vocales in palabra2:
        if vocales in lista:
            voca += vocales
    print(voca)
vocal(palabra2)

palabra3 = input(str("Dime una palabra: "))
def siguiente(palabra3):
    lista = "aeiou"
    sig = ""
    for siguientes in palabra3:
        if siguientes == "a":
            sig += "e"
        elif siguientes == "e":
            sig += "i"
        elif siguientes == "i":
            sig += "o"
        elif siguientes == "o":
            sig += "u"
        elif siguientes == "u":
            sig += "a"
        else:
            sig += siguientes
    print(sig)
siguiente(palabra3)

#PALÍNDROMO:
palabra = input(str("Dame una palabra: "))
def palin (palabra):
    if palabra == palabra[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
palin(palabra)

#INDICAR SI UNA CADENA ES UNA SUBCADENA, DEVOLVER SOLO EL QUE ESTE ANTES EN EL ORDEN ALFABÉTICO:
palabra = input(str("Dime una palbara: "))
palabra2 = input(str("Dime otra palabra: "))
subcadena = "sub"
def sub(palabra,palabra2,subcadena):
    if palabra in subcadena+palabra2:
        print("Es una subcadena")
    else:
        print("no es una subcadena")
sub(palabra,palabra2,subcadena)

primero = input(str("Dime una palabra: "))
segundo = input(str("Dime otra palabra: "))
def orden (primero,segundo):
    if primero < segundo:
        print(primero)
    else:
        print(segundo)
orden(primero,segundo)

#PASAR BINARIO A DECIMAL:
#(variable, 2)

numero = input("Dame un número: ")
def binario(numero):
    return int(numero, 2)
print("decimal: ",binario(numero))

#COGER LONGITUD DE UNA PALABRA E IMPRIMIR EN ESA LONGITUD CARACTERES, Recibindo unha cadea de caracteres e un caracter, a función terá que comprobar si o caracter está na cadea. A función retornará un String no que aparezan guións e o caracter na posición ou posicións onde coincida na cadea.
palabra2 = input(str("Dime una palabra: "))
caracter2 = input(str("Dime un caracter: "))
raya = str("-")
def guion(palabra2,caracter2,raya):
    resultado = ""
    for palabras in palabra2:
        if palabras == caracter2:
            resultado = resultado + caracter2
        else:
            resultado = resultado + raya
    print(resultado)
guion(palabra2,caracter2,raya)

#VALIDAR CXONTRASEÑA=Escribe a función que permita validar un contasinal, recibindo o contrasinal como parámetro. O contrasinal ten que cumprir as condicións de mínimo 8 caracteres, o menos unha maiúscula, unha minúscula e un número. A función ten que retornar un booleano especificando si é válida ou non.
#SI QUEREMOS VAALIDAR ALGO SIEMPRE TENDRA QUE EMPEZAR EN False
#variable.isupper() es mayuscula...
#and todas las condiciones
#or una de ellas o si se cumple alguna
contraseña = input("Dame tu contraseña: ")
def validar_contraseña(contraseña):
    valido = False
    valido1 = False
    valido2 = False
    valido3 = False
    if len(contraseña) >= 8:
        valido = True
    for contra in contraseña:
        if contra.isupper():
            valido1 = True
        elif contra.islower():
            valido2 = True
        elif contra.isdigit():
            valido3 = True
    return valido and valido1 and valido2 and valido3
print(validar_contraseña(contraseña))

#RETURN LO QUE HACE ES DEVOLVER UN RESULTADO (EJ: def sumar(a, b): return a + b | resultado = sumar(3, 5) | print(resultado)

#FORMATEAR=Escribe a función que permita formatear de nomes. A función ten que eliminar os espazos en branco e poñer en maiúsculas o primeiro caracter d o nome e apelido pasado como parámetro. Finalmente retornará unha cadea co nome e apelidos co formato solicitado.
llamar = input(str("Dime tu nombre y apellido: "))
def nombre (llamar):
    llamar = llamar.split()
    mayus = ""
    for palabra in llamar:
        mayus += palabra[0].upper() + palabra[1:]
    print(mayus)
nombre(llamar)

#Crear a función que permíta realizar un analisis simple de texto. O analizador ten  a función de contar palabras, caracteres e encontrar a palabra mais longa. Mostrar os resultados por pantalla.
palabra = input(str("Dime una frase: "))
def analisis (palabra):
    letras = 0
    for letra in palabra:
        if letra in "abcdefghijkmlnñopqrstuvwxyzABCDEFGHIJKMLNÑOPQRSTUVWXYZ":
            letras = letras+1
    print(f"Tiene {letras} letras")
    caracteres = 0
    for letra in palabra:
        if letra in palabra:
            caracteres = caracteres + 1
    print(f"Tiene {caracteres} caracteres")
    palabras = palabra.split()
    largo = ""
    for letra in palabras:
        if len(letra) > len(largo):
            largo = letra
    print(f"La palabra mas larga es {largo}")
analisis(palabra)

#TUPLA=
#tupla = (1, 2 ,3) ("a","b","d") (1,"a",True)

#CONVERTIR EN TUPLA=
#variable = tuple(variable.split(",")

#INDICAR SI UNA TUPLA ESTA ORDENADA DE MENOR A MAYOR:
lista = input("Dame una tupla: ")
def orden(lista):
    lista = tuple(lista.split(','))
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            print("La tupla no está en orden de menor a mayor")
            return
    print("La tupla está en orden de menor a mayor")
orden(lista)

#INDICAR SI DOS FICHAS DE DOMINO ENCAJAN:
#BOOLEANO ES QUE VA A RECIBIR DE VALOR TRUE O FALSE, ES DECIR, NO HARÁ FALTA UN PRINT
ficha1 = input("Dime la ficha: ")
ficha2 = input("Dime otra: ")
def encaja(ficha1, ficha2):
    ficha1 = tuple(ficha1.split(','))
    ficha2 = tuple(ficha2.split(','))
    valido = False
    for val1 in ficha1:
        for val2 in ficha2:
            if val1 == val2:
                valido = True
    return valido
print(encaja(ficha1, ficha2))

#Escribir unha función que reciba unha tupla con nomes e para cada nome imprima unha mensaxe ‘Estimado don/dona Nome’
nombres = ("marta","alan","carlos")
def mensaje (nombres):
    for nombre in nombres:
        print(f"Estimado don/doña {nombre}")
mensaje (nombres)

#Escribir unha función que reciba unha tupla con nomes, unha posición de orixen p e unha cantidade n, e imprima a mensaxe anterior (exercicio 3) para os n nombres que se encontran a partires da posición p.
def mensaje(nombres, p, n):
    for nombre in nombres[p:p+n]:
        print(f"Estimado don/doña {nombre}")
lista_nombres = ("carlos", "alan", "ivan", "adrian", "marta", "martin")
mensaje(lista_nombres, 2, 4)

#Modificar as funcións anteriores para que teñan en conta o xénero do destinatario, para elo, deberán recibir unha tupla de tuplas, contendo o nome e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.
def mensaje(nombres):
    for nombre in nombres:
        if nombre[1] == "h":
            print(f"Hola don {nombre[0]}")
        elif nombre[1] == "m":
            print(f"Hola doña {nombre[0]}")
lista_nombres = (("carlos","h"), ("alan","h"), ("ivan","h"), ("adrian","h"), ("marta","m"), ("martin","h"))
mensaje(lista_nombres)

#DEVOLVER PRIMOS, SUMATORIO, PROMEDIO, FACTORIAL
lista = [1,2,3,4,5,6,7,8,9]
def numeros (n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for n in lista:
    if numeros(n):
        print(f"{n} primo ")
    else:
        print(f"{n} no es primo")
suma = 0
promedio = 0
for n in range (1,n+1):
    suma = suma + n
    promedio = suma//9
print(f"El sumatorio es {suma}, y el promedio {promedio}")
for n in range (1,n+1):
    fact = 1
    for r in range(fact,n+1):
        fact = fact * r
    print(f"el factorial de cada numero es {n}-{fact}")
numeros(lista)

#DEVOLVER 3 LISTAS, UNA CON LOS MENORES DE UN N8UMERO, OTRA MAYORES Y OTRA MULTIPLOS Y IGUALES
lista = [1,2,3,4,5,6,7,8,9,10]
numero = 4
mas = []
menos = []
multiplo = []
igual = []
def numeros (lista,numero):
    for i in lista:
        if i > numero:
            mas.append(i)
        if i < numero:
            menos.append(i)
        if i % numero == 0:
            multiplo.append(i)
        if i == numero:
            igual.append(i)
    print(mas)
    print(menos)
    print(igual)
    print(multiplo)
numeros(lista,numero)

#ORDENAR TUPLA=Escribir unha función que reciba unha lista de tuplas (Apelido, Nome, Inicial_segundo_nome) e devolte unha lista de cadenas onde cada unha conteña primero o nome, logo a inicial cun punto, e logo o apelido.
lista = [("Sande", "Adrian", "D")]
nueva_lista = []
def orden(lista,nueva_lista):
    for apellido, nombre, inicial in lista:
        cadena = f"{nombre} {inicial}. {apellido}"
        nueva_lista.append(cadena)
    print(nueva_lista)
orden(lista,nueva_lista)

#INDICAR REPETICIONES=Escribir unha función empaquetar para unha lista, onde empaquetar significa indicar a repetición de valores consecutivos mediante unha tupla (valor, cantidade de repeticións). Por exemplo, empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devoltar [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].
lista = [(1,1,1,3,5,1,1,3,3)]
def empaquetar(lista):
    numeros = lista[0]
    resultado = []
    actual = numeros[0]
    contador = 1
    for numero in numeros[1:]:
        if numero == actual:
            contador += 1
        else:
            resultado.append((actual, contador))
            actual = numero
            contador = 1
    resultado.append((actual, contador))
    print(resultado)
empaquetar(lista)

#SUMA DE MATRICES Y PRODUCTO:
matriz1 = [1,2]
matriz2 = [4,6]
def suma (matriz1,matriz2):
    suma1 = matriz1[0]+matriz2[0]
    suma2 = matriz1[1]+matriz2[1]
    print((f"({suma1},{suma2})"))
suma(matriz1,matriz2)
def producto (matriz1,matriz2):
    suma1 = matriz1[0]*matriz2[0]
    suma2 = matriz1[1]*matriz2[1]
    resultado = suma1 + suma2
    print(resultado)
producto(matriz1,matriz2)

#Pregado de un texto. Escribir unha función que reciba un texto e unha lonxitude e devolva unha lista de cadeas de como máximo esa lonxitude. As líñas deben cortarse correctamente nos espazos (sen cortar as palabras).
def plegar_texto(texto, max_len):
    palabras = texto.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if len(linea_actual) + len(palabra) + (1 if linea_actual else 0) > max_len:
            lineas.append(linea_actual)
            linea_actual = palabra
        else:
            if linea_actual:
                linea_actual += " " + palabra
            else:
                linea_actual = palabra
    if linea_actual:
        lineas.append(linea_actual)

    return lineas
texto = "Escribir unha función que reciba un texto e unha lonxitude e devolva unha lista de cadeas."
resultado = plegar_texto(texto, 20)
for linea in resultado:
    print(linea)

#AHORCADO COMPLEJO:
import random
import unicodedata
palabras = [
    "apple", "table", "chair", "house", "water", "bread", "light", "music", "sport", "plant",
    "fruit", "style", "world", "sleep", "smile", "drink", "dance", "beach", "cloud", "stone",
    "grass", "heart", "brain", "dream", "power", "quiet", "quick", "happy", "magic", "green",
    "black", "white", "brown", "ocean", "river", "earth", "stars", "shine", "sweet", "sugar",
    "spice", "spicy", "honey", "berry", "peach", "mango", "lemon", "grape", "melon", "olive",
    "onion", "pizza", "pasta", "bacon", "cream", "sauce", "toast", "flour", "salad", "steak",
    "sushi", "curry", "bagel", "donut", "fries", "mocha", "latte", "cocoa", "guava", "papaw",
    "pecan", "maple", "cedar", "birch", "sprig", "coral", "shell", "plank", "brush", "cloth",
    "shirt", "pants", "dress", "scarf", "socks", "shoes", "watch", "phone", "cable", "mouse",
    "print", "paper", "ruler", "paint", "color", "azure", "fauna", "flora"
]
vidas = [   "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\\\n"
            "|  / \\\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\\\n"
            "|  /\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\\\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|   |\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "=========",
            ]
palabra = random.choice(palabras)
guess = ["_"] * len(palabra)
vida = 9
print(vidas[vida])
while "_" in guess:
    print("".join(guess))
    letrat = str(input("Ingresa una letra: ")).lower()
    letrat = unicodedata.normalize("NFD", letrat)
    letra = ""
    for c in letrat:
        if unicodedata.category(c) != 'Mn':
            letra += c
    if letra in palabra:
        pos = []
        for i in range(len(palabra)):
            if palabra[i] == letra:
                guess[i] = letra
    else:
        vida -= 1
        if vida > 0:
            print("La letra no está")
            print(vidas[vida])
        else:
            print("Te quedaste sin vidas")
            guess = palabra
            print("La palabra era: ", guess)
print("Ganaste!!! la palabra era: ", "".join(guess))

#AHORCADO SENCILLO
import random
palabras = ["jotaro kujo", "star platinum", "dio brando", "the world", "joseph joestar", "hermit purple", "josuke higashikata", "crazy diamond", "okuyasu nijimura", "the hand", "koichi hirose", "echoes", "rohan kishibe", "heaven’s door", "giorno giovanna", "gold experience", "bruno bucciarati", "sticky fingers", "narancia ghirga", "aerosmith", "guido mista", "sex pistols", "leone abbacchio", "moody blues", "trish una", "spice girl", "jolyne cujoh", "stone free", "enrico pucci", "made in heaven", "weather report", "foo fighters", "johnny joestar", "tusk", "gyro zeppeli", "yoshikage kira", "killer queen", "caesar zeppeli", "lisa lisa", "hol horse", "lucy steel", "hot pants", "diego brando", "scary monsters", "sandman", "in a silent way", "pocoloco", "hey ya!", "valentine", "dirty deeds done dirt cheap", "mountain tim", "oh! lonesome me", "josuke higashikata (jojolion)", "soft & wet", "yasuho hirose", "paisley park", "jobin higashikata", "speed king", "tooru", "wonder of u", "norisuke higashikata iv", "king nothing", "rai muromuzé", "born this way"]
palabra = random.choice(palabras)
letras_adivinadas = [letra if letra == " " else "_" for letra in palabra]
intentos = 10
print("Estas jugando al ahorcado de JoJo's")
while intentos > 0:
    print("Palabra:", " ".join(letras_adivinadas))
    if "".join(letras_adivinadas) == palabra:
        print("¡Buena! Adivinaste de una:", palabra)
        break
    intento = input("Adivina una letra: ").lower()
    if intento in palabra:
        print("¡Lesgoo, bien hecho!")
        for i in range(len(palabra)):
            if palabra[i] == intento:
                letras_adivinadas[i] = intento
    else:
        print("MAL.")
        intentos -= 1
        print("Te quedan", intentos, "intentos.")
if intentos == 0:
    print("CAGASTE, la palabra era:", palabra)

#CAJAS SUPER:
efectivo = [['2', [50, 4], [20, 5], [0.5, 6]],
            ['1', [20, 15], [10, 5], [0.2, 5], [0.1, 4]],
            ['3', [20, 12], [5, 6], [0.02, 5]]]
def mostrarContidoUnhaCaixa(totalEfectivoCaixas):
    for contidoCaixa in totalEfectivoCaixas:
        caixa = contidoCaixa[0]
        print('O contido da caixa', caixa, 'e:')
        for i in range(1, len(contidoCaixa)):
            if contidoCaixa[i][0] > 2.0:
                print(contidoCaixa[i][1], 'billetes de', contidoCaixa[i][0], 'euros')
            else:
                print(contidoCaixa[i][1], 'moedas de', contidoCaixa[i][0], 'euros')
        print()
mostrarContidoUnhaCaixa(efectivo)

#COMPROBADOR DE FECHAS:
fecha = input("Dime una fecha formato (dd/mm/aaaa): ")
formato_valido = ( len(fecha) == 10 and
                   fecha[2] == "/" and
                   fecha[5] == "/" and " " not in fecha and
                   fecha.replace("/", "").isdigit() )

if formato_valido:
    dia = int(fecha[:2])
    mes = int(fecha[3:5])
    year = int(fecha[6:])
    if 1 <=dia <=31 and 1 <=mes <=12 and year <=2025:
        print("Formato correcto")
    else:
        print("Formato incorrecto")
else:
    print("Formato incorrecto")

#GENERADOR DE CONTRASEÑAS:
import random
num = random.randint(6, 12)
print(num)
passwd = ''
while num != 0:
    passwd += chr(random.randint(33, 126))
    num -= 1
print(passwd)

#GENERADOR DE CONTRASEÑAS PIDIENDO YO EL DÍGITO:
import random
def contraseña(numero):
    contra = ""
    i = 0
    while i < numero:
        contra += chr(random.randint(33, 126))
        i += 1
    return contra
while True:
    numero = int(input("Dime la longitud de la contraseña: "))
    if 6 <= numero <= 12:
        print("Contraseña generada:", contraseña(numero))
    elif numero == 0:
        break
    else:
        print("La longitud tiene que ser entre 6 y 12")

#LISTA DE LA COMPRA:
list_compra = ['Limones', 'Naranjas', 'Queso', 'Pavo']
def añadir_elemento(lista):
    elemento = input('Engadir elemento: ')
    lista.append(elemento)
    print(lista)
def eliminar_elemento(lista):
    print(lista)
    eliminar = str(input('Que elemento desea eliminar: '))
    if eliminar in lista:
        lista.remove(eliminar)
def enseñar_lista(lista):
    print('Tu lista de la compra contiene:')
    for elemento in lista:
        print(elemento)
def menu():
    while True:
        print(''' Opciones:
          [1] Añadir elemento a lista
          [2] Eliminar elemento de lista
          [3] Enseñar lista
          [4] Salir''')
        opcion = int(input('Elija una opcion: '))
        if opcion == 1:
            añadir_elemento(list_compra)
        elif opcion == 2:
            eliminar_elemento(list_compra)
        elif opcion == 3:
            enseñar_lista(list_compra)
        elif opcion == 4:
            break
menu()

#QUITAR ACENTOS:
def eliminar_acentos(cadena):
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U")
    )
    for a, b in reemplazos:
        cadena = cadena.replace(a, b)
    return cadena

print(eliminar_acentos("Antón foi de viaxe a Ávila."))

#QUITAR ESPACIOS:
frase = str(input("Ingresa una frase: "))
while frase[0] == " ":
    frase = frase[1:]
frase = frase[::-1]
while frase[0] == " ":
    frase = frase[1:]
frase = frase[::-1]
print(frase)

#find / index
#Localizar subcadena
#s.find('x'), s.index('x')

#startswith / endswith
#Comprobar inicio/fin
#s.startswith('Hola')

#format / f-strings
#string formateada
#f"Hola {name}", "{} {}".format(a,b)

#Escapes / nuevas líneas
#salto de línea, tab
#\n, \t, \\

#Modificar elemento
#mi_lista[1] = 99
#Cambiar el valor en una posición

#mi_lista.append(4)
#Agregar un elemento al final

#mi_lista.insert(1, "nuevo")
#Insertar un valor en una posición específica

#mi_lista.remove(2)
#Eliminar la primera ocurrencia de un valor
#mi_lista.pop(0)
#Eliminar y devolver el valor en una posición
#mi_lista.clear()
#Eliminar todos los elementos
#copia = mi_lista.copy()
#Crear una copia independiente
#mi_lista.reverse()
#Invertir el orden de los elementos
#mi_lista.count(3)
#Contar cuántas veces aparece un valor
#mi_lista.index(3)
#Obtener la posición de un valor
#3 in mi_lista
#Saber si un valor está en la lista
#mi_lista[1:4]
#lista[::-1] invierte
#Obtener una sublista desde el índice 1 al 3
#for x in mi_lista:
#Iterar sobre todos los elementos
#mi_tupla[0]
#Obtener el primer elemento
#mi_tupla.count(2)
#Contar cuántas veces aparece un valor
#mi_tupla.index(2)
#Obtener la posición de un valor
#2 in mi_tupla
#Saber si un valor está en la tupla
#mi_tupla[1:3]
#Obtener una subtupla desde el índice 1 al 2
#for x in mi_tupla:
#Iterar sobre todos los elementos
numero = float(input("Introduce un número: "))

raiz = numero ** 0.5
raiz_entera = round(raiz)
resto = numero -(raiz_entera ** 2)

print("Número:", numero)
print("Raíz cuadrada aproximada:", raiz)
print("Raíz cuadrada entera más cercana:", raiz_entera)
print("Resto (diferencia con su cuadrado):", resto)
def main():
    hora = int(input("Introduce las horas: "))
    minuto = int(input("Introduce los minutos: "))
    segundo = int(input("Introduce los segundos: "))
    segundos_mas = int(input(f"Introduce los segundos que le quieres añadir a la hora ({hora}:{minuto}:{segundo}): "))

    while segundos_mas >= 60:
        minuto += 1
        segundos_mas -= 60

    while segundo + segundos_mas >= 60:
        segundo = segundo + segundos_mas - 60
        minuto += 1
        segundos_mas = 0

    segundo += segundos_mas

    while minuto >= 60:
        minuto -= 60
        hora += 1

    print(f"La hora actual es: {hora}:{minuto}:{segundo}")

if __name__ == "__main__":
    main()

def main():
    n = int(input("Escriba un número natural para saber su raíz cuadrada entera y su resto (si lo tiene): "))

    if n < 0:
        print("Error: la raíz cuadrada no está definida para números negativos.")
        return

    raiz_entera = 0
    while (raiz_entera + 1) ** 2 <= n:
        raiz_entera += 1

    cuadrado = raiz_entera ** 2
    resto = n - cuadrado

    if resto == 0:
        print(f"La raíz cuadrada de {n} es exacta: {raiz_entera}")
    else:
        print(f"La raíz entera más cercana de {n} es: {raiz_entera}")
        print(f"El cuadrado de {raiz_entera} es: {cuadrado}")
        print(f"El resto es: {resto}")

if __name__ == "__main__":
    main()








