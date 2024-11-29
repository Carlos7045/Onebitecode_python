# def wellcome():
#     print("Hello World")

# def create_game():
#     name = input("Digite o nome do jogo \\n")
#     yearLaunch = int(input("Digite o ano de lançamento\\n"))
#     gamePrice = float(input("Digite o preço do jogo\\n"))
#     noteRating = float(input("Digite a nota de avaliação do jogo\\n"))
#     print(name)
#     print(yearLaunch)
#     print(gamePrice)
#     print(noteRating)

# wellcome()
# create_game()



#========= FUNÇÃO COM ARGUMENTO ============

# def nome_completo(nome1, nome2):
#     print(f'Nome completo é {nome1} {nome2}')

# nome_completo('Carlos', 'Salgado')


def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\\n"))
rating_game(rating)


