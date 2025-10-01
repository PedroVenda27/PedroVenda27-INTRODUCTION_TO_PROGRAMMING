#5) Crie um programa que leia 2 strings do utilizador e indique qual das strings está
#primeiro na ordem alfabética.

nome1 = input("Introduza o Nome: ")
nome1 = nome1.strip()
nome2 = input("Introduza o Nome: ")
nome2 = nome2.strip()


if nome1.lower() < nome2.lower():
    print (nome1,"esta primeiro na ordem alfabetica que",nome2)
elif nome2.lower()  < nome1.lower() :
    print (nome2,"esta primeiro na ordem alfabetica que",nome1)
else:
    print ("os nomes são iguais" , nome1 , "=" , nome2)