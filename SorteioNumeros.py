import random
import Cartela

numeros_sorteados = []


def sorteio_numeros():
    numero_aleatorio = random.randrange(1, 100)
    while numero_aleatorio in numeros_sorteados:
        numero_aleatorio = random.randrange(1, 100)

        if len(numeros_sorteados) > 100:
            break
    numeros_sorteados.append(numero_aleatorio)

    return numero_aleatorio

