import threading
import time

trava_cruzamento = threading.Lock()

sentido = None

def controlar_carro(nome, direcao):
    global sentido

    with trava_cruzamento:
        sentido = direcao
        print(f"{nome} entrou no cruzamento: sentido {sentido}.")
        time.sleep(2)  
        print(f"{nome} saiu do cruzamento.")
        sentido = None

if __name__ == "__main__":
    carros = [
        ("Carro 1", "Norte -> Sul"),
        ("Carro 2", "Oeste -> Leste"),
        ("Carro 3", "Leste -> Oeste"),
        ("Carro 4", "Sul -> Norte"),
    ]

    threads = [
        threading.Thread(target=controlar_carro, args=(nome, direcao))
        for nome, direcao in carros
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Todos os carros atravessaram.")
