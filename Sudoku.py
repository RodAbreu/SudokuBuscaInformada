# Rodrigo Pesse de Abreu, RA: 726588
# Primeiro trabalho de IA - Sudoku com best first

import time
#variaveis globais
quantVezes = 0
dimensao = 9
dimensaoQuadrante = 3

#
def set_quantVezes():
    global quantVezes
    quantVezes += 1

#printa a matriz na tela
def printa_matriz(matriz):
    print("----------------------")
    for lin in range(0, dimensao):
        if lin == 3 or lin == 6:
            print("----------------------")
        for col in range(0, dimensao):
            if col == 3 or col == 6:
                print("|", end=" ")
            print(matriz[lin][col], end=" ")
        print()
    print("----------------------")

#recebe a matriz de parâmetro e a lista l, na qual recebera as coordenadas do item em questão
def findCoordPrioridade(matriz, l):

    # SEM FUNCAO HEURISTICA
    # Codigo no qual a funcao heuristica não é implementada, apenas há uma busca simples
    # passando por todos os campos da matriz


    # for row in range(0, 9):
    #     for col in range(0, 9):
    #         if (matriz[row][col] == 0):
    #             l[0] = row
    #             l[1] = col
    #             return True
    # return False

    # COM FUNCAO HEURÍSTICA
    # cria uma lista com prioridades para os itens que possuem a maior soma de itens já inseridos
    # tanto na linha, na coluna e na matriz do item em questão

    #a variavel lista recebe uma lista ordenada de itens medidos por prioridade
    lista = InsereSomaCLQ(matriz)
    for i in lista:
        if matriz[i[1]][i[2]]==0:
            l[0] = i[1]
            l[1] = i[2]
            print("Posicao: [", l[0], "][", l[1], "]")
            #retorna True se conseguiu inserir as coordenadas no parâmetro l
            return True
    #retorna False caso não consiga
    return False

#funcao que verifica a existência de um item especifico na linha
def permissao_linha(matriz, row, num):
    for i in range(0, dimensao):
        if (matriz[row][i] == num):
            return False
    return True


#funcao que verifica a existência de um item especifico na linha
def permissao_coluna(matriz, col, num):
    for i in range(0, dimensao):
        if (matriz[i][col] == num):
            return False
    return True


#funcao que verifica a existência de um item especifico no quadrante
def permissao_quadrante(matriz, row, col, num):
    for i in range(0, dimensaoQuadrante):
        for j in range(0, dimensaoQuadrante):
            if (matriz[i + row][j + col] == num):
                return False
    return True


#funcao que verifica todos os alicerces de uma vez: coluna, linha e quadrante
def permissao_geral(matriz, linha, coluna, valor):
    return permissao_linha(matriz, linha, valor) \
           and permissao_coluna(matriz, coluna, valor) \
           and permissao_quadrante(matriz, linha - linha % 3, coluna - coluna % 3, valor)
            #esse tratamento se dá para descobrir o inicio da linha e da coluna dentro do quadrante


def solve_sudoku(matriz):
    #  lista na qual receberá as coordenadar da função findCoordPrioridade
    l = [0, 0]

    # Confere se todos itens já foram consultados
    if (not findCoordPrioridade(matriz, l)):
        return True

    # Recebem as coordenadas do parametro da função findCoordPrioridade acima
    linha = l[0]
    coluna = l[1]

    # valores possíveis para serem inseridos 1-9
    for valor in range(1, 10):
        print("Tentativa: ", valor)

        # confere se aquele valor respeita as condições: linha, coluna e quadrante
        if (permissao_geral(matriz, linha, coluna, valor)):

            # caso a permissão seja concedida a posição em questão recebe o valor
            matriz[linha][coluna] = valor

            print("\nValor inserido: ",matriz[linha][coluna],"\n")

            # chamada recursiva
            if (solve_sudoku(matriz)):
                return True

            # caso falhe o valor inserido, a posicao receberá zero para receber o backtracking
            matriz[linha][coluna] = 0

    #incrementa o valor de vezes que o algoritmo passou por esse caminho (apenas para termos uma contagem)
    set_quantVezes()
    # backtracking
    print("\nbacktracking\n")
    print("Retorna anterior\n")
    return False


#função na qual encontra todos os vazios da matriz
def vaziosMatriz(matriz):
    lista = []
    for x in range(0, dimensao):
        for y in range(0, dimensao):
            if matriz[x][y] == 0:
                lista.append([x, y])
        pass
    pass
    return lista


#calcula a soma de todos os valores contidos dentro da coluna, linha e quadrante da posicao em questão
def InsereSomaCLQ(matriz):
    lista = vaziosMatriz(matriz)
    # todas as posições com a mesma prioridade
    for i in lista:
        i.insert(0, 0)

    for i in lista:
        valor = somaValorColunaLinhaQuadrante(matriz, i[1], i[2])
        i[0] = valor

    # ordenando por prioridade
    lista_ordenada = sorted(lista, key=lambda lista: lista[0])

    # deixando a maior prioridade em primeiro lugar
    lista_ordenada.reverse()

    return lista_ordenada


def somaValorColunaLinhaQuadrante(matriz, linha, coluna):  # coordenadas x e y
    somaLinha, somaColuna, somaQuadrante = 0, 0, 0

    # descobre o quadrante do item em questão
    quadranteX = (3 * (linha // 3))
    quadranteY = (3 * (coluna // 3))

    # soma os valores de toda linha e de toda coluna
    for i in range(0, dimensao):
        somaLinha += matriz[linha][i]
        somaColuna += matriz[i][coluna]

    # soma os valores do quadrante
    for x in range(quadranteX, quadranteX + 3):
        for y in range(quadranteY, quadranteY + 3):
            # garante que não vá somar itens já somados pela linha e coluna
            if x != linha and y != coluna:
                somaQuadrante += matriz[x][y]

    return somaLinha + somaColuna + somaQuadrante


# Driver main function to quantVezes above functions
if __name__ == "__main__":

    # valores da matriz molde para o trabalho
    matriz = [[0, 0, 7, 0, 0, 0, 0, 8, 0],
              [0, 5, 0, 0, 0, 4, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 4, 6, 0],
              [4, 0, 0, 0, 9, 6, 0, 1, 0],
              [0, 6, 0, 0, 1, 3, 0, 0, 2],
              [8, 0, 0, 0, 2, 5, 0, 3, 0],
              [6, 0, 0, 0, 0, 0, 7, 9, 0],
              [0, 2, 0, 0, 0, 7, 0, 0, 4],
              [0, 0, 8, 0, 0, 0, 0, 2, 0]]

    inicio = time.time()
    print(InsereSomaCLQ(matriz))
    # condição para trabalhar com o resultado do algoritmo
    if (solve_sudoku(matriz)):
        # caso retorne True: encontrou uma solução
        printa_matriz(matriz)
    else:
        # caso retorne False: não encontrou uma solução
        print("No solution exists")

    fim = time.time()
    print(fim - inicio)
    print(quantVezes)



