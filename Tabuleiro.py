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
        result = all([valor != self.matriz[linha][i] for i in range(0, self.dimensao)])
        return result

    # verifica coluna
    def permiteColuna(self, coluna, valor):
        # retorna true caso todos os itens forem diferentes do valor
        return all([valor != self.matriz[i][coluna] for i in range(0, self.dimensao)])
        return result

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

        if (self.permiteLinha(linha,valor) and self.permiteColuna(coluna,valor) and self.permiteQuadrante(linha,coluna, valor)) == True:
            return True
        else:
            return False


    def resolveQuadrante(self):

        #incializa a lista de prioridade
        listaPrioridade = []

        #recebe os espaços vazios
        listaPrioridade = self.vaziosQuadrante()

        #inicializa a lista de valores possíveis
        listaValoresPossiveis = self.numerosPossiveisQuadrante()

        #ordena de forma crescente (mais próximo para mais distante)
        listaPrioridade.sort()

        #adicionar valor
        for x in listaPrioridade:
            print(x[0])
            print(x[1])
            for y in listaValoresPossiveis:
                if self.permiteGeral(x[0], x[1], y) == True:
                    self.setMatriz(x[0], x[1], y)
                    break

        self.printaMatriz()


    def vaziosQuadrante(self):
        lista = []
        for x in range(0,3):
            for y in range(0,3):
                if self.matriz[x][y] == 0:
                    lista.append([x,y])
            pass
        pass
        return lista

    def numerosPossiveisQuadrante(self):
        lista = [1,2,3,4,5,6,7,8,9]
        for x in range(0,3):
            for y in range(0,3):
                if self.matriz[x][y] != 0:
                    lista.remove(self.matriz[x][y])
            pass
        pass

        return lista










