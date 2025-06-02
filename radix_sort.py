def counting_sort_digito(lista, digito):
    n = len(lista)
    output = [0] * n
    contador = [0] * 10

    
    for i in range(n):
        indice = (lista[i] // digito) % 10
        contador[indice] += 1

   
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    
    i = n - 1
    while i >= 0:
        indice = (lista[i] // digito) % 10
        output[contador[indice] - 1] = lista[i]
        contador[indice] -= 1
        i -= 1

    
    for i in range(n):
        lista[i] = output[i]

def radix_sort(lista):
    if not lista:
        return

    maior = max(lista)
    digito = 1

    while maior // digito > 0:
        counting_sort_digito(lista, digito)
        print(f"Depois de ordenar pelo dígito {digito}: {lista}")
        digito *= 10


dados = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original:", dados)
radix_sort(dados)
print("Ordenada:", dados)
