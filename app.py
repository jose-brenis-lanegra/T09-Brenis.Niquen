import libreria
import os

#ejercicio 01
#hallar el area de un triangulo, de base mayor a 136 y de altura menor a 359
b=int(os.sys.argv[1])
a=int(os.sys.argv[2])

area=libreria.area_triangulo(b,a)
print("el area del triangulo es:", area)

#ejercicio 02
#hallar el area de un cuadrado
l=int(os.sys.argv[3])

area=libreria.area_cuadrado(l)
print("el area del cuadrado es:", area)

#ejercicio 03
#hallar el area del rombo
dme=int(os.sys.argv[4])
dma=int(os.sys.argv[5])

area=libreria.area_rombo(dme,dma)
print("el area del rombo es:", area)

#ejercicio 04
#hallar el perimetro del romboide
b=int(os.sys.argv[6])
a=int(os.sys.argv[7])

perimetro=libreria.perimetro_romboide(b,a)
print("el perimetro del romboide es:", perimetro)

#ejercicio 05
#hallar el area de un trapecio
bma=int(os.sys.argv[8])
bme=int(os.sys.argv[9])
a=int(os.sys.argv[10])

area=libreria.area_trapecio(bma,bme,a)
print("el area del trapecio es:", area)

#ejercicio 06
#hallar la suma de las area de un hexagono cuando el apotema esta comprendido de 1 a 16
bh=int(os.sys.argv[11])

suma_area=libreria.suma_area_hexagono(bh)
print("la suma de las area del hexagono es:", suma_area)

#ejercicio 07
#hallar el tamaño del circulo
pi=float(os.sys.argv[12])
r=int(os.sys.argv[13])

tamano=libreria.tamano_circulo(pi,r)
print("el tamaño del circulo es:", tamano)

#ejercicio 08
#calcular el tipo de elipse
sma=int(os.sys.argv[14])
sme=int(os.sys.argv[15])

tipo=libreria.tipo_elipse(sma,sme)
print("el tipo de elipse es:", tipo)

#ejercicio 09
#hallar el tipo del cuadrilatero encontrado
l1=int(os.sys.argv[16])
l2=int(os.sys.argv[17])
l3=int(os.sys.argv[18])
l4=int(os.sys.argv[19])

tipo=libreria.tipo_cuadrilatero(l1,l2,l3,l4)
print("el tipo del cuadrilatero es:", tipo)

#ejercicio 10
#hallar el volumen de un cubo
a=int(os.sys.argv[20])

volumen=libreria.volumen_cubo(a)
print("el volumen del cubo es:", volumen)

#ejercicio 11
#hallar el volumen del prisma
la=int(os.sys.argv[21])
an=int(os.sys.argv[22])
al=int(os.sys.argv[23])

volumen=libreria.volumen_prisma(la,an,al)
print("el volumen del prisma es:", volumen)

#ejercicio 12
#demostrar si el volumen de una esfera esta correcto
pi=float(os.sys.argv[24])
r=int(os.sys.argv[25])

demostrar=libreria.demostrar_esfera(pi,r)
print("el volumen de esta esfera esta:", demostrar)

#ejercicio 13
#hallar la suma de las areas totales del cilindro cuando su altura esta comprendido de 1 a 13
pi=float(os.sys.argv[26])
r=int(os.sys.argv[27])

suma_area_total=libreria.suma_area_total_cilindro(pi,r)
print("el area total del cilindro es:", suma_area_total)

#ejercicio 14
#hallar el area lateral del cono
pi=float(os.sys.argv[28])
r=int(os.sys.argv[29])
a=int(os.sys.argv[30])

area_lateral=libreria.area_lateral_cono(pi,r,a)
print("el area lateral del como es:", area_lateral)

#ejercicio 15
#hallar el volumen de una piramide
ar=int(os.sys.argv[31])
al=int(os.sys.argv[32])

volumen=libreria.volumen_piramide(ar,al)
print("el volumen de la piramide es:", volumen)

#ejercicio 16
#hallar la volumen de un tetraedro
a=int(os.sys.argv[33])

volumen=libreria.volumen_teraedro(a)
print("el volumen del tetraedro es:", volumen)

#ejercicio 17
#hallar el volumen de un octaedro
a=int(os.sys.argv[34])

volumen=libreria.volumen_octaedro(a)
print("el volumen del octaedro es:", volumen)

#ejercicio 18
#hallar el volumen de un dodecaedro
a=int(os.sys.argv[35])

volumen=libreria.volumen_dodecaedro(a)
print("el volumen del dodecaedro es:", volumen)

#ejercicio 19
#hallar el volumen de un icosaedro
a=int(os.sys.argv[36])

volumen=libreria.volumen_icosaedro(a)
print("el volumen del icosaedro es:", volumen)

#ejercicio 20
#hallar que tipo de raices tiene la ecuacion
a=int(os.sys.argv[37])
b=int(os.sys.argv[38])
c=int(os.sys.argv[39])

raiz=libreria.raices(a,b,c)
print("las raices de la ecuacion son:", raiz)

#ejercicio 21
#hallar si el mensaje es palindromo
msg=os.sys.argv[40]

inv=libreria.palindromo(msg)
print("¿la cadena es palindromo?:", inv)

#ejercicio 22
#demostrar si se puede acceder a una caja fuerte
cad1=os.sys.argv[41]
cad2=os.sys.argv[42]

caja=libreria.comparacion_len(cad1,cad2)
print("¿se puede acceder a la caja fuerte?:", caja)

#ejercicio 23
#hallar la nueva cadena
msg=os.sys.argv[43]

str=libreria.cortar(msg)
print("la nueva cadena es:", str)

#ejercicio 24
#hallar la posicion de "V" en el mensaje
msg=os.sys.argv[44]

bus=libreria.busqueda(msg)
print("la V en el mensaje esta en la posicion:", bus)

#ejercicio 25
#hallar la longitud de la cadena
cad=os.sys.argv[45]

medida=libreria.longitud(cad)
print("la longitud de la cadena es:", medida)
