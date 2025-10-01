tabuada = -1

while tabuada < 0 or tabuada >= 20:
    tabuada = int(input("Diz me um número entre 1 - 20: "))
teste = 1
while teste <=10:

    print(tabuada, "*", teste, "=", tabuada*teste)
    teste = teste+1