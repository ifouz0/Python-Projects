'''
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def decimal_a_binario(numero_decimal) -> str:
    if numero_decimal == 0:
        return "0"
    binario = ""
    while numero_decimal > 0:
        bit = numero_decimal % 2
        binario = str(bit) + binario
        numero_decimal //= 2
#        print(numero_decimal)
    return binario
def binario_a_decimal(numero_binario: str) -> int:
    decimal = 0
    longitud = len(numero_binario)
    for i in range(longitud):
        bit = int(numero_binario[i]) * (2 ** (longitud - 1 - i))
        decimal += bit
    return decimal  

if __name__ == "__main__":
    numero = int(input("Introduce un número decimal: "))
    resultado = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {resultado}")
#   print(f"El número {resultado} en decimal es: {binario_a_decimal(resultado)}")
    binario = input("Introduce un número binario: ") 
    for c in binario:
        if c not in '01':
            print("El número binario no es válido.")
            exit()
    print(f"El número {binario} en decimal es: {binario_a_decimal(binario)}")
 #  print(f"El número {binario_a_decimal(binario)} en binario es: {decimal_a_binario(binario_a_decimal(binario))}")


