# import random
import Cartela
import SorteioNumeros

# import SorteioCartelas

print(" ###################### ")
print(" ------- BINGO -------- ")
print(" ______________________ ")

numero_cartelas = 10
x = 0
todas_cartelas = []

while x < numero_cartelas:
    gerandoCartelas = Cartela.Cartela.sorteio_cartela()
    todas_cartelas.append(gerandoCartelas)
    x += 1


# cartela_escolhida = int(input("Escolha a cartela entre 1 e 10"))

def imprimir_cartelas():
    numero_cartela = 1
    for cartela in todas_cartelas:
        print(numero_cartela, " - ", cartela)
        numero_cartela += 1


# imprimir_cartelas()


def IniciarBingo():
    rodadas = 0

    # Percorre todas as listas enquanto não tem nenhuma ZERADA
    for cart in todas_cartelas:
        while sum(cart) != 0:
            # Sorteia um numero da função: SorteioNumeros
            numerosortiado = SorteioNumeros.sorteio_numeros()

            # Percore numero a numero das cartelas trocando para 0 caso seja o numero sorteado
            for cartela in todas_cartelas:
                for numero in cartela:
                    if numerosortiado == numero:
                        posicao = cartela.index(numero)
                        cartela[posicao] = 0
                    # Valida cada cartela somando seus elementos para ver se deu BINGO
                    for validacaocartela in todas_cartelas:
                        if sum(validacaocartela) == 0:
                            print("======================================")
                            rodadas += 1
                            print("Rodada", rodadas)
                            print("Numero Sorteado: ", numerosortiado)
                            imprimir_cartelas()
                            print("======================================")
                            numeros_sorteados_sequencia = SorteioNumeros.numeros_sorteados[:]
                            numeros_sorteados_sequencia.sort()
                            return print("A Cartela", todas_cartelas.index(validacaocartela) + 1, "Venceu!",
                                         "\nNumeros Sorteados por Ordem: ",
                                         SorteioNumeros.numeros_sorteados, "\nNumeros Sorteados: ",
                                         numeros_sorteados_sequencia)

            print("======================================")

            rodadas += 1
            print("Rodada", rodadas)
            print("Numero Sorteado: ", numerosortiado)
            imprimir_cartelas()
            print("======================================")



IniciarBingo()

# while numeros in todas_cartelas:
