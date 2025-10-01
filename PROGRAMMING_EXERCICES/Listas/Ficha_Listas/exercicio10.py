# 10) Escreva um programa que preencha um vetor de 20 posições com
# os primeiros 20 números primos. 


i = 2
primos = []

while len(primos) < 20:
  e_primo = True
  for x in range(2, i):
    if i % x == 0:
      e_primo = False
      break
  if e_primo:
    primos.append(i)
  i += 1

print(primos)
