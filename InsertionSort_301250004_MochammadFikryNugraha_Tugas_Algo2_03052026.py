#Nama Program      : Insertion Sort
#NIM               : 301250004
#Nama              : Mochammad Fikry Nugraha
#Tanggal Pembuatan : 03-Mei-2026
#Nama File         : InsertionSort_301250004_MochammadFikryNugraha_Tugas_Algo2_03052026.py
import os
import random
from loop_insert import insertion_sort

def generate_data(jumlah):
    data = []
    for i in range(jumlah):
        angka = random.randint(1, 200)
        data.append(angka)
    return data

def tampil_hasil(data, hasil, perbandingan):
    # Output
    print("\n===== HASIL INSERTION SORT =====")
    print(f"Data awal  : {data}")
    print(f"Data urut  : {hasil}")
    print(f"Perbandingan : {perbandingan} kali")

def main():
    # Input
    jumlah = int(input("Masukkan jumlah elemen (min 20): "))
    data = generate_data(jumlah)
    print(f"Data yang digenerate : {data}")

    # Process
    hasil, perbandingan = insertion_sort(data)

    tampil_hasil(data, hasil, perbandingan)

main()
console = input("Tekan Enter untuk keluar...") 
os.system('cls' if os.name == 'nt' else 'clear')