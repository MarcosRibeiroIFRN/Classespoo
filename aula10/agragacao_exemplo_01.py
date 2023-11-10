class Produto:
    def __init__(self, nome:str,valor:float):
        self.__nome=nome
        self.__valor=valor
    
#    def __str__(self) -> str:
 #       return "produto: {}\n valor: {}".format(self.__nome,self.__valor)


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__itens[]

    def adicionarProduto(self,prod:Produto):
        self.__itens.append(prod)
        print("produto {} adicionado ao carrinho".format(prod))
    
    def FinalizarCompra(self):
        print("Compra finalizada com sucesso!!!")
        