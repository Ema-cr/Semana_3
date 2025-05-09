# Lista global para almacenar los productos añadidos.
lista_compras = []

# Función para añadir un producto a la lista de compras.
def añadir_producto ():
    while True:
        # Solicita el nombre del producto y verifica que no esté vacío ni contenga números.
        nombre_prod = input("Ingresa el nombre del producto deseado: ").strip()
        if nombre_prod == "":
            print ("El nombre no puede estar vacio")
            continue
        elif any(char.isdigit() for char in nombre_prod):  # Verifica si el nombre contiene números.
            print ("Debes de ingresar solo letras")
            continue
        else:
            break  # Si el nombre es válido, salimos del bucle.

#----------------------------------------------------------------------------------------------------
    while True:
        # Solicita el precio del producto y verifica que sea un número positivo.
        try:
            precio_prod = float (input("Ingresa el precio del producto deseado: "))
            if precio_prod > 0:
                break  # Si el precio es válido, salimos del bucle.
            else:
                print ("Ingresa un precio valido.")
        except ValueError:
            print ("Ingresa un valor numerico valido.")  # Si ocurre un error, indica que el valor debe ser numérico.
            
#---------------------------------------------------------------------------------------------------
    while True:
        # Solicita la cantidad del producto y verifica que sea un número entero positivo.
        try:                
            cantidad_prod = int(input("Ingresa la cantidad que deseas: ")) 
            if cantidad_prod > 0:
                break  # Si la cantidad es válida, salimos del bucle.
            else:
                print("Ingresa una cantidad valida.")
        except ValueError:
            print ("Ingresa un numero valido entero. ")  # Si ocurre un error, indica que debe ser un número entero.

#---------------------------------------------------------------------------------------------------
    # Crea un diccionario con los datos del producto y lo agrega a la lista de compras.
    diccionario_productos = {
        "nombre" : nombre_prod,
        "precio" : precio_prod,
        "cantidad" : cantidad_prod
    }   
        
    lista_compras.append(diccionario_productos)  # Añade el producto a la lista de compras.
    print("Producto añadido correctamente. ")

    # Muestra todos los productos de la lista.
    print(" Lista de todos los productos: ")
    for producto in lista_compras:
        print(f"{producto['cantidad']} unidades de {producto['nombre']} a ${producto['precio']:.2f} cada un/a")
#----------------------------------------------------------------------------------------------------------------------------

# Función para buscar un producto por nombre en la lista de compras.
def buscar_prod (nombre_a_buscar, lista_compras): 
    for producto in lista_compras:
        # Compara los nombres de los productos (en minúsculas para no ser sensible a mayúsculas).
        if producto["nombre"].lower() == nombre_a_buscar.lower():
            return producto  # Si encuentra el producto, lo devuelve.

#---------------------------------------------------------------------------------------------------------
# Función para actualizar el precio de un producto en la lista.
def actualizar_precio(nombre_a_buscar, nuevo_precio): 
    for producto in lista_compras:
        if producto["nombre"].lower() == nombre_a_buscar.lower():
            producto["precio"] = nuevo_precio  # Actualiza el precio.
            print("Precio actualizado correctamente. ")
        else:
            print("No se pudo actualizar el precio. Producto no encontrado.")

#--------------------------------------------------------------------------------------------------
# Función para eliminar un producto de la lista.
def eliminar_producto(nombre):
    for i, producto in enumerate(lista_compras):
        if producto["nombre"].lower() == nombre.lower():
            lista_compras.pop(i)  # Elimina el producto de la lista.
            print("Se ha eliminado con exito el producto. ")
            return  # Si encuentra el producto, lo elimina y sale de la función.
    print("No se ha encontrado el producto. ")  # Si no lo encuentra, muestra un mensaje.

#--------------------------------------------------------------------------------------------------       
# Función para calcular y mostrar el total de la compra (precio * cantidad).
def mostrar_total():
    # Suma el total de los productos (precio * cantidad) y lo devuelve.
    return sum(map(lambda producto: producto.get("precio",0) * producto.get("cantidad", 1), lista_compras))

# Función principal que muestra el menú y maneja la interacción con el usuario.
def Menu():
    while True:
        # Muestra las opciones del menú para el usuario.
        print ("""Bienvenido a la Tienda Riwi, Ingresa la opción que deseas!:
        -----------------------Menu Principal---------------------------
        1. Añadir producto.
        2. Consultar productos.
        3. Actualizar precio.
        4. Eliminar productos.
        5. Ver el Valor Total.
        0. Salir. 
    """)
    
        # Lee la opción que el usuario elige.
        opcion = input("Selecciona una opción: ")
        
        # Dependiendo de la opción, llama a la función correspondiente.
        if opcion == "1":
            añadir_producto()  # Añadir un producto.
            
        elif opcion == "2":
            # Busca un producto por nombre e imprime los detalles.
            nombre_a_buscar = input("Ingresa el nombre del producto que deseas buscar: ").strip()
            resultado = buscar_prod(nombre_a_buscar, lista_compras)

            if resultado:
                print(f"El nombre del producto es {resultado['nombre']} hay {resultado['cantidad']} unidades a este precio ${resultado['precio']:.2f}")
            else:
                print("Producto no encontrado. ")

        elif opcion == "3":
            # Actualiza el precio de un producto.
            nombre_a_buscar = input("Ingresa el nombre del producto que deseas buscar: ").strip()
            try:
                nuevo_precio = float(input(f"Ingrese el nuevo precio para '{nombre_a_buscar}': "))
                if nuevo_precio < 0:
                    print("El precio debe ser mayor a cero.")
                else:
                    actualizar_precio(nombre_a_buscar, nuevo_precio)  # Llama a la función para actualizar el precio.
            except ValueError:
                print("El precio debe ser un número válido.")  # Si el precio ingresado no es válido, muestra un error.

        elif opcion == "4":
            # Elimina un producto de la lista.
            nombre = input("Ingresa el nombre del producto que deseas eliminar: ").strip()
            eliminar_producto(nombre)  # Llama a la función para eliminar el producto.

        elif opcion == "5":
            # Muestra el total de la compra.
            total_sumas = mostrar_total()
            print(f"La suma de todos los productos es: ${total_sumas:.2f}")
            
        elif opcion == "0":
            # Sale del menú.
            print("Gracias por preferirnos.")
            break  # Termina el bucle y sale del programa.
        
        else:
            # Si el usuario elige una opción no válida.
            print("Opción no válida, por favor elige una opción del menú.")

# Llama a la función Menu para ejecutar el programa.
Menu()
