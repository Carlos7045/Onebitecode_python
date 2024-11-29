# def checar_texto(text):
#     tipo = {'Maiuscula': 0, 'Minuscula': 0}
#     for checar in text:
#         if checar.isupper():
#             tipo ['Maiuscula'] +=1
#         elif checar.islower():
#             tipo ['Minuscula'] +=1 
#     print(f'O texto original: {text}')
#     print(f'Numero de letras maiusculas: {tipo["Maiuscula"]}')
#     print(f'Numero de letras minusculas: {tipo["Minuscula"]}')
# checar_texto('Olá meu nome é Carlos Salgado')

#=================== CHEGAR SE O NUMERO É PAR E IMPA E ADD NAS LISTAS ====================
def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))