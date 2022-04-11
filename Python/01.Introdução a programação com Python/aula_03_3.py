a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))

b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Primeiro bimestre: '))

c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Primeiro bimestre: '))

d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Primeiro bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi informada alguma nota errada')
