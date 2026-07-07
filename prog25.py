valor1 = float(input("digite um valor: "))
valor2 = float(input("digite o segundo valor: "))

print("---ESCOLHA A OPCAO---")
print("1 - somar(+)")
print("2 - subtracao(-)")
print("3 - multiplicar(*)")
print("4 - divisao(/)")

operador = str(input("escolha seu operador: "))

match operador:
    case "1":
        print(f"RESULTADO: {valor1 + valor2}") 
    case "2":
        print(f"RESULTADO: {valor1 - valor2}")
    case "3":
        print(f"RESULTADO: {valor1 * valor2}")
    case "4":
        if valor2 != 0:
            print(f"RESULTADO: {valor1 / valor2}")
        else:
            print("Divisao por 0!!!")
    case _:
        print("Operador invalido")
        print("teste de PULL")
        print("teste de push pelo vscode")
        print("teste de push pelo vscode 2")
        print("te amo muito gszada_do_01")
