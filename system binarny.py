print("Liczba w systemie binarnym (a):")
a = str(input())

def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna.__len__()
    wynik = 0

@@ -10,5 +7,22 @@ def dekoduj_system_binarny(liczba_binarna):

    return wynik

def zamień_na_system_binarny(liczba):
    temp = int(liczba)
    liczba_binarna = ""
    while temp > 0:
        reminder = temp % 2
        temp //= 2
        liczba_binarna = str(reminder) + liczba_binarna

    return liczba_binarna

print("Liczba w systemie binarnym (a):")
a = str(input())
print("Liczba w systemie dziesiętnym:")
print(dekoduj_system_binarny(a))
print(dekoduj_system_binarny(a))

print("Liczba w systemie dziesiętnym: (b):")
b = str(input())
print("Liczba w systemie binarnym")
print(zamień_na_system_binarny(b))