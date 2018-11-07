class Tabuleiro():

    def __init__(self):
        self.dimensao = 9
        self.matriz = [[0,0,7,0,0,0,0,8,0],
                       [0,5,0,0,0,4,0,0,1],
                       [1,0,0,0,0,0,4,6,0],
                       [4,0,0,0,9,6,0,1,0],
                       [0,6,0,0,1,3,0,0,2],
                       [8,0,0,0,2,5,0,3,0],
                       [6,0,0,0,0,0,7,9,0],
                       [0,2,0,0,0,7,0,0,4],
                       [0,0,8,0,0,0,0,2,0]]

    def printaMatriz(self):
        for x in range(0, self.dimensao):
            print(self.matriz[x])

    def setMatriz(self, linha, coluna, valor):
        self.matriz[linha][coluna] = valor

    # verifica linha
    def permiteLinha(self, linha, valor):
        #retorna true caso todos os itens forem diferentes do valor
        return all([valor != self.matriz[linha][i] for i in range(0, self.dimensao)])


    # verifica coluna
    def permiteColuna(self, coluna, valor):
        # retorna true caso todos os itens forem diferentes do valor
        return all([valor != self.matriz[i][coluna] for i in range(0, self.dimensao)])

    #verifica quadrantes
    def permiteQuadrante(self, linha, coluna, valor):
        #obtem o quadrante desejado
        linha = ( 3 * (linha//3) )
        coluna = ( 3 * (coluna//3) )

        for x in range(linha, linha+3):
            for y in range(coluna, coluna+3):
                if self.matriz[x][y] == valor:
                    return False

        return True

    #da a permissão geral para adicionar um numero
    def permiteGeral(self, linha, coluna, valor):

        if self.permiteLinha(linha,valor) and self.permiteColuna(coluna,valor) and self.permiteQuadrante(linha,coluna, valor) == True:
            return True
        else:
            return False


    def resolveQuadrante(self, quadrante):

        #incializa a lista de prioridade
        listaPrioridade = []

        #recebe os espaços vazios
        listaPrioridade = self.vaziosQuadrante(quadrante)
        # print(listaPrioridade)

        #inicializa a lista de valores possíveis
        listaValoresPossiveis = self.numerosPossiveisQuadrante(quadrante)
        # print(listaValoresPossiveis)

        #ordena de forma crescente (mais próximo para mais distante)
        listaPrioridade.sort()

        #adicionar valor
        for x in listaPrioridade:
            for y in listaValoresPossiveis:
                if self.permiteGeral(x[0], x[1], y) == True:
                    self.setMatriz(x[0], x[1], y)
                    break

        # self.printaMatriz()


    def vaziosQuadrante(self, quadrante):

        coordenadas = self.linhaColunaDoQuadrante(quadrante)
        # print(coordenadas)
        lista = []
        for x in range(coordenadas[0],coordenadas[1]):
            for y in range(coordenadas[2],coordenadas[3]):
                if self.matriz[x][y] == 0:
                    lista.append([x,y])
            pass
        pass
        return lista

    def numerosPossiveisQuadrante(self, quadrante):
        lista = [1,2,3,4,5,6,7,8,9]
        coordenadas = self.linhaColunaDoQuadrante(quadrante)
        for x in range(coordenadas[0],coordenadas[1]):
            for y in range(coordenadas[2],coordenadas[3]):
                if self.matriz[x][y] != 0:
                    lista.remove(self.matriz[x][y])
            pass
        pass

        return lista


    def linhaColunaDoQuadrante(self, quadrante):
        if quadrante == 1 or quadrante == 2 or quadrante == 3:
            a = 0
            b = 3
        elif quadrante == 4 or quadrante == 5 or quadrante == 6:
            a = 3
            b = 6
        elif quadrante == 7 or quadrante == 8 or quadrante == 9:
            a = 7
            b = 9

        if quadrante == 1 or quadrante == 4 or quadrante == 7:
            c = 0
            d = 3
        elif quadrante == 2 or quadrante == 5 or quadrante == 8:
            c = 3
            d = 6
        elif quadrante == 3 or quadrante == 6 or quadrante ==9:
            c = 6
            d = 9

        return [a,b,c,d]

    def verificaMatriz(self):
        for x in range(0, self.dimensao):
            for y in range(0, self.dimensao):
                if(self.matriz[x][y]==0):
                    return False

        return True

    def setMatrizOriginal(self):
        self.matriz = [[0,0,7,0,0,0,0,8,0],
                       [0,5,0,0,0,4,0,0,1],
                       [1,0,0,0,0,0,4,6,0],
                       [4,0,0,0,9,6,0,1,0],
                       [0,6,0,0,1,3,0,0,2],
                       [8,0,0,0,2,5,0,3,0],
                       [6,0,0,0,0,0,7,9,0],
                       [0,2,0,0,0,7,0,0,4],
                       [0,0,8,0,0,0,0,2,0]]








