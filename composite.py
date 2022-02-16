class ElementoFolha:
    def __init__(self, *args):
        self.position = args[0]

    def mostrarDetalhes(self):
        print("\t", end="")
        print(self.position)


class ElementoComposite:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def mostrarDetalhes(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.mostrarDetalhes()


if __name__ == "__main__":
    topLevelMenu = ElementoComposite("Gerente Geral")
    subMenuItem1 = ElementoComposite("Gerente 1")
    subMenuItem2 = ElementoComposite("Gerente 2")
    subMenuItem11 = ElementoFolha("Desenvolvedor 1")
    subMenuItem12 = ElementoFolha("Desenvolvedor 2")
    subMenuItem21 = ElementoFolha("Desenvolvedor 3")
    subMenuItem22 = ElementoFolha("Desenvolvedor 4")

    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem21)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)

    topLevelMenu.mostrarDetalhes()
