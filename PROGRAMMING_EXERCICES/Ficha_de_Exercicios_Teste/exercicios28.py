# 28) Escreva um programa que, a partir do preço em euros e do
# dinheiro entregue, apresente o troco usando o menor número
# possível de moedas.

preçoapagar= float(input("Introduza o preço a pagar: "))
dinheirointregue= float(input("Introduza o dinheiro que intregou para pagar: "))

troco = dinheirointregue-preçoapagar
print("Troco =",troco)
print(" O troco deverá ser dado da seguinte forma:")

moedas2 = int(troco / 2)
print(moedas2 , "moeda(s) de 2 euros")
troco = troco - (2*moedas2)

moedas1 = int(troco / 1)
print(moedas1 , "moeda(s) de 1 euros")
troco = troco - (1*moedas1)

moedas050 = int(troco / 0.5)
print(moedas050 , "moeda(s) de 50 centimos")
troco = troco - (0.5*moedas050)

moedas020 = int(troco / 0.2)
print(moedas020 , "moeda(s) de 20 centimos")
troco = troco - (0.2*moedas020)

moedas010 = int(troco / 0.1)
print(moedas010 , "moeda(s) de 10 centimos")
troco = troco - (0.1*moedas010)

moedas005 = int(troco / 0.05)
print(moedas005 , "moeda(s) de 5 centimos")
troco = troco - (0.05*moedas005)

moedas002 = int(troco / 0.02)
print(moedas002 , "moeda(s) de 2 centimos")
troco = troco - (0.02*moedas002)

moedas001 = int(troco / 0.01)
print(moedas001 , "moeda(s) de 1 centimos")
troco = troco - (0.01*moedas001)