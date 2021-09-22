#4.
#var1 = int(input('Esconha um número:'))
#while var1 != 'X' :
#    var2 = int(input('escolha outro número'))
#    resto = var1 / var2 % 2
#    print('A quantidade de número que tem é:', resto)
#    var1 = var1 + 1

#def sub (a, b):
#    sub = num1 - num2
#    print('A subtração é:', sub)
#num1 = float(input('Insira o primeiro número:'))
#num2 = float(input('Insira o segundo número:'))
#sub(num1, num2)
#print('-------------------------------------------')
#def mult (a, b):
#    mult = num1 - num2
#print('A multiplicação é:', mult)
#num1 = float(input('Insira o primeiro número:'))
#num2 = float(input('Insira o segundo número:'))
#mult(num1, num2)
#----------------------------------
#1. Desenvolver um programa que mostre os números ímpares entre 100 e 200.  (MAIS OU MENOS)
impares = 0
contador = 0

while contador <= 200:
    if contador % 2 == 1:
      impar = impar + 1

    contador = contador +1
print('os números ímpares são:', impar)

#2. Desenvolva um programa que imprima todos os números inteiros de 0 a 50.
inicio = 51

while inicio >= 0:
    print('Os números são:', inicio)
    inicio = inicio - 1

#3. Desenvolva um programa que receba dez números do usuário e imprima a metade de cada número.
c = 1
var1 = input('Digite seu nome:')

while c <= 10:
    num1 = float(input('Insira um número:'))
    divisao = float(num1 / 2)
    print('A metade do número {} é {}'.format(num1, divisao))
    print('----------------------------------')
    c = c + 1

#4. Desenvolva um programa que leia um número determinado de valores e calcule e escreva a média aritmética
#dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos.
contador = 1
while contador <= 2:
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    num3 = float(input('Digite o terceiro número:'))
    calculo = (num1 + num2 + num3) / 3
    if calculo > 0:
        print('A média aritmética de {} + {} + {} é:{}. Positivo.'.format(num1, num2, num3, calculo))
    elif calculo < 0:
        print('A média aritmética de {} + {} + {} é: {}. Negativo.'.format(num1, num2, num3, calculo))
    else:
        print('A média aritmética de {} + {} + {} é: {}. Neutro.'.format(num1, num2, num3, calculo))

#5. Desenvolva um programa que efetue a soma de todos os números ímpares que são múltiplos de trêse que
# se encontram no conjunto dos números de 1 a 500.     (NÃO CONSEGUI FAZER)

#6.Escreva um programa que leia um valor inicial A e imprima a sequência de valores do cálculo de A1 e o seu
#resultado. Ex.: 5!= 5 x 4 x 3 x 2 x 1= 120.
contador = 1
nom1 = input('Para sair digite "FORA":')

while nom1 != 'FORA':
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    num3 = float(input('Digite o terceiro número:'))
    calculo = num1 + num2 + num3
    print('A soma de {} + {} + {} é igual a:{}'.format(num1, num2, num3, calculo))

#7.Escreva um programa que receba vários números e ao final imprima o maior número digitado. O algoritmo acaba
#quando se digita - 9999.

contador = 1
var1 = input('Para sair digite "9999":')

while var1 != '9999':
    num1 = float(input('Digite o primeiro número:'))
    num2 = float(input('Digite o segundo número:'))
    num3 = float(input('Digite o terceiro número:'))
    if num1 > num2 and num1 > num3:
        print('O maior número é {}.'.format(num1))
        print('----------------------')
    elif num2 > num1 and num2> num3:
        print('O maior número é {}.'.format(num2))
        print('----------------------')
    elif num3 > num1 and num3 > num2:
        print('O maior número é {}.'.format(num3))
        print('----------------------')
    else:
        print('Todos os números são iguais.')
        print('----------------------')


