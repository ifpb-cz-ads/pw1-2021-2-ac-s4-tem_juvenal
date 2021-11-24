#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a 
#velocidade média esperada para a viagem.

distancia = float(input("Digite a distância em km: "))
velocidadeMedia = float(input("Digite a velocidade média em km: "))
tempo = distancia/velocidadeMedia
print("O tempo estimado é de %5.2f horas " % tempo)
