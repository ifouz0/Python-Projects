'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''

def fizz_buzz():
    for i in range(1,101):
        num=True
        if i % 3 == 0:
            print("fizz", end="")
            num=False
        if i % 5 == 0:
            print("buzz", end="")
            num=False  
        print (str(i)) if num else print("")


if __name__ == "__main__":
    print("FIZZ BUZZ")
    print("----------")
    print("Números del 1 al 100 con las sustituciones indicadas:\n")
    print("Multiplos de 3 por 'fizz'")
    print("Multiplos de 5 por 'buzz'")
    print("Multiplos de 3 y 5 por 'fizzbuzz'")
    print("----------")

    fizz_buzz()