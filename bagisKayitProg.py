from tkinter import * #pencere oluşturuyoruz.
from PIL import ImageTk, Image #arkaplan için tanımlama yapılır.
import sqlite3 #veritabanı tanımlaması

	
	
root = Tk() #pencere
root.geometry('500x500')#pencerenin ölçüleri girilir
root.title("IHTIYAC KAYIT EKRANI")#pencerenin başlığı girilir.
path = "kedi.png" #arkaplan fotoğrafı için kullanacağımız dosyayı tanımlamak için kullanıyoruz.
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "no")#fotoğrafın biçimsel boyutları için kullanılır

	

ad=StringVar() #Ad değişkeninin türü
telNo=IntVar() #Telefon Numarası değişkeninin türü
cinsler=StringVar() #Cins değişkeninin türü
bgsList=StringVar() #bgsList değişkenin türü
konum=StringVar() #konum değişkeninin türü	

	

	

def database():
   adSoyad=ad.get()#veritabanından ad soyadı döndürür
   telefon=telNo.get()#veritabanından telefon no'yu döndürür
   cins=cinsler.get()#veritabanından cinsleri döndürür
   bagisListesi=bgsList.get()#veritabanından  döndürür
   mekan=konum.get()#veritabanından konum döndürür
   conn = sqlite3.connect('bagis.db')#veritabanı bağlantısı  sağlanır ve veritabanının adı girilir.
   with conn: #bağlantı sağlandı
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS bagisListesi (adSoyad TEXT,telefon TEXT,cins TEXT,bagisListesi TEXT,mekan TEXT)')#veritabanındaki tabloda değişkenlerin oluşturulması
   cursor.execute('INSERT INTO bagisListesi (adSoyad,telefon,cins,bagisListesi,mekan) VALUES(?,?,?,?,?)',(adSoyad,telefon,cins,bagisListesi,mekan))#veritabanındaki değerler eklenir.
   for row in cursor.execute('SELECT * FROM bagisListesi'):
      print(row)
      conn.commit()#veritabanı bağlantı
	   
	   
	             
label_0 = Label(root, text="Sokak Hayvanları İhtiyaç Kayıt Ekranı",width=30,font=("bold", 15))#label_0'ı "Sokak Hayvanları İhtiyaç Kayıt Ekranı"olarak tanımlar.
label_0.place(x=90,y=53)#label_0'ın konumu
	

	
label_1 = Label(root, text="İsim ve Soyisim",bg='green',fg='white',width=20,font=("bold", 10))#label_1'i"İsim Soyisim"olarak tanımlar ve özelliklerini belirler.
label_1.place(x=70,y=130)#label_1'in konumu
entry_1 = Entry(root,textvar=ad)#ad soyad için label atadık
entry_1.place(x=260,y=130) #entry_1'in konumu
	

label_2 = Label(root, text="Tel No(Başında '0' olmadan)",bg='green',fg='white',width=20,font=("bold", 10))#label_2'yi"Tel No"olarak tanımlar ve özelliklerini belirler.
label_2.place(x=70,y=180)#label_2'nin konumu
	

entry_2 = Entry(root,textvar=telNo)#telno için label atadık
entry_2.place(x=260,y=180)#entry_2'nin konumu
	

label_3 = Label(root, text="Cins",bg='green',fg='white',width=20,font=("bold", 10))#label_3'ü"Cins"olarak tanımlar ve özelliklerini belirler.
label_3.place(x=70,y=230)#label_3'ün konumu
	

Radiobutton(root, text="Kedi",padx = 5, variable=cinsler, value='Kedi').place(x=255,y=230)#cins belirlemek için yapılmış buton ve butonların konumları.|Kedi Butonu
Radiobutton(root, text="Köpek",padx = 20, variable=cinsler, value='Köpek').place(x=310,y=230)#cins belirlemek için yapılmış buton ve butonların konumları.|Köpek Butonu
	

label_4 = Label(root, text="Yardım Türü",bg='green',fg='white',width=20,font=("bold", 10))#label_4'ü"Bağış Türü"olarak tanımlar.
label_4.place(x=70,y=280)#label_4'ün konumu
	
list1 = ['Mama','Su','Temizlik','Veteriner']; #gereksinimlerin listesi
droplist=OptionMenu(root,bgsList, *list1)#listenin içeriğine liste 1 diyoruz
droplist.config(width=20)#listenin boyutu
bgsList.set('İhtiyaç Türünü Seçin') #listenin başlığı 
droplist.place(x=255,y=280) #listenin konumu 

label_5 = Label(root, text="Adres",bg='green',fg='white',width=20,font=("bold", 10)) #label_5'i"Bağış Türü"olarak tanımlar.
label_5.place(x=70,y=330)#label_5'in konumu
entry_3 = Entry(root,textvar=konum)#konum için label atadık
entry_3.place(x=260,y=330)#entry_3'ün konumu

Button(root, text='Kaydet',width=20,bg='purple',fg='black',command=database).place(x=180,y=380)#kaydet butonu ve özellikleri

	
root.mainloop()#pencereyi döngüye sokar
