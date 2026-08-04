class Roupa:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
        
    def vestir(self):
        return f"{self.cor}, essa cor caiu bem"
    
roupa1 = Roupa("camisa", "laranja")
roupa2 = Roupa("casaco", "branca")

print(f"sua {roupa1.tipo} é boa e a cor dela é {roupa1.cor}")
print(f"a sua segunda roupa é um {roupa2.tipo} e a cor dela é {roupa2.cor}")

print(roupa1.vestir())
print(roupa2.vestir())