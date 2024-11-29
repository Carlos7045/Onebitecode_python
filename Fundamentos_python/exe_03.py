print(f'========== Calculando a distancia ==========')

distancia = float(input('Digita a distancia a percorrer: '))

valor_ate_200_km = 0.50 * distancia
valor_longa_distancia = 0.35 * distancia



if distancia <= 200:
    print(f'O valor para percorrer essa distancia é: R${valor_ate_200_km :.2f}')
elif distancia > 200:
    print(f'O valor para percorrer essa distancia é: R${valor_longa_distancia :.2f}')
else:
    print('Digite um valor valido!')    


