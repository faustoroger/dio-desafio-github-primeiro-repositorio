#!/usr/bin/env python3
# -*- coding: utf-8 -*-

counter = 0
for _ in range(6):
    number = float(input())
    if number > 0:
        counter += 1

print("\n{} valores positivos".format(counter))
