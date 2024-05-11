"""Solicitar nombre
Solicitar rut
Solicitar prevision (isapre/fonasa)
Solicitar Seguro complementario (Si/No)
Elegir prestacion
Calcular el precio de la prestacion
Isapre -4000
Fonasa -3300

Seguro Complementario
-5000"""

consulta_general=30000
consulta_especialidad=45000
sangre=15000
imagenes=60000
nombre=input("ingrese su nombre: \n")
rut=input("ingrese su rut: \n")
prevision=int(input("Seleccione su previsión:\n1.Isapre\n2.Fonasa\n"))
segurocomp=input("Posee seguro complementario: Si/No\n").lower()
prestación=int(input("Seleccione su prestación:\n1.Consulta General\n2.Consulta Especialidad\n3.Examen de sangre\n4.Examen de Imágenes\n"))

#dependiendo del tipo de prestación seleccionada por el usuario definiremos que valor se le asignará a la variable "valor_prestacion"
if prestación==1:
    valor_prestacion=consulta_general      #Ej: "valor_prestacion" equivale al valor que le asignamos a "consulta_general" en la línea 13
elif prestación==2:
    valor_prestacion=consulta_especialidad
elif prestación==3:
    valor_prestacion=sangre
elif prestación==4:
    valor_prestacion=imagenes


if prevision==1:
    valor_prevision=valor_prestacion-4000    #aparece una nueva variable "valor_prevision", la que definimos en base al punto anterior
elif prevision==2:
    valor_prevision=valor_prestacion-3300


if segurocomp=="si":
    valor_final=valor_prevision-5000     #aparece el "valor_final" que será el anterior menos el dscto si tiene seguro
else:
    valor_final=valor_prevision          # y si no tiene seguro el "valor_final" seguirá siendo "valor_prevision" porque no se le descuentan más cosas.

print(f"nombre: {nombre}")
print(f"RUT: {rut}")
print(f"Costo original de la prestación:$ {valor_prestacion}")
print(f"Costo con previsión: ${valor_prevision}")
if segurocomp=="si":
    print(f"Costo total con seguro complementario: ${valor_final}")
else:
    print(f"Costo total: ${valor_final}")

