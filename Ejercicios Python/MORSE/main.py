'''
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
'''
alfabeto_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}

def texto_a_morse(texto):

    
    texto = texto.upper()
    morse = []
    
    for char in texto:
        if char in alfabeto_morse:
            morse.append(alfabeto_morse[char])
        else:
            morse.append(char)  # Mantener caracteres no soportados sin cambios
    
    return ' '.join(morse)

def morse_a_texto(morse):
    morse = morse.split(' ')
    texto = []
    for char in morse:
        if char == '':
            texto.append(' ')
        elif char in alfabeto_morse.values():
            for key, value in alfabeto_morse.items():
                if value == char:
                    texto.append(key)
                    break
        else:
            texto.append(char)
    return ''.join(texto)



def es_morse(texto):
    for char in texto:
        if char not in ['.', '-', ' ']:
            return False
    return True

if __name__ == "__main__":

    entrada = input("Introduce el texto o código morse: ")
    
    if es_morse(entrada):
        print("Detectado código morse.")
        resultado = morse_a_texto(entrada)
        print("Texto traducido:", resultado)
    else:
        print("Detectado texto natural.")
        resultado = texto_a_morse(entrada)
        print("Código morse traducido:", resultado)