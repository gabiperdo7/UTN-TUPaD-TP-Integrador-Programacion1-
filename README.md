Gestión de Datos de Países en Python

-Alumno: Gabriel Maximiliano Perdomo
-Materia: Programación 1
-Carrera: Tecnicatura Universitaria en Programación a Distancia
-Institución: Universidad Tecnológica Nacional

*Descripción del trabajo
Este trabajo corresponde al Trabajo Práctico Integrador de la materia Programación 1.  
El objetivo es desarrollar una aplicación en Python que permita gestionar información sobre países, utilizando listas, diccionarios, funciones, condicionales, estructuras repetitivas, ordenamientos y estadísticas.

El sistema carga los datos desde un archivo CSV y permite realizar búsquedas, filtros, ordenamientos y cálculos estadísticos sobre la información.

*Funcionalidades principales
El programa ofrece un menú en consola con las siguientes opciones:
1. Buscar país por nombre (coincidencia parcial o exacta).  
2. Filtrar países por:
   - Continente  
   - Rango de población  
   - Rango de superficie  
3. Ordenar países por:
   - Nombre  
   - Población  
   - Superficie (ascendente o descendente)  
4. Mostrar estadísticas:
   - País con mayor y menor población  
   - Promedio de población  
   - Promedio de superficie  
   - Cantidad de países por continente
5. Agregar nuevo país:
   Permite inegresar manualmente las datos de un país nuevo (nombre, población, superficie y continente).
   Elsistema verifica que el país no exista previamente y, si es nuevo, lo agrega a la lista principal y actualiza automáticamente el archivo CSV.
6. Actualizar datos de un país:
   Permite modificar los valores de población y superficie de un país existente.
   Una vez actualizado, los cambios se guardan directamente en el archivo CSV.
7. Salir del programa.

*Conceptos aplicados
- Listas: para almacenar la colección de países.  
- Diccionarios: para representar los datos de cada país.  
- Funciones: modularizan el código en tareas específicas.  
- Condicionales: control de flujo y validación de opciones.  
- Bucles: ejecución repetitiva de acciones (menú y recorridos).  
- Ordenamientos: uso de sorted() con claves personalizadas.  
- Estadísticas: uso de max(), min(), sum(), len() para generar indicadores.  
- Archivos CSV: lectura y conversión a diccionarios mediante csv.DictReader.
- Gestión dinámica de datos: el sistema mantiene la base de datos actualizada automáticamente.

*Estructura del proyecto
Proyecto_Paises/
1.paises.csv
2.tp_integrador.py
3.README.md
4.TPI_Programación1.docx

*Formato del archivo CSV
El archivo paises.csv contiene los datos base:
-nombre,poblacion,superficie,continente
-Argentina,45376763,2780400,América
-Japón,125800000,377975,Asia
-Brasil,213993437,8515767,América
-Alemania,83149300,357022,Europa
-Egipto,109262178,1002450,África
-Australia,25925600,7692024,Oceanía

*Ejemplo de ejecución:
===== MENÚ PRINCIPAL =====
1. Buscar país por nombre
2. Filtrar países
3. Ordenar países
4. Mostrar estadísticas
5. Agregar nuevo país
6. Actualizar datos de un país
0. Salir
Seleccione una opción: 4

===== ESTADÍSTICAS =====
-País con mayor población: Brasil (213993437)
-País con menor población: Australia (25925600)
-Promedio de población: 100122046.33
-Promedio de superficie: 3512090.33

Cantidad de países por continente:
 - América: 2
 - Asia: 1
 - Europa: 1
 - África: 1
 - Oceanía: 1



