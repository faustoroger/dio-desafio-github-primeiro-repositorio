#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lados = [float(x) for x in input().split()]

a = lados[0]
b = lados[1]
c = lados[2]

if a + b > c and a + c > b and b + c > a:
    perimetro = a+b+c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c)/2
    print(f"Area = {area:.1f}")
