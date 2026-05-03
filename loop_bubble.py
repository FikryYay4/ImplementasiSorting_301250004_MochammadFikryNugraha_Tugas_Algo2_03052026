def bubble_sort(data):
    n = len(data)
    hasil = data[:]
    perbandingan = 0

    for i in range(n):
        for j in range(n - i - 1):
            perbandingan += 1
            if hasil[j] > hasil[j + 1]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

    return hasil, perbandingan