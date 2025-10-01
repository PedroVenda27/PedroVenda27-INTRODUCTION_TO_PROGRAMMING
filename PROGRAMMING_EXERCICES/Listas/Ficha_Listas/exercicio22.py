# 22) Desenvolva um programa para simular o embaralhar de um baralho
# de cartas. Use um vetor e embaralhe as cartas fazendo trocas entre
# os elementos. Depois dê 4 mãos de 13 cartas.

import random

# criar um baralho de cartas
baralho = [
    '2 de Paus', '3 de Paus', '4 de Paus', '5 de Paus', '6 de Paus', '7 de Paus', '8 de Paus', '9 de Paus', '10 de Paus', 'Valete de Paus', 'Dama de Paus', 'Rei de Paus', 'Ás de Paus',
    '2 de Ouros', '3 de Ouros', '4 de Ouros', '5 de Ouros', '6 de Ouros', '7 de Ouros', '8 de Ouros', '9 de Ouros', '10 de Ouros', 'Valete de Ouros', 'Dama de Ouros', 'Rei de Ouros', 'Ás de Ouros',
    '2 de Copas', '3 de Copas', '4 de Copas', '5 de Copas', '6 de Copas', '7 de Copas', '8 de Copas', '9 de Copas', '10 de Copas', 'Valete de Copas', 'Dama de Copas', 'Rei de Copas', 'Ás de Copas',
    '2 de Espadas', '3 de Espadas', '4 de Espadas', '5 de Espadas', '6 de Espadas', '7 de Espadas', '8 de Espadas', '9 de Espadas', '10 de Espadas', 'Valete de Espadas', 'Dama de Espadas', 'Rei de Espadas', 'Ás de Espadas'
]

# baralhar as cartas
random.shuffle(baralho)


# Dar as Cartas print das Mãos

# MÃO 1

mao1 = []
for n in range(0,13):
     mao1.append(baralho[n])
     n = n + 1 

# Normal
#print("Mão do jogador 1:", mao1)
# Carta por Linha
print("Mão do jogador 1:")
for carta in mao1:
     print(carta)




# MÃO 2

mao2 = []
for n in range(13,26):
     mao2.append(baralho[n])
     n = n + 1 

# Normal
#print("Mão do jogador 2:", mao2)
# Carta por Linha
print("Mão do jogador 2:")
for carta in mao2:
     print(carta)




# MÃO 3
     
mao3 = []
for n in range(26,39):
     mao3.append(baralho[n])
     n = n + 1 

# Normal
#print("Mão do jogador 3:", mao3)
# Carta por Linha
print("Mão do jogador 3:")
for carta in mao3:
     print(carta)




# MÃO 4
     
mao4 = []
for n in range(39,52):
     mao4.append(baralho[n])
     n = n + 1 

# Normal
#print("Mão do jogador 4:", mao4)
# Carta por Linha
print("Mão do jogador 4:")
for carta in mao4:
     print(carta)