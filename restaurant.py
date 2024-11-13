import threading
import random
import time

# Opciones de comida y sus tiempos de preparación en segundos
tiempos_de_preparacion = {
    "Pizza": 8,
    "Hamburguesa": 6,
    "Ensalada": 4,
    "Pasta": 5,
    "Sopa": 3
}

# Clase para representar una Mesa
class Mesa(threading.Thread):
    def __init__(self, id_mesa):
        super().__init__()
        self.id_mesa = id_mesa
        self.pedido = None
        self.lock = threading.Lock()

    def run(self):
        # Solicitar un pedido aleatorio
        with self.lock:
            self.pedido = random.choice(list(tiempos_de_preparacion.keys()))
            print(f"Mesa {self.id_mesa}: Pedido de {self.pedido}")
            time.sleep(random.uniform(1, 3))  # Simular tiempo para hacer el pedido

# Clase para representar un Camarero
class Camarero(threading.Thread):
    def __init__(self, id_camarero, mesas):
        super().__init__()
        self.id_camarero = id_camarero
        self.mesas = mesas

    def run(self):
        while True:
            for mesa in self.mesas:
                if mesa.lock.acquire(blocking=False):  # Intentar adquirir el lock de la mesa sin bloquear
                    if mesa.pedido:  # Si hay un pedido en la mesa
                        tiempo_preparacion = tiempos_de_preparacion[mesa.pedido]
                        print(f"Camarero {self.id_camarero}: Preparando pedido de {mesa.pedido} para la mesa {mesa.id_mesa}")
                        time.sleep(tiempo_preparacion)  # Simular tiempo de preparación según el pedido
                        print(f"Camarero {self.id_camarero}: Entregando pedido de {mesa.pedido} a la mesa {mesa.id_mesa}")
                        mesa.pedido = None  # Pedido entregado
                    mesa.lock.release()  # Liberar el lock después de atender

            # Verificar si todas las mesas han sido atendidas
            if all(mesa.pedido is None for mesa in self.mesas):
                return

# Crear las mesas y camareros
mesas = [Mesa(i + 1) for i in range(5)]
camareros = [Camarero(i + 1, mesas) for i in range(3)]

# Iniciar las mesas
for mesa in mesas:
    mesa.start()

# Iniciar los camareros
for camarero in camareros:
    camarero.start()

# Esperar a que todas las mesas terminen
for mesa in mesas:
    mesa.join()

# Esperar a que todos los camareros terminen
for camarero in camareros:
    camarero.join()

print("Todos los pedidos han sido entregados.")