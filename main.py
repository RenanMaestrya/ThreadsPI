import random
import sys
import time
import threading

def calcular_pi_parcial(numero_de_pontos, resultado, indice):
    pontos_dentro_do_circulo = 0
    for _ in range(numero_de_pontos):
        x, y = random.random(), random.random()
        distancia_ao_centro = x**2 + y**2
        if distancia_ao_centro <= 1:
            pontos_dentro_do_circulo += 1
    resultado[indice] = pontos_dentro_do_circulo

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Use: python main.py <numero_de_pontos> <numero_de_threads>")
        sys.exit(1)

    numero_de_pontos = int(sys.argv[1])
    numero_de_threads = int(sys.argv[2])
    
    pontos_por_thread = numero_de_pontos // numero_de_threads
    pontos_restantes = numero_de_pontos % numero_de_threads
    
    threads = []
    resultado = [0] * numero_de_threads
    
    start_time = time.time()  
    
    for i in range(numero_de_threads):
        pontos = pontos_por_thread + (1 if i < pontos_restantes else 0)  
        thread = threading.Thread(target=calcular_pi_parcial, args=(pontos, resultado, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    total_pontos_dentro_do_circulo = sum(resultado)
    pi_estimado = 4 * total_pontos_dentro_do_circulo / numero_de_pontos
    
    end_time = time.time()  
    
    print(f"Aproximação de π com {numero_de_pontos} pontos usando {numero_de_threads} threads é: {pi_estimado}")
    print(f"Tempo de execução: {end_time - start_time} segundos")
