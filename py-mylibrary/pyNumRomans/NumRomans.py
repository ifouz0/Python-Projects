'''
    Module: Clase para convertir numeros romanos en numeros enteros y viceversa.
            El número máximo es 999.
    Author: Iván 
    Version: 1.0
'''
# Importaciones del módulo


# Atributos a nivel de módulo

UNIDADES = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
DECENAS = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
CENTENAS = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

# Definición clase
class numRomans:
    #Atributos a nivel de Clase
    _count: int = 0
    def __init__(self, num: int) -> None:
        self._number = num
        self._count += 1
    
    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        self._number = number
    
    @property
    def count(self) -> int:
        return self._count

    def count(cls) -> int:
        return cls._count

    def converToRoman(self) -> str:
        con = f'{self.number:03d}'
        return f'{CENTENAS[int(con[0])]}{DECENAS[int(con[1])]}{UNIDADES[int(con[2])]}'

    def converToNum(self, roman: str) -> int:
        romanValue = {'I':1, 'IV':4, 'V':5, 'IX': 9, 'X':10, 'XL':40, 'L':50, 'XC': 90, 'C':100, 'CD': 400, 'D':500, 'CM': 900}
        index: int = 0
        result: int =0
        while index < len(roman):
            if (roman[index:index+2] in romanValue) and (index +1  < len(roman)):
                result += romanValue[roman[index:index+2]]
                index += 2
            else:
                result += romanValue[roman[index]]
                index += 1
        return result
