from Tkinter import *


# Define as operacoes

# class calculadora:

def adicao(num1, num2):
    """ adicao """
    return num1 + num2


def subtracao(num1, num2):
    """ subtracao """
    return num1 - num2


def multiplicacao(num1, num2):
    """ multiplicacao """
    return num1 * num2


def divisao(num1, num2):
    """ divisao """
    return num1 / num2


def potenciacao(num1, num2):
    """ potenciacao """
    return num1 ** num2


def radiciacao(num1, num2):
    """ radiciacao """
    return num1 ** (1 / num2)


def nao_escolheu():
    """ sem escolha """
    print("Nao escolheu funcao valida")


# Prepara a base para a funcao que escolhe a operacao a ser feita

print("Escolha a operacao:")
print("1.adicao")
print("2.Subtracao")
print("3.Multiplicacao")
print("4.Divisao")
print("5.Potenciacao")
print("6.Radiciacao")
print("7.Nenhuma")

Escolha = input("Escolha a operacao pelo numero:")
Numero1 = int(input("Primeiro numero: "))
Numero2 = int(input("Segundo numero: "))

if Escolha == 1:
    print Numero1, '+', Numero2, '=', adicao(Numero1, Numero2)

elif Escolha == 2:
    print Numero1, '-', Numero2, '=', subtracao(Numero1, Numero2)

elif Escolha == 3:
    print Numero1, 'x', Numero2, '=', multiplicacao(Numero1, Numero2)

elif Escolha == 4:
    print Numero1, '/', Numero2, '=', divisao(Numero1, Numero2)

elif Escolha == 5:
    print Numero1, 'elevado a ', Numero2, '=', potenciacao(Numero1, Numero2)

elif Escolha == 6:
    print 'raiz ', Numero2, 'de', Numero1, '=', radiciacao(Numero1, Numero2)

elif Escolha == 7:
    print 'Nao escolheu uma operacao'
