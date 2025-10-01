
# from decimal import Decimal
# Variavel de Saida

nota_maior = 0
nome_melhor_nota =""
ciclos = 0
total = 0
nota_consola = 0

perguntas = 2 # variavel de controlo

while True:
    if perguntas == 2:
        nome_consola = input("Introduza um Nome: ")
        if nome_consola == "STOP" or nome_consola == "stop":
            break
        if nome_consola == "":
            print("AVISO: Nome Inválido")
        else:
            perguntas = 1

    if perguntas == 1:
        nota_consola = int(input(f"{nome_consola} , Introduza a sua classificação a Português: "))
        if nota_consola > 0 and nota_consola <= 20:   
            perguntas = 2 
            if nota_consola > nota_maior:
                nota_maior = nota_consola
                nome_melhor_nota = nome_consola
                total = (nota_consola + total)
                ciclos = (ciclos + 1)
                mediatotal = (total / ciclos)
        else:
            print("AVISO:Nota invalida!")  

if nome_melhor_nota == "":
    print("Não foi introduzida qualquer nome e idade")
else:
    print(f"A Pessoa Com melhor Classificação a Portugues Chama-se {nome_melhor_nota}, e obteve a classificação de {nota_maior} Valores") 
    print(f"A Media das classificaçoes à disciplina de Portugues é {mediatotal} Valores ") 
   
    print(F" {total} " )
    print(f"{ciclos}")
