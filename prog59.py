class Biscoito:
    def __init__(self, sabor, gosto):
        self.sabor = sabor
        self.gosto = gosto
    
    def croc(self):
        return f"{self.sabor}, faz croc croc"
    
biscoito1 = Biscoito("choco-maluco", "baunilha ultra doce e cremoso")
biscoito2 = Biscoito("amanteigado de leite", "leite condensado")

print(f"o primeiro biscoito tem um sabor de {biscoito1.sabor} e tem um gosto de {biscoito1.gosto}")
print(f"o segundo biscoito tem um sabor de {biscoito2.sabor} e um gosto de {biscoito2.gosto}")

print(biscoito1.croc())
print(biscoito2.croc())   