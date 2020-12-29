#!/usr/bin/env python3

#importar a biblioteca sys
import sys

import re

#transformando o arquivo multifasta da linha de comandos em letras maiúsculas para padronizar e evitar erros ao rodar o script
dna = list(sys.argv[1].upper())

#Open Reading Frame inicia com os códons AUC

#verificando se o tamanho da sequência de dna é múltipla de 3

if len(dna)%3 == 0:
	print('A sequência de dna é múltiplo de 3')

#verificando se há códons de terminação, os quais são UAA, UAG, UGA

if 'TAA' in dna == True:
	print('TAA é o códon de terminação')

if 'TAG' in dna == True:
	print('TAG é o códon de terminação')

if 'TGA' in dna == True:
	print('TGA é o códon de terminação')

#procurando as sequências que iniciam com o códon de abertura e encerram com o códon de terminação

sequencia1 = re.search(r'ATG(.+?)TAG',dna).group(1)

sequencia2 = re.search(r'ATG(.+?)TAA',dna).group(2)

sequencia3 = re.search(r'ATG(.+?)TGA',dna).group(3)

#verificando o tamanho das sequências a fim de utilizar a sequência de maior comprimento

comprimento1 = len(sequencia1)
comprimento2 = len(sequencia2)
comprimento3 = len(sequencia3)

if comprimento1 > comprimento and comprimento3:
	maior_sequencia = sequencia1
elif comprimento2 > comprimento3:
	maior_sequencia = sequencia2
else:
	maior_sequencia = sequencia3

print('A maior sequência da fita de dna é:', maior_sequencia)

#escrevendo um arquivo com a maior sequência

f = open('ORF.fna', 'w')
f.write(maior_sequencia)
f.close


#escrevendo um arquivo complementar à maior sequência

peptideo = maior_sequencia.complement()

f2 = open('ORF.faa', 'w')
f2.write(peptideo)
f.close


