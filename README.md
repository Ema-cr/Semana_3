¡Por supuesto! Aquí tienes un ejemplo de un archivo README para este código:

---

# Tienda Riwi - Gestión de Productos

Este programa permite gestionar una lista de compras en una tienda virtual. Los usuarios pueden añadir productos, consultar la lista de productos, actualizar precios, eliminar productos y calcular el valor total de la compra.

## Funcionalidades

### 1. **Añadir Producto**

Permite al usuario agregar un producto a la lista de compras proporcionando:

* Nombre del producto.
* Precio del producto.
* Cantidad del producto.

Se realizan validaciones para asegurarse de que el nombre no esté vacío ni contenga números, que el precio sea un número positivo, y que la cantidad sea un número entero positivo.

### 2. **Consultar Productos**

Permite al usuario buscar un producto por su nombre. Si el producto se encuentra en la lista, se muestra el nombre, cantidad disponible y precio de cada unidad.

### 3. **Actualizar Precio**

Permite al usuario actualizar el precio de un producto existente en la lista de compras. Se debe ingresar el nombre del producto y el nuevo precio.

### 4. **Eliminar Producto**

Permite al usuario eliminar un producto de la lista de compras proporcionado el nombre del producto.

### 5. **Ver Valor Total**

Muestra el valor total de la compra, sumando el precio de todos los productos multiplicado por su respectiva cantidad.

### 0. **Salir**

Permite al usuario salir del programa y finalizar la ejecución.

---

## Requisitos

Este programa está escrito en Python 3. Asegúrate de tener Python 3.x instalado en tu sistema para ejecutar este código.

* Python 3.x

---

## Instrucciones de Uso

1. Clona o descarga este repositorio en tu computadora.

2. Abre una terminal o consola y navega hasta la carpeta donde se encuentra el archivo `tienda.py`.

3. Una vez que se ejecute el programa, aparecerá un menú con varias opciones. El usuario puede interactuar con el programa eligiendo las opciones del menú.

---

## Menú de Opciones

```
Bienvenido a la Tienda Riwi, Ingresa la opción que deseas!:
-----------------------Menu Principal---------------------------
1. Añadir producto.
2. Consultar productos.
3. Actualizar precio.
4. Eliminar productos.
5. Ver el Valor Total.
0. Salir.
```

### Opciones:

* **Opción 1**: Añadir un producto.
* **Opción 2**: Consultar los productos existentes en la lista.
* **Opción 3**: Actualizar el precio de un producto.
* **Opción 4**: Eliminar un producto.
* **Opción 5**: Ver el total de la compra (precio \* cantidad).
* **Opción 0**: Salir del programa.

---

## Ejemplo de Uso

```plaintext
Bienvenido a la Tienda Riwi, Ingresa la opción que deseas!:
-----------------------Menu Principal---------------------------
1. Añadir producto.
2. Consultar productos.
3. Actualizar precio.
4. Eliminar productos.
5. Ver el Valor Total.
0. Salir.

Selecciona una opción: 1
Ingresa el nombre del producto deseado: Manzanas
Ingresa el precio del producto deseado: 2.50
Ingresa la cantidad que deseas: 10
Producto añadido correctamente.

Lista de todos los productos:
10 unidades de Manzanas a $2.50 cada un/a

Selecciona una opción: 5
La suma de todos los productos es: $25.00
```

---

## Estructura del Código

* **`añadir_producto()`**: Permite añadir productos a la lista de compras con las validaciones necesarias.
* **`buscar_prod()`**: Permite buscar productos por nombre en la lista de compras.
* **`actualizar_precio()`**: Permite actualizar el precio de un producto en la lista.
* **`eliminar_producto()`**: Permite eliminar un producto de la lista.
* **`mostrar_total()`**: Calcula y muestra el total de la compra.
* **`Menu()`**: Interfaz de usuario que permite elegir una opción del menú y ejecutar la función correspondiente.

---

## Contribución

Si deseas mejorar este proyecto o agregar nuevas funcionalidades, ¡siéntete libre de crear un pull request!

---
