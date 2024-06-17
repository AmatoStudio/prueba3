import csv
plan = []

# Función para agregar categoría
def agregar_plan():
    numero_id = int(input("Ingrese ID (número) del plan: "))
    nombre = input("Ingrese nombre: ")
    porcentaje_efectividad = int(input("Ingrese porcentaje, en número entero: "))
    categoria_interna = ""
    
# Función la clasificación de planes.
    categoria_interna = ""
    if porcentaje_efectividad >= 0 and porcentaje_efectividad <= 25:
        categoria_interna = "chiste"
    elif porcentaje_efectividad >= 26 and porcentaje_efectividad <= 50:
        categoria_interna = "anécdota"
    elif porcentaje_efectividad >= 51 and porcentaje_efectividad <= 75:
        categoria_interna = "peligro"
    elif porcentaje_efectividad >= 76 and porcentaje_efectividad <= 99:
        categoria_interna = "ATENCIÓN"
    else:
        categoria_interna = "ESCLAVITUD"
        
    planes ={"numero_id": numero_id, "nombre": nombre, "porcentaje_efectividad": porcentaje_efectividad, "categoria_interna": categoria_interna}
    plan.append(planes)
    
    print("Planes agregado con éxito.")
        
    
# Función listar planes
def listar_planes():
    if not plan:
        print("No hay planen la lista.")
    else:
        print("Lista de planes: ")
        for plan in planes:
            print(plan)

# Función eliminar plan por ID.
def eliminar_plan_por_id():
    numero_id = int(input("Ingrese el número de Plan por Id que desea elimina: "))
    for planes in plan:
        if planes["numero_id"] == numero_id:
            confirmacion = input(f"Estás seguro de eliminar el plan {planes['eliminar_plan_por_id']}? (s/n): ")
            if confirmacion.lower() == "s":
                plan.remove(planes)
                print("Plan por ID eliminado con éxito!.")
            else:
                print("Eliminación cancelada!.")
            return
        print("Plan no encontrado.")
        
# Función generar BBDD
def ggenerar_bbdd():
    with open ('plan.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['numero_id', 'nombre', 'porcentaje_efectividad','categoria_interna'])
        writer.writeheader()
        writer.writerow(plan)
    print("Base de datos generada con éxito!.")
    
# Función para cargar base de datos.
def cargar_bbdd():
    plan.clear()
    with open('plan.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            plan.append(row)
    print("Datos cargados desde archivo con éxito!.")
    
    
    
#Bucle principal del programa que muestra el menú y ejecuta las funciones.
while True:
    print("\n Menú Principal")
    print("1. Agregar planes")
    print("2. Listar planes")
    print("3. Eliminar plan por ID")
    print("4. Generar bbdd")
    print("5. Estadisticas")
    print("0. Salir")
    
    opcion = input("Seleccionar una opción: ")
    
    if opcion =='1':
        agregar_plan()
    elif opcion == '2':
        listar_planes()
    elif opcion == '3':
        eliminar_plan_por_id()
    elif opcion == '4':
        generar_bbdd()
    elif opcion == '5':
        cargar_bbdd()
    elif opcion == '6':
        estadisticas()
    elif opcion == '0':
        break
    else:
        print("Opción inválida. Por favor sellecione una opción valida.")