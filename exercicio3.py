import threading
import random

QUANTIDADE_SAPOS = 5

def corrida(numero_sapo, distancia_maxima):
    posicao = 0.0

    while posicao < distancia_maxima:
        salto = random.uniform(1, 5)  
        posicao += salto

        print(
            f"Sapo {numero_sapo}: saltou {salto:.2f} cm; "
            f"percorreu {posicao:.2f} cm."
        )

    print(
        f" Sapo {numero_sapo} terminou! "
        f"Posição final: {posicao:.2f} cm "
        f"(meta: {distancia_maxima:.2f} cm)."
    )

if __name__ == "__main__":
    try:
        distancia = float(input("Informe a distância da corrida (cm): "))
        if distancia <= 0:
            raise ValueError
    except ValueError:
        print("Digite uma distância numérica maior que zero.")
        raise SystemExit(1)

    threads = [
        threading.Thread(target=corrida, args=(i, distancia))
        for i in range(1, QUANTIDADE_SAPOS + 1)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Corrida encerrada!")