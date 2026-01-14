import random # Mengimpor modul random untuk menghasilkan angka acak
import sys # Mengimpor modul sys untuk mengontrol exit program

class NumberGuessGame: # Kelas untuk permainan tebak angka
    def __init__(self): # Inisialisasi angka rahasia
        self.secret = random.randint(1, 100) # Menghasilkan angka acak antara 1 dan 100

    def start(self): # Memulai permainan
        print("\n=== Number Guessing Game Tugas UAS Zakaria ===") # Menampilkan judul permainan
        print("Tebak Angka (1 - 100)!") # Instruksi permainan

        while True: # Loop utama permainan
            try: # Mencoba untuk mendapatkan input dari pemain
                guess = int(input("Masukkan tebakanmu: ")) # Meminta input tebakan dari pemain
            except ValueError: # Menangani kesalahan jika input bukan angka
                print("Input harus berupa angka!") # Memberi tahu pemain tentang kesalahan input
                continue # Melanjutkan ke iterasi berikutnya

            if guess < self.secret: # Memeriksa apakah tebakan terlalu kecil
                print("Terlalu kecil!") 
            elif guess > self.secret: # Memeriksa apakah tebakan terlalu besar
                print("Terlalu besar!")
            else: # Tebakan benar
                print("Benar! Kamu menang!") # Memberi tahu pemain bahwa mereka menang
                break # Keluar dari loop permainan jika tebakan benar


def main(): # Fungsi utama untuk menjalankan permainan
    while True: # Loop untuk mengulang permainan
        # Membuat objek game baru setiap ronde
        game = NumberGuessGame() # Membuat instance dari kelas NumberGuessGame
        game.start() # Memulai permainan

        ulang = input("\nMain lagi? (ya/tidak): ").lower() # Meminta input dari pemain untuk mengulang permainan

        if ulang != "ya": # Memeriksa apakah pemain ingin mengulang permainan
            print("\nGame telah berakhir.") 
            print("Terima kasih sudah bermain!")
            sys.exit()  # algoritma menutup program


# Program utama
if __name__ == "__main__": # Memastikan bahwa file ini dijalankan sebagai program utama
    main() # Memanggil fungsi utama untuk memulai program