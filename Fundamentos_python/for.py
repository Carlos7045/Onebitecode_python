nome_jogo = input('Digite o nome do jogo: ')
quantidade_avaliacao = int(input('Quantas vezes deseja avaliar? '))

notas = 0
for i in range(quantidade_avaliacao):
    nota = float(input('Digite sua nota: '))
    notas += nota
print(f'a nota media do jogo {nome_jogo} é: {notas / quantidade_avaliacao}.')