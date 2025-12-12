def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    results = []  # lista pozycji, gdzie znaleziono wzorzec

    for i in range(n - m + 1):  # możliwe pozycje startowe
        match = True
        for j in range(m):  # porównywanie znak po znaku
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            results.append(i)

    return results


# Testy
print(naive_search("ababcabcab", "abc"))  # [2, 5]