def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Assume que o menor valor está na posição atual
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        # Troca os elementos
        lista[i], lista[menor] = lista[menor], lista[i]

# Exemplo de uso
dados = [28, 65, 20, 34, 57]
selection_sort(dados)
print("Lista ordenada:", dados)

