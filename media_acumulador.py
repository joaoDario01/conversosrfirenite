#programa onde pode se escolher a quantidade de numeros para se fazer a media
contador = 1
soma = 0
repeticoes = int(input('digite quantos numeros irao ser somados: '))
while contador <= repeticoes:
    print('digite a nota ',contador)
    acumulador = (float(input()))
    soma += acumulador
    contador += 1
media = soma / repeticoes
print(soma)
print(media)
