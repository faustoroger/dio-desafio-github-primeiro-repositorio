#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lista = [1, 3, 5, 7]
lista_animal = ['gato','cachorro', 'elefante', 'lobo', 'arara']
print(lista_animal[1])

nova_lista = lista_animal * 3
print(nova_lista)

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)


for x in lista_animal:
    print(x)

soma = 0
for y in lista:
    print(y)
    soma += y
print(soma)

