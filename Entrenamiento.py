def añadir_producto ():
    while True:
        nombre_prod =str(input("Ingresa el nombre del producto deseado: ")).strip()
        try:
            if nombre_prod == "":
                print ("El nombre no puede estar vacio")
                continue
            elif any(char.isdigit() for char in nombre_prod):
                print ("Debes de ingresar solo caracteres")
                continue
            else:
                break
        except ValueError:
            print("Porfavor ingresa un dato valido. ")

    while True:
        try:
            precio_prod = float (input("Ingresa el precio del producto deseado: "))      # Si estás solicitando un número y el usuario ingresa una letra
            if precio_prod > 0:
                break
            else:
                print ("Ingresa un caracter o un precio valido.")
        except ValueError:
            print ("Ingresa un valor numerico valido.")

    while True:       # en lugar de arrojar una excepción debes mostrar una notificación adecuada
        try:                
            cantidad_prod =int (input("Ingresa la cantidad que deseas: ")) 
            if cantidad_prod > 0:
                break
            else:
                print("Ingresa una cantidad valida.")
        except ValueError:
            print ("Ingresa un numero valido entero. ")

    diccionario_productos = {
        "nombre" : nombre_prod,
        "precio" : precio_prod,
        "cantidad" : cantidad_prod
        }   
        
    lista_compras.append(diccionario_productos)
    print("Producto añadido correctamente. ")
    if lista_compras:
        print(" Lista de todos los productos: ")
    for producto in lista_compras:
        print(f"{producto['cantidad']} unidades de {producto['nombre']} a ${producto['precio']:.2f} cada un/a")
lista_compras = []

añadir_producto()

def buscar_prod (nombre_prod, lista_compras):
    busca_produ=str(input("Ingresa el producto que deseas buscar: ")) #Buscar adentro de la lista el diccionario para los productos con precio y cantidad
    for busca_produ in lista_compras:
        if busca_produ["nombre"].lower() == nombre_prod.lower():
            return busca_produ["precio"], busca_produ["cantidad"]
    return None
buscar_prod()
    #def actualizar_precio (): #Cambiar los datos adentro de la lista(dicc)


    #def eliminar_prod (): #Eliminar un producto de la lista con el nombre del prod


    # ACA una funcion LMBDA para calcular el valor total del inventario

def Menu():
    print ("""Bienvenido a la Tienda Riwi,Ingresa la opcion que deseas!:
    -----------------------Menu---------------------------
    1.Añadir Producto." 
    2.Consultar Productos.
    3.Actualizar Precio.
    4.Eliminar Productos.
    5.Calcular el Valor Total.""") 
while True:
    Menu()
    opcion = input("Selecciona una opcion. ")
    if opcion == 1:
        añadir_producto()
    elif opcion == 2:
        buscar_prod()
    elif opcion == 3:
        actualizar_precio()
    elif opcion == 4:
        eliminar_prod()
    #else
        #funcion lambda      ****#EN CONSTRUCCION****


    #ACA una funcion LMBDA para calcular el valor total del inventario
