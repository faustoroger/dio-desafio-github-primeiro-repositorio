#!/usr/bin/env python3
# -*- coding: utf-8 -*-

segundos = int(input())

horas = segundos // 3600
print('Horas:', horas)

minutos = int((segundos - (horas * 3600)) / 60)
print('Minutos:', minutos)

segundos = int(segundos - (minutos * 60 + horas * 3600))
print('Segundos:', segundos)

# # horas = int((segundos + (minutos * 60)) / 3600)

# # minutos = int(minutos - (horas * 60))
# # print('Minutos:', minutos)

# print("{}:{}:{}".format(horas, minutos, segundos))




# segundos = int(input())

# minutos = #TODO Implementar a formula para calcular os minutos.
# segundos = int(segundos - (minutos * 60))
# horas = #TODO Implementar a formula para calcular as horas.
# minutos = int(minutos - (horas * 60))

# print("{}:{}:{}".format(horas, minutos, segundos))