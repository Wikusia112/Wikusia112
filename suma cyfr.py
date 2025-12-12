def suma_cyfr(zakres, suma):
    lista = []

    for i in range(zakres + 1):
        pierwsza_cyfra = int(i / 100)
        druga_cyfra = int(i / 10) - pierwsza_cyfra * 10
        trzecia_cyfra = int(i) - (druga_cyfra * 10 + pierwsza_cyfra * 100)
        wynik = pierwsza_cyfra + druga_cyfra + trzecia_cyfra
        if wynik == suma:
            lista.append(i)

    return lista

print("Podaj zakres (max 999):")
a = int(input())
print("Podaj sumę cyfr:")
b = int(input())
print("Znalezione liczby:")
print(suma_cyfr(a, b))