import threading
import random
import time

DISTANCIA = 200  
trava_porta = threading.Lock()

def caminhar(numero):
    velocidade = random.uniform(4, 6)  
    tempo_caminhada = DISTANCIA / velocidade

    print(
        f"Pessoa {numero} começou a caminhar "
        f"(velocidade: {velocidade:.2f} m/s)."
    )
    time.sleep(tempo_caminhada)
    print(f"Pessoa {numero} chegou à porta.")

    with trava_porta:
        tempo_porta = random.uniform(1, 2)
        print(
            f"Pessoa {numero} está abrindo e atravessando a porta "
            f"(leva {tempo_porta:.2f} s)."
        )
        time.sleep(tempo_porta)
        print(f"Pessoa {numero} atravessou a porta.")

if __name__ == "__main__":
    threads = [
        threading.Thread(target=caminhar, args=(i,))
        for i in range(1, 5)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("As quatro pessoas atravessaram a porta.")