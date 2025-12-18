#  Escribe una función que reciba dos palabras (String) y retorne
# * verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS
# *   las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.
 

def anagrama(s1, s2):
    index = 0
    if s1 == s2:
       return False
    for index in range(len(s1)):
       if s1[index] not in s2:
          return False
    for index in range(len(s2)):
       if s2[index] not in s1:
          return False
    return True
    

if __name__ == "__main__":
    print(anagrama("roma", "amor"))  # True
    print(anagrama("roma", "amorx")) # False
    print(anagrama("roma", "ramo")) # True
    print(anagrama("roma", "roma"))  # False
    
