#leitura da escolha
print('escolha qual o tipo de operacao quer fazer')
print('''         1 - somar
         2 - subtrair
         3 - multiplicar
         4 - dividir      
''')

operacao = int(input())
#processamento da escolha
if operacao == 1:
    #leitura
    print('SOMA')
    print('digite o primeiro valor')
    operador1 = float(input())
    print('digite o segundo valor')
    operador2 = float(input())
    #processamento
    resultado = operador1 + operador2
    print('o resultado e:', resultado)
elif operacao == 2:
    #leitura
    print('SUBTRACAO')
    print('digite o primeiro valor')
    operador1 = float(input())
    print('digite o segundo valor')
    operador2 = float(input())
    #processamento
    resultado = operador1 - operador2
    print('o resultado e:', resultado)
elif operacao == 3:
    #leitura
    print('MULTIPLICACAO')
    print('digite o primeiro valor')
    operador1 = float(input())
    print('digite o segundo valor')
    operador2 = float(input())
    # processamento
    resultado = operador1 * operador2
    print('o resultado e:', resultado)
elif operacao == 4:
    #leitura
    print('DIVISAO')
    print('digite o primeiro valor')
    operador1 = float(input())
    print('digite o segundo valor')
    operador2 = float(input())
    # processamento
    resultado = operador1 / operador2
    print('o resultado e:', resultado)