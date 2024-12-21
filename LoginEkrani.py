from tkinter import *
from tkinter import messagebox
import GUI  # FilmDiziArayuz sınıfı için
import KayitOlEkrani
import ast
class LoginEkrani:
    def __init__(self, root):
        self.root = root
        self.root.title("Giriş Ekranı")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="#0b105e")
        self.root.resizable(False, False)

        def kayit_ol_buton():
            self.root.destroy()
            kayit_pencere = Tk()
            KayitOlEkrani.KayitOlEkrani(kayit_pencere)
            kayit_pencere.mainloop()
        def giris_yap():
            kullanici_ad = kullanici.get()
            kullanici_sifre = sifre.get()

            try:
                # Kullanıcı bilgilerini data.txt dosyasından kontrol et
                with open("data.txt", "r") as file:
                    data = file.read()
                    r = ast.literal_eval(data)  # Data dosyasını dict'e dönüştür

                if kullanici_ad in r and r[kullanici_ad] == kullanici_sifre:
                    messagebox.showinfo("Başarılı", "Giriş Başarılı!")
                    self.root.destroy()  # Giriş ekranını kapat
                    ana_pencere = Tk()  # Yeni pencere aç
                    GUI.FilmDiziArayuz(ana_pencere)  # GUI ekranını başlat
                    ana_pencere.mainloop()
                else:
                    messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

            except FileNotFoundError:
                messagebox.showerror("Hata", "Kullanıcı bilgileri bulunamadı!")
            except Exception as e:
                messagebox.showerror("Hata", f"Beklenmeyen bir hata oluştu: {e}")

        self.img = PhotoImage(file="Resimler/1.png")
        Label(self.root, image=self.img, bg="#0b105e").place(x=40, y=50)

        frame = Frame(self.root, width=350, height=350, bg="#161f99")
        frame.place(x=480, y=70)

        hg_label = Label(frame, text="Hoşgeldiniz", fg="white", bg="#161f99",
                         font=("Microsoft YaHei UI Light", 23, "bold"))
        hg_label.place(x=100, y=5)

        def on_enter(e):
            kullanici.delete(0, "end")

        def on_leave(e):
            name = kullanici.get()
            if name == '':
                kullanici.insert(0, "Kullanıcı adı:")

        kullanici = Entry(frame, width=25, fg="white", border=0, bg="#161f99", font=("Microsot YaHei UI Light", 11))
        kullanici.place(x=30, y=80)
        kullanici.insert(0, "Kullanıcı adı:")
        kullanici.bind('<FocusIn>', on_enter)
        kullanici.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

        def on_enter(e):
            sifre.delete(0, "end")

        def on_leave(e):
            name = sifre.get()
            if name == '':
                sifre.insert(0, "Şifre:")

        sifre = Entry(frame, width=25, fg="white", border=0, bg="#161f99", font=("Microsot YaHei UI Light", 11))
        sifre.place(x=30, y=150)
        sifre.insert(0, "Şifre:")
        sifre.bind('<FocusIn>', on_enter)
        sifre.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

        Button(frame, width=39, pady=7, text="Giriş Yap", bg="#f23031", fg="white", border=0, command=giris_yap).place(
            x=35, y=200)

        label = Label(frame, text="Hesabın yok mu?", fg="white", bg="#161f99", font=("Arial", 9))
        label.place(x=85, y=270)

        kayit_ol = Button(frame, width=6, text="Kayıt Ol", border=0, fg="white", bg="#f23031", cursor="hand2",command=kayit_ol_buton)
        kayit_ol.place(x=215, y=270)