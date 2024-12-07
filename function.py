from veri_yonetimi import VeriYonetimi
from tkinter import messagebox
import json
class Function:
    def __init__(self, film_dizi_ad_entry, tur_sec, durum_sec, yildiz_var, notlar_textbox, film_listbox, dizi_listbox,film_dizi_sec):
        self.film_dizi_ad_entry = film_dizi_ad_entry
        self.tur_sec = tur_sec
        self.durum_sec = durum_sec
        self.yildiz_var = yildiz_var
        self.notlar_textbox = notlar_textbox
        self.film_listbox = film_listbox
        self.dizi_listbox = dizi_listbox
        self.film_dizi_sec = film_dizi_sec
        self.veri_yonetimi = VeriYonetimi()
        self.dosya_adi = "veriler.json"  # Dosya adı buradan kontrol ediliyor
        self.veri_yukle()

    def ekle(self):
        # Film/Dizi ekleme işlevi
        ad = self.film_dizi_ad_entry.get()
        tur = self.tur_sec.get()
        durum = self.durum_sec.get()
        yildiz = self.yildiz_var.get()
        if not ad or not tur or not durum or not yildiz:
            return #eksik bilgi varsa işlem yaptırmıyor.
        if tur == "Film":
            self.film_listbox.insert("end", f"{ad} - {durum} - {yildiz} Yıldız")
        elif tur == "Dizi":
            self.dizi_listbox.insert("end", f"{ad} - {durum} - {yildiz} Yıldız")

        # Değer ekleme işlemi
        mevcut_degerler = self.film_dizi_sec["values"]
        yeni_degerler = list(mevcut_degerler) + [ad]
        self.film_dizi_sec['values'] = yeni_degerler  # Güncellenmiş değeri tekrar ata

        # Alanları temizle
        self.film_dizi_ad_entry.delete(0, "end")
        self.tur_sec.set('')
        self.durum_sec.set('')
        self.yildiz_var.set('')
        self.notlar_textbox.delete("1.0", "end")

    def sil(self):
        secilen_deger = self.film_dizi_sec.get()  # ComboBox'tan seçilen değeri al
        if secilen_deger:
            # ComboBox'tan seçilen değeri sil
            mevcut_degerler = list(self.film_dizi_sec["values"])
            if secilen_deger in mevcut_degerler:
                mevcut_degerler.remove(secilen_deger)
                self.film_dizi_sec['values'] = mevcut_degerler  # Güncellenmiş değerleri tekrar ata
                self.film_dizi_sec.set("")
            # Film-dizi listbox'ında seçilen öğe varsa sil
            for i in range(self.film_listbox.size()):
                parts1=self.film_listbox.get(i).split("-")
                index = parts1[0].strip()
                if index == secilen_deger:
                    self.film_listbox.delete(i)
            for i in range(self.dizi_listbox.size()):
                parts2=self.dizi_listbox.get(i).split("-")
                index = parts2[0].strip()
                if index == secilen_deger:
                    self.dizi_listbox.delete(i)

    def duzenle(self):
        selected_value = self.film_dizi_sec.get()  # ComboBox'tan seçilen değeri al
        if selected_value:
            # Seçilen öğe için düzenleme işlemi
            ad = self.film_dizi_ad_entry.get()
            tur = self.tur_sec.get()
            durum = self.durum_sec.get()
            yildiz = self.yildiz_var.get()
            notlar = self.notlar_textbox.get("1.0", "end-1c")

            # Film listbox'ındaki öğeyi düzenleme
            for i in range(self.film_listbox.size()):
                parts1 = self.film_listbox.get(i).split(" - ")
                index1 = parts1[0].strip()
                if index1 == selected_value:
                    self.film_listbox.delete(i)  # Eski öğeyi sil
                    # Yeni öğeyi ekle
                    self.film_listbox.insert(i, f"{ad} - {durum} - {yildiz} Yıldız")
                    break  # Düzenleme işlemi tamamlandığında döngüyü bitir

            # Dizi listbox'ındaki öğeyi düzenleme
            for i in range(self.dizi_listbox.size()):
                parts2 = self.dizi_listbox.get(i).split(" - ")
                index2 = parts2[0].strip()
                if index2 == selected_value:
                    self.dizi_listbox.delete(i)  # Eski öğeyi sil
                    # Yeni öğeyi ekle
                    self.dizi_listbox.insert(i, f"{ad} - {durum} - {yildiz} Yıldız")
                    break  # Düzenleme işlemi tamamlandığında döngüyü bitir

            # ComboBox'taki değerleri güncelleme
            current_values = list(self.film_dizi_sec["values"])
            if selected_value in current_values:
                current_values.remove(selected_value)
                current_values.append(ad)  # Yeni adı listeye ekle
                self.film_dizi_sec['values'] = current_values  # Güncellenmiş değeri tekrar ata
                self.film_dizi_sec.set(ad)  # ComboBox'ı yeni ad ile güncelle

            # Alanları temizle (isteğe bağlı)
            self.film_dizi_ad_entry.delete(0, "end")
            self.tur_sec.set('')
            self.durum_sec.set('')
            self.yildiz_var.set('')
            self.notlar_textbox.delete("1.0", "end")
    def kaydet(self):
        film_listesi = [self.film_listbox.get(i) for i in range(self.film_listbox.size())]
        dizi_listesi = [self.dizi_listbox.get(i) for i in range(self.dizi_listbox.size())]
        veri = {"Filmler": film_listesi, "Diziler": dizi_listesi}
        self.veri_yonetimi.veri_kaydet(veri)

    def veri_yukle(self):
        veri = self.veri_yonetimi.veri_yukle()
        #filmler ve dizileri listboxlara ekle
        for film in veri.get("Filmler", []):
            self.film_listbox.insert("end", film)
        for dizi in veri.get("Diziler", []):
            self.dizi_listbox.insert("end", dizi)

        #filmler ve dizileri combobox'a ekle
        tum_veriler = [item.split(" - ")[0] for item in veri.get("Filmler", []) + veri.get("Diziler", [])]
        self.film_dizi_sec['values'] = tum_veriler