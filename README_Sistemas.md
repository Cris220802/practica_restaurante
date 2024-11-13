# Sistema de Gestión de Pedidos de Restaurante Simulado

## Alumnos 
 - Felipe Martinez Reyna
 - Gerardo Issac Luna Rodarte
 - Cristopher Isaí Velázquez Medina
 - Rodrigo Emiliano Maldonado de la Cruz
 -  Rogelio Bustamante Ibarra
 
Este programa simula el flujo de pedidos y entrega de comida en un restaurante utilizando programación concurrente con hilos (threads) en Python. Cada "mesa" realiza un pedido de comida, y un "camarero" atiende y entrega los pedidos según un tiempo de preparación específico.

## Descripción del Proyecto

El sistema cuenta con las siguientes características:

- **Mesas:** Representadas como hilos, cada mesa realiza un pedido aleatorio de un menú predefinido.
- **Camareros:** Representados también como hilos, los camareros recorren las mesas para preparar y entregar los pedidos en función del tiempo de preparación de cada plato.
- **Menú:** El menú de opciones de comida está definido con tiempos de preparación en segundos:
  - Pizza: 8 segundos
  - Hamburguesa: 6 segundos
  - Ensalada: 4 segundos
  - Pasta: 5 segundos
  - Sopa: 3 segundos

El programa simula la concurrencia en un restaurante donde varias mesas pueden hacer pedidos y los camareros los gestionan y entregan. La ejecución finaliza cuando todas las mesas han recibido su pedido.

## Estructura del Código

### 1. Diccionario `tiempos_de_preparacion`

Define los tiempos de preparación de cada plato en segundos.

### 2. Clase `Mesa`

Representa una mesa en el restaurante. Cada mesa es un hilo que:
- Realiza un pedido aleatorio de uno de los elementos del menú.
- Utiliza un `lock` para asegurar que un camarero atienda solo a una mesa a la vez.

### 3. Clase `Camarero`

Representa a un camarero en el restaurante. Cada camarero es un hilo que:
- Recorre todas las mesas verificando si alguna tiene un pedido pendiente.
- Si una mesa tiene un pedido, el camarero simula el tiempo de preparación y entrega el pedido.
- Utiliza un `lock` para asegurar la exclusividad en el acceso a cada mesa.

### 4. Ejecución Principal

- Se crean 5 mesas y 3 camareros, que funcionan de forma independiente.
- Los hilos de las mesas y los camareros se inician, y el programa espera a que todos terminen de atender las mesas.
- Al finalizar, se imprime un mensaje indicando que todos los pedidos han sido entregados.

## Cómo Ejecutar el Código

1. Asegúrate de tener Python instalado en tu sistema.
2. Guarda el código en un archivo llamado `restaurante.py`.
3. Ejecuta el código con el siguiente comando:
   ```bash
   python restaurante.py
   ```

## Salida espereda

```bash
Mesa 1: Pedido de Pizza
Camarero 1: Preparando pedido de Pizza para la mesa 1
Camarero 1: Entregando pedido de Pizza a la mesa 1
...
Todos los pedidos han sido entregados
```
Estos mensajes muestran la interacción entre mesas y camareros y el proceso de preparación y entrega de los pedidos.

