class Passarinho:
    def __init__(self, raca, cor):
        self.raca = raca
        self.cor = cor
        
    def cantar(self):
        return f"{self.raca}, essa raca de passarinho canta!"

passarinho1 = Passarinho("canario-da-terra", "amarela")
passarinho2 = Passarinho("trica-ferro", "verde")

print(f"o primeiro passarinho é um {passarinho1.raca} e tem uma cor {passarinho1.cor} viva.")
print(f"o segundo passarinho é um {passarinho2.raca} e possui uma cor {passarinho2.cor} olivácea.")

print(passarinho1.cantar())
print(passarinho2.cantar())