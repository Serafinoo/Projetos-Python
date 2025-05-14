#calculadora em texto
import math
e = 0
n1 = 0
n2 = 0
cont = "S"
print("Calculadora:")
while e != 7 and cont.upper() != "N":
    e = int(input("""
[1]Somar
[2]Subtrair
[3]Multiplicar
[4]Dividir
[5]Potenciação
[6]Raiz Quadrada
[7]Sair
                  Opção: """))
    if e == 1:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        print(f"{n1} + {n2} = {n1 + n2}")
        cont = input("Deseja continuar? [S/N]: ")
    elif e == 2:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        print(f"{n1} - {n2} = {n1 - n2}")
        cont = input("Deseja continuar? [S/N]: ")
    elif e == 3:
        n1 = int(input("Primeiro Número:"))
        n2 = int(input("Segundo Número:"))
        print(f"{n1} X {n2} = {n1 * n2}")
        cont = input("Deseja continuar? [S/N]: ")
    elif e == 4:
        n1 = int(input("Primeiro Número:"))
        n2 = int(input("Segundo Número:"))
        print(f"{n1} / {n2} = {n1 // n2}")
        cont = input("Deseja continuar? [S/N]: ")
    elif e == 5:
        n1 = int(input("Primeiro Número:"))
        n2 = int(input("Segundo Número:"))
        print(f"{n1} ^ {n2} = {n1 ** n2}") 
        cont = input("Deseja continuar? [S/N]: ") 
    elif e == 6:
        n1 = int(input("Digite um número:")) 
        print(f"Raiz quadrada de {n1} = {math.sqrt(n1)}")
        cont = input("Deseja continuar? [S/N]: ")
    else:
        print("Resposta invalida")
print("FIM")
