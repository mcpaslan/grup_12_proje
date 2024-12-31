import tkinter
from tkinter import ttk
from function import Function
import main

class FilmDiziArayuz:

    def __init__(self, window):

        self.window = window
        self.window.configure(bg="#34495E")
        self.window.title("FILM/DIZI UYGULAMASI")
        self.window.resizable(False, False)
        self.window.minsize(700, 600)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TCombobox", fieldbackground="#BDC3C7", background="#BDC3C7", foreground="black")  # Soft gri combobox

        self.gui_elemanlarini_olustur()

    def gui_elemanlarini_olustur(self):
        # Ana çerçeve
        self.frame = tkinter.Frame(self.window, bg="#34495E")
        self.frame.pack(fill="both", expand=True)

        # Film/Dizi Değerlendirme Çerçevesi
        self.secenek_giris_frame = tkinter.LabelFrame(self.frame, bg="#2980B9", fg="white", text="Film/Dizi Değerlendirme ve Durum Alanı", font=("Arial", 12, "bold"))
        self.secenek_giris_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Film/Dizi Adı Girişi
        self.film_dizi_ad_label = tkinter.Label(self.secenek_giris_frame, bg="#2980B9", fg="white", text="Film/Dizi Adı Gir", anchor="w", font=("Arial", 11))
        self.film_dizi_ad_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.film_dizi_ad_entry = tkinter.Entry(self.secenek_giris_frame, width=30, bg="#BDC3C7", fg="black", relief="flat", font=("Arial", 11), bd=2)
        self.film_dizi_ad_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Film/Dizi Türü Seçimi
        self.film_dizi_tur_label = tkinter.Label(self.secenek_giris_frame, bg="#2980B9", fg="white", text="Film/Dizi Türü Seç", anchor="w", font=("Arial", 11))
        self.film_dizi_tur_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.n1 = tkinter.StringVar()
        self.tur_sec = ttk.Combobox(self.secenek_giris_frame, width=15, textvariable=self.n1, font=("Arial", 11), state="readonly")
        self.tur_sec['values'] = ('Film', 'Dizi')
        self.tur_sec.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Durum Seçimi
        self.durum_label = tkinter.Label(self.secenek_giris_frame, bg="#2980B9", fg="white", text="Durum", anchor="w", font=("Arial", 11))
        self.durum_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.n2 = tkinter.StringVar()
        self.durum_sec = ttk.Combobox(self.secenek_giris_frame, width=15, textvariable=self.n2, font=("Arial", 11), state="readonly")
        self.durum_sec['values'] = ('İzlendi', 'İzlenecek', 'Bekleniyor')
        self.durum_sec.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Puanlama
        self.yildiz_label = tkinter.Label(self.secenek_giris_frame, bg="#2980B9", fg="white", text="Yıldız", anchor="w", font=("Arial", 11))
        self.yildiz_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.yildiz_list = ["1", "2", "3", "4", "5"]
        self.yildiz_var = tkinter.StringVar()
        self.yildiz_sec = tkinter.OptionMenu(self.secenek_giris_frame, self.yildiz_var, *self.yildiz_list)

        # OptionMenu renk ayarları
        self.yildiz_sec.config(bg="#2980B9", fg="white", font=("Arial", 10, "bold"), width=5)
        self.yildiz_sec.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Not ekleme kısmı
        self.notlar_label = tkinter.Label(self.secenek_giris_frame, bg="#2980B9", fg="white", text="Notlar", anchor="w", font=("Arial", 11))
        self.notlar_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.notlar_textbox = tkinter.Text(self.secenek_giris_frame, width=25, height=10, bg="#BDC3C7", fg="black", font=("Arial", 11), relief="flat", bd=2)
        self.notlar_textbox.grid(row=4, column=1, padx=5, pady=5)

        # Filmler Listesi Çerçevesi
        self.film_list_frame = tkinter.LabelFrame(self.frame, bg="#2980B9", fg="white", text="Filmler Listesi", font=("Arial", 12, "bold"))
        self.film_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="NE")

        # Filmler için listbox (soft gri)
        self.film_listbox = tkinter.Listbox(self.film_list_frame, height=10, width=30, background="#BDC3C7", fg="black", font=("Arial", 10, "bold"))
        self.film_listbox.grid(row=0, column=0, padx=10, pady=10)

        # Diziler Listesi Çerçevesi
        self.dizi_list_frame = tkinter.LabelFrame(self.frame, bg="#2980B9", fg="white", text="Diziler Listesi", font=("Arial", 12, "bold"))
        self.dizi_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="SE")

        # Diziler için listbox (soft gri)
        self.dizi_listbox = tkinter.Listbox(self.dizi_list_frame, height=10, width=30, background="#BDC3C7", fg="black", font=("Arial", 10, "bold"))
        self.dizi_listbox.grid(row=0, column=0, padx=10, pady=10)

        # Düzenleme/Silme Çerçevesi
        self.duzen_sil_frame = tkinter.LabelFrame(self.frame, bg="#2980B9", fg="white", text="Düzenleme/Silme Alanı", font=("Arial", 12, "bold"))
        self.duzen_sil_frame.grid(row=2, column=0, padx=10, pady=10, sticky="SW")

        self.film_dizi_sec = tkinter.Label(self.duzen_sil_frame, bg="#2980B9", fg="white", text="Film/Dizi Seç", anchor="w", font=("Arial", 11))
        self.film_dizi_sec.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.n3 = tkinter.StringVar()
        self.eklenen_sec = ttk.Combobox(self.duzen_sil_frame, width=15, textvariable=self.n3, font=("Arial", 11), state="readonly")
        self.eklenen_sec.grid(row=2, column=1, padx=5, pady=5)

        # Instance oluşturma
        self.function_nesne = Function(
            self.film_dizi_ad_entry,
            self.tur_sec,
            self.durum_sec,
            self.yildiz_var,
            self.notlar_textbox,
            self.film_listbox,
            self.dizi_listbox,
            self.eklenen_sec,
            main.ad
        )

        # Bilgileri Ekle Butonu (turuncu buton)
        self.bilgi_ekle_buton = tkinter.Button(self.secenek_giris_frame, text="EKLE", width=25, bg="#E67E22", fg="white", command=self.function_nesne.ekle)
        self.bilgi_ekle_buton.grid(row=5, column=1, columnspan=2, pady=5)

        # Düzenle ve Sil Butonları
        self.duzenle_buton = tkinter.Button(self.duzen_sil_frame, text="DÜZENLE", width=15, bg="#F39C12", fg="white", command=self.function_nesne.duzenle)
        self.duzenle_buton.grid(row=3, column=0, padx=5, pady=5)

        self.sil_buton = tkinter.Button(self.duzen_sil_frame, text="SİL", bg="#E74C3C", fg="white", width=15, border=2, command=self.function_nesne.sil)
        self.sil_buton.grid(row=3, column=1, padx=5, pady=5)

        self.bilgi_kaydet = tkinter.Button(self.duzen_sil_frame, text="Değişiklikleri kaydet", bg="#27AE60", fg="white", command=self.function_nesne.kaydet)
        self.bilgi_kaydet.grid(row=4, column=1, sticky="S")
