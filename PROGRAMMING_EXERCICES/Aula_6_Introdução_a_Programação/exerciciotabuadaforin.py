 #Tabuada com for In


tabuada = -1

while tabuada < 0 or tabuada >= 20:
    tabuada = int(input("Diz me um número entre 1 - 20: "))


#versão ciclo for 
for i in range(1,11):
     res = tabuada * i
     print(tabuada, "x", i, "=", res)

