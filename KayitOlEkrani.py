from tkinter import *
from tkinter import messagebox
import LoginEkrani
import ast

class KayitOlEkrani:
    def __init__(self,window):
        self.window = window
        self.window.title("Kayıt Ekranı")
        self.window.geometry('925x500+300+200')
        self.window.configure(bg="#fff")
        self.window.resizable(False, False)
        def giris_yap():
            self.window.destroy()  # Giriş ekranını kapat
            ana_pencere = Tk()  # Yeni pencere oluştur
            LoginEkrani.LoginEkrani(ana_pencere)  # Ana uygulamayı başlat
            ana_pencere.mainloop()
        def kayit_ol():
            kullanici_ad = kullanici.get()
            kullanici_sifre = k_sifre.get()
            kullanici_sifre_onayla = sifre_dogrula.get()

            if kullanici_sifre == kullanici_sifre_onayla:
                try:
                    # Dosyayı okuma ve veri güncelleme
                    with open('data.txt', 'r+') as file:
                        data = file.read()
                        if data:
                            r = ast.literal_eval(data)  # Veriyi bir Python dict olarak çözümle
                        else:
                            r = {}  # Eğer dosya boşsa, boş bir dict oluştur
                        dict2 = {kullanici_ad: kullanici_sifre}
                        r.update(dict2)  # Yeni kullanıcıyı ekle
                        file.truncate(0)  # Dosyayı temizle
                        file.seek(0)  # Başlangıç noktasına git
                        file.write(str(r))  # Güncellenmiş veriyi dosyaya yaz

                    messagebox.showinfo("Kayıt Ol", "Kayıt Olundu")
                except FileNotFoundError:
                    # Eğer dosya yoksa, yeni bir dosya oluştur
                    with open('data.txt', 'w') as file:
                        r = {kullanici_ad: kullanici_sifre}
                        file.write(str(r))
                    messagebox.showinfo("Kayıt Ol", "Kayıt Olundu")
            else:
                messagebox.showerror('Hata', 'Her 2 şifre de aynı olmalı!')

        self.img = PhotoImage(file='Resimler/2.png')
        Label(self.window, image=self.img, border=0, bg="white").place(x=50, y=90)

        frame = Frame(self.window, width=350, height=350, bg="#fff")
        frame.place(x=480, y=50)

        kayit_ol_heading = Label(frame, text="Kayıt Ol", fg="#57a1f8", bg="white",
                                 font=("Microsoft Yahei UI Light", 23, "bold"))
        kayit_ol_heading.place(x=100, y=5)

        def on_enter(e):
            kullanici.delete(0, "end")

        def on_leave(e):
            name = kullanici.get()
            if name == '':
                kullanici.insert(0, "Kullanıcı adı:")

        kullanici = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
        kullanici.place(x=30, y=80)
        kullanici.insert(0, "Kullanıcı adı:")
        kullanici.bind('<FocusIn>', on_enter)
        kullanici.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

        def on_enter(e):
            k_sifre.delete(0, "end")

        def on_leave(e):
            sifre = k_sifre.get()
            if sifre == '':
                k_sifre.insert(0, "Şifre:")

        k_sifre = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
        k_sifre.place(x=30, y=150)
        k_sifre.insert(0, "Şifre")
        k_sifre.bind('<FocusIn>', on_enter)
        k_sifre.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

        def on_enter(e):
            sifre_dogrula.delete(0, "end")

        def on_leave(e):
            s_dogrula = sifre_dogrula.get()
            if s_dogrula == '':
                sifre_dogrula.insert(0, "Şifre doğrula:")

        sifre_dogrula = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
        sifre_dogrula.place(x=30, y=220)
        sifre_dogrula.insert(0, "Şifre Doğrula")
        sifre_dogrula.bind("<FocusIn>", on_enter)
        sifre_dogrula.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

        Button(frame, width=39, pady=7, text="Kayıt Ol", bg="#57a1f8", fg="white", border=0, command=kayit_ol).place(x=35,
                                                                                                                     y=270)
        label = Label(frame, text="Bir hesabın var mı?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
        label.place(x=90, y=320)

        giris_yap = Button(frame, width=6, text="Giriş yap", border=0, bg="white", cursor='hand2', fg="#57a1f8",command=giris_yap)
        giris_yap.place(x=200, y=320)