#!/usr/bin/env python3
# -*- coding: utf-8 -*-

segundos = int(input())

horas = segundos // 3600
print('Horas:', horas)

minutos = int((segundos - (horas * 3600)) / 60)
print('Minutos:', minutos)

segundos = int(segundos - (minutos * 60 + horas * 3600))
print('Segundos:', segundos)
