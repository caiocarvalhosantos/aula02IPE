print("Medidor de imc")
nome = input("Qual é seu nome:")
peso = float(input("Qual é o seu peso:")) 
altura = float(input("Qual sua altura:"))

try:
   imc = peso / (altura * altura)
   if imc <= 18.5:
       print (f"{nome} seu IMC é de: {imc} portanto, você está abaixo do peso")
   elif imc <= 24.9:
       print(f"{nome} seu IMC é de: {imc} portanto, você está dentro do peso ideal")
   elif imc <=29.9:
       print(f"{nome}seu IMC é de: {imc} portanto, você está com sobrepeso")
   else: 
       print(f"{nome} seu IMC é de:{imc} portanto, você está com obesidade")
except ZeroDivisionError:
    print("O programa não é capaz de dividir por zero!")
   