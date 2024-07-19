import random

lista_con_sueldos=[]

def validar_entrada(numero):
    entrada=int(numero)
    try:
        if 5 <=entrada<=1:
            return entrada
        else:
            print("opción inválida")
            return False
    except ValueError:
        print("opción inválida")
        return False

def asignar_sueldos():
    lista_trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

    for t in lista_trabajadores:
        nombre=t
        sueldo=random.randrange(300000,2500000)

        nuevo_trabajador=({'Nombre':t, 'Sueldo':sueldo})
        lista_con_sueldos.append(nuevo_trabajador)
        
    print(lista_con_sueldos)
    return lista_con_sueldos

def clasificar_sueldos(lista_con_sueldos):
    sueldo_bajo=[]
    sueldo_medio=[]
    sueldo_alto=[]

    for t in lista_con_sueldos:
        if int(t['Sueldo'])<=800000:
            sueldo_bajo.append(t)
        elif 800000<=int(t['Sueldo'])<=2000000:
            sueldo_medio.append(t)
        elif int(t['Sueldo'])>2000000:
            sueldo_alto.append(t)
            
    print (len(sueldo_bajo))

    sueldos_only=[]
    for t in lista_con_sueldos:
        sueldo_t=int(t['Sueldo'])
        sueldos_only.append(sueldo_t)

    total_sueldos=0
    for element in sueldos_only:
        total_sueldos+=element


    print(f"Sueldos menores a $800.000 TOTAL:{(len(sueldo_bajo))}")
    for t in sueldo_bajo:
        print(f"Nombre empleado: {t['Nombre']}    Sueldo: {t['Sueldo']}")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL:{(len(sueldo_medio))}")
    for t in sueldo_medio:
        print(f"Nombre empleado: {t['Nombre']}    Sueldo: {t['Sueldo']}")
    print(f"Sueldos superiores a $2.000.000 TOTAL:{(len(sueldo_alto))}")
    for t in sueldo_bajo:
        print(f"Nombre empleado: {t['Nombre']}    Sueldo: {t['Sueldo']}")
    print(f"TOTAL SUELDOS:{total_sueldos}")

def ver_estadisticas(lista_con_sueldos):
    pass 

def reporte_sueldos(lista_con_sueldos):
    for t in lista_con_sueldos:
        nombre_empleado=t
        sueldo_liquido=int(t['Sueldo'])
        descuento_AFP=(sueldo_bruto*0.12)
        descuento_salud=(sueldo_bruto*0.07)
        sueldo_bruto=sueldo_liquido-descuento_AFP-descuento_salud

    print(f"Nombre empleado: {nombre_empleado}, Sueldo Base: {sueldo_bruto}, Sueldo Líquido: {sueldo_liquido}, Descuento AFP: {descuento_AFP}, Descuento Salud: {descuento_salud}")


def salir():
    while True:
        confirmar_salida=input("Está seguro de querer salir del programa? y/n\n").lower()
        if confirmar_salida=="y":
            print("Finalizando programa...")
            print("Desarrollado por Carla Mulatti")
            print("RUT: 17.052.706-2")
            return True
        elif confirmar_salida=="n":
            return False
        else:
            print("opción inválida")



system=True
main_menu=True
opcion=False
sueldos_asignados=False
while system==True:
    while main_menu==True:
        while not opcion:
            choices=input("Ingrese su opción:\n1.Asignar sueldos aleatorios\n2.Clasificar sueldos\n3.Ver estadísticas\n4.Reporte de sueldos\n5.Salir del programa\n")
            opcion=validar_entrada(choices)

            if choices=="1":
                asignar_sueldos()
                sueldos_asignados=True
            elif choices=="2":
                if sueldos_asignados==True:
                    clasificar_sueldos(lista_con_sueldos)
                else:
                    print("Debe asignar los sueldos primero!")
            elif choices=="3":
                if sueldos_asignados==True:
                    ver_estadisticas(lista_con_sueldos)
                else:
                    print("Debe asignar los sueldos primero!")
            elif choices=="4":
                if sueldos_asignados==True:
                    reporte_sueldos(lista_con_sueldos)
                else:
                    print("Debe asignar los sueldos primero!")
            elif choices=="5":
                if salir():
                    opcion=True
                    main_menu=False
                    system=False
                else:
                    break