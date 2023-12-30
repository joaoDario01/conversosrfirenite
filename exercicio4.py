nota1= float(input('digite a primeira nota:'))
while nota1<0 or nota1>10:
    print('digite uma nota valida!!')
    nota1 = float(input('digite a primeira nota:'))

nota2= float(input('digite a segunda nota'))
while nota2<0 or nota2>10:
    print('digite uma nota valida!!')
    nota1 = float(input('digite a segunda nota:'))

media = (nota1+nota2)/2
print(f'a media das duas notas foi {media}')