#O program recebe 2 notas de 40 alunos, calcula e retorna a média da sala
#Dá um valor vazio para a váriavel soma
soma=0

#Inicia laço de repetição for
for i in range(40):
    #Recebe b1 e b2
    b1 = float(input("Digite uma Nota"))
    b2 = float(input("Digite outra nota"))
    #A váriavel media será somada com os dois valores
    soma+=b1+b2
#A variável média recebe a média da sala
media = soma/80
#retorna o valor encontrado
print("A média da turma foi: ",media)