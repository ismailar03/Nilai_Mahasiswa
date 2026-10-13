import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nilai import hitung_nilai_akhir, tentukan_grade, cek_kelulusan


class TestHitungNilaiAkhir(unittest.TestCase):
    def test_tc1_nilai_normal(self):
        self.assertEqual(hitung_nilai_akhir(80, 70, 90), 81.0)

    def test_tc2_semua_nol(self):
        self.assertEqual(hitung_nilai_akhir(0, 0, 0), 0)

    def test_tc3_semua_seratus(self):
        self.assertEqual(hitung_nilai_akhir(100, 100, 100), 100)

    def test_tc4_nilai_negatif(self):
        with self.assertRaises(ValueError):
            hitung_nilai_akhir(-1, 70, 90)

    def test_tc5_nilai_lebih_dari_100(self):
        with self.assertRaises(ValueError):
            hitung_nilai_akhir(80, 101, 90)


class TestTentukanGrade(unittest.TestCase):
    def test_tc1_grade_a(self):
        self.assertEqual(tentukan_grade(85), "A")

    def test_tc2_grade_b(self):
        self.assertEqual(tentukan_grade(70), "B")

    def test_tc3_grade_c(self):
        self.assertEqual(tentukan_grade(55), "C")

    def test_tc4_grade_d(self):
        self.assertEqual(tentukan_grade(40), "D")

    def test_tc5_grade_e(self):
        self.assertEqual(tentukan_grade(39.99), "E")

    def test_tc6_nilai_tidak_valid(self):
        with self.assertRaises(ValueError):
            tentukan_grade(101)


class TestCekKelulusan(unittest.TestCase):
    def test_tc1_lulus(self):
        self.assertEqual(cek_kelulusan(70, 80), "LULUS")

    def test_tc2_nilai_kurang(self):
        self.assertEqual(cek_kelulusan(50, 90), "TIDAK LULUS")

    def test_tc3_kehadiran_kurang(self):
        self.assertEqual(cek_kelulusan(80, 60), "TIDAK LULUS")

    def test_tc4_nilai_dan_kehadiran_kurang(self):
        self.assertEqual(cek_kelulusan(40, 50), "TIDAK LULUS")

    def test_tc5_batas_tepat(self):
        self.assertEqual(cek_kelulusan(55, 75), "LULUS")

    def test_tc6_input_tidak_valid(self):
        with self.assertRaises(ValueError):
            cek_kelulusan(80, 150)


if __name__ == "__main__":
    unittest.main(verbosity=2)
