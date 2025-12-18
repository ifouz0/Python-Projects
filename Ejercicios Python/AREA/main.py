 # Crea una única función (importante que sólo sea una) que sea capaz
 # de calcular y retornar el área de un polígono.
 # - La función recibirá por parámetro sólo UN polígono a la vez.
 # - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 # - Imprime el cálculo del área de un polígono de cada tipo.
import math


def area_triangulo(base, altura):
    return (base * altura) / 2

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

if __name__ == "__main__":
    # Cálculo áre Triangulo
    base=int(input("Ingrese la base del triángulo: "))
    altura=int(input("Ingrese la altura del triángulo: "))
    print(f"El área del triángulo de base {base} y altura {altura} es: {area_triangulo(base, altura)}")
    #Cálculo área Cuadrado
    lado =int(input("Ingrese el lado del cuadrado: "))
    print(f"El área del cuadrado de lado {lado} es: {area_cuadrado(lado)}")
    #Cálculo área Rectángulo
    base=int(input("Ingrese la base del rectángulo: "))
    altura=int(input("Ingrese la altura del rectángulo: "))
    print(f"El área del rectángulo de base {base} y altura {altura} es: {area_rectangulo(base, altura)}")
    print("\n")
    print("Gracias por usar el programa de cálculo de áreas.")