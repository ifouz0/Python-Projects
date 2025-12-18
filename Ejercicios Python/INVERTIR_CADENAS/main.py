'''/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */ '''

def invertir_cadena(cadena):
    result = ""
    for c in cadena:
        result = c + result
    return result

if __name__ == "__main__":
    texto = input("Introduce una cadena de texto: ")
    print("Cadena invertida:", invertir_cadena(texto))