senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input(f"digite a senha(tentativa{tentativas + 1}/{max_tentativas}): ")
    if tentativas == senha_correta:
        print("Acesso concedido! Bem-vindo.")
        break
    else:
        print("Senha incorreta.")
        tentativa += 1
else:
    print("Voce excede o numero maximo e tentativas. Acesso Bloqueado.")