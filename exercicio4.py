import threading
import random
import time

QUANTIDADE_EQUIPES = 7
CARROS_POR_EQUIPE = 2
LIMITE_PISTA = 5
QUANTIDADE_VOLTAS = 3

semaforo_pista = threading.Semaphore(LIMITE_PISTA)

travas_equipes = {
    equipe: threading.Lock()
    for equipe in range(1, QUANTIDADE_EQUIPES + 1)
}


TEMPO_MIN_VOLTA = 1
TEMPO_MAX_VOLTA = 5

def piloto(equipe, carro):
    nome = f"Equipe {equipe} - Carro {carro}"

    print(f"{nome} aguardando para entrar na pista...")

    
    with travas_equipes[equipe]:
        with semaforo_pista:
            print(f"{nome} entrou na pista.")

            for volta in range(1, QUANTIDADE_VOLTAS + 1):
                tempo = random.uniform(TEMPO_MIN_VOLTA, TEMPO_MAX_VOLTA)
                inicio = time.perf_counter()
                time.sleep(tempo)
                tempo_real = time.perf_counter() - inicio

                print(
                    f"{nome} - volta {volta}: "
                    f"{tempo_real:.2f} segundos."
                )

            print(f"{nome} terminou as {QUANTIDADE_VOLTAS} voltas e saiu da pista.")

if __name__ == "__main__":
    threads = []

    for equipe in range(1, QUANTIDADE_EQUIPES + 1):
        for carro in range(1, CARROS_POR_EQUIPE + 1):
            thread = threading.Thread(
                target=piloto,
                args=(equipe, carro)
            )
            threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Treino de Fórmula 1 encerrado!")