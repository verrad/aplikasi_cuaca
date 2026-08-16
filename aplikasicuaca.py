"""
Aplikasi Cuaca Sederhana
-------------------------
Proyek belajar Python untuk pemula: konsumsi API, parsing JSON, dan
penanganan error dasar.

API yang dipakai: wttr.in — GRATIS, TANPA API KEY, tanpa perlu daftar.
Cocok untuk latihan sebelum pindah ke API yang butuh key (misal
OpenWeatherMap).

Cara pakai:
    python aplikasi_cuaca.py
    lalu ketik nama kota, misal: Bandung

Butuh library 'requests'. Kalau belum ada, install dulu:
    pip install requests
"""

import requests


def ambil_data_cuaca(nama_kota: str) -> dict | None:
    """
    Mengambil data cuaca dari API wttr.in untuk kota tertentu.
    Mengembalikan dictionary berisi data cuaca, atau None jika gagal.
    """
    # format=j1 artinya minta hasil dalam bentuk JSON lengkap
    url = f"https://wttr.in/{nama_kota}?format=j1"

    try:
        respons = requests.get(url, timeout=10)
        respons.raise_for_status()  # error jika status code bukan 200
        return respons.json()
    except requests.exceptions.ConnectionError:
        print("❌ Gagal terhubung ke internet. Cek koneksi kamu.")
    except requests.exceptions.Timeout:
        print("❌ Permintaan terlalu lama (timeout). Coba lagi.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Terjadi error dari server: {e}")
    except Exception as e:
        print(f"❌ Terjadi kesalahan tak terduga: {e}")

    return None


def tampilkan_cuaca(data: dict, nama_kota: str) -> None:
    """
    Menampilkan data cuaca dengan format yang mudah dibaca.
    """
    try:
        kondisi_sekarang = data["current_condition"][0]

        suhu_celsius = kondisi_sekarang["temp_C"]
        terasa_seperti = kondisi_sekarang["FeelsLikeC"]
        kelembapan = kondisi_sekarang["humidity"]
        kecepatan_angin = kondisi_sekarang["windspeedKmph"]
        deskripsi = kondisi_sekarang["weatherDesc"][0]["value"]

        print("\n" + "=" * 40)
        print(f"  CUACA DI {nama_kota.upper()}")
        print("=" * 40)
        print(f"  Kondisi        : {deskripsi}")
        print(f"  Suhu           : {suhu_celsius}°C")
        print(f"  Terasa seperti : {terasa_seperti}°C")
        print(f"  Kelembapan     : {kelembapan}%")
        print(f"  Kecepatan angin: {kecepatan_angin} km/jam")
        print("=" * 40 + "\n")

    except (KeyError, IndexError):
        print("❌ Format data tidak sesuai. Mungkin nama kota salah.")


def main():
    print("=== APLIKASI CUACA SEDERHANA ===")
    print("(Ketik 'keluar' untuk berhenti)\n")

    while True:
        nama_kota = input("Masukkan nama kota: ").strip()

        if nama_kota.lower() == "keluar":
            print("Sampai jumpa!")
            break

        if not nama_kota:
            print("⚠️  Nama kota tidak boleh kosong.\n")
            continue

        data = ambil_data_cuaca(nama_kota)

        if data:
            tampilkan_cuaca(data, nama_kota)


if __name__ == "__main__":
    main()
    