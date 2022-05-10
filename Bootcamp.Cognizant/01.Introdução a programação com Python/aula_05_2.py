#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

print(f'Sum: {sum(lista)}')
print(f'Min: {min(lista)}')
print(f'Max: {max(lista)}')

if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

if 'lobo' in lista_animal:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista. Será incluído.')
    lista_animal.append('lobo')
    # print(lista_animal)

print(lista_animal)
lista_animal.pop()
lista_animal.pop(1)
lista_animal.remove('elefante')
print(lista_animal)

