class Carros:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def buzinar(self):
        return f"{self.modelo} faz bibi"
        
carro1 = Carros("toyota", "corolla")
carro2 = Carros("BMW", "IX")

print(f"a marca do seu carro é {carro1.marca} e o modelo dele é {carro1.modelo}")
print(f"a marca do segundo carro é {carro2.marca} e o modelo dele é {carro2.modelo}")

print(carro1.buzinar())
print(carro2.buzinar())