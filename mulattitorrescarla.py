def validar_entrada(numero):
    try:
        if not numero:   
            return False
        entrada = int(numero)
        if entrada < 1 or entrada > 7:
            print("Opción inválida")
            return False
        else:
            return entrada
    except ValueError:
        print("Menú sólo acepta números")
        return False


import csv
def procesar_lista_estudiantes(ListaCurso5B):
    notas_curso = []
    with open(ListaCurso5B, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            notas_curso.append(dict(row))  
    return notas_curso




system = True
main_menu = True
opcion = False

while system:
    while main_menu:
        while not opcion:
            opcion = int(input("1.Procesar lista de estudiantes\n2.Registrar estudiantes\n3.Modificar nota\n4.Eliminar estudiante\n5.Generar Promedio\n6.Generar acta de cierre\n7.Salir\nIngrese opción deseada:\n"))
            opcion = validar_entrada(opcion)    
        
        if opcion == 1:
            ListaCurso5B = 'ListaCurso5B.csv'
            students_data = procesar_lista_estudiantes(ListaCurso5B)

            for student in students_data:
                print(f"Rut: {student['Rut']}, Nombre: {student['Nombre']}, Nota1: {student['Nota 1']}, Nota2: {student['Nota 2']}")

            opcion = False  

        elif opcion == 2:
            ListaCurso5B = 'ListaCurso5B.csv'
            opcion2=False

        
            while not opcion2:
                while True:
                    try:
                        rut = int(input("Ingrese rut del estudiante sin puntos ni guión:\n"))
                        break  
                    except ValueError:
                        print("Error de ingreso")

                nombre = input("Ingrese nombre y apellidos del estudiante:\n")

                while True:
                    try:
                        nota1 = float(input("Ingrese nota 1 del estudiante sin puntos ni guión:\n"))
                        break  
                    except ValueError:
                        print("Error de ingreso")

                while True:
                    try:
                        nota2 = float(input("Ingrese nota 2 del estudiante sin puntos ni guión:\n"))
                        break  
                    except ValueError:
                        print("Error de ingreso")

                
                nuevo_estudiante = {
                    "Rut": rut,
                    "Nombre": nombre,
                    "Nota 1": nota1,
                    "Nota 2": nota2,
                }
                
                opcion2=False    
            
            with open("ListaCurso5B.csv","a",newline="") as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow(nuevo_estudiante)

                    
        elif opcion == 3:
            opcion = False 
        elif opcion == 4:
            opcion = False 
        elif opcion == 5:
            opcion = False 
        elif opcion == 6:
            opcion = False 
        elif opcion == 7:
            salir=False
            while not salir:
                confirmar_salida=input("esta seguro de querer salir? y/n: \n").lower()
                if confirmar_salida=="y":
                    salir=True
                    main_menu=False
                    system=False
                elif confirmar_salida=="n":
                    salir=True
                    opcion=False
                else:
                    print("opcion inválida")