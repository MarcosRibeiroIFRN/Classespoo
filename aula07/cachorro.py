class Cachorro:
    raca=" "
    nome=" "
    idade=0
    
    def Cachorro(self,raca,nome,idade):
        self.raca=raca
        self.nome=nome
        self.idade=idade

    def uivando(self):
        print("O {}, {} está uivando \n AUUUUUUUUUUUUUUUUUUUUUUUUU".format(self.raca,self.nome))

p1=Cachorro()
p1.Cachorro("rusky","belo",5)
p1.uivando()      