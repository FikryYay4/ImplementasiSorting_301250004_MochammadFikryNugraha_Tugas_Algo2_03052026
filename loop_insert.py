def insertion_sort(data):
    hasil = data[:]
    perbandingan = 0

    for i in range(1, len(hasil)):
        kunci = hasil[i]
        j = i - 1

        while j >= 0:
            perbandingan += 1
            if hasil[j] > kunci:
                hasil[j + 1] = hasil[j]
                j -= 1
            else:
                break

        hasil[j + 1] = kunci

    return hasil, perbandingan