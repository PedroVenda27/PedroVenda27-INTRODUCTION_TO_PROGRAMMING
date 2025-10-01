# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
#"Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Serão relizadas 5 perguntas sobre o crime por favor reponda (1 = Sim) (2 = Não)")

pergunta1 =int(input("Telefonou para a vítima?: "))
pergunta2 =int(input("Esteve no local do crime?: "))
pergunta3 =int(input("Mora perto da vítima?: "))
pergunta4 =int(input("Devia para a vítima?: "))
pergunta5 =int(input("Já trabalhou com a vítima?: "))

if (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5) == 3 or (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5) == 4:
    print("Cumplice")
if (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5) == 5:
    print("Assasino")
if (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5) == 2:
    print("Suspeita")
if (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5) == 1 or (pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5) == 0:
    print("Inocente")
