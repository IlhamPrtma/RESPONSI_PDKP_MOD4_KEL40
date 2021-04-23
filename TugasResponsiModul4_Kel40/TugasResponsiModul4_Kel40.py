import decryption

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = 40

print("------------------------------------------")
print("                KELOMPOK 40               ");
print("ARDHIKA AZHAR PRATAMA       21120120140036")
print("MUHAMMAD FACHRURAZI         21120120140104")
print("RIZAL AGATHA ERDIN AGESYAH  21120120120010")
print("ILHAM PRATAMA               21120120130060")
print("             RESPONSI MODUL 4             ")
print("------------------------------------------")

print("1. Enkripsi")
print("2. Dekripsi")
kode = int(input("Pilih mode : "))
print("------------------------------------------")

def encode(kata,cipher_key):
  kata = kata.lower()
  hasil_encode = ''
  for char in kata:
    if char in abjad:
      index_lama = abjad.index(char)
      index_baru = (index_lama + cipher_key ) % len(abjad)
      abjad_baru = abjad[index_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode

kata = input('Masukkan kata/kalimat : ')

if kode == 1 :
    kata_hasil = encode(kata,key)
    print('Hasil enkripsi yaitu : ', kata_hasil)
elif kode == 2 : 
    kata_hasil = encode(kata,-key)
    dekrip = decryption.decryption
    kata_awal = dekrip()
    print('Hasil dekripsi yaitu : ', kata_hasil)
