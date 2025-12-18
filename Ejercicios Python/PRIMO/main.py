
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
#        print (str(i))
#        print(str(n))
        if n % i == 0:
            return False
    return True



if __name__ == "__main__":
    numeros = range(1, 101)
    print("Números primos entre 1 y 100:")
    for num in numeros:
        if es_primo(num):
            print(str(num))
    print("\n")
    print("\n")
    print("Fin de la lista de números primos.")
