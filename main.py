print("hello world")#çıktı aldık
print("kerem arda açar")

x = 3# int değişken tanımladık
print(x)#değişkenin çıktıısnı aldık
isim = "kerem"#string
fiyat = 13.95#float
aldimi = True  #boolean

#örnek
isim = "Moby Dick"
mobyDicksayfa = 195
mobyDickagirlik = 13.45
yenimi = True
print(isim)

print(type(mobyDicksayfa))

isim = input("isminiz nedir? ")
print("merhaba "+isim)

#örnek
yemek = input("en sevdiğin yemek? ")
isim = input("ismin nedir? ")
print(isim+" "+yemek+" sever")

isim = "kerem"

yas=31
print(isim+" "+str(yas)+" "+"yasinda")#int i stringe çevirdik
#bool() boolean çevirme
#float() float çevirme için

#matematik işlemleri
x = 9
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x // y)# // sayıları tam olarak böler
print(x % y)# % kalan bulur
print(x ** y)#x in y ye üstünü alır 9 üzeri 5

#proje
x = input("ilk sayıyı giriniz: ")
y = input("ikinci sayiyi giriniz: ")
print(int(x) + int(y))

#matematik fonksiyonları

print(round(9.8))#yuvarlama yapar
print(abs(-9))#mutlak değer yani sıfıra olan uzaklığını alır
import math#math kütüphanesi ekledik
print(math.sqrt(9))# karekök alma
print(min(9,10,56))#içine yazılan sayıların en küçüğünü bulur
print(max(9,10,56))#içine yazılan sayıların en büyüğünü bulur

# #stringler
isim = 'muh"a"mmet'

mektup = """merhba kerem 
umarim iyisindir"""

print(mektup)

isim = 'muhammet okula gidiyor'
       #01234567
print(isim[0])# muhammetteki m yi çıktı aldık

print(isim[0:3])#0dan başla 3 e kadar git ama 3 ü alma dedik
print(isim[-4:-1])#mme çıktısını aldık
print(len(isim))#uzunluğunu öğrendik
print(isim.title())#ilk harfi büyütttü
print(isim.upper())#bütün harfeleri büyüttü
print(isim.lower())#bütün harfeleri küçülttü
print(isim.find("e"))#e harfinin sırasını gösteriyor UYARI:e yerine E yazsaydık E olmadığı için -1 değeri verir
print(isim.replace("gidiyor", "gitmiyor"))#gidiyoru gitmiyor olarak değiştirdik

#proje
isim = input("lütfen adınızı giriniz: ")
print(isim.title())

#KOŞULLU İFADELER
yagmurlu = False
gunesli = False

if yagmurlu:
    print("ceketini giy")

elif gunesli:
    print("güneş gözlüğünü tak")
else:
    print("normal bir şekilde dışarı çık")

#MANTIKSAL OPERATÖRLER
ehliyet = True  # Örnek: Ehliyet varsa True, yoksa False
araba = True  # Örnek: Araba varsa True, yoksa False

if ehliyet and araba:
    print("Araba kullanabilirsin")

elif araba and not ehliyet:
    print("Araba kullanmak için kursa git")

elif ehliyet or araba:
    print("Araba kullanmana çok az kaldı")

else:
    print("Araba kullanmak için çok zaman var")

#karşılaştırma operatörleri
sıcaklık = 30

if sıcaklık > 30:
    print("hava çok sıcak")

elif sıcaklık >= 0:
    print("hava çok soğuk")

#Proje
yas = int(input("Yaşınızı giriniz: "))
okul = input("Okula gidiyor musunuz? (Evet: 'e', Hayır: 'h'): ")

if yas >= 18 and okul == "h":
    print("Askere git")

elif yas >= 18 and okul == 'e':
    print("Okul bitince askere git")

else:
    print("askerlik yaşın gelmedi")

#WHİLE DÖNGÜSÜ
i = 1
while i <= 5:
    print(i)
    i = i + 1
# 5 yerine örneğin 1000 yazarsa bine kadar çıkıt alırsın

#DİZELER
isciler = ["mehmet","ahmet","abdul","kerim","ali"]
print(isciler[0])#sondaki ismi aliyi yazdırmak için -1 yazarsın kerim için -2 falan
isciler = ["mehmet","ahmet","abdul","kerim","ali"]
print(isciler[0:3])#0 dan 3 e kadar ama kerim dahil değil

#HESAP MAKİNESİ
sayi1 = int(input("ilk sayıyı giriniz: "))
sayi2 = int(input("ikinci sayıyı giriniz: "))
islem = input("""yapmak istediğiniz işlemi giriniz: 
(+-*/)""")

if islem == "+":
    print("sonuc:"+str(sayi1+sayi2))

elif islem == "-":
    print("sonuc:" + str(sayi1 - sayi2))
elif islem == "*":
    print("sonuc:" + str(sayi1 * sayi2))
elif islem == "/":
    print("sonuc:" + str(sayi1 / sayi2))



