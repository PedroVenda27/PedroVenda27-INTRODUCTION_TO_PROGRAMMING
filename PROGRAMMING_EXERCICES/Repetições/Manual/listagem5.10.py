pontos = 0
questão = 1

while questão <=3:

 resposta = input("Introduza a resposta a questão %d: " % questão )

 # NOTAS
 # %d = Vai Buscar o Valor 


 if questão == 1 and resposta == "b":
    pontos = pontos +1

 if questão == 2 and resposta == "a": 
    pontos = pontos +1

 if questão == 3 and resposta == "d": 
    pontos = pontos +1
 questão = questão + 1
    
print( "O aluno fes %d ponto(s)" % pontos )