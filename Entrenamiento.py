lista_compras = []

def añadir_producto ():
    while True:
        nombre_prod = input("Ingresa el nombre del producto deseado: ").strip()
        if nombre_prod == "":
            print ("El nombre no puede estar vacio")
            continue
        elif any(char.isdigit() for char in nombre_prod):
            print ("Debes de ingresar solo letras")
            continue
        else:
            break
#----------------------------------------------------------------------------------------------------
    while True:
        try:
            precio_prod = float (input("Ingresa el precio del producto deseado: "))
            if precio_prod > 0:
                break
            else:
                print ("Ingresa un caracter o un precio valido.")
        except ValueError:
            print ("Ingresa un valor numerico valido.")
#---------------------------------------------------------------------------------------------------
    while True:
        try:                
            cantidad_prod = int(input("Ingresa la cantidad que deseas: ")) 
            if cantidad_prod > 0:
                break
            else:
                print("Ingresa una cantidad valida.")
        except ValueError:
            print ("Ingresa un numero valido entero. ")
#---------------------------------------------------------------------------------------------------
    diccionario_productos = {
        "nombre" : nombre_prod,
        "precio" : precio_prod,
        "cantidad" : cantidad_prod
    }   
        
    lista_compras.append(diccionario_productos)
    print("Producto añadido correctamente. ")

    print(" Lista de todos los productos: ")
    for producto in lista_compras:
        print(f"{producto['cantidad']} unidades de {producto['nombre']} a ${producto['precio']:.2f} cada un/a")
#----------------------------------------------------------------------------------------------------------------------------

def buscar_prod (nombre_a_buscar,lista_compras): 
    for producto in lista_compras:
        if producto["nombre"].lower() == nombre_a_buscar.lower():
            return producto
#---------------------------------------------------------------------------------------------------------
def actualizar_precio(nombre_a_buscar, nuevo_precio): #Cambiar los datos adentro de la lista(dicc)
    for producto in lista_compras:
        if producto["nombre"].lower() == nombre_a_buscar.lower():
            producto["precio"] = nuevo_precio
            print("Precio actualizado correctamente. ")
        else:
            print("No se pudo actualizar el precio. Producto no encontrado.")

#--------------------------------------------------------------------------------------------------

def eliminar_producto(nombre):
    for i, producto in enumerate(lista_compras):
        if producto["nombre"].lower() == nombre.lower():
            lista_compras.pop(i)
            print("Se ha eliminado con exito el producto. ")
        else:
            print("No se ha encontrado el producto. ")    
#--------------------------------------------------------------------------------------------------       
def mostrar_total():
    return sum(map(lambda producto: producto.get("precio",0) * producto.get("cantidad", 1),lista_compras))



def Menu():
    while True:
        print ("""Bienvenido a la Tienda Riwi,Ingresa la opcion que deseas!:
        -----------------------Menu Principal---------------------------
        1.Añadir producto." 
        2.Consultar productos.
        3.Actualizar precio.
        4.Eliminar productos.
        5.Ver el Valor Total.
        0.Salir. 
    """)
    

        opcion = input("Selecciona una opcion. ")
        if opcion == "1":
            añadir_producto()
            
            
        elif opcion == "2":
            nombre_a_buscar = input("Ingresa el nombre del producto que deseas buscar: ").strip()
            resultado = buscar_prod(nombre_a_buscar,lista_compras)

            if resultado:
                print(f"El nombre del producto es {resultado['nombre']} hay {resultado['cantidad']} unidades a este precio ${resultado['precio']:.2f} ")
                break
            else:
                print("Producto no encontrado. ")
            buscar_prod()
            
        elif opcion == "3":
            nombre_a_buscar=input("Ingresa el nombre del producto que deseas buscar: ").strip()
            nuevo_precio = float(input(f"Ingrese el nuevo precio para '{nombre_a_buscar}': "))
            if nuevo_precio < 0:
                print("El precio debe ser mayor a cero. ")
            else:
                actualizar_precio(nombre_a_buscar,nuevo_precio) 
                    
        elif opcion == "4":
            nombre=input("Ingresa el nombre del producto que deseas eliminar: ").strip()
            eliminar_producto(nombre)

        elif opcion == "5":
            total_sumas = mostrar_total()
            print(f"La suma de todos los productos es: {total_sumas}")
            
        elif opcion == "0":
            print("Gracias por preferirnos. ")
            break
        else:
            print("Opción no valida,por favor elige una opcion del menú.  ")

Menu()
