# 20) Crie um programa que simule 100 lançamentos de 2 dados, guarde
# os resultados em vetores e produza uma estatística. 

vetor1 = []
vetor2 = []

import random

# Dado 1
for x in range (0,100):
     dado1 = random.randint(1,6)
     vetor1.append(dado1)

# Dado 2
for x in range (0,100):
     dado2 = random.randint(1,6)
     vetor2.append(dado2)

print("valores do Dado 1: " , vetor1)

print("valores do Dado 2: " , vetor2)
