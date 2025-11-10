#O programa recebe 100 números, verifica se são pares ou não e retorna apenas números ímpares
#Inicia Laço de repetição for
for i in range(100):
    #reccebe numero
    numero = int(input("Digite um número inteiro"))
    #Se o resto do número dividido por 2 for diferente de 0, retorna o numero
    if numero % 2 != 0:
        print(numero)
