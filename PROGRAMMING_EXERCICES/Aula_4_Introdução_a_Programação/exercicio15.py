mes = (input("Indique um mês"))


if mes == "janeiro" or mes == "Janeiro" or mes == "março" or mes == "Março" or mes == "maio" or mes == "Maio" or mes == "julho" or mes == "Julho" or mes == "agosto" or mes == "Agosto" or mes == "outubro" or mes == "Outubro" or mes == "dezembro" or mes == "Dezembro":
    print("O més tem 31 dias")
elif mes == "abril" or mes == "Abril" or mes == "junho" or mes == "Junho" or mes == "setembro" or mes == "Setembro" or mes == "novembro" or mes == "Novembro":
    print("O més tem 30 dias")
elif mes == "fevereiro":
    print("O més tem 29 dias")
else:
    print("O mês não existe")