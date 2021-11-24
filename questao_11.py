#Faça um programa que solicite o preço de uma mercadoria e o per- centual de desconto. 
#Exiba o valor do desconto e o preço a pagar.

precoMercadoria = float(input("Digite o preço da mercadoria: "))
desconto = int(input("Informe o per-centual de descoto: "))

valorDesconto = (desconto*precoMercadoria/100)

precoPagar = precoMercadoria - valorDesconto

print("O desconto foi de R$ = {} e o novo preço R$ = {} ".format(valorDesconto,precoPagar))
