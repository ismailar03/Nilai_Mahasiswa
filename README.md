# Nilai Mahasiswa - Mini Program & Unit Test

Mini program Python untuk menghitung nilai akhir, grade, dan status kelulusan mahasiswa.
Dibuat untuk Tugas Pertemuan 4 - Membuat Unit Test.

## Fungsi
| Fungsi | Keterangan |
|---|---|
| `hitung_nilai_akhir(tugas, uts, uas)` | 30% tugas + 30% UTS + 40% UAS |
| `tentukan_grade(nilai)` | A >= 85, B >= 70, C >= 55, D >= 40, selain itu E |
| `cek_kelulusan(nilai_akhir, kehadiran)` | LULUS jika nilai >= 55 dan kehadiran >= 75% |

## Cara menjalankan
```bash
python nilai.py                      # jalankan program
python -m unittest discover -v tests # jalankan unit test
```
