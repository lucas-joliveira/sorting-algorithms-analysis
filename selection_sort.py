import sys
import time


def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

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
    selection_sort(lista)
    fim = time.perf_counter()

    tempo_ms = (fim - inicio) * 1000

    print("Algoritmo: Selection Sort")
    print(f"Arquivo: {nome_arquivo}")
    print(f"Elementos: {len(lista)}")
    print(f"Ordenado corretamente: {'Sim' if lista == sorted(lista_original) else 'Não'}")
    print(f"Primeiros 10: {lista[:10]}")
    print(f"Tempo: {tempo_ms:.3f} ms")


if __name__ == "__main__":
    main()
