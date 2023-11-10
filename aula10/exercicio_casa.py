class Casa:
    def __init__(self) -> None:
        self.__comodos=[]

    @property
    def comodos(self):
        return self.__comodos
    
    @comodos.setter
    def comodos(self,comodos):
        self.__comodos=comodos
    @comodos.getter
    def comodos(self,comodos):
        self.__comodos=comodos    
class Comodo:
    def __init__(self,cor:str,ar:bool,porta:bool) -> None:
        self.__cor=cor
        self.__ar=ar
        self.__porta=bool