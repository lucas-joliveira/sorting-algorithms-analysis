import time

# 1. Função auxiliar: Busca Binária para achar a posição correta
def busca_binaria(array, valor, inicio, fim):
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if array[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio

# 2. Carrega os dados primeiro (Fora da medição)
with open("1000_numbers.txt", "r") as arquivo:
    lista_array = [int(linha.strip()) for linha in arquivo if linha.strip()]

# 3. INÍCIO DA MEDIÇÃO
tempo_inicial = time.perf_counter()

# Algoritmo Binary Insertion Sort
n = len(lista_array)
for i in range(1, n):
    valor_atual = lista_array[i]
    
    # Descobre onde o valor_atual deve entrar olhando apenas para a parte já ordenada (0 até i-1)
    posicao_correta = busca_binaria(lista_array, valor_atual, 0, i - 1)
    
    # Desloca todos os elementos maiores para a direita para abrir espaço
    j = i - 1
    while j >= posicao_correta:
        lista_array[j + 1] = lista_array[j]
        j -= 1
        
    # Insere o elemento na posição encontrada
    lista_array[posicao_correta] = valor_atual

# 4. FIM DA MEDIÇÃO
tempo_final = time.perf_counter()

print("Ordenação concluída!")

# Imprime os 10 primeiros
for i in range(10):
    print(lista_array[i], end=" ")

# Cálculo em milissegundos
tempo_decorrido_ms = (tempo_final - tempo_inicial) * 1000
print(f"\nTempo gasto no Binary Insertion Sort: {tempo_decorrido_ms:.2f} ms")