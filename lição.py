print ("Classificação de Veículos")

marca = input("marca:")
modelo = input("modelo:")
km_percorrido = float(input("Km_percorrido:"))
litros_gastos = float(input("litros_gastos:"))
try:
    consumo = km_percorrido / litros_gastos
    if consumo <= 6:
        faixa = "Altissimo consumo"
    elif consumo <= 9:
        faixa = "Alto consumo"
    elif consumo  <=12:
        faixa = "Médio consumo"
    elif consumo  <= 15:
        faixa = "Bom consumo"
    else:
        faixa = "Ótimo consumo"
except Exception as e:
     print(F"O programa não pode realizar o cálculo, o motivo do erro é {e}")


print (f"Seu {marca}, {modelo} fez {consumo}Km/L e isso é considerado um {faixa}")
