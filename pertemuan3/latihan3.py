class Motor:
    def __init__(self, warna, merek, tahun):
        self.warna = warna
        self.merek = merek
        self.tahun = tahun
    
    def klakson(self):
        print("TITTT TITTTT!!!!!")

    def kebut(self):
        print("VROOM VROOOMMM!!!!")
    
m1 = Motor("Hitam" , "Yamaha" , "2020")
m2 = Motor("Putih" , "Beat" , "2024")
m3 = Motor("Merah" , "Mio" , "2019")

print(f"Sebelum diubah, Warna : {m2.warna}")
m2.warna = "Pink" 
m2.klakson()
m2.kebut()
print(f"Setelah diubah, Warna : {m2.warna}")