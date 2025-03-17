from stack import ArrayStack

def reverse_data(archivo_stack):
    pila = ArrayStack()
    with open(archivo_stack, 'r', encoding='utf8') as archivo:
        for linea in archivo:
            pila.push(linea.strip())

    while not pila.is_empty():
        print((pila.pop()))

print(reverse_data("archivo_stack"))