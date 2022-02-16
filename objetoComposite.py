from abc import ABC, abstractmethod

class Objeto(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError("Implementar aqui!")


class CompositeObjeto:
    def __init__(self, *args) -> None:
        self.position = args[0]
        self.objetos = []

    def render(self) -> None:
        print(self.position)
        for objeto in self.objetos:
            print("\t", end="")
            objeto.render()

    def add(self, objeto: Objeto) -> None:
        self.objetos.append(objeto)

    def remove(self, objeto: Objeto) -> None:
        self.objetos.remove(objeto)


class Linha:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def render(self) -> None:
        print(f"Linha: {self.nome}")

class SemiCirculo:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def render(self) -> None:
        print(f"Semi circulo: {self.nome}")


linha1 = Linha("1")
linha2 = Linha("2")
linha3 = Linha("3")
linha4 = Linha("4")
semicirculo1 = SemiCirculo("1")
semicirculo2 = SemiCirculo("2")

quadrado = CompositeObjeto("quadrado")
circulo = CompositeObjeto("circulo")

quadrado.add(linha1)
quadrado.add(linha2)
quadrado.add(linha3)
quadrado.add(linha4)
circulo.add(semicirculo1)
circulo.add(semicirculo2)

agrupar = CompositeObjeto("Agrupar")

agrupar.add(quadrado)
agrupar.add(circulo)



quadrado.render()
semicirculo1.render()
semicirculo2.render()