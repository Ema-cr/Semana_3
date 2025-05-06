def Menu():
    print ("""Bienvenido a la Tienda Riwi,Ingresa la opcion que deseas!:
    -----------------------Menu---------------------------
    1.Añadir Producto." 
    2.Consultar Productos.
    3.Actualizar Precio.
    4.Eliminar Productos.
    5.Calcular el Valor Total.""") 

while True:
    print (Menu())
    break

lista_compras = []        #Lista meterle diccionarios

def añadir_producto ():
     nombre_prod = input("")
     precio_prod = float (input(""))      # Si estás solicitando un número y el usuario ingresa una letra
     cantidad_prod =int (input(""))      # en lugar de arrojar una excepción debes mostrar una notificación adecuada

# def buscar_prod  (): #Buscar adentro de la lista el diccionario para los productos con precio y cantidad


# def actualizar_precio (): #Cambiar los datos adentro de la lista(dicc)


# def eliminar_prod (): #Eliminar un producto de la lista con el nombre del prod


# #ACA una funcion lmbda para calcular el valor total del inventario