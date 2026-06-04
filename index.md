# 🚀 Round Robin Load Balancer Simulation

## 👨‍🎓 Informasi Mahasiswa

**Nama:** Mohammad Imam Tanthowi  
**NIM:** 152024156  
**Kelas:** AA  

---

## 📖 Deskripsi Project

Project ini merupakan simulasi **Load Balancing** menggunakan algoritma **Round Robin** yang bertujuan mendistribusikan request ke beberapa server secara bergiliran sehingga beban kerja menjadi lebih merata.

---

## 🎯 Tujuan

- Memahami konsep Load Balancing.
- Mengimplementasikan algoritma Round Robin.
- Mempelajari dasar Komputasi Paralel menggunakan Thread.
- Mensimulasikan distribusi request pada sistem terdistribusi.

---

## ⚙️ Cara Kerja

1. Request masuk ke Load Balancer.
2. Load Balancer memilih server berikutnya.
3. Request dikirim ke server yang dipilih.
4. Server memproses request.
5. Proses berulang hingga seluruh request selesai.

---

## 🖥️ Arsitektur Sistem

```text
CLIENT
   |
   v
LOAD BALANCER
 /    |    \
v     v     v
S1    S2    S3
```

---

## 📊 Hasil Program

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

## 📈 Analisis

Distribusi request:

| Server | Jumlah Request |
|---------|---------------|
| Server 1 | 4 |
| Server 2 | 3 |
| Server 3 | 3 |

Hasil menunjukkan bahwa algoritma Round Robin berhasil mendistribusikan request secara merata.

---

## ✅ Kesimpulan

Algoritma Round Robin berhasil membagi request ke tiga server secara bergiliran sehingga beban kerja menjadi lebih seimbang. Program juga menggunakan **threading** untuk mensimulasikan konsep dasar komputasi paralel.
