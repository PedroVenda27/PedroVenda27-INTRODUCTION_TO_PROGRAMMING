#6) Crie um jogo com 3 advinhas do tipo "Qual a cor do cavalo branco do
# Napoleão?", cada uma com 3 alternativas, apresentando o resultado final

pontos = 0

# PERGUNTA 1

print(" 1) Qual a cor do cavalo branco de Napoleão?")
print( "A) = PRETO" )
print( "B) = BRANCO" )
print( "C) = CASTANHO" )

resposta = input("Escolha a alternativa correta (A, B ou C): ").upper()

if resposta == "B":
    pontos = pontos + 1

# PERGUNTA 2

print("2)  Qual o resultado da operação 3 + 1?")

print("A) 2")
print("B) 6")
print("C) 4")

resposta = input("Escolha a alternativa correta (A, B ou C): ").upper()
 
if resposta == "C":
    pontos += 1

# PERGUNTA 3

print("3)  Qual o animal mais pesado do mundo?")

print("A) Baleia Azul")
print("B) Elefante")
print("C) Sua Mãe")

resposta = input("Escolha a alternativa correta (A, B ou C): ").upper()
 
if resposta == "C":
    pontos += 1

print("Você acertou" , pontos , "perguntas")
