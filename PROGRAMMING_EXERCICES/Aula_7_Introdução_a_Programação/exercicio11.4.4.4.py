# Variavel de Saida
idade_mais_jovem = 130
nome_mais_jovem =""

perguntas = 2 # variavel de controlo

while True:
    if perguntas == 2:
        nome_consola = input("Introduza um Nome")
        if nome_consola == "STOP" or nome_consola == "stop":
            break
        if nome_consola == "":
            print("AVISO: Nome Inválido")
        else:
            perguntas = 1

    if perguntas == 1:
        idade_consola = int(input(f"{nome_consola} , Introduza a sua idade"))
        if idade_consola > 0 and idade_consola < 130:   
            perguntas = 2 
            if idade_consola < idade_mais_jovem:
                idade_mais_jovem = idade_consola
                nome_mais_jovem = nome_consola
        else:
            print("AVISO:Idade invalida!")  

if nome_mais_jovem == "":
    print("Não foi introduzida qualquer nome e idade")
else:
    print(f"A Pessoa mais nova Chama-se {nome_mais_jovem}, e tem {idade_mais_jovem} anos")     