class Tabuleiro():

    def __init__(self):
        self.dimensao = 9
        self.matriz = [[0,0,7,0,0,0,0,8,0],
                       [0,5,0,0,0,4,0,0,1],
                       [1,0,0,0,0,0,4,6,0],
                       [4,0,0,0,9,6,0,1,2],
                       [0,6,0,0,1,3,0,0,2],
                       [8,0,0,0,2,5,0,3,0],
                       [6,0,0,0,0,0,7,9,0],
                       [0,2,0,0,0,7,0,0,4],
                       [0,0,8,0,0,0,0,2,0]]

    def setMatrizNula(self):
        for x in range(0, self.dimensao):
            for y in range(0, self.dimensao):
                self.matriz[x][y] = 0

    def printaMatriz(self):
        for x in range(0, self.dimensao):
            print(self.matriz[x])

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
        linha = 3 * (linha//3)
        coluna = 3 * (coluna//3)

        for x in range(linha, linha+3):
            for y in range(coluna, coluna+3):
                if self.matriz[x][y] == valor:
                    return False

        return True















