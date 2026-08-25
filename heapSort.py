import time

# 1. Função que garante a "Regra do Chefe" na pirâmide (Max Heap)
def heapify(array, n, i):
    maior = i              # Inicializa assumindo que a raiz é o maior
    esquerda = 2 * i + 1   # Índice do filho da esquerda
    direita = 2 * i + 2    # Índice do filho da direita

    # Verifica se o filho da esquerda existe e é maior que a raiz
    if esquerda < n and array[esquerda] > array[maior]:
        maior = esquerda

    # Verifica se o filho da direita existe e é maior que o "maior" atual
    if direita < n and array[direita] > array[maior]:
        maior = direita

    # Se o maior número não for a raiz, faz a troca e reorganiza a base
    if maior != i:
        array[i], array[maior] = array[maior], array[i]  # Troca (swap)
        heapify(array, n, maior)                         # Reorganiza recursivamente

# 2. Carrega os dados (Fora da medição)
with open("1000_numbers.txt", "r") as arquivo:
    lista_array = [int(linha.strip()) for linha in arquivo if linha.strip()]

# 3. INÍCIO DA MEDIÇÃO
tempo_inicial = time.perf_counter()

# Algoritmo Heap Sort
n = len(lista_array)

# Passo A: Constrói a pirâmide inicial (Max Heap) a partir do array desordenado
for i in range(n // 2 - 1, -1, -1):
    heapify(lista_array, n, i)

# Passo B: Extrai os elementos um por um
for i in range(n - 1, 0, -1):
    # Move a raiz atual (o maior número de todos) para o final do array
    lista_array[i], lista_array[0] = lista_array[0], lista_array[i]
    
    # Chama o heapify na árvore reduzida (ignorando o que já foi pro final)
    heapify(lista_array, i, 0)

# 4. FIM DA MEDIÇÃO
tempo_final = time.perf_counter()

print("Ordenação concluída!")

# Imprime os 10 primeiros
for i in range(10):
    print(lista_array[i], end=" ")

# Cálculo em milissegundos
tempo_decorrido_ms = (tempo_final - tempo_inicial) * 1000
print(f"\nTempo gasto no Heap Sort: {tempo_decorrido_ms:.2f} ms")