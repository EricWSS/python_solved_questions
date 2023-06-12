#Projeto super alculadora apenas com funções (SEM POO)

def somar(soma):
    soma=a+b
    return soma

def subtrair(sub):
    sub=a-b
    return sub

def multiplicar(mult):
    mult=a*b
    return mult

def dividir(div):
    div=a/b
    return div

def potenciacao(pot):
    pot=a**b
    pass


#################################b=float(input("Insira o número a ser calculado: "))
while True:
    print("=-"*20)
    a=float(input("Insira o número a ser calculado: "))
    calcular=(input("""
    Digitea operação:  
    Soma: +
    Subtração: -
    Multiplicação: *
    Divisão: /
    Potenciação: **
    """))
    if calcular == '+':
        b=float(input("Insira o número a ser somado: "))
        resultadoParcial=somar(a,b)

    break

