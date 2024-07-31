print("hello world")
print(3.14)
#çıktı aldık

#DEĞİŞKENLER
#değer saklanmak için ayrılmış hafıza konumu
A = 10
a = 10
# bunlar iki farklı değişken yani python büyük küçük harf farkını biliyor

isim = "acark"
km = 130.7

#TYPE FONKSİYONU
print(type(A))
#type komudu ile değişkenin türünü öğreniyoruz

print("kerem" + "arda")

#TOPLAMA
ilkdeger = 5
ikincideger = 6
print(ilkdeger + ikincideger)
#iki değişkeni topladık

#İNPUT
#kullanıdan girdi alır
x = input("isim gir: ")
print(x)
print(type(x))

y = input("yaşını gir: ")
print(type(y))# değişkenden input aldığımızda her zaman türü string olur eğer işlem yapacaksak bunu int e çevirmeliyiz

z = int(input("yaşını gir: "))
print(type(z))

# ÖRNEKLER
ornek_isim = input("adınızı giriniz: ")
print("hoş geldin" + " " + ornek_isim)