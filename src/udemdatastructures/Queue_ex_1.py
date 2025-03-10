from src.udemdatastructures.queue import ArrayQueue

class CallCenter:
    def __init__(self):
        self.cola_llamadas = ArrayQueue()

    def recibir_llamada(self, numero):
        print(f"llamada del número {numero}")
        self.cola_llamadas.enqueue(numero)

    def atender_llamada(self):
        if self.cola_llamadas.is_empty():
            print("No hay llamadas pendientes")
        else:
            numero = self.cola_llamadas.dequeue()
            print(f"Atendiendo llamada del número {numero}")

llamadas = CallCenter()

llamadas.recibir_llamada("1")
llamadas.recibir_llamada("2")
llamadas.recibir_llamada("3")

llamadas.atender_llamada()
llamadas.atender_llamada()
llamadas.atender_llamada()
llamadas.atender_llamada()