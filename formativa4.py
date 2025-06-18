turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}

def turistas_por_pais(pais):
    resultado = [datos[0] for datos in turistas.values() if datos[1].lower() == pais.lower()]
    if resultado:
        print(resultado)
    else:
        print("No hay turistas de ese país.")

def turistas_por_mes(mes):
    mes_dig = f"-{mes:02d}-"
    total_turistas = len(turistas)
    turistas_en_mes = sum(1 for datos in turistas.values() 
    if mes_dig in datos[2])
    porcentaje = (turistas_en_mes / total_turistas) * 100 if total_turistas > 0 else 0
    return round(porcentaje, 1)

def eliminar_turista():
    nombre = input("Ingrese nombre del turista a eliminar: ").lower()
    for id, datos in list(turistas.items()):
        if datos[0].lower() == nombre:
            del turistas[id]
            print("Turista eliminado con éxito.")
            return
    print("Turista no encontrado. No se pudo eliminar.")

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por país.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")

        opcion = input("Ingrese opción: ")
        if opcion == "1":
            pais = input("Ingrese país a buscar: ")
            turistas_por_pais(pais)
        elif opcion == "2":
            while True:
                try:
                    mes = int(input("Ingrese mes a buscar (1-12): "))
                    if 1 <= mes <= 12:
                        print(f"El número de turistas equivale al {turistas_por_mes(mes)} % del total.")
                        break
                    else:
                        print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                except ValueError:
                    print("Ingrese un número válido.")
        elif opcion == "3":
            eliminar_turista()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

menu()