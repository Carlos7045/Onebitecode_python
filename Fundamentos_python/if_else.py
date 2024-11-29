# nameJogo = input('Digita o nome do jogo: ')
# yearLaunch = int(input('Ano de lançamento:'))
# classification = float(input('Digita a classificação:'))

# if classification <= 6.9:
#     print('Jogo de uma classificação ruim! ')
# elif classification <= 8:
#     print('Jogo de classificação boa!')
# else:
#     print('Jogo de classificação otima!')

print(f'==== Calculadora =====')
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
operacao = int(input('Qual operação deseja fazer \n 1 para Somar \n 2 para Subtração \n 3 para Mutiplicação \n 4 para Divisão \n 5 para Sair: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicao = n1 * n2
divisao = n1 / n2

if operacao == 1:
    print(f'A soma de {n1} e {n2} é: {soma}')   
elif operacao == 2:
    print(f'A subtração de {n1} e {n2} é: {subtracao}')
elif operacao == 3:
    print(f'A multiplicação de {n1} e {n2} é: {multiplicao}')  
elif operacao == 4:
    print(f'A divisão de {n1} e {n2} é: {divisao}')
elif operacao == 5:
    print('Você saiu da calculadora')   
else:
    print('Digite um valor valido!')