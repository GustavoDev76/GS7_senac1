cargo = str(input("escolha um cargo: ")).lower() .strip()

if cargo == "caixa":
    salario = 1500
elif cargo == "vendedor":
    salario = 2400
elif cargo == "gerente":
    salario = 4000
else:
    salario = 0
    print("Nenhum cargo selecionado")

inss = salario * 0.12


if salario > 2000:
    irrf = salario * 0.14
else:
    irrf = salario * 0.08


salario_final = salario - irrf - inss

print(f"Cargo: {cargo}")
print(f"Salaruio: {salario}")
print(f"INSS: {inss}")
print(f"IRRF: {irrf:.2F}")
print(f"Salario final: {salario_final}")