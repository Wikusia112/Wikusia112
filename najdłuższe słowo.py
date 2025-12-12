def najdluzsze_slowo(tekst):
    tekst = tekst + " "
    dlugosc = len(tekst)
    liczba_liter = 0
    liczba_liter_najdluzsze = 0

    for j in range(0, dlugosc, liczba_liter + 1):
        liczba_liter = 0
        for i in range(dlugosc):
            if tekst[i+j] != " " and i+j < dlugosc-1:
                liczba_liter += 1
            else:
                if liczba_liter > liczba_liter_najdluzsze:
                    liczba_liter_najdluzsze = liczba_liter
                break

    return liczba_liter_najdluzsze

print("Podaj tekst:")
a = str(input())
print("Liczba liter w najdłuższym słowie:")
print(najdluzsze_slowo(a))