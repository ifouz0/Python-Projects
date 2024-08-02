"""
Module Name: pylib.utilities.strutils
Module Description: String Utilities Module
"""

import random
import re
import string
from typing import Iterable
import unicodedata

# Atributos o variables a nivel de módulo
EMPTY:str = ""
WHITESPACE:str = " "
DEGREES:str = "\u00B0"
DEGREES_CELSIUS:str= "\u2103"
DEGREES_FAHRENHEIT:str = "\u2109"
PRIME: str = "\u2032"
DOUBLE_PRIME: str = "\u2033"
HAPPY_FACE: str = "\U0001F603"
VOWELS_UPPERCASE: str  = "AEIOU"
VOWELS_LOWERCASE: str  = "aeiou"

# Funciones o métodos a nivel de módulo (Helpers / Utilities Functions)
def abbreviate(text: str, max_length: int, placeholder: str = "...") -> str:
    """Python DocString"""
    return text if len(text) <= max_length else f"{text[0:max_length - len(placeholder)]}{placeholder}"


def random_code(length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> str:
    """Python DocString"""
    alphabet = f"{string.ascii_uppercase if uppercase_letters else EMPTY}{string.ascii_lowercase if lowercase_letters else EMPTY}{string.digits if digits else EMPTY}{string.punctuation if punctuation else EMPTY}"
    code = EMPTY
    for i in range(length):
        code += random.choice(alphabet)
    return code


def random_code_v2(length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> str:
    """Python DocString"""
    alphabet = f"{string.ascii_uppercase if uppercase_letters else EMPTY}{string.ascii_lowercase if lowercase_letters else EMPTY}{string.digits if digits else EMPTY}{string.punctuation if punctuation else EMPTY}"
    return EMPTY.join([random.choice(alphabet) for i in range(length)])


def random_codes(num_codes: int, length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> list[str]:
    """Python DocString"""
    codes = []
    for i in range(num_codes):
        code = random_code(length, uppercase_letters, lowercase_letters, digits,punctuation)
        codes.append(code)
    return codes


def random_codes_v2(num_codes: int, length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> list[str]:
    """Python DocString"""
    codes = [random_code(length, uppercase_letters, lowercase_letters, digits,punctuation) for i in range(num_codes)]
    return codes

def trim(text: str) -> str:
    """Python DocString"""
    return re.sub(r"\s+", WHITESPACE, text.strip())


def no_whitespaces(text: str) -> str:
    """Python DocString"""
    return re.sub(r"\s+", EMPTY, text)


def no_symbols(text: str) -> str:
    """Python DocString"""
    return re.sub(fr"[{string.punctuation}]+", EMPTY, text)


def only_digits(text: str) -> str:
    """Python DocString"""
    return re.sub(r"[^0-9]", EMPTY, text)


def normalize(text: str) -> str:
    """Python DocString"""
    text_nfd = unicodedata.normalize("NFD", text)
    return ''.join([c for c in text_nfd if unicodedata.category(c) != 'Mn'])
    #return re.sub(r"\p{Mn}", EMPTY, text_nfd)


def choices(values: Iterable[object], k: int) -> list[object]:
    
    result = [random.choice(values) for i in range(k)]
    return result


def letters(text: str) -> tuple[str]:
    """Python DocString"""
    text_upper = text.upper()

    letters = [letter for letter in string.ascii_uppercase if letter in text_upper]
    return tuple(letters)


def vowels(text: str) -> tuple[str]:
    """Python DocString"""
    text_upper = text.upper()

    vowels = [vowel for vowel in "AEIOU" if vowel in text_upper]
    return tuple(vowels)


def digits(text: str) -> tuple[str]:
    """Python DocString"""
    text_upper = text.upper()

    digits = [digit for digit in string.digits if digit in text_upper]
    return tuple(digits)


def letters_count(text: str, show_empty:bool = False) -> dict[str,int]:
    """Python DocString"""
    text_lower = text.lower()
    letters_c = {}
    for letter in string.ascii_lowercase:
        if (text_lower.count(letter) != 0 or show_empty):
            letters_c[letter] = text_lower.count(letter)

    return letters_c


def letters_count_v2(text: str, show_empty:bool = False) -> dict[str,int]:
    """Python DocString"""
    text_lower = text.lower()
    letters_c = {letter: text_lower.count(letter) for letter in string.ascii_lowercase if (text_lower.count(letter) != 0 or show_empty)}
    return letters_c


def vowels_count(text: str, show_empty:bool = False) -> dict[str,int]:
    """Python DocString"""
    text_lower = text.lower()
    vowels_c = dict()
    for vowel in VOWELS_LOWERCASE:
        if (text_lower.count(vowel) != 0 or show_empty):
            vowels_c[vowel] = text_lower.count(vowel)

    return vowels_c


def vowels_count_v2(text: str, show_empty:bool = False) -> dict[str,int]:
    """Python DocString"""
    text_lower = text.lower()
    vowels_c = {vowel: text_lower.count(vowel) for vowel in VOWELS_LOWERCASE if (text_lower.count(vowel) != 0 or show_empty)}
    return vowels_c



def digits_count(text: str, show_empty:bool = False) -> dict[str,int]:
    """Python DocString"""
    text_lower = str.lower()
    digits_c = {}
    for digit in string.digits:
        if (text_lower.count(digit) != 0 or show_empty):
            digits_c[digit] = text_lower.count(digit)

    return digits_c


def digits_count_v2(text: str, show_empty:bool = False) -> dict[str,int]:
    """Python DocString"""
    text_lower = text.lower()
    digits_c = {digit: text_lower.count(digit) for digit in string.digits if (text_lower.count(digit) != 0 or show_empty)}
    return digits_c


def to_morse(text: str) -> tuple[str]:
    """Python Docstring"""
    alphabet = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                 'I':'..', 'J':'.---', 'K':'-.-',  'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
                 '1':'.----', '2':'..---', '3':'...--',  '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                 '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ' : ' '}
    
    text_upper = text.upper()
    result = [alphabet[char] for char in text_upper if char in alphabet]
    return tuple(result)


def to_icao(text: str) -> tuple[str]:
    """Python Docstring"""
    alphabet = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H': 'Hotel', 'I':'India', 'J':'Juliet', 
                'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 
                'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu', ' ' : ' '}

    text_upper = text.upper()
    result = [alphabet.get(char) for char in text_upper if char in alphabet]
    return tuple(result)



def num_chars(text: str) -> int:
    """Python DocString"""
    return len(no_whitespaces(text))


def num_words(text: str) -> int:
    """Python DocString"""
    return len(no_symbols(text).split())


def word_count(text: str, word: str) -> int:
    """Python DocString"""
    return (no_symbols(text.lower()).count(word.lower()))


def words_count(text: str) -> dict[str,int]:
    """Python DocString"""
    words = no_symbols(text.lower()).split()
    words_c = {}
    for word in words:
        if word in words_c:
            continue
        words_c[word] = no_symbols(text.lower()).count(word)

    return words_c
