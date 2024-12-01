import webbrowser

done = False

while not done:
    print('O que deseja fazer:')
    print('1 - Aprender Python')
    print('2 - Aprender assistir videos7')
    print('3 - Visitar a pagina da Onebitecode')
    print('4 - Sair')

    choice = int(input('>'))

    if choice == 1:
        webbrowser.open('https://comunidade.onebitcode.com/c/formacao-completa/sections/360222/lessons/1337958')
    elif choice == 2:
        webbrowser.open('https://www.youtube.com/watch?v=wF4tlq3vnNw')
    elif choice == 3:
        webbrowser.open('https://onebitcode.com/?&utm_medium=paid-traffic&utm_source=x&ltk_gcm=21276967619&ltk_gag=&ltk_gac=&ltk_gne=x&gad_source=1&gclid=CjwKCAiAjKu6BhAMEiwAx4UsAn_6YVvcKGL0cQKNInotSHmypNdrNK8gSoLCMzTfKm6-ptC0OAHBOBoCDMYQAvD_BwE')
    elif choice == 4:
        done = True
        print('Você saiu do programa!')
    else:
        print('Opção invalida!')