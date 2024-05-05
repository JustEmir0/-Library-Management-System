import tkinter as tk
from tkinter import messagebox
from customtkinter import *
from CTkListbox import * 


kullanici_bilgileri = {'isim': '', 'soyisim': ''}


def kaydet():
    with open("kullanici_bilgileri.txt", "w") as dosya:
        dosya.write(f"isim: {isim_entry.get()}\n")
        dosya.write(f"soyisim: {soyisim_entry.get()}\n")

def yükle():
    kullanici_bilgileri = {}
    dosya_adı = "kullanici_bilgileri.txt"
    if os.path.exists(dosya_adı):
        with open(dosya_adı, "r") as dosya:
            for satir in dosya:
                satir = satir.strip()
                if satir:
                    parcalar = satir.split(":")
                    if len(parcalar) == 2:
                        anahtar, deger = parcalar[0].strip(), parcalar[1].strip()
                        kullanici_bilgileri[anahtar] = deger
                    else:
                        print(f"Hatalı biçimlendirilmiş satır: {satir}")
    else:
        print(f"{dosya_adı} adlı dosya bulunamadı. Otomatik olarak oluşturulacak.")
        # Dosyayı otomatik olarak oluştur
        with open(dosya_adı, "w") as dosya:
            dosya.write("isim: \n")
            dosya.write("tC: \n")
    return kullanici_bilgileri


def giriş_yap_üye():
    isim = isim_entry.get()
    soyisim = soyisim_entry.get()

    if len(isim) + len(soyisim) < 5:
        messagebox.showerror('Hata', 'İsim 5 karakterden az olamaz.')
        return

    kullanici_bilgileri['isim'] = isim
    kullanici_bilgileri['soyisim'] = soyisim

    kullanici_bilgilerini_kaydet(kullanici_bilgileri)

    messagebox.showinfo("Başarılı","Üye Kaydınız Oluşturulmuştur.\nKütüphanemize Hoşgeldiniz!")
    root_log.destroy()
    kütüpahane_sistemine_giriş()


def kullanici_bilgilerini_kaydet(bilgiler):
    with open("kullanici_bilgileri.txt", "w") as dosya:
        for anahtar, deger in bilgiler.items():
            dosya.write(f"{anahtar}: {deger}\n")


class Üye:
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim


    def __str__(self):
        return f"{self.isim} {self.soyisim}"
    
class Kitap:
    def __init__(self,kitap_ıd,ad,yazar):
        self.kitap_ıd = kitap_ıd
        self.ad = ad
        self.yazar = yazar
        self.kitap_durum = True

    def kitap_kontrol(self):
        return self.kitap_durum
    

    def __str__(self):
        return f"{self.ad} - {self.yazar}"

class Odunc:
    def __init__(self, kitap, süre, üye):
        self.kitap = kitap
        self.süre = süre
        self.üye = üye


def kütüpahane_sistemine_giriş():
    root = CTk()
    root.title('Kütüphane Yönetim Sistemi')
    root.geometry("700x600")
    frame = CTkFrame(master=root, width=650 , height=500 , corner_radius=30,)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER )

    label_giriş = CTkLabel(master=frame,text="Atatürk Kütüphanesi Dijital Sayfasına Hoşgeldiniz",font=('Arial',20))
    label_giriş.place(x=90, y=10)

    l1 = CTkLabel(master=frame,text="--- Kitap Kiralama Üzerine ---",font=('Arial',16))
    l1.place(x=410,y=50)

    l2 = CTkLabel(master=frame,text="1 - Her Kitabı Birden Fazla\n Kiralayabilirsiniz",font=('Arial',16))
    l2.place(x=390,y=90)

    l3 = CTkLabel(master=frame,text="2 - 4 haftadan daha uzun süre\n kiralama yapamazsınız",font=('Arial',16))
    l3.place(x=390,y=135)

    l4 = CTkLabel(master=frame,text="3 - Tek seferde 3 den fazla kitap \nkiralayamazsınız",font=('Arial',16))
    l4.place(x=390,y=190)


    label_kitaplar = CTkLabel(master=frame,text="Kitap Seçimi",font=('Arial',16))
    label_kitaplar.place(x=17, y=50)
    sec_kitaplar = CTkComboBox(master=frame, values=kitaplar_adlar ,width=250)
    sec_kitaplar.place(x=17, y=80)

    label_odunc_sure = CTkLabel(master=frame,text="Kiralama Süresi(Hafta)",font=('Arial',16))
    label_odunc_sure.place(x=17, y=120)
    entry_odunc_sure = CTkEntry(master=frame,width=70,height=20)
    entry_odunc_sure.place(x=17, y=145)


    label_kiralanan_kitaplar = CTkLabel(master=frame,text="--- Kitaplarınız ---",font=('Arial',20))
    label_kiralanan_kitaplar.place(x=230, y=240)
    listbox_kiralanan_kitaplar = CTkListbox(master=frame, width=570, height=150,)
    listbox_kiralanan_kitaplar.place(x=17, y=270)


    def odunc_al():
        if listbox_kiralanan_kitaplar.size() >= 3:
            messagebox.showerror("Hata", "Maksimum 3 kitap kiralanabilir.")
            return

        isim = kullanici_bilgileri.get('isim')
        soyisim = kullanici_bilgileri.get('soyisim')
        kitap = sec_kitaplar.get()
        süre = entry_odunc_sure.get()

        if not süre.strip():  # Check if süre is empty after stripping whitespace
            messagebox.showerror("Hata", "Kiralama Süresi boş bırakılamaz.")
            return
    
        listbox_kiralanan_kitaplar.insert(tk.END, f"{kitap}, {isim} {soyisim} adına {süre} hafta süre ile kiralanmıştır")
        messagebox.showinfo("Başarılı", "Kitap Kiralama İşlemi Başarılı Bir Şekilde Gerçekleşmiştir")


    btn_kirala = CTkButton(master=frame, width=250, height=27, text="Kitabı Kirala",font=('Arial',16),command=odunc_al)
    btn_kirala.place(x=17,y=180)
    
    
    def odunc_ipt():
        selected_index = listbox_kiralanan_kitaplar.curselection()
        listbox_kiralanan_kitaplar.delete(selected_index)
        messagebox.showinfo("Başarılı", "Kitap İade İşlemi Başarılı Bir Şekilde Gerçekleşmiştir")


    btn_iade = CTkButton(master=frame, width=250 , height=27 , text="Kitabı İade Et",font=('Arial',16),command=odunc_ipt)
    btn_iade.place(x=40, y=455)

    def tümünü_iade_et():
        listbox_kiralanan_kitaplar.delete(0, tk.END)

    btn_temizle = CTkButton(master=frame, width=250, height=27, text="Tümünü İade Et", font=('Arial', 16), command=tümünü_iade_et)
    btn_temizle.place(x=350, y=455)
    
    root.mainloop()


# Bileşenler
kir_kitap = {}
kitaplar = [Kitap("1","Olasılıksız","Adam Fawer"),
            Kitap("2","1984","Gerorge Orwell"),
            Kitap("3","Tehlikeli Oyunlar","Oğuz Atay"),
            Kitap("4","Son Dilek","Andrew Sapkowski"),
            Kitap("5","Simyacı","Paulo Coelho"),
            Kitap("6","Babalar Ve Oğullar","İvan Turgenvey")]
kitaplar_adlar = [f"{kitap.ad} --- {kitap.yazar}" for kitap in kitaplar]

#  ------ Logın Page -------#
root_log = CTk()
root_log.geometry('400x400')
root_log.title('Logın Page')

f1 = CTkFrame(master=root_log,width=250,height=350)
f1.place(x=80,y=20)

l1 = CTkLabel(master=f1,text="Giriş Yap",font=("Helvetica", 22))
l1.place(x=75,y=30)

label_isim = CTkLabel(master=f1,text="İsim",font=('Arial',16))
label_isim.place(x=50, y=90)
isim_entry = CTkEntry(master=f1,width=140, height=23)
isim_entry.place(x=50, y=125)

label_soyisim = CTkLabel(master=f1,text="Soyisim",font=('Arial',16))
label_soyisim.place(x=50, y=160)
soyisim_entry = CTkEntry(master=f1,width=140, height=20)
soyisim_entry.place(x=50, y=195)

btn_giriş_yap_ = CTkButton(master=f1,text='Giriş Yap',font=('Arial',16),width=140, height=23,command=giriş_yap_üye)
btn_giriş_yap_.place(x=50, y=245)

root_log.mainloop()