import time

# 1. Carrega os dados primeiro (Fora da medição de tempo)
with open("1000_numbers.txt", "r") as arquivo:
    lista_array = [int(linha.strip()) for linha in arquivo]

# 2. INÍCIO DA MEDIÇÃO (Apenas o algoritmo)
tempo_inicial = time.perf_counter()

n = len(lista_array)
for i in range(n - 1):
    indice_menor = i
    for j in range(i + 1, n):
        if lista_array[j] < lista_array[indice_menor]:
            indice_menor = j
    
    # Troca de posição
    temp = lista_array[indice_menor]
    lista_array[indice_menor] = lista_array[i]
    lista_array[i] = temp

# 3. FIM DA MEDIÇÃO
tempo_final = time.perf_counter()

print("Ordenação concluída!")

# Imprime os 10 primeiros
for i in range(10):
    print(lista_array[i], end=" ")

# Cálculo em milissegundos
tempo_decorrido_ms = (tempo_final - tempo_inicial) * 1000
print(f"\nTempo gasto no Selection Sort: {tempo_decorrido_ms:.2f} ms")