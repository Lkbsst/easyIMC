import os
 
peso = float(input("Digite seu Peso em Kg:"))

altura = float(input("Digite sua Altura em Metros ex 1.63: "))

imc = peso / altura ** 2

print("Resultado:", imc)

if(imc < 18.5):
  print("Baixo peso")

elif(imc >= 18.5 and imc < 25):
  print("Peso adequado")

elif(imc >= 25 and imc < 30):
  print("Sobrepeso")

else:
  print("Obesidade")
