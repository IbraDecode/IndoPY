
# Referensi Bahasa Pemrograman IndoPy

**Pembuat:** Ibra Ramdan

IndoPy adalah bahasa pemrograman yang dirancang untuk pemula dan pelajar di Indonesia, dengan sintaks yang intuitif dan mudah dimengerti menggunakan Bahasa Indonesia. IndoPy merupakan turunan dari Python dan JavaScript, menggabungkan kemudahan penggunaan Python dengan fleksibilitas JavaScript, serta mempertahankan pemetaan 1:1 yang logis ke Python untuk kompilasi.

## Daftar Isi

1.  [Struktur Kontrol](#struktur-kontrol)
    *   [jika (if)](#jika)
    *   [jika tidak (else)](#jika-tidak)
    *   [jika kondisi lain (elif)](#jika-kondisi-lain)
    *   [selama (while)](#selama)
    *   [untuk (for)](#untuk)
2.  [Fungsi & Kelas](#fungsi--kelas)
    *   [fungsi (def)](#fungsi)
    *   [kembali (return)](#kembali)
    *   [kelas (class)](#kelas)
    *   [__init__ (constructor)](#__init__)
    *   [self (this)](#self)
3.  [Operator & Logika](#operator--logika)
    *   [dan (and)](#dan)
    *   [atau (or)](#atau)
    *   [bukan (not)](#bukan)
    *   [lebih dari (>)](#lebih-dari)
    *   [kurang dari (<)](#kurang-dari)
    *   [sama dengan (==)](#sama-dengan)
    *   [tidak sama dengan (!=)](#tidak-sama-dengan)
    *   [lebih dari atau sama dengan (>=)](#lebih-dari-atau-sama-dengan)
    *   [kurang dari atau sama dengan (<=)](#kurang-dari-atau-sama-dengan)
4.  [Tipe Data](#tipe-data)
    *   [angka (int, float)](#angka)
    *   [teks (str)](#teks)
    *   [daftar (list)](#daftar)
    *   [kamus (dict)](#kamus)
    *   [benar (True)](#benar)
    *   [salah (False)](#salah)
5.  [Fitur Umum](#fitur-umum)
    *   [tulis (print)](#tulis)
    *   [masukan (input)](#masukan)
    *   [acak (random)](#acak)
    *   [waktu (time)](#waktu)
    *   [buka file (open)](#buka-file)
    *   [hapus file (os.remove)](#hapus-file)
6.  [Import Modul](#import-modul)
    *   [pakai nama_modul (import module_name)](#pakai-nama_modul)
7.  [Error Handling](#error-handling)
    *   [coba (try)](#coba)
    *   [jika error (except)](#jika-error)
    *   [akhir (finally)](#akhir)
8.  [Komentar](#komentar)
    *   [-- komentar (# comment)](#--komentar)




## 1. Struktur Kontrol

Struktur kontrol digunakan untuk mengatur alur eksekusi program berdasarkan kondisi atau iterasi.

### jika (if)

Digunakan untuk mengeksekusi blok kode jika suatu kondisi bernilai `benar`.

**Sintaks:**
```indopy
jika kondisi:
    -- blok kode yang akan dieksekusi
```

**Contoh:**
```indopy
umur = 20
jika umur >= 17:
    tulis("Kamu sudah cukup umur untuk memiliki KTP.")
```

### jika tidak (else)

Digunakan bersama dengan `jika` untuk mengeksekusi blok kode alternatif jika kondisi `jika` bernilai `salah`.

**Sintaks:**
```indopy
jika kondisi:
    -- blok kode jika kondisi benar
jika tidak:
    -- blok kode jika kondisi salah
```

**Contoh:**
```indopy
suhu = 25
jika suhu > 30:
    tulis("Cuaca sangat panas.")
jika tidak:
    tulis("Cuaca cukup nyaman.")
```

### jika kondisi lain (elif)

Digunakan untuk mengecek kondisi tambahan jika kondisi `jika` sebelumnya bernilai `salah`. Bisa digunakan berkali-kali.

**Sintaks:**
```indopy
jika kondisi1:
    -- blok kode jika kondisi1 benar
jika kondisi lain kondisi2:
    -- blok kode jika kondisi2 benar
jika tidak:
    -- blok kode jika semua kondisi di atas salah
```

**Contoh:**
```indopy
nilai = 75
jika nilai >= 90:
    tulis("Nilai A")
jika kondisi lain nilai >= 80:
    tulis("Nilai B")
jika kondisi lain nilai >= 70:
    tulis("Nilai C")
jika tidak:
    tulis("Nilai D")
```

### selama (while)

Mengeksekusi blok kode berulang kali selama suatu kondisi bernilai `benar`.

**Sintaks:**
```indopy
selama kondisi:
    -- blok kode yang akan diulang
```

**Contoh:**
```indopy
hitung = 0
selama hitung < 5:
    tulis("Hitungan ke:", hitung)
    hitung = hitung + 1
```

### untuk (for)

Mengeksekusi blok kode untuk setiap item dalam sebuah urutan (misalnya, daftar atau string).

**Sintaks:**
```indopy
untuk variabel dalam urutan:
    -- blok kode yang akan dieksekusi
```

**Contoh:**
```indopy
daftar_buah = ["apel", "pisang", "ceri"]
untuk buah dalam daftar_buah:
    tulis("Saya suka", buah)

untuk i dalam rentang(5):
    tulis("Angka:", i)
```



## 2. Fungsi & Kelas

Fungsi dan kelas adalah blok bangunan fundamental untuk mengorganisir kode dan menciptakan program yang modular dan dapat digunakan kembali.

### fungsi (def)

Digunakan untuk mendefinisikan sebuah fungsi, yaitu blok kode yang dapat dipanggil dan dieksekusi berkali-kali.

**Sintaks:**
```indopy
fungsi nama_fungsi(parameter1, parameter2, ...):
    -- blok kode fungsi
    kembali nilai -- (opsional)
```

**Contoh:**
```indopy
fungsi tambah(a, b):
    hasil = a + b
    kembali hasil

angka1 = 10
angka2 = 5
jumlah = tambah(angka1, angka2)
tulis("Hasil penjumlahan:", jumlah)
```

### kembali (return)

Digunakan di dalam fungsi untuk mengembalikan sebuah nilai dari fungsi tersebut. Setelah `kembali` dieksekusi, fungsi akan berhenti.

**Sintaks:**
```indopy
kembali nilai
```

**Contoh:**
```indopy
fungsi kali(x, y):
    kembali x * y

hasil_kali = kali(7, 8)
tulis("Hasil perkalian:", hasil_kali)
```

### kelas (class)

Digunakan untuk mendefinisikan sebuah kelas, yang merupakan cetak biru untuk membuat objek. Kelas mendefinisikan properti (atribut) dan perilaku (metode) yang akan dimiliki oleh objeknya.

**Sintaks:**
```indopy
kelas NamaKelas:
    -- definisi atribut dan metode
```

**Contoh:**
```indopy
kelas Mobil:
    fungsi __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    fungsi info(self):
        tulis("Mobil ini bermerek", self.merek, "dan berwarna", self.warna)

mobil_saya = Mobil("Toyota", "Merah")
mobil_saya.info()
```

### __init__ (constructor)

Metode khusus dalam sebuah kelas yang secara otomatis dipanggil saat objek baru dari kelas tersebut dibuat. Digunakan untuk menginisialisasi atribut objek.

**Sintaks:**
```indopy
fungsi __init__(self, parameter1, ...):
    self.atribut = parameter1
```

**Contoh:**
```indopy
kelas Hewan:
    fungsi __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        tulis(self.nama, "adalah seekor", self.jenis)

kucing = Hewan("Kitty", "Kucing")
```

### self (this)

Parameter pertama dari setiap metode dalam sebuah kelas, yang secara konvensional dinamakan `self`. Ini merujuk pada instance objek itu sendiri, memungkinkan akses ke atribut dan metode lain dari objek tersebut. Mirip dengan `this` di JavaScript atau Java.

**Sintaks:**
```indopy
fungsi nama_metode(self, parameter, ...):
    self.atribut = nilai
```

**Contoh:**
```indopy
kelas Lingkaran:
    fungsi __init__(self, radius):
        self.radius = radius

    fungsi hitung_luas(self):
        -- Menggunakan self.radius untuk mengakses atribut objek
        kembali 3.14 * self.radius * self.radius

lingkaran_kecil = Lingkaran(5)
tulis("Luas lingkaran:", lingkaran_kecil.hitung_luas())
```



## 3. Operator & Logika

Operator digunakan untuk melakukan operasi pada nilai dan variabel. Operator logika digunakan untuk menggabungkan atau memodifikasi kondisi.

### dan (and)

Operator logika yang mengembalikan `benar` jika kedua operand bernilai `benar`.

**Sintaks:**
```indopy
kondisi1 dan kondisi2
```

**Contoh:**
```indopy
umur = 25
memiliki_sim = benar

jika umur >= 18 dan memiliki_sim:
    tulis("Anda bisa mengemudi.")
```

### atau (or)

Operator logika yang mengembalikan `benar` jika salah satu dari operand bernilai `benar`.

**Sintaks:**
```indopy
kondisi1 atau kondisi2
```

**Contoh:**
```indopy
hari = "Minggu"
jika hari == "Sabtu" atau hari == "Minggu":
    tulis("Ini adalah akhir pekan.")
```

### bukan (not)

Operator logika yang membalik nilai kebenaran dari operand. Jika operand `benar`, `bukan` akan mengembalikan `salah`, dan sebaliknya.

**Sintaks:**
```indopy
bukan kondisi
```

**Contoh:**
```indopy
is_aktif = salah

jika bukan is_aktif:
    tulis("Pengguna tidak aktif.")
```

### lebih dari (>)

Operator perbandingan yang mengembalikan `benar` jika operand kiri lebih besar dari operand kanan.

**Sintaks:**
```indopy
nilai1 > nilai2
```

**Contoh:**
```indopy
a = 10
b = 5

jika a > b:
    tulis("a lebih besar dari b")
```

### kurang dari (<)

Operator perbandingan yang mengembalikan `benar` jika operand kiri lebih kecil dari operand kanan.

**Sintaks:**
```indopy
nilai1 < nilai2
```

**Contoh:**
```indopy
a = 10
b = 5

jika b < a:
    tulis("b lebih kecil dari a")
```

### sama dengan (==)

Operator perbandingan yang mengembalikan `benar` jika kedua operand memiliki nilai yang sama.

**Sintaks:**
```indopy
nilai1 == nilai2
```

**Contoh:**
```indopy
status = "selesai"

jika status == "selesai":
    tulis("Tugas telah selesai.")
```

### tidak sama dengan (!=)

Operator perbandingan yang mengembalikan `benar` jika kedua operand memiliki nilai yang berbeda.

**Sintaks:**
```indopy
nilai1 != nilai2
```

**Contoh:**
```indopy
kata1 = "apel"
kata2 = "jeruk"

jika kata1 != kata2:
    tulis("Kata-kata ini berbeda.")
```

### lebih dari atau sama dengan (>=)

Operator perbandingan yang mengembalikan `benar` jika operand kiri lebih besar dari atau sama dengan operand kanan.

**Sintaks:**
```indopy
nilai1 >= nilai2
```

**Contoh:**
```indopy
umur_minimum = 18
umur_pengguna = 18

jika umur_pengguna >= umur_minimum:
    tulis("Diizinkan masuk.")
```

### kurang dari atau sama dengan (<=)

Operator perbandingan yang mengembalikan `benar` jika operand kiri lebih kecil dari atau sama dengan operand kanan.

**Sintaks:**
```indopy
nilai1 <= nilai2
```

**Contoh:**
```indopy
batas_maksimal = 100
jumlah_item = 99

jika jumlah_item <= batas_maksimal:
    tulis("Jumlah item masih dalam batas.")
```



## 4. Tipe Data

Tipe data mendefinisikan jenis nilai yang dapat disimpan dan dimanipulasi dalam program.

### angka (int, float)

Mewakili nilai numerik. `int` untuk bilangan bulat (contoh: 10, -5), `float` untuk bilangan desimal (contoh: 3.14, -0.5).

**Contoh:**
```indopy
jumlah_apel = 10 -- Tipe data int
harga_per_kg = 2.5 -- Tipe data float

tulis("Jumlah apel:", jumlah_apel)
tulis("Harga per kg:", harga_per_kg)
```

### teks (str)

Mewakili urutan karakter, seperti kata atau kalimat. Ditulis dalam tanda kutip tunggal atau ganda.

**Contoh:**
```indopy
salam = "Halo dunia!" -- Tipe data teks
nama_produk = 'IndoPy'

tulis(salam)
tulis("Nama produk:", nama_produk)
```

### daftar (list)

Mewakili koleksi item yang terurut dan dapat diubah. Item-item dipisahkan oleh koma dan diapit oleh kurung siku `[]`.

**Contoh:**
```indopy
daftar_angka = [1, 2, 3, 4, 5] -- Tipe data daftar
daftar_campuran = ["apel", 10, benar]

tulis("Daftar angka:", daftar_angka)
tulis("Item pertama:", daftar_angka[0])

daftar_angka.tambah(6) -- Menambahkan item
tulis("Daftar setelah ditambah:", daftar_angka)
```

### kamus (dict)

Mewakili koleksi pasangan kunci-nilai yang tidak terurut dan dapat diubah. Kunci harus unik dan tidak dapat diubah (immutable).

**Contoh:**
```indopy
data_pengguna = {"nama": "Budi", "umur": 30, "kota": "Jakarta"} -- Tipe data kamus

tulis("Nama pengguna:", data_pengguna["nama"])

data_pengguna["pekerjaan"] = "Programmer" -- Menambahkan pasangan kunci-nilai
tulis("Data pengguna terbaru:", data_pengguna)
```

### benar (True)

Mewakili nilai boolean `True` (benar). Digunakan dalam ekspresi logika dan kondisi.

**Contoh:**
```indopy
is_valid = benar

jika is_valid:
    tulis("Data valid.")
```

### salah (False)

Mewakili nilai boolean `False` (salah). Digunakan dalam ekspresi logika dan kondisi.

**Contoh:**
```indopy
is_selesai = salah

jika is_selesai == salah:
    tulis("Tugas belum selesai.")
```



## 5. Fitur Umum

Fitur-fitur umum ini menyediakan kemampuan dasar untuk interaksi dengan pengguna, manipulasi data, dan operasi sistem file.

### tulis (print)

Digunakan untuk menampilkan output ke konsol atau layar. Dapat menerima satu atau lebih argumen.

**Sintaks:**
```indopy
tulis(argumen1, argumen2, ...)
```

**Contoh:**
```indopy
tulis("Halo, IndoPy!")

pesan = "Ini adalah pesan."
angka = 123
tulis(pesan, angka, "selesai.")
```

### masukan (input)

Digunakan untuk menerima input dari pengguna melalui konsol. Input yang diterima selalu dalam bentuk `teks` (string).

**Sintaks:**
```indopy
variabel = masukan("Pesan prompt: ")
```

**Contoh:**
```indopy
nama_pengguna = masukan("Masukkan nama Anda: ")
tulis("Selamat datang,", nama_pengguna)

umur_str = masukan("Berapa umur Anda? ")
umur_int = int(umur_str) -- Konversi ke angka jika diperlukan
tulis("Umur Anda adalah:", umur_int)
```

### acak (random)

Modul `acak` menyediakan fungsi untuk menghasilkan angka acak. Anda perlu mengimpornya terlebih dahulu.

**Sintaks:**
```indopy
pakai acak

angka_acak = acak.randint(batas_bawah, batas_atas) -- Menghasilkan bilangan bulat acak
```

**Contoh:**
```indopy
pakai acak

dadu = acak.randint(1, 6)
tulis("Anda melempar dadu dan mendapatkan:", dadu)
```

### waktu (time)

Modul `waktu` menyediakan fungsi terkait waktu, seperti menunda eksekusi program (`waktu.tidur`). Anda perlu mengimpornya terlebih dahulu.

**Sintaks:**
```indopy
pakai waktu

waktu.tidur(detik) -- Menunda eksekusi selama \'detik\' yang ditentukan
```

**Contoh:**
```indopy
pakai waktu

tulis("Mulai...")
waktu.tidur(2) -- Menunggu 2 detik
tulis("2 detik berlalu.")
```

### buka file (open)

Digunakan untuk membuka file untuk operasi baca, tulis, atau tambah. Mengembalikan objek file.

**Sintaks:**
```indopy
file_obj = buka("nama_file.txt", "mode")
-- mode: "r" (baca), "w" (tulis, akan menimpa), "a" (tambah)

-- Pastikan untuk menutup file setelah selesai
file_obj.tutup()
```

**Contoh:**
```indopy
-- Menulis ke file
file_tulis = buka("catatan.txt", "w")
file_tulis.tulis("Baris pertama.\n")
file_tulis.tulis("Baris kedua.")
file_tulis.tutup()

-- Membaca dari file
file_baca = buka("catatan.txt", "r")
isi = file_baca.baca()
tulis("Isi file:\n", isi)
file_baca.tutup()
```

### hapus file (os.remove)

Digunakan untuk menghapus file dari sistem. Anda perlu mengimpor modul `os` terlebih dahulu.

**Sintaks:**
```indopy
pakai os

os.hapus("nama_file.txt")
```

**Contoh:**
```indopy
pakai os

-- Buat file dummy untuk dihapus
file_dummy = buka("file_untuk_dihapus.txt", "w")
file_dummy.tulis("Ini akan dihapus.")
file_dummy.tutup()

tulis("Mencoba menghapus file...")
os.hapus("file_untuk_dihapus.txt")
tulis("File berhasil dihapus.")
```



## 6. Import Modul

Modul adalah file Python yang berisi definisi dan pernyataan. Dengan mengimpor modul, Anda dapat menggunakan fungsi, kelas, dan variabel yang didefinisikan di dalamnya.

### pakai nama_modul (import module_name)

Digunakan untuk mengimpor modul atau bagian tertentu dari modul agar dapat digunakan dalam kode Anda.

**Sintaks:**
```indopy
pakai nama_modul
-- atau
pakai nama_modul sebagai alias
-- atau
dari nama_modul pakai nama_objek
```

**Contoh:**
```indopy
pakai math -- Mengimpor seluruh modul math
tulis("Nilai PI:", math.pi)

pakai acak sebagai rnd -- Mengimpor modul acak dengan alias rnd
angka_random = rnd.randint(1, 100)
tulis("Angka acak:", angka_random)

dari waktu pakai tidur -- Mengimpor fungsi tidur dari modul waktu
tulis("Menunggu 1 detik...")
tidur(1)
tulis("Selesai menunggu.")
```



## 7. Error Handling

Penanganan kesalahan memungkinkan program untuk merespons kesalahan yang terjadi selama eksekusi tanpa berhenti secara tiba-tiba.

### coba (try)

Mendefinisikan blok kode yang akan dipantau untuk kesalahan (exception).

**Sintaks:**
```indopy
coba:
    -- blok kode yang mungkin menimbulkan kesalahan
jika error TipeKesalahan:
    -- blok kode yang dieksekusi jika TipeKesalahan terjadi
jika error:
    -- blok kode yang dieksekusi jika kesalahan lain terjadi
akhir:
    -- blok kode yang selalu dieksekusi, terlepas dari apakah ada kesalahan atau tidak
```

**Contoh:**
```indopy
coba:
    hasil = 10 / 0
    tulis(hasil)
jika error:
    tulis("Terjadi kesalahan: Pembagian dengan nol tidak diizinkan.")
selesai

coba:
    angka = int("abc")
jika error ValueError:
    tulis("Kesalahan nilai: Input bukan angka.")
jika error:
    tulis("Terjadi kesalahan lain.")
akhir:
    tulis("Proses penanganan kesalahan selesai.")
selesai
```

### jika error (except)

Menentukan blok kode yang akan dieksekusi jika jenis kesalahan tertentu (atau kesalahan apa pun jika tidak ditentukan) terjadi di dalam blok `coba`.

**Sintaks:**
```indopy
jika error NamaKesalahan:
    -- tangani NamaKesalahan
atau
jika error:
    -- tangani semua kesalahan
```

**Contoh:**
```indopy
coba:
    daftar_angka = [1, 2, 3]
    tulis(daftar_angka[3])  -- Akan menyebabkan IndexError
jika error IndexError:
    tulis("Kesalahan indeks: Indeks di luar jangkauan.")
selesai
```

### akhir (finally)

Mendefinisikan blok kode yang akan selalu dieksekusi, terlepas dari apakah kesalahan terjadi atau tidak di dalam blok `coba`. Berguna untuk operasi pembersihan.

**Sintaks:**
```indopy
akhir:
    -- blok kode yang selalu dieksekusi
```

**Contoh:**
```indopy
file_obj = buka("data.txt", "w")

coba:
    file_obj.tulis("Beberapa data.")
akhir:
    file_obj.tutup()
    tulis("File telah ditutup.")
selesai
```

---

## 8. Komentar

Komentar digunakan untuk menambahkan catatan atau penjelasan dalam kode yang diabaikan oleh interpreter. Berguna untuk membuat kode lebih mudah dibaca dan dipahami.

### `#` komentar

Digunakan untuk membuat komentar satu baris. Semua teks setelah `#` pada baris yang sama akan dianggap sebagai komentar.

**Sintaks:**
```indopy
# Ini adalah komentar satu baris
variabel = 10  # Ini juga komentar, menjelaskan variabel
```

**Contoh:**
```indopy
# Program sederhana untuk menghitung luas persegi panjang

panjang = 10     # Mendefinisikan panjang
lebar = 5        # Mendefinisikan lebar

luas = panjang * lebar   # Menghitung luas

tulis("Luas persegi panjang adalah:", luas)  # Menampilkan hasil
```

---

## Lisensi

MIT License â€“ bebas digunakan & dimodifikasi untuk edukasi.