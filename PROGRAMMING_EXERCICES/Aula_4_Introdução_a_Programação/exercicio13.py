
red = (input("introduduza o Valor referente a vermelho (0-255) "))
green = (input("introduduza o Valor referente a verde (0-255) "))
blue = (input("introduduza o Valor referente a azul (0-255)"))

if red == blue == green or red == blue and red > green or blue == green and blue > red or red == green and red > blue:
    print("não existe uma cor predominante")
elif red > blue and red > green:
    print("vermelho é a cor predominante")
elif blue > red and blue > green:
    print("azul é a cor predominante")
elif green > red and green > blue:
    print("azul é a cor predominante")

