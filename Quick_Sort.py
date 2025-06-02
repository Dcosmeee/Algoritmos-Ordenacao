def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]

        return quick_sort(menores) + [pivo] + quick_sort(maiores)

dados = [8, 5, 9, 7, 2, 3, 4]
print(f'lista original:{dados}')
ordenada = quick_sort(dados)
print(f'lista ordenada:{ordenada}')   