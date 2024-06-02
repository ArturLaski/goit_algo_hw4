# Porównanie Wydajności Algorytmów Sortujących

## Wprowadzenie

Niniejsze badanie porównuje wydajność trzech algorytmów sortujących: Merge Sort (Sortowanie Przez Scalanie), Insertion Sort (Sortowanie Przez Wstawianie) i Timsort (wbudowana funkcja sortująca w Pythonie). Porównanie opiera się na czasach wykonania algorytmów dla różnych zestawów danych.

## Algorytmy

### Merge Sort

Merge Sort to algorytm dziel i zwyciężaj o złożoności czasowej O(n log n).

### Insertion Sort

Insertion Sort to prosty algorytm porównawczy o złożoności czasowej O(n^2).

### Timsort

Timsort to algorytm hybrydowy, wywodzący się z merge sort i insertion sort, o złożoności czasowej O(n log n) w najgorszym przypadku i O(n) w najlepszym przypadku.

## Metodologia

Testowaliśmy algorytmy na zestawach danych o różnych rozmiarach (100, 1000 i 10000) i składach (losowe, posortowane i odwrotnie posortowane). Każdy test był uruchamiany 10 razy, a średni czas wykonania był rejestrowany za pomocą modułu timeit.

## Wyniki

| Zestaw Danych     | Merge Sort | Insertion Sort | Timsort |
|-------------------|------------|----------------|---------|
| Losowe 100        |  0.000097  | 0.000135       | 0.000003|
| Losowe 1000       |  0.001353  | 0.013505       | 0.000065|
| Losowe 10000      |  0.018154  | 1.421449       | 0.000946|
| Posortowane 100   |  0.000094  | 0.000007       | 0.000001|
| Posortowane 1000  |  0.001216  | 0.000073       | 0.000008|
| Posortowane 10000 |  0.015859  | 0.000796       | 0.000078|
| Odwrotne 100      |  0.000088  | 0.000257       | 0.000001|
| Odwrotne 1000     |  0.001225  | 0.025992       | 0.000007|
| Odwrotne 10000    |  0.015949  | 2.794999       | 0.000067|

## Wnioski

Wyniki pokazują, że Timsort przewyższa zarówno Merge Sort, jak i Insertion Sort we wszystkich testowanych scenariuszach. Ta wydajność wynika z hybrydowej natury Timsort, łączącej najlepsze aspekty sortowania przez scalanie i sortowania przez wstawianie. W rezultacie programiści często polegają na wbudowanych algorytmach, takich jak Timsort, ze względu na ich efektywność i niezawodność.

## Repozytorium

Kod do tej analizy jest dostępny w repozytorium `goit-algo-hw-04`.
