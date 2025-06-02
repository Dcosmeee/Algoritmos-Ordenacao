def insertion_sort(lista):
    for c in range(1, len(lista)):
        chave = lista[c]
        j = c - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave
        print(f'passos {c}: {lista}')

dados = [5, 8, 10, 7, 6, 0, 27, 36, 97, 100]
print(f'lista original: {dados}')
insertion_sort(dados)
print(f'lista ordenada:{dados}')

