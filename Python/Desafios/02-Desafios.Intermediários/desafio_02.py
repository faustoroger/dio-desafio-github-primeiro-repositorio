#!/usr/bin/env python3
# -*- coding: utf-8 -*-

X, Y = map(int, input().split())
while (True):
    floor = min(X, Y)
    top = max(X, Y)
    if (X < Y):
        print("Crescente")
    elif (X > Y):
        print("Decrescente")
    elif ( X == Y):
        break
    X, Y = map(int, input().split())
