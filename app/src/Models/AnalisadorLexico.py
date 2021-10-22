# -*- coding: utf-8 -*-
#coding: utf-8

from os.path import dirname, abspath
from AnalisadorSintatico import *
from FileReader import FileReader
from FileWriter import FileWriter
from automato import Automato


def readFileInputs(path, pathOutput, filename, index):
    #tokens = Automato(path + '\\' + filename).getTokens()
    tokens = Automato(path + '/' + filename).getTokens()

    if len(tokens['errors']) >= 1:
        for idx, token in enumerate(tokens['errors']):
            lineTxt = str(token.getLine()+1) + ' ' + \
                token.getType() + ' ' + token.getWord()
            print(lineTxt)
            print('\n')
        print(len(tokens['errors']),
              "erro(s) léxico(s) detectado no arquivo: entrada" + str(index) + '.txt')
        print('Por favor, corrija entes de prosseguir...')
        print('\n')
    else:
        AnalisadorSintatico(tokens).parse()

    FileWriter.write(path, pathOutput, filename, index, tokens)


def main():
    path = dirname(dirname(dirname(dirname(abspath(__file__)))))
    pathOutput = path + '\\output'
    pathInput = path + '\\input'
    pathOutput = path + '/output'
    pathInput = path + '/input'

    try:
        inputFiles = FileReader.getInputFiles(pathInput)
        for idx, file in enumerate(inputFiles):
            readFileInputs(pathInput, pathOutput, file[0], file[1])

    except OSError:
        print("Erro ao escanear e analisar um dos arquivos")


main()
