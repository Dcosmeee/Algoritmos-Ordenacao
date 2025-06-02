def Bubble_Sort(lista):
    n = len(lista)

    for j in range(n- 1):
        for c in range(n-1):
            if lista[c] > lista[c + 1]:
                lista[c], lista[c + 1] = lista[c + 1], lista[c]

dados = [8 , 6, 3, 7, 9, 4, 5]
Bubble_Sort(dados)
print(f'dados ordenamdos:',dados)             
