import random 
import csv
# Lista de trabajadores
trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

#sueldos de los trabajadores
sueldos = []



def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos asignados exitosamente.\n")


def clasificar_sueldos():
    menores = []
    medios = []
    mayores = []

    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            menores.append((trabajadores[i], sueldo))
        elif 80000 <= sueldo <= 2000000:
            medios.append((trabajadores[i], sueldo))
        else:
            mayores.append((trabajadores[i], sueldo))

    print("Sueldos menores a $800.000 TOTAL:", len(menores))
    for nombre, sueldo in menores:
        print(f"{nombre} ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len(medios))
    for nombre, sueldo in medios:
        print(f"{nombre} ${sueldo}")

    print("\nSueldos superiores a $2.000.000 TOTAL:", len(mayores))
    for nombre, sueldo in mayores:
        print(f"{nombre} ${sueldo}")

    print("\nTOTAL SUELDOS: $", sum(sueldos), "\n")


def ver_estadisticas():
    if not sueldos:
        print("Primero debe asignar sueldos a los trabajadores.\n")
        return

    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    

    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${promedio:.2f}\n")


def reporte_sueldos():
    if not sueldos:
        print("Primero debe asignar sueldos a los trabajadores.\n")
        return

    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i, sueldo in enumerate(sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow({
                'Nombre empleado': trabajadores[i],
                'Sueldo Base': sueldo,
                'Descuento Salud': descuento_salud,
                'Descuento AFP': descuento_afp,
                'Sueldo Líquido': sueldo_liquido
            })

    print("Reporte de sueldos generado exitosamente.\n")

 
def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            asignar_sueldos_aleatorios()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Finalizando programa…")
            print("Desarrollado por Adrian Lizana")
            print("RUT 17.679.099-7")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.\n")


menu()
