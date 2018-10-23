from Tabuleiro import Tabuleiro


def main():
    x = Tabuleiro()
    print(x.permiteColuna(2,3))
    print(x.permiteLinha(0,8))
    print(x.permiteQuadrante(4,5,4))
    print(x.printaMatriz())
    pass

if __name__ == '__main__':
    main()
