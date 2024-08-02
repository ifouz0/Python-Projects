from pyNumRomans.NumRomans import numRomans

index = int(input('Introduce num Decimal: '))
num = numRomans(num=index)
print(f'Numero Decimal: {num.number:03d}')
num_roman = num.converToRoman()
print(f'Numero Romano: {num_roman}')

num = numRomans(num=123)
num2 = numRomans(num=321)
num3 = numRomans(num=456)
num4 = numRomans(num=654)

#print(f'Num Clases: {numRomans.count()}')
index2=input('Numero Romano: ')
print(f'Numero Romano{index2}')
print(f'Numero Decimal: {num.converToNum(index2)}')
