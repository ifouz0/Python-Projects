'''
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
'''


def balanced_expression(expression: str) -> bool:
    simbols = {'(': ')', '{': '}', '[': ']'}
    offset = []
    for c in expression:
        if c in simbols:
            offset.append(c)
        elif c in simbols.values():
            if not offset:
                return False
            last = offset.pop()
            if simbols[last] != c:
                return False
    return not offset
        
if __name__ == '__main__':
    expresion = input("Ingrese una expresión: ")
    if balanced_expression(expresion):
        print("La expresión está equilibrada.")
    else:
        print("La expresión no está equilibrada.")