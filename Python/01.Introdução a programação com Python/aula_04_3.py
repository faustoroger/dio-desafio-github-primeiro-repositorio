#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))

b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Primeiro bimestre: '))

c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Primeiro bimestre: '))

d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Primeiro bimestre: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))
