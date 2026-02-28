# NOMOR 1

angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

# Ketika user memasukkan nilai 0, kode akan mengakses angka_list[0] sehingga mencetak 10
# Ketika user memasukkan huruf seperti 'a', kode akan gagal mengkonversi huruf tersebut menjadi angka,
# sehingga program akan error, tepatnya ValueError
# Ketika user memasukkan bilangan positif maupun negatif, itu tergantung terhadap nilainya apakah diluar indeks atau tidak
# jika didalam indeks (0 sampai 2) dan (-1 sampai -3), maka kode akan berjalan lancar
# sedangkan jika diluar itu, maka program akan error, tepatnya IndexError
# Setelah itu, apapun yang user input, program akan tetap menjalankan blok kode finally, sehingga tetap mencetak
# 'Selesai', apapun yang terjadi


# NOMOR 2

try:
    bilangan_pertama = float(input("Masukkan nilai bilangan pertama : "))
    bilangan_kedua = float(input("Masukkan nilai bilangan kedua : "))
except ValueError:
    print("Harus berupa bilangan!")
except ZeroDivisionError:
    print("Penyebut tidak boleh nol (0)!")    
except Exception as e:
    print("Terjadi kesalahan yang tidak terduga")
else:
    hasil = bilangan_pertama/bilangan_kedua
    print(f"Hasil bagi kedua bilangan tersebut adalah : {hasil}")
finally:
    print("Selesai.")