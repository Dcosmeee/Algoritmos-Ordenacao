def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def Heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    print(f'heap Maximo:{lista}')


    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
        print(f'passo {n - 1}:{lista}')
dados = [8, 0, 7, 9, 2, 4, 10, 87, 6, 20, 14]
print(f'lista original:{dados}')
Heap_sort(dados)
print(f'lista ordenada:{dados}')                        