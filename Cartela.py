import random

class Cartela():


    def sorteio_cartela():
        cartela = []

        tamanho_cartela = 10
        n = 0

        while n < tamanho_cartela:
            numero = random.randrange(1, 100)
            if len(cartela) == 0:
                cartela.append(numero)
                n += 1
            if numero not in cartela:
                cartela.append(numero)
                n += 1

        cartela.sort()
        return cartela
