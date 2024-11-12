nama_siswa = input('Masukan Nama siswa:')
jumlah_siswa =int(input('Masukan jumlah siswa : '))

total_nilai= 0
for a in range(jumlah_siswa): 
   nilai = float(input(f'Masukan Nilai Ujian Siswa ke-{a + 1 }:'))
   total_nilai += nilai

# if jumlah_siswa > 0:
rata_rata = total_nilai / jumlah_siswa
print(f'Rata-rata nilai dari {jumlah_siswa} siswa adalah: {rata_rata: .2F}')
# else:
#   print('harus lebih dari 0.')


