#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input())
n = list()

for i in range(10):
    n.append(x)
    x = n[i] * 2
    print(f'N[{i}] = {n[i]}')
