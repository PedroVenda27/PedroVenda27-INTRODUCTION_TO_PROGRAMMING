n = 1

while True:
    nome_atleta = input(f"Digite o nome do {n}º atleta (ou 'fim' para encerrar): ")
    
    if nome_atleta.lower() == 'fim':
        break
    
    saltos = []

    for numsalto in range(1, 6):
        salto = float(input(f"Digite a distância do {numsalto}º salto em metros: "))
        saltos.append(salto)
    
    media_saltos = sum(saltos) / len(saltos)

    print("Resultado final:")
    print(f"Atleta: {nome_atleta}")
    print("Saltos:" , saltos)
    print(f"Média dos saltos: {media_saltos}")

    n = n + 1
