# inicio = int(input('Digite o numero para iniciar a tabuada: '))
# fim = int(input('Digita qual numero a tabuada deve para: '))

# for inicio in range(inicio):
#     n1 = int(input('Digite um numero:'))
#     n2 = int(input('Digite outro numero:'))
#     operacao = int(input('Qual operação deseja fazer \n 1 para Somar \n 2 para Subtração \n 3 para Mutiplicação \n 4 para Divisão \n 5 para Sair: '))

import winsound


lançamento = 10

while lançamento >= 0:
    print(lançamento)
    lançamento -= 1
winsound.Beep(2500, 500)
   