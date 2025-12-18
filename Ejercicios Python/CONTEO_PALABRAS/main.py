'''
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 '''


def contar_palabras(texto):
    result = {}
    palabra_actual = ''
    for c in texto:
        if c != ' ' and c not in '.,;:!?¡¿"\'()[]{}':
            palabra_actual += c.lower()
        else:
            if palabra_actual:
                result[palabra_actual] = result.get(palabra_actual, 0) + 1
                palabra_actual = ''
    return result



if __name__ == '__main__':
    texto = input("Introduce un texto: ")
    conteo = contar_palabras(texto)
    for palabra, cantidad in conteo.items():
        print(f"La palabra '{palabra}' se repite {cantidad} veces.")