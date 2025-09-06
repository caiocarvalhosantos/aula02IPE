print ("Verificador de idade")
nome = input("Qual seu nome?")
idade = int(input("Qual sua idade?"))

if idade > 18:
     print(f"{nome} é maior de idade")

elif idade == 18:
     print(f"{nome} é maior de idade, e possui exatamente 18 anos")

else:
    print(f"{nome} é menor de idade")



