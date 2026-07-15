def boas_vindas():
    print("ola! bem-vindo a nossa aula de python!")

# TESTANDO A FUNCAO
boas_vindas()
boas_vindas()

# TESTANDO PARAMETROS
def sauda_usuario(nome, sobrenome):
    print(f"eae {nome} {sobrenome}! ta suave?")

sauda_usuario("gugu", "lindo")
sauda_usuario("tony", "kross")

# DEF COM INPUT
def sauda_user(nome, sobrenome):
    print(f"seja bem-vindo {nome} {sobrenome}!!")

nome1 = input("digite seu nome: ")
sobrenome1 = input("digite seu sobrenome: ")

sauda_user(nome1, sobrenome1)

nome2 = input("digite seu nome: ")
sobrenome2 = input("digite seu sobrenome: ")
sauda_user(nome2, sobrenome2)

# PROCESSAMENTO: RETURN (SEMPRE USAR COM CALCULOS)
def somar(valor1, valor2):
    return valor1 + valor2
total = somar(10, 5)
print(f"o total da conta foi {total}")
