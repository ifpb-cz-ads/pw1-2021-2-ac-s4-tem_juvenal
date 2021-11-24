#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
#assim como a quantidade de dias pelos quais o carro foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$ 
#60 por dia e R$ 0,15 por km rodado. 

km = float(input("Quantidade de km percorridos: "))
dias = int(input("Quantidade de dias: "))

print ('Valor do aluguel: R$ %.2f' %(km*0.15 + dias*60) )
