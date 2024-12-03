import tkinter
from tkinter import ttk

# Ana pencere
window = tkinter.Tk()
window.title("FILM/DIZI UYGULAMASI")
window.minsize(700, 600)

# Ana çerçeve
frame = tkinter.Frame(window)
frame.pack(fill="both") #fill="both" Widget, hem yatay hem de dikey yönde genişler.

# Film/Dizi Değerlendirme Çerçevesi
secenek_giris_frame = tkinter.LabelFrame(frame, text="Film/Dizi Değerlendirme ve Durum Alanı")
secenek_giris_frame.grid(row=0, column=0, padx=10, pady=10,sticky="w")

# Film/Dizi Adı Girişi
film_dizi_ad_label = tkinter.Label(secenek_giris_frame, text="Film/Dizi Adı Gir", anchor="w")
film_dizi_ad_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

film_dizi_ad_entry = tkinter.Entry(secenek_giris_frame, width=30)
film_dizi_ad_entry.grid(row=0, column=1, padx=5, pady=5)

# Film/Dizi Türü Seçimi
film_dizi_tur_label = tkinter.Label(secenek_giris_frame, text="Film/Dizi Türü Seç", anchor="w")
film_dizi_tur_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

n1 = tkinter.StringVar()
tur_sec = ttk.Combobox(secenek_giris_frame, width=15, textvariable=n1)
tur_sec['values'] = ('Film', 'Dizi')
tur_sec.grid(row=1, column=1, padx=5, pady=5)

# Durum Seçimi
durum_label = tkinter.Label(secenek_giris_frame, text="Durum", anchor="w")
durum_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

n2 = tkinter.StringVar()
durum_sec = ttk.Combobox(secenek_giris_frame, width=15, textvariable=n2)
durum_sec['values'] = ('İzlendi', 'İzlenecek', 'Bekleniyor')
durum_sec.grid(row=2, column=1, padx=5, pady=5)

# Puanlama
yildiz_label = tkinter.Label(secenek_giris_frame, text="Yıldız", anchor="w")
yildiz_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

yildiz_list = ["1", "2", "3", "4", "5"]
yildiz_var = tkinter.StringVar()
yildiz_sec = tkinter.OptionMenu(secenek_giris_frame, yildiz_var, *yildiz_list)
yildiz_sec.grid(row=3, column=1, padx=5, pady=5)

# Not ekleme kısmı
notlar_label = tkinter.Label(secenek_giris_frame, text="Notlar", anchor="w")
notlar_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")  # Sol tarafa yaslanır

notlar_textbox = tkinter.Text(secenek_giris_frame, width=25, height=10)
notlar_textbox.grid(row=4, column=1, padx=5, pady=5)

# Bilgileri Kaydet Butonu
bilgi_ekle_buton = tkinter.Button(secenek_giris_frame, text="EKLE", bg="green", fg="white")
bilgi_ekle_buton.grid(row=5, column=0, columnspan=2, pady=10)

# Filmler Listesi Çerçevesi
film_list_frame = tkinter.LabelFrame(frame, text="Filmler Listesi")
film_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="NE")

# Filmler için listbox
film_listbox = tkinter.Listbox(film_list_frame, height=10, width=30)
film_listbox.grid(row=0, column=0, padx=10, pady=10)

# Diziler Listesi Çerçevesi
dizi_list_frame = tkinter.LabelFrame(frame, text="Diziler Listesi")
dizi_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="SE")

# Diziler için listbox
dizi_listbox = tkinter.Listbox(dizi_list_frame, height=10, width=30)
dizi_listbox.grid(row=0, column=0, padx=10, pady=10)


window.mainloop()
