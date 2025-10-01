

print("Indique uma hora indicando primeiro a hora e de seguida os minutos")

hora = int(input("Indique a hora: "))
minutos = int(input("Indique os minutos: "))

print("Hora selecionada:" , hora ,":", minutos)

minmeinoi = ((24-1 - hora)*60)+( 60-minutos )

print("Faltam:" , minmeinoi ,"minutos para a meia noite")
