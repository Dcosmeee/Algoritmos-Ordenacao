def Merge_Sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]


        Merge_Sort(esquerda)
        Merge_Sort(direita)
        
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k+= 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1 

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1


        print(f'intercalaçao:{lista}')

dados = [8, 3, 5, 2, 9, 1]
print(f'lista original:{dados}')
Merge_Sort(dados)
print(f'lista ordenada:{dados}')        

