class Circulo():
    def __init__(self, raio, valorPi) -> None:
        
        self.raio = raio
        self.valorPi= valorPi

    def calculaArea(self):
        self.area = self.raio**2 * self.valorPi
        print(f'A area do circulo é {self.area}')

circulo = Circulo(3, 3.14)
circulo.calculaArea()

class Cilindro(Circulo):
    def __init__(self, raio, valorPi, altura) -> None:
        super().__init__(raio, valorPi)
        self.altura=altura
    def volumeCilindro(self):
        self.volume = self.raio**2 * self.valorPi * self.altura
        print(f'O volume do cilindro é {self.volume}')
cilindro = Cilindro(2,3.14,4)
cilindro.volumeCilindro()