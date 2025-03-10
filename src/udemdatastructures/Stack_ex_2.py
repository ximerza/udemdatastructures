
from stack import ArrayStack

def matching_delimiters(expresion):
    abierto = ArrayStack()
    pares = {')': '(', ']': '[', '}': '{'}

    for elemento in expresion:
        if elemento in "{([":
            abierto.push(elemento)
        elif elemento in "})]":
            if abierto.is_empty() or abierto.pop() != pares[elemento]:
                return False

    return abierto.is_empty()

expresion = "[()]"
print(matching_delimiters(expresion))

