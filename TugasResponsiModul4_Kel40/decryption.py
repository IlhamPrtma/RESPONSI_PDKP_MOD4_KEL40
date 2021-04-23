class decryption :

    def dekrip(kata):
        kata = kata.lower()
        hasil_encode = ''
        for char in kata:
            if char in abjad:
             index_lama = abjad.index(char)
             index_baru = (index_lama + -40) % len(abjad)
             abjad_baru = abjad[index_baru]
             hasil_encode = hasil_encode + abjad_baru 
            else:
             hasil_encode = hasil_encode + ' ' 
        return hasil_encode

