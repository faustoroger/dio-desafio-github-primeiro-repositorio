#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# importação
from aula_07_4 import Televisao
from aula_07_2 import Calculadora
from aula_08_2 import contador_letras, teste

if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(10, 5)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra na lista: {}'.format(total_letras))
    print(teste())
