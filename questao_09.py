#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de  Horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os Segundos: "))

diasSegundo = dias * 86400 
horaSegundos = horas * 3600
minutoSegundos = minutos * 60;
TotalSegundos = diasSegundo + horaSegundos + minutoSegundos + segundos

print("Total de segundos = ", TotalSegundos)

