contador = 1
numero = 0
negativos = 0
while contador <= 5:
    numero = float(input(f'digite o {contador} numero:'))
    if numero <= -1:
        negativos += 1
    print(contador)
    contador += 1

print(f'foram digitados {negativos} numeros negativos')