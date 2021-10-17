x = input("İlk sayıyı giriniz: ")
y = input("İkinci sayıyı giriniz: ")
x=float(x)
y=float(y)

###########
print("[1] Toplama")
print("[2] Çıkartma")
print("[3] Çarpma")
print("[4] Bölme")
print("[5] Üs Alma")
print("[6] Çıkış")

z=input("Lütfen yapmak istediğiniz işlemi seçiniz:")
z=int(z)
############


if z==1:
    print("Sonuç:",x+y)
elif z==2:
    print("Sonuç:",x-y)
elif z==3:
    print("Sonuç:",x*y)
elif z==4:
    print("Sonuç:",x/y)
elif z==5:
    print("Sonuç:",x**y)
elif z==6:
    print("Çıkılıyor...")
    quit()
else:
    print("Hatalı girdiniz!!!")
