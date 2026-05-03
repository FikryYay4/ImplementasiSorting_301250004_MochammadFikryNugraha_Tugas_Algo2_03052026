#Nama Program      : Perbandingan Sort
#NIM               : 301250004
#Nama              : Mochammad Fikry Nugraha
#Tanggal Pembuatan : 03-Mei-2026
#Nama File         : Perbandingansort_301250004_MochammadFikryNugraha_Tugas_Algo2_03052026.py
import os
import os
import random
from loop_bubble import bubble_sort
from loop_insert import insertion_sort

def generate_data(jumlah):
    data = []
    for i in range(jumlah):
        angka = random.randint(1, 200)
        data.append(angka)
    return data

def tampil_perbandingan(data, hasil_bubble, hasil_insertion):
    # Output
    urut_b, perbandingan_b = hasil_bubble
    urut_i, perbandingan_i = hasil_insertion

    print("\n========================================")
    print("  PERBANDINGAN BUBBLE vs INSERTION SORT")
    print("========================================")
    print(f"Data awal   : {data}")
    print(f"Data urut   : {urut_b}")
    print("----------------------------------------")
    print(f"{'':20} {'Bubble':>10} {'Insertion':>10}")
    print(f"{'Perbandingan':20} {perbandingan_b:>10} {perbandingan_i:>10}")
    print("----------------------------------------")

    selisih = perbandingan_b - perbandingan_i
    if selisih > 0:
        print(f"Insertion Sort lebih efisien {selisih} perbandingan.")
    elif selisih < 0:
        print(f"Bubble Sort lebih efisien {abs(selisih)} perbandingan.")
    else:
        print("Keduanya membutuhkan jumlah perbandingan yang sama.")

def main():
    # Input
    jumlah = int(input("Masukkan jumlah elemen (min 20): "))
    data = generate_data(jumlah)
    print(f"Data yang digenerate : {data}")

    # Process
    hasil_bubble = bubble_sort(data)
    hasil_insertion = insertion_sort(data)

    tampil_perbandingan(data, hasil_bubble, hasil_insertion)

main()
console = input("Tekan Enter untuk keluar...") 
os.system('cls' if os.name == 'nt' else 'clear')