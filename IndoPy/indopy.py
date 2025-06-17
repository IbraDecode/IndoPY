import sys
from translator import translate_indo

def jalankan_file(nama_file):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            kode_indo = file.read()
        kode_python = translate_indo(kode_indo)
        print("=== Hasil Eksekusi ===")
        exec(kode_python, globals())
    except FileNotFoundError:
        print(f"Kesalahan: File tidak ditemukan: {nama_file}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan kode: {e}")

def __main__():
    if len(sys.argv) < 2:
        print("Penggunaan: indopy <nama_file.indopy>")
        print("Contoh: indopy contoh.indopy")
    else:
        jalankan_file(sys.argv[1])

if __name__ == "__main__":
    __main__()


