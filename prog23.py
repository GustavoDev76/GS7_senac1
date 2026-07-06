dia = input("digite o dia da semana: ")

match dia:
    case "Segunda" | "Terca" | "Quarta" | "Quinta" | "Sexta":
        print("Dia de meio de semana, Dia de programacao")
    case "Sabado" | "Domingo":
        print("Fim de semana! Dia de relaxar")
    case _:
        print("Dia invalido!")