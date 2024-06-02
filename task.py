import random
import timeit

# Implementacja algorytmu Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Implementacja algorytmu Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generowanie zestawów danych
def generate_data_sets():
    sizes = [100, 1000, 10000]
    data_sets = {
        'random': [random.sample(range(size * 10), size) for size in sizes],
        'sorted': [list(range(size)) for size in sizes],
        'reverse_sorted': [list(range(size, 0, -1)) for size in sizes]
    }
    return data_sets

# Pomiar czasu wykonania algorytmu sortującego
def measure_time(sort_func, data):
    def wrapper():
        sort_func(data.copy())

    return timeit.timeit(wrapper, number=10) / 10

# Porównanie algorytmów
def compare_algorithms(data_sets):
    results = {'merge_sort': [], 'insertion_sort': [], 'timsort': []}

    for key, data_set in data_sets.items():
        for data in data_set:
            results['merge_sort'].append(measure_time(merge_sort, data))
            results['insertion_sort'].append(measure_time(insertion_sort, data))
            results['timsort'].append(measure_time(sorted, data))

    return results

# Generowanie zestawów danych
data_sets = generate_data_sets()

# Porównanie algorytmów
results = compare_algorithms(data_sets)

# Prezentacja wyników w tabeli
df_results = pd.DataFrame(results, index=[
    'random_100', 'random_1000', 'random_10000',
    'sorted_100', 'sorted_1000', 'sorted_10000',
    'reverse_100', 'reverse_1000', 'reverse_10000'
])

# Wyświetlenie wyników
print("Wyniki porównania czasów wykonania algorytmów sortujących:")
print(df_results)
