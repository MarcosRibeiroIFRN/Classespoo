class Carro:
    marca=" "
    ano=" "
    modelo=" "
    
    def Carro(self,marca,ano,modelo):
        self.marca=marca
        self.ano=ano
        self.modelo=modelo

    def sobreOCarro(self):
        print("O carro em questão é da marca {}, ano {} e modelo {}".format(self.marca,self.ano,self.modelo))

p1=Carro()
p1.Carro("Audi",1999,"q3")
p1.sobreOCarro()      