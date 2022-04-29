#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pathlib
import shutil

# print(os.path.dirname(os.path.abspath(__file__)))
cur_dir = str(pathlib.Path(__file__).parent.absolute())
path_file = cur_dir + os.sep


def escrever_arquivo(texto):
    arquivo = open(path_file + 'teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(path_file + nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(path_file + nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(path_file + nome_arquivo, 'r')
    aluno_nota = arquivo.read().split('\n')
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media =  lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo, dest_dir):
    shutil.copy(nome_arquivo, dest_dir)


def move_arquivo(nome_arquivo, dest_dir):
    shutil.move(nome_arquivo, dest_dir)


if __name__ == '__main__':
    # escrever_arquivo('Primeira linha.\n')
    # aluno = 'Cesar,8,7,5,3\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')    
    print(media_notas('notas.txt'))
    copia_arquivo(path_file + 'notas.txt', '/tmp/')
    # move_arquivo(path_file + 'notas.txt', path_file + 'notas.rtf')
