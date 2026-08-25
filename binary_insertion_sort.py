import sys
import time


def busca_binaria(lista, valor, inicio, fim):
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] <= valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio


def binary_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_atual = lista[i]
        pos = busca_binaria(lista, valor_atual, 0, i - 1)

        j = i - 1
        while j >= pos:
            lista[j + 1] = lista[j]
            j -= 1

        lista[pos] = valor_atual

    return lista


def carregar_dados(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return [int(linha.strip()) for linha in arquivo if linha.strip()]


def main():
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} <arquivo.txt>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]

    try:
        lista = carregar_dados(nome_arquivo)
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
        sys.exit(1)
    except ValueError:
        print("Erro: conteúdo inválido no arquivo.")
        sys.exit(1)

    lista_original = lista.copy()

    inicio = time.perf_counter()
    binary_insertion_sort(lista)
    fim = time.perf_counter()

    tempo_ms = (fim - inicio) * 1000

    print("Algoritmo: Binary Insertion Sort")
    print(f"Arquivo: {nome_arquivo}")
    print(f"Elementos: {len(lista)}")
    print(f"Ordenado corretamente: {'Sim' if lista == sorted(lista_original) else 'Não'}")
    print(f"Primeiros 10: {lista[:10]}")
    print(f"Tempo: {tempo_ms:.3f} ms")


if __name__ == "__main__":
    main()
