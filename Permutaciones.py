import itertools

n = int(input("Digite el valor de n: "))

if n > 0 and n < 10:
    miLista = []
    i = 1
    while i <= n:
        miLista.append(i)
        i +=1

    resultado = list(itertools.permutations(miLista))
    print(resultado)
else:
    print("el numero debe ser mayor que cero y menor que 10")