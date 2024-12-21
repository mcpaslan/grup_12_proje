import tkinter
from tkinter import ttk
from function import Function
class FilmDiziArayuz:

    def __init__(self,window):
        # Ana pencere
        self.window = window
        self.window.title("FILM/DIZI UYGULAMASI")
        self.window.minsize(700, 600)
        self.gui_elemanlarini_olustur()
    def gui_elemanlarini_olustur(self):
        # Ana çerçeve
        self.frame = tkinter.Frame(self.window)
        self.frame.pack(fill="both") #fill="both" Widget, hem yatay hem de dikey yönde genişler.

        # Film/Dizi Değerlendirme Çerçevesi
        self.secenek_giris_frame = tkinter.LabelFrame(self.frame, text="Film/Dizi Değerlendirme ve Durum Alanı")
        self.secenek_giris_frame.grid(row=0, column=0, padx=10, pady=10,sticky="w")

        # Film/Dizi Adı Girişi
        self.film_dizi_ad_label = tkinter.Label(self.secenek_giris_frame, text="Film/Dizi Adı Gir", anchor="w")
        self.film_dizi_ad_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.film_dizi_ad_entry = tkinter.Entry(self.secenek_giris_frame, width=30)
        self.film_dizi_ad_entry.grid(row=0, column=1, padx=5, pady=5)

        # Film/Dizi Türü Seçimi
        self.film_dizi_tur_label = tkinter.Label(self.secenek_giris_frame, text="Film/Dizi Türü Seç", anchor="w")
        self.film_dizi_tur_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.n1 = tkinter.StringVar()
        self.tur_sec = ttk.Combobox(self.secenek_giris_frame, width=15, textvariable=self.n1)
        self.tur_sec['values'] = ('Film', 'Dizi')
        self.tur_sec.grid(row=1, column=1, padx=5, pady=5)

        # Durum Seçimi
        self.durum_label = tkinter.Label(self.secenek_giris_frame, text="Durum", anchor="w")
        self.durum_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.n2 = tkinter.StringVar()
        self.durum_sec = ttk.Combobox(self.secenek_giris_frame, width=15, textvariable=self.n2)
        self.durum_sec['values'] = ('İzlendi', 'İzlenecek', 'Bekleniyor')
        self.durum_sec.grid(row=2, column=1, padx=5, pady=5)

        # Puanlama
        self.yildiz_label = tkinter.Label(self.secenek_giris_frame, text="Yıldız", anchor="w")
        self.yildiz_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.yildiz_list = ["1", "2", "3", "4", "5"]
        self.yildiz_var = tkinter.StringVar()
        self.yildiz_sec = tkinter.OptionMenu(self.secenek_giris_frame, self.yildiz_var, *self.yildiz_list)
        self.yildiz_sec.grid(row=3, column=1, padx=5, pady=5)

        # Not ekleme kısmı
        self.notlar_label = tkinter.Label(self.secenek_giris_frame, text="Notlar", anchor="w")
        self.notlar_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.notlar_textbox = tkinter.Text(self.secenek_giris_frame, width=25, height=10)
        self.notlar_textbox.grid(row=4, column=1, padx=5, pady=5)

        # Filmler Listesi Çerçevesi
        self.film_list_frame = tkinter.LabelFrame(self.frame, text="Filmler Listesi")
        self.film_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="NE")

        # Filmler için listbox
        self.film_listbox = tkinter.Listbox(self.film_list_frame, height=10, width=30)
        self.film_listbox.grid(row=0, column=0, padx=10, pady=10)

        # Diziler Listesi Çerçevesi
        self.dizi_list_frame = tkinter.LabelFrame(self.frame, text="Diziler Listesi")
        self.dizi_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="SE")

        # Diziler için listbox
        self.dizi_listbox = tkinter.Listbox(self.dizi_list_frame, height=10, width=30)
        self.dizi_listbox.grid(row=0, column=0, padx=10, pady=10)

        # Düzenleme/Silme Çerçevesi
        self.duzen_sil_frame = tkinter.LabelFrame(self.frame, text="Düzenleme/Silme Alanı")
        self.duzen_sil_frame.grid(row=2, column=0, padx=10, pady=10, sticky="SW")

        self.film_dizi_sec = tkinter.Label(self.duzen_sil_frame, text="Film/Dizi Seç", anchor="w")
        self.film_dizi_sec.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.n3 = tkinter.StringVar()
        self.eklenen_sec = ttk.Combobox(self.duzen_sil_frame, width=15, textvariable=self.n3)
        self.eklenen_sec.grid(row=2, column=1, padx=5, pady=5)
        #instance oluşturma
        self.function_nesne = Function(
            self.film_dizi_ad_entry,
            self.tur_sec,
            self.durum_sec,
            self.yildiz_var,
            self.notlar_textbox,
            self.film_listbox,
            self.dizi_listbox,
            self.eklenen_sec
        )
        # Bilgileri Ekle Butonu
        self.bilgi_ekle_buton = tkinter.Button(self.secenek_giris_frame, text="EKLE", bg="green", fg="white",command=self.function_nesne.ekle)
        self.bilgi_ekle_buton.grid(row=5, column=0, columnspan=2, pady=10)

        self.duzenle_buton = tkinter.Button(self.duzen_sil_frame, text="DÜZENLE", bg="blue", fg="white",command=self.function_nesne.duzenle)
        self.duzenle_buton.grid(row=3, column=0, padx=5, pady=5)

        self.sil_buton = tkinter.Button(self.duzen_sil_frame, text="SİL", bg="red", fg="white",command=self.function_nesne.sil)
        self.sil_buton.grid(row=3, column=1, padx=5, pady=5)

        self.bilgi_kaydet = tkinter.Button(self.duzen_sil_frame, text="Değişiklikleri kaydet", bg="green", fg="white",command=self.function_nesne.kaydet)
        self.bilgi_kaydet.grid(row=4, column=1, sticky="S")