import Cartela
import SorteioNumeros

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


def imprimir_cartelas():
    numero_cartela = 1
    for cartela in todas_cartelas:
        print(numero_cartela, " - ", cartela)
        numero_cartela += 1


imprimir_cartelas()


def IniciarBingo():
    rodadas = 0
    cartelas_vencedoras = []

    def imprimir_resultado():
        print("======================================")
        print("Rodada", rodadas)
        print("Numero Sorteado: ", numerosortiado)
        imprimir_cartelas()
        print("======================================")

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

            # Valida cada cartela somando seus elementos e salva as cartelas vencedoras em cartelas_vencedoras pelo
            # numero da Cartela
            for i, valor in enumerate(todas_cartelas):
                if sum(valor) == 0:
                    cartelas_vencedoras.append((i + 1))

            numeros_sorteados_sequencia = SorteioNumeros.numeros_sorteados[:]
            numeros_sorteados_sequencia.sort()

            # Verificar se teve 1 vencedor
            if len(cartelas_vencedoras) == 1:
                rodadas += 1
                imprimir_resultado()

                return print("A Cartela", cartelas_vencedoras, "Venceu!",
                             "\nNumeros Sorteados por Ordem: ",
                             SorteioNumeros.numeros_sorteados, "\nNumeros Sorteados: ",
                             numeros_sorteados_sequencia)

            # Verifica se houve mais de um vencedor
            elif len(cartelas_vencedoras) > 1:
                rodadas += 1
                imprimir_resultado()

                return print("As Cartelas", cartelas_vencedoras, "Venceram!",
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
