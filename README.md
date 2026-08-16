# 🌤️ Aplikasi Cuaca Sederhana

Aplikasi cuaca berbasis terminal (CLI) yang dibuat dengan Python. Proyek ini dibuat sebagai latihan untuk memahami konsumsi API, parsing JSON, dan penanganan error dasar di Python.

## ✨ Fitur

- Cek cuaca real-time untuk kota mana pun di dunia
- Menampilkan suhu, "terasa seperti", kelembapan, dan kecepatan angin
- Tidak butuh API key — langsung jalan setelah install dependency
- Penanganan error dasar (koneksi internet mati, kota tidak ditemukan, timeout)

## 🧰 Teknologi yang Digunakan

- **Python 3**
- **[requests](https://pypi.org/project/requests/)** — untuk mengirim HTTP request
- **[wttr.in](https://wttr.in)** — API cuaca gratis tanpa perlu registrasi/API key

## 📦 Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/USERNAME-KAMU/NAMA-REPO.git
   cd NAMA-REPO
   ```

2. Install dependency yang dibutuhkan:
   ```bash
   pip install requests
   ```

## 🚀 Cara Menjalankan

```bash
python aplikasicuaca.py
```

Lalu ketik nama kota saat diminta, misalnya:

```
Masukkan nama kota: Bandung
```

Ketik `keluar` untuk menghentikan program.

## 📸 Contoh Output

```
========================================
  CUACA DI BANDUNG
========================================
  Kondisi        : Partly cloudy
  Suhu           : 24°C
  Terasa seperti : 26°C
  Kelembapan     : 78%
  Kecepatan angin: 12 km/jam
========================================
```

## 🗺️ Rencana Pengembangan (To-Do)

- [ ] Prakiraan cuaca 7 hari ke depan
- [ ] Dukungan satuan Fahrenheit
- [ ] Versi GUI (Tkinter atau web dengan Flask)
- [ ] Simpan riwayat pencarian kota

## 📄 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran, bebas digunakan dan dimodifikasi.

## 🙋 Kontak

Dibuat oleh **Farrel Radyandry w/Claude AI** — jangan ragu buka issue atau pull request kalau ada saran perbaikan.
