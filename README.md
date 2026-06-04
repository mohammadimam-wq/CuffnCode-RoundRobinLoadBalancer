# Round Robin Load Balancer Simulation

## Deskripsi Project

Project ini merupakan simulasi sederhana algoritma **Load Balancing Round Robin** menggunakan bahasa pemrograman Python.

Tujuan dari project ini adalah mendistribusikan request yang masuk ke beberapa server secara bergiliran sehingga beban kerja dapat terbagi secara merata.

Project ini dibuat sebagai implementasi konsep **Komputasi Paralel dan Sistem Terdistribusi**.

---

## Anggota Kelompok

**Nama:** Mohammad Imam Tanthowi

**NIM:** 152024156

**Kelas:** AA

---

## Latar Belakang

Dalam sistem komputer modern, banyak pengguna dapat mengakses layanan secara bersamaan. Jika semua request diproses oleh satu server, maka server tersebut dapat mengalami overload dan menurunkan performa sistem.

Salah satu solusi yang digunakan adalah **Load Balancing**, yaitu teknik untuk membagi beban kerja ke beberapa server agar pemrosesan menjadi lebih efisien.

Pada project ini digunakan algoritma **Round Robin**, yaitu metode yang membagikan request secara bergiliran ke setiap server yang tersedia.

---

## Konsep Round Robin

Algoritma Round Robin bekerja dengan cara memberikan request ke server secara berurutan.

Contoh:

Request 1 → Server 1

Request 2 → Server 2

Request 3 → Server 3

Request 4 → Server 1

Request 5 → Server 2

Request 6 → Server 3

dan seterusnya.

Dengan metode ini setiap server memperoleh beban kerja yang relatif seimbang.

---

## Source Code

```python
import threading
import time

servers = ["Server 1", "Server 2", "Server 3"]
index = 0

def process_request(server, request):
    print(f"Request {request} diproses oleh {server}")
    time.sleep(1)

def load_balancer(request):
    global index

    server = servers[index]

    t = threading.Thread(
        target=process_request,
        args=(server, request)
    )

    t.start()

    index = (index + 1) % len(servers)

for i in range(1, 11):
    load_balancer(i)
```

---

## Cara Menjalankan Program

### 1. Clone Repository

```bash
git clone https://github.com/username/round-robin-load-balancer.git
```

### 2. Masuk ke Folder Project

```bash
cd round-robin-load-balancer
```

### 3. Jalankan Program

```bash
python load_balancing.py
```

---

## Output Program

```text
Request 1 diproses oleh Server 1
Request 2 diproses oleh Server 2
Request 3 diproses oleh Server 3
Request 4 diproses oleh Server 1
Request 5 diproses oleh Server 2
Request 6 diproses oleh Server 3
Request 7 diproses oleh Server 1
Request 8 diproses oleh Server 2
Request 9 diproses oleh Server 3
Request 10 diproses oleh Server 1
```

---

## Analisis Hasil

Jumlah request yang diproses:

| Server   | Total Request |
| -------- | ------------- |
| Server 1 | 4             |
| Server 2 | 3             |
| Server 3 | 3             |

Hasil menunjukkan bahwa algoritma Round Robin berhasil mendistribusikan request secara bergiliran sehingga beban kerja server menjadi lebih merata.

---

## Hubungan dengan Komputasi Paralel

Project ini menerapkan beberapa konsep dalam Komputasi Paralel dan Sistem Terdistribusi:

* Load Balancing
* Distributed System
* Resource Allocation
* Task Distribution
* Parallel Processing menggunakan Thread

Penggunaan modul `threading` memungkinkan beberapa request diproses secara bersamaan sehingga mensimulasikan lingkungan komputasi paralel sederhana.

---

## Flowchart

```text
START
  |
  v
Request Masuk
  |
  v
Load Balancer
  |
  v
Pilih Server Berikutnya
  |
  v
Kirim Request ke Server
  |
  v
Proses Request
  |
  v
Tampilkan Output
  |
  v
END
```

---

## Arsitektur Sistem

```text
               +------------+
               |   CLIENT   |
               +------------+
                     |
                     v
           +------------------+
           | LOAD BALANCER    |
           +------------------+
              /      |      \
             /       |       \
            v        v        v

      +---------+ +---------+ +---------+
      |Server 1 | |Server 2 | |Server 3 |
      +---------+ +---------+ +---------+
```

---

## Kelebihan Algoritma Round Robin

* Mudah diimplementasikan
* Distribusi beban merata
* Tidak memerlukan perhitungan kompleks
* Cocok untuk simulasi load balancing sederhana

---

## Kekurangan Algoritma Round Robin

* Tidak memperhatikan kapasitas masing-masing server
* Tidak mempertimbangkan kondisi server saat ini
* Kurang optimal jika spesifikasi server berbeda

---

## Kesimpulan

Berdasarkan hasil pengujian, algoritma Round Robin berhasil mendistribusikan request ke beberapa server secara bergiliran. Metode ini mampu menjaga pemerataan beban kerja sehingga tidak ada server yang menerima seluruh request secara bersamaan.

Project ini menunjukkan implementasi sederhana konsep Load Balancing, Sistem Terdistribusi, dan Komputasi Paralel menggunakan bahasa Python.

---

## Lisensi

Project ini dibuat untuk keperluan pembelajaran pada mata kuliah Komputasi Paralel dan Sistem Terdistribusi.
