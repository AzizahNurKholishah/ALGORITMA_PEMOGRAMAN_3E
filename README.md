# 🔺 Menentukan Jenis Segitiga Berdasarkan Panjang Sisi

## 📝 Deskripsi Masalah

Diberikan tiga buah panjang sisi, yaitu sisi a, b, dan c. Tidak semua tiga panjang sisi dapat membentuk sebuah segitiga, sehingga perlu dilakukan pemeriksaan berdasarkan syarat pembentukan segitiga. Jika ketiga sisi memenuhi syarat tersebut, program akan menentukan jenis segitiga berdasarkan kesamaan panjang sisinya, yaitu segitiga sama sisi, segitiga sama kaki, atau segitiga sembarang.

Program ini dibuat menggunakan percabangan untuk mengevaluasi setiap kondisi dan menampilkan hasil sesuai dengan tiga panjang sisi yang dimasukkan oleh pengguna.

## 📥 Input-Proses-Output

**Input:**  Tiga panjang sisi segitiga, yaitu sisi a, b, dan c.

**Proses:**  Program memeriksa apakah ketiga sisi dapat membentuk segitiga menggunakan syarat:
- a + b > c
- a + c > b
- b + c > a

Jika memenuhi, program menentukan jenis segitiga berdasarkan kesamaan panjang sisinya.

**Output:**  Jenis segitiga atau keterangan bahwa ketiga sisi bukan merupakan segitiga.

## 💻 Pseudocode

```text
INPUT a
INPUT b
INPUT c

IF a <= 0 OR b <= 0 OR c <= 0 THEN
    OUTPUT "Bukan segitiga"

ELSE IF a + b <= c OR a + c <= b OR b + c <= a THEN
    OUTPUT "Bukan segitiga"

ELSE IF a = b AND b = c THEN
    OUTPUT "Segitiga sama sisi"

ELSE IF a = b OR a = c OR b = c THEN
    OUTPUT "Segitiga sama kaki"

ELSE
    OUTPUT "Segitiga sembarang"
END IF

