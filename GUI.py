import tkinter
from tkinter import ttk
from function import Function
class FilmDiziArayuz:

    def __init__(self,window):
        # Ana pencere
        self.window = window
        self.window.configure(bg="#0b105e")
        self.window.title("FILM/DIZI UYGULAMASI")
        self.window.resizable(False, False)
        self.window.minsize(700, 600)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TCombobox", fieldbackground="#0b105e", background="#0b105e", foreground="white")

        self.gui_elemanlarini_olustur()
    def gui_elemanlarini_olustur(self):
        # Ana çerçeve
        self.frame = tkinter.Frame(self.window,bg="#0b105e")
        self.frame.pack(fill="both") #fill="both" Widget, hem yatay hem de dikey yönde genişler.

        # Film/Dizi Değerlendirme Çerçevesi
        self.secenek_giris_frame = tkinter.LabelFrame(self.frame,bg="#0b105e",fg="white", text="Film/Dizi Değerlendirme ve Durum Alanı", font=("Arial", 12))
        self.secenek_giris_frame.grid(row=0, column=0, padx=10, pady=10,sticky="w")

        # Film/Dizi Adı Girişi
        self.film_dizi_ad_label = tkinter.Label(self.secenek_giris_frame,bg="#0b105e",fg="white", text="Film/Dizi Adı Gir", anchor="w", font=("Microsot YaHei UI Light", 11))
        self.film_dizi_ad_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.film_dizi_ad_entry = tkinter.Entry(self.secenek_giris_frame, width=30,bg="#0b105e",fg="white")
        self.film_dizi_ad_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Film/Dizi Türü Seçimi
        self.film_dizi_tur_label = tkinter.Label(self.secenek_giris_frame,bg="#0b105e",fg="white", text="Film/Dizi Türü Seç", anchor="w", font=("Microsot YaHei UI Light", 11))
        self.film_dizi_tur_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.n1 = tkinter.StringVar()
        self.tur_sec = ttk.Combobox(self.secenek_giris_frame, width=15, textvariable=self.n1)
        self.tur_sec['values'] = ('Film', 'Dizi')
        self.tur_sec.grid(row=1, column=1, padx=5, pady=5,sticky="w")

        # Durum Seçimi
        self.durum_label = tkinter.Label(self.secenek_giris_frame,bg="#0b105e",fg="white", text="Durum", anchor="w", font=("Microsot YaHei UI Light", 11))
        self.durum_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.n2 = tkinter.StringVar()
        self.durum_sec = ttk.Combobox(self.secenek_giris_frame ,width=15, textvariable=self.n2)
        self.durum_sec['values'] = ('İzlendi', 'İzlenecek', 'Bekleniyor')
        self.durum_sec.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Puanlama
        self.yildiz_label = tkinter.Label(self.secenek_giris_frame, bg="#0b105e", fg="white", text="Yıldız", anchor="w",
                                          font=("Microsot YaHei UI Light", 11))
        self.yildiz_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.yildiz_list = ["1", "2", "3", "4", "5"]
        self.yildiz_var = tkinter.StringVar()
        self.yildiz_sec = tkinter.OptionMenu(self.secenek_giris_frame, self.yildiz_var, *self.yildiz_list)

        # OptionMenu renk ayarları
        self.yildiz_sec.config(bg="#0b105e", fg="white", font=("Arial", 10, "bold"), width=5)
        self.yildiz_sec.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Dropdown menü (açılır liste) için renk ayarları
        self.window.option_add('*TMenu*Background', '#0b105e')  # Açılır liste arka plan rengi
        self.window.option_add('*TMenu*Foreground', 'white')  # Açılır liste yazı rengi
        self.window.option_add('*TMenu*Font', ('Arial', 10, 'bold'))  # Açılır liste yazı tipi


        # Not ekleme kısmı
        self.notlar_label = tkinter.Label(self.secenek_giris_frame,bg="#0b105e",fg="white", text="Notlar", anchor="w", font=("Microsot YaHei UI Light", 11))
        self.notlar_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

        self.notlar_textbox = tkinter.Text(self.secenek_giris_frame, width=25, height=10,bg="#0b105e",fg="white")
        self.notlar_textbox.grid(row=4, column=1, padx=5, pady=5)

        # Filmler Listesi Çerçevesi
        self.film_list_frame = tkinter.LabelFrame(self.frame,bg="#0b105e",fg="white", text="Filmler Listesi", font=("Arial", 12))
        self.film_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="NE")

        # Filmler için listbox
        self.film_listbox = tkinter.Listbox(self.film_list_frame, height=10, width=30,background="#0b105e",fg="white", font=("Arial", 10,"bold"))
        self.film_listbox.grid(row=0, column=0, padx=10, pady=10)

        # Diziler Listesi Çerçevesi
        self.dizi_list_frame = tkinter.LabelFrame(self.frame,bg="#0b105e",fg="white", text="Diziler Listesi", font=("Arial", 12))
        self.dizi_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="SE")

        # Diziler için listbox
        self.dizi_listbox = tkinter.Listbox(self.dizi_list_frame, height=10, width=30,background="#0b105e",fg="white", font=("Arial", 10,"bold"))
        self.dizi_listbox.grid(row=0, column=0, padx=10, pady=10)

        # Düzenleme/Silme Çerçevesi
        self.duzen_sil_frame = tkinter.LabelFrame(self.frame,bg="#0b105e",fg="white", text="Düzenleme/Silme Alanı", font=("Arial", 12))
        self.duzen_sil_frame.grid(row=2, column=0, padx=10, pady=10, sticky="SW")

        self.film_dizi_sec = tkinter.Label(self.duzen_sil_frame,bg="#0b105e",fg="white", text="Film/Dizi Seç", anchor="w", font=("Microsot YaHei UI Light", 11))
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
        self.bilgi_ekle_buton = tkinter.Button(self.secenek_giris_frame, text="EKLE",width=25, bg="green", fg="white",command=self.function_nesne.ekle)
        self.bilgi_ekle_buton.grid(row=5, column=1, columnspan=2, pady=5)

        self.duzenle_buton = tkinter.Button(self.duzen_sil_frame, text="DÜZENLE",width=15, bg="blue", fg="white",command=self.function_nesne.duzenle)
        self.duzenle_buton.grid(row=3, column=0, padx=5, pady=5)

        self.sil_buton = tkinter.Button(self.duzen_sil_frame, text="SİL", bg="#f23031", fg="white",width=15, border=2,command=self.function_nesne.sil)
        self.sil_buton.grid(row=3, column=1, padx=5, pady=5)

        self.bilgi_kaydet = tkinter.Button(self.duzen_sil_frame, text="Değişiklikleri kaydet", bg="green", fg="white",command=self.function_nesne.kaydet)
        self.bilgi_kaydet.grid(row=4, column=1, sticky="S")