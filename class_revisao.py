class Carros:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def buzinar(self):
        return f"{self.modelo} faz bibi"
    
carro1 = Carros("toyotta", "corolla")
carro2 = Carros("VW", "gol")

print(f"a marca do primeiro carro é um {carro1.marca} e o modelo dele é {carro1.modelo}")
print(f"a marca do segundo carro é um {carro2.marca} e seu modelo é o {carro2.modelo}")
print(carro1.buzinar())
print(carro2.buzinar())