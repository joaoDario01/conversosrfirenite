continua = str('s')
soma = 0
contador = 1

while continua == 's':
    nota = float(input('digite a sua nota: '))

    #loop de verificacao
    while nota > 10 or nota < 0:
        print ('digite uma nota valida')
        nota = input ('digite a sua nota: ')

    soma += nota
    contador += 1
    continua = input('quer continuar? s/n: ')

print(soma/contador)