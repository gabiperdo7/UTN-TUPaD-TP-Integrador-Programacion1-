import csv

#Función para leer los datos desde un archivo CSV
def cargar_datos(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except ValueError:
                    print("Error: datos inválidos en una fila, se omitirá.")
        print(f"{len(paises)} países cargados correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifica el nombre o la ruta.")
    return paises


#Función para guardar los datos nuevamente en el CSV
def guardar_datos(nombre_archivo, paises):
    with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)
    print("Datos guardados correctamente en el archivo.")


#Función para mostrar el menú principal
def menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Buscar país por nombre")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("5. Agregar nuevo país")
    print("6. Actualizar datos de un país")
    print("0. Salir")
    return input("Seleccione una opción: ")


#Buscar país por nombre 
def buscar_pais(paises, nombre_busqueda):
    resultados = [p for p in paises if nombre_busqueda.lower() in p["nombre"].lower()]
    if resultados:
        for pais in resultados:
            print(f"{pais['nombre']} - {pais['poblacion']} hab. - {pais['superficie']} km² - {pais['continente']}")
    else:
        print("No se encontraron países con ese nombre.")


#Filtros
def filtrar_por_continente(paises, continente):
    filtrados = [p for p in paises if p["continente"].lower() == continente.lower()]
    if filtrados:
        for p in filtrados:
            print(f"{p['nombre']} ({p['continente']}) - {p['poblacion']} hab.")
    else:
        print("No hay países en ese continente.")


def filtrar_por_rango(paises, campo, minimo, maximo):
    filtrados = [p for p in paises if minimo <= p[campo] <= maximo]
    if filtrados:
        for p in filtrados:
            print(f"{p['nombre']} - {campo}: {p[campo]}")
    else:
        print("No hay países en ese rango.")


#Ordenamientos
def ordenar_paises(paises, campo, descendente=False):
    paises_ordenados = sorted(paises, key=lambda x: x[campo], reverse=descendente)
    for p in paises_ordenados:
        print(f"{p['nombre']} - {campo}: {p[campo]}")
    return paises_ordenados


#Estadísticas
def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos cargados.")
        return
    pais_mayor = max(paises, key=lambda x: x["poblacion"])
    pais_menor = min(paises, key=lambda x: x["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)
    print("\n===== ESTADÍSTICAS =====")
    print(f"País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})")
    print(f"País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    continentes = {}
    for p in paises:
        continentes[p["continente"]] = continentes.get(p["continente"], 0) + 1
    print("\nCantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f" - {cont}: {cant}")


#Agregar un nuevo país
def agregar_pais(paises, nombre_archivo):
    nombre = input("Nombre del país: ").strip()
    if any(p["nombre"].lower() == nombre.lower() for p in paises):
        print("Ese país ya existe en la base de datos.")
        return
    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie (km²): "))
        continente = input("Continente: ").capitalize()
        nuevo = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        paises.append(nuevo)
        guardar_datos(nombre_archivo, paises)
        print(f"País '{nombre}' agregado correctamente.")
    except ValueError:
        print("Error: los valores de población y superficie deben ser numéricos.")


#Actualizar población y superficie
def actualizar_pais(paises, nombre_archivo):
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Datos actuales: {pais['nombre']} - {pais['poblacion']} hab., {pais['superficie']} km²")
            try:
                nueva_poblacion = int(input("Nueva población: "))
                nueva_superficie = int(input("Nueva superficie (km²): "))
                pais["poblacion"] = nueva_poblacion
                pais["superficie"] = nueva_superficie
                guardar_datos(nombre_archivo, paises)
                print("Datos actualizados correctamente.")
            except ValueError:
                print("Error: debe ingresar valores numéricos.")
            return
    print("No se encontró un país con ese nombre.")


#Programa principal
def main():
    archivo = "paises.csv"
    paises = cargar_datos(archivo)
    while True:
        opcion = menu()
        if opcion == "1":
            nombre = input("Ingrese el nombre (o parte) del país: ")
            buscar_pais(paises, nombre)
        elif opcion == "2":
            print("\n1. Por continente\n2. Por rango de población\n3. Por rango de superficie")
            tipo = input("Seleccione tipo de filtro: ")
            if tipo == "1":
                cont = input("Ingrese continente: ")
                filtrar_por_continente(paises, cont)
            elif tipo == "2":
                min_p = int(input("Población mínima: "))
                max_p = int(input("Población máxima: "))
                filtrar_por_rango(paises, "poblacion", min_p, max_p)
            elif tipo == "3":
                min_s = int(input("Superficie mínima: "))
                max_s = int(input("Superficie máxima: "))
                filtrar_por_rango(paises, "superficie", min_s, max_s)
        elif opcion == "3":
            print("\n1. Por nombre\n2. Por población\n3. Por superficie")
            campo = input("Seleccione campo: ")
            descendente = input("¿Orden descendente? (s/n): ").lower() == "s"
            if campo == "1":
                ordenar_paises(paises, "nombre", descendente)
            elif campo == "2":
                ordenar_paises(paises, "poblacion", descendente)
            elif campo == "3":
                ordenar_paises(paises, "superficie", descendente)
        elif opcion == "4":
            mostrar_estadisticas(paises)
        elif opcion == "5":
            agregar_pais(paises, archivo)
        elif opcion == "6":
            actualizar_pais(paises, archivo)
        elif opcion == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


#Ejecución del programa
if __name__ == "__main__":
    main()


