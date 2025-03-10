from src.udemdatastructures.queue import ArrayQueue


class Ticketing_system:
    def __init__(self):
        self.cola_clientes = ArrayQueue()
        self.id = 1

    def llegada_clientes(self):
        cliente_id = self.id
        print (f"El cliente {cliente_id} ha llegado y está en espera")
        self.cola_clientes.enqueue(cliente_id)
        self.id +=1

    def atender_cliente(self):
        if self.cola_clientes.is_empty():
            print("No hay ningún cliente en espera")
        else:
            cliente_id = self.cola_clientes.dequeue()
            print(f"Atendiendo al cliente{cliente_id}")


taquilla = Ticketing_system()

taquilla.llegada_clientes()
taquilla.llegada_clientes()
taquilla.llegada_clientes()

taquilla.atender_cliente()
taquilla.atender_cliente()
taquilla.atender_cliente()
taquilla.atender_cliente()