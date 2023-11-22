#nonor 1
def profil(Nama, Alamat, Gender, Umur, Hobi):
    print("Nama saya adalah:",Nama)
    print("Alamat saya:",Alamat)
    print("Gender saya adalah:",Gender)
    print("Umur saya adalah:",Umur)
    print("Hobi saya adalah:",Hobi)

profil("Arfan Khoeri", "Kubu Raya", " Laki-Laki",20, "Badminton") 

#nomor 2
def kelulusan(nilai):
    if nilai >= 0 and nilai <= 60:
        return "Gagal"
    elif nilai <= 70:
        return "Baik"
    elif nilai <= 80:
        return "Sangat Baik"
    elif nilai >= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid!"
          
print(kelulusan(60)) 

#nomor 3
def bilangan_ganjil(Nilai): 
    for i in range (Nilai) :
      if i % 2 == 1: 
        print(i)
bilangan_ganjil(100)