contador = 15
start = 'n'

start = input('quer iniciar o programa?(s/n)')

if start == 's':
    while contador <= 200:
        print(contador,'-',contador ** 2)
        contador += 1