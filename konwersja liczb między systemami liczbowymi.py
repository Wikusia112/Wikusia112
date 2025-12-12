def convert_from_decimal(n: int, base: int) -> str:
    """Konwertuje z systemu dziesiętnego do systemu o podanej podstawie (≤10)."""
    if not (2 <= base <= 10):
        raise ValueError("Podstawa systemu musi być w zakresie 2–10.")

    if n == 0:
        return "0"

    wynik = ""
    while n > 0:
        wynik = str(n % base) + wynik
        n //= base
    return wynik


def convert_to_decimal(number: str, base: int) -> int:
    """Konwertuje liczbę z systemu o podanej podstawie (≤10) na dziesiętny."""
    if not (2 <= base <= 10):
        raise ValueError("Podstawa systemu musi być w zakresie 2–10.")

    wynik = 0
    potega = 1

    for cyfra in reversed(number):
        wynik += int(cyfra) * potega
        potega *= base

    return wynik


# Testy
print("Testy konwersji:")
print("255 (10) ->", convert_from_decimal(255, 2), "(binarnie)")
print("255 (10) ->", convert_from_decimal(255, 8), "(ósemkowo)")
print("255 (10) ->", convert_from_decimal(255, 5), "(piątkowo)")
print("11111111 (2) ->", convert_to_decimal("11111111", 2))
print("377 (8) ->", convert_to_decimal("377", 8))