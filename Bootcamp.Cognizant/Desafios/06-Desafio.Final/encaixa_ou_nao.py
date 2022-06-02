#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input('Digite o numero de testes:'))
for i in range(n):
    x, y = input(' Digite o valor de X e Y ').split()
    teste = 0
    cont = 0
    if len(y) > len(x):
        print("nao encaixa")
    else:
        for j in range(len(y)):
            teste -= 1
            print(f'Valor de teste: {teste}')
            if x[teste] == y[teste]:
                cont += 1
                print(f'Valor de cont: {cont}')
        if cont == len(y):
            print("encaixa")
        else:
            print("nao encaixa")
