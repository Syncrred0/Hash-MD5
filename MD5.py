# ============================================================
# Program: Deteksi Perubahan Data Profil User dengan MD5
# Bahasa : Python 3
# Library: hashlib (built-in, tidak perlu instalasi)
# ============================================================

import hashlib

def buat_hash_md5(nama: str, email: str, nomor_hp: str) -> str:
    """
    Menggabungkan data profil user, lalu menghasilkan hash MD5-nya.
    
    Argumen:
        nama      : Nama lengkap user
        email     : Alamat email user
        nomor_hp  : Nomor HP user

    Return:
        String hash MD5 sepanjang 32 karakter (huruf kecil hex)
    """
    # Gabungkan semua field dengan separator '|' agar
    # "Ana|Budi" tidak dianggap sama dengan "An|aBudi"
    data_gabungan = f"{nama}|{email}|{nomor_hp}"

    # Encode ke bytes (MD5 bekerja pada level bytes, bukan string)
    data_bytes = data_gabungan.encode("utf-8")

    # Buat objek MD5 dan hitung hash-nya
    hash_md5 = hashlib.md5(data_bytes).hexdigest()

    return hash_md5


def tampilkan_hasil(hash_lama: str, hash_baru: str) -> None:
    """
    Membandingkan dua hash MD5 dan menampilkan hasilnya ke layar.
    """
    print("\n" + "=" * 50)
    print("        HASIL PEMERIKSAAN INTEGRITAS DATA")
    print("=" * 50)
    print(f"  Hash Lama : {hash_lama}")
    print(f"  Hash Baru : {hash_baru}")
    print("-" * 50)

    if hash_lama == hash_baru:
        print("  STATUS    : ✅ Data Tetap Sama")
    else:
        print("  STATUS    : ⚠️  Data Telah Dimodifikasi!")

    print("=" * 50)


def input_profil(label: str) -> tuple[str, str, str]:
    """
    Meminta user memasukkan data profil dari keyboard.
    Mengembalikan tuple (nama, email, nomor_hp).
    """
    print(f"\n{'─' * 50}")
    print(f"  INPUT DATA {label}")
    print(f"{'─' * 50}")
    nama     = input("  Nama     : ").strip()
    email    = input("  Email    : ").strip()
    nomor_hp = input("  Nomor HP : ").strip()
    return nama, email, nomor_hp


# ─────────────────────────────────────────────
#                  PROGRAM UTAMA
# ─────────────────────────────────────────────
if __name__ == "__main__":

    print("╔══════════════════════════════════════════════╗")
    print("║   SISTEM DETEKSI PERUBAHAN DATA PROFIL USER  ║")
    print("╚══════════════════════════════════════════════╝")

    # LANGKAH 1 & 2: Terima input awal, buat hash pertama
    nama1, email1, hp1 = input_profil("AWAL (Data Tersimpan)")
    hash_awal = buat_hash_md5(nama1, email1, hp1)

    # LANGKAH 3: Simpan hash awal (simulasi: disimpan di variabel/database)
    print(f"\n  [INFO] Hash awal tersimpan: {hash_awal}")

    # LANGKAH 4: Terima input data baru (simulasi admin/user mengedit)
    nama2, email2, hp2 = input_profil("BARU  (Data Diperiksa Admin)")
    hash_baru = buat_hash_md5(nama2, email2, hp2)

    # LANGKAH 5 & 6: Bandingkan dan tampilkan status
    tampilkan_hasil(hash_awal, hash_baru)