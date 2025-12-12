def dekoduj_system_o_podstawie(liczba_binarna, podstawa):
    dlugosc_tekstu = liczba_binarna.__len__()
    wynik = 0
    for i in range(dlugosc_tekstu):
        znak = liczba_binarna[dlugosc_tekstu - i - 1]
        wynik += int(znak) * podstawa ** i

    return wynik

def zamien_na_system_o_podstawie(liczba, podstawa):
    temp = int(liczba)
    liczba_binarna = ""
    while temp > 0:
        reminder = temp % podstawa
        temp //= podstawa
        liczba_binarna = str(reminder) + liczba_binarna

    return liczba_binarna

print("Podaj liczbę w innym systemie niż dziesiętny:")
a = str(input())
print("Podaj podstawę systemu (<10) tej liczby:")
podstawa1 = int(input())
print("Liczba w systemie dziesiętnym:")
print(dekoduj_system_o_podstawie(a, podstawa1))

# --- konwersja z systemu dziesiętnego na dowolny system (podstawa <= 10) ---
print("Podaj liczbę w systemie dziesiętnym:")
b = str(input())
print("Podaj podstwaę systemu (<10) na który chcesz konwertowac tą liczbę:")
podstawa2 = int(input())
print("Liczba w tym systemie:")
print(zamien_na_system_o_podstawie(b, podstawa2))