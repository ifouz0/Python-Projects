'''
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
'''

def elimina_caracteres (str1, str2) -> list:
    out1 = ""
    out2 = ""
    if not str1 or not str2:
        return ["Datos incorrectos", "Datos incorrectos"]
    for c in str1:
        out1 += c if c.lower() not in str2.lower() else ""
    for c in str2:
        out2 += c if c.lower() not in str1.lower() else ""
    return [out1, out2]

if __name__ == "__main__":
    str1 = input("Introduce la primera cadena: ")
    str2 = input("Introduce la segunda cadena: ")
    resultado = elimina_caracteres(str1, str2)
    print (f'Cadena {str1} sin caracteres de {str2}: {resultado[0]}')
    print (f'Cadena {str2} sin caracteres de {str1}: {resultado[1]}')
