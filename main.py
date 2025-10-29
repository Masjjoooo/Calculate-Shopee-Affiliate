import os
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)
NAMA_FILE = "hasil.txt"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print(Fore.CYAN + "=" * 55)
    print(Fore.YELLOW + "💸 Shopee Affiliate Komisi Calculator (by Masjjoooo)")
    print(Fore.CYAN + "=" * 55 + "\n")

def hitung_komisi(harga_produk, persen_komisi):
    return round(harga_produk * (persen_komisi / 100), 2)

def simpan_hasil(teks):
    """Simpan hasil ke file txt"""
    with open(NAMA_FILE, "a", encoding="utf-8") as f:
        f.write(teks + "\n")

def tampilkan_hasil(harga, persen, komisi, simpan=True):
    hasil_teks = (
        f"Harga Produk : Rp{harga:,.2f}\n"
        f"Persentase   : {persen}%\n"
        f"Komisi Dapat : Rp{komisi:,.2f}\n"
        f"{'-'*40}"
    )

    print(Fore.GREEN + "\n📊 Hasil Perhitungan:")
    print(Fore.WHITE + "-" * 40)
    print(f"{Fore.CYAN}Harga Produk : {Fore.WHITE}Rp{harga:,.2f}")
    print(f"{Fore.CYAN}Persentase   : {Fore.WHITE}{persen}%")
    print(f"{Fore.CYAN}Komisi Dapat : {Fore.YELLOW}Rp{komisi:,.2f}")
    print(Fore.WHITE + "-" * 40 + "\n")

    if simpan:
        simpan_hasil(hasil_teks)

def hitung_satu_produk():
    clear()
    header()
    harga = float(input(Fore.GREEN + "Masukkan harga produk (Rp): " + Fore.WHITE))
    persen = float(input(Fore.GREEN + "Masukkan persen komisi (%): " + Fore.WHITE))
    komisi = hitung_komisi(harga, persen)
    tampilkan_hasil(harga, persen, komisi)

    # Simpan catatan tambahan
    simpan_hasil(f"[SINGLE] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    simpan_hasil("")

    input(Fore.MAGENTA + "✅ Hasil disimpan ke 'hasil.txt'. Tekan ENTER untuk kembali ke menu...")

def hitung_massal():
    clear()
    header()
    total_komisi = 0
    n = int(input(Fore.GREEN + "Berapa jumlah produk yang ingin dihitung? " + Fore.WHITE))
    print()

    simpan_hasil(f"[MASSAL] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    simpan_hasil("-" * 40)

    for i in range(1, n + 1):
        print(Fore.YELLOW + f"Produk ke-{i}:")
        harga = float(input(Fore.GREEN + "  Harga produk (Rp): " + Fore.WHITE))
        persen = float(input(Fore.GREEN + "  Persen komisi (%): " + Fore.WHITE))
        komisi = hitung_komisi(harga, persen)
        total_komisi += komisi
        tampilkan_hasil(harga, persen, komisi, simpan=True)

    total_line = f"💰 Total komisi dari {n} produk: Rp{total_komisi:,.2f}"
    print(Fore.MAGENTA + total_line + "\n")
    simpan_hasil(total_line)
    simpan_hasil("=" * 40 + "\n")

    input(Fore.MAGENTA + "✅ Semua hasil disimpan ke 'hasil.txt'. Tekan ENTER untuk kembali ke menu...")

def menu():
    while True:
        clear()
        header()
        print(Fore.CYAN + "Pilih mode perhitungan:\n")
        print(Fore.YELLOW + "1." + Fore.WHITE + " Hitung satu produk (single)")
        print(Fore.YELLOW + "2." + Fore.WHITE + " Hitung banyak produk (massal)")
        print(Fore.YELLOW + "3." + Fore.WHITE + " Lihat file hasil komisi")
        print(Fore.YELLOW + "4." + Fore.WHITE + " Keluar\n")

        pilihan = input(Fore.GREEN + "Masukkan pilihan [1/2/3/4]: " + Fore.WHITE)

        if pilihan == '1':
            hitung_satu_produk()
        elif pilihan == '2':
            hitung_massal()
        elif pilihan == '3':
            clear()
            if os.path.exists(NAMA_FILE):
                header()
                print(Fore.YELLOW + f"📂 Isi file {NAMA_FILE}:\n")
                with open(NAMA_FILE, "r", encoding="utf-8") as f:
                    print(Fore.WHITE + f.read())
            else:
                print(Fore.RED + "Belum ada hasil tersimpan.")
            input(Fore.MAGENTA + "\nTekan ENTER untuk kembali ke menu...")
        elif pilihan == '4':
            clear()
            print(Fore.CYAN + "Terima kasih telah menggunakan kalkulator komisi Shopee! 💫\n")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            input("Tekan ENTER untuk ulang...")

if __name__ == "__main__":
    menu()
