from veri_yonetimi import VeriYonetimi
from tkinter import messagebox
class Function:
    def __init__(self, film_dizi_ad_entry, tur_sec, durum_sec, yildiz_var, notlar_textbox, film_listbox, dizi_listbox,film_dizi_sec, kullanici_ad):
        self.film_dizi_ad_entry = film_dizi_ad_entry
        self.tur_sec = tur_sec
        self.durum_sec = durum_sec
        self.yildiz_var = yildiz_var
        self.notlar_textbox = notlar_textbox
        self.film_listbox = film_listbox
        self.dizi_listbox = dizi_listbox
        self.film_dizi_sec = film_dizi_sec
        self.kullanici_ad = kullanici_ad  # Set the username
        file = f"{self.kullanici_ad}.json"  # Use the user's specific file
        self.veri_yonetimi = VeriYonetimi(file)
        self.yaz()
    def yaz(self):
        for i, veri in enumerate(self.veri_yonetimi.veri_yukle()):
            if(veri["tur"]=="Film"):
                self.film_listbox.insert(i,f"{veri['ad']}-{veri['durum']}-{veri['yildiz']}\n")
            else:
                self.dizi_listbox.insert(i, f"{veri['ad']}-{veri['durum']}-{veri['yildiz']} \n")
            current_values = self.film_dizi_sec["values"]
            new_values = list(current_values) +[veri["ad"]]
            self.film_dizi_sec['values'] = new_values  # Güncellenmiş değeri tekrar ata
    def kaydet(self):
        # Film ve dizi verilerini al
        film_dizi_listesi = []

        for i in range(self.film_listbox.size()):
            film_info = self.film_listbox.get(i).split("-")
            film_dizi_listesi.append({
                'ad': film_info[0],
                'tur': "Film",
                'durum': film_info[1],
                'yildiz': film_info[2]
            })

        for i in range(self.dizi_listbox.size()):
            dizi_info = self.dizi_listbox.get(i).split("-")
            film_dizi_listesi.append({
                'ad': dizi_info[0],
                'tur': "Dizi",
                'durum': dizi_info[1],
                'yildiz': dizi_info[2]
            })

        # Verileri kaydet
        self.veri_yonetimi.film_dizi_listesi = film_dizi_listesi
        self.veri_yonetimi.veri_kaydet(self.veri_yonetimi.film_dizi_listesi)
        messagebox.showinfo("Sonuç:","Veriler kaydedildi.")

    def ekle(self):
        # Film/Dizi ekleme işlevi
        ad = self.film_dizi_ad_entry.get()
        tur = self.tur_sec.get()
        durum = self.durum_sec.get()
        yildiz = self.yildiz_var.get()
        if not ad or not tur or not durum or not yildiz:
            messagebox.showwarning("Sonuç","Tüm alanları doldur")
            return  # Eksik bilgi varsa işlem yapma

        if tur == "Film":
            self.film_listbox.insert("end", f"{ad}-{durum}-{yildiz} Yıldız")
            messagebox.showinfo("Sonuç:","Film eklendi")
        elif tur == "Dizi":
            self.dizi_listbox.insert("end", f"{ad}-{durum}-{yildiz} Yıldız")
            messagebox.showinfo("Sonuç:", "Dizi eklendi")

        # Değer ekleme işlemi
        current_values = self.film_dizi_sec["values"]
        new_values = list(current_values) + [ad]
        self.film_dizi_sec['values'] = new_values  # Güncellenmiş değeri tekrar ata

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
            mevcut_degerler.remove(secilen_deger)
            self.film_dizi_sec['values'] = mevcut_degerler  # Güncellenmiş değerleri tekrar ata
            self.film_dizi_sec.set("")
            # Film-dizi listbox'ında seçilen öğe varsa sil
            for i in range(self.film_listbox.size()):
                parts1 = self.film_listbox.get(i).split("-")
                index = parts1[0].strip()
                if index == secilen_deger:
                    self.film_listbox.delete(i)
                    messagebox.showinfo("Sonuç","Film silindi")
                    break
            for i in range(self.dizi_listbox.size()):
                parts2 = self.dizi_listbox.get(i).split("-")
                index = parts2[0].strip()
                if index == secilen_deger:
                    self.dizi_listbox.delete(i)
                    messagebox.showinfo("Sonuç", "Dizi silindi")
                    break
        else:
            messagebox.showwarning("Sonuç","Film/dizi kısmından bir değer seç")
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
                parts1 = self.film_listbox.get(i).split("-")
                index1 = parts1[0].strip()
                if index1 == selected_value:
                    self.film_listbox.delete(i)  # Eski öğeyi sil
                    # Yeni öğeyi ekle
                    self.film_listbox.insert(i, f"{ad}-{durum}-{yildiz} Yıldız")
                    messagebox.showinfo("Sonuç","Film düzenlendi")
                    break  # Düzenleme işlemi tamamlandığında döngüyü bitir

            # Dizi listbox'ındaki öğeyi düzenleme
            for i in range(self.dizi_listbox.size()):
                parts2 = self.dizi_listbox.get(i).split("-")
                index2 = parts2[0].strip()
                if index2 == selected_value:
                    self.dizi_listbox.delete(i)  # Eski öğeyi sil
                    # Yeni öğeyi ekle
                    self.dizi_listbox.insert(i, f"{ad}-{durum}-{yildiz} Yıldız")
                    messagebox.showinfo("Sonuç","Dizi düzenlendi")
                    break  # Düzenleme işlemi tamamlandığında döngüyü bitir
        else:
            messagebox.showwarning("Sonuç", "Fİlm/dizi kısmından bir değer seç")
            # ComboBox'taki değerleri güncelleme
            current_values = list(self.film_dizi_sec["values"])
            if selected_value in current_values:
                current_values.remove(selected_value)
                current_values.append("ad")  # Yeni adı listeye ekle
                self.film_dizi_sec['values'] = current_values  # Güncellenmiş değeri tekrar ata
                self.film_dizi_sec.set("ad")  # ComboBox'ı yeni ad ile güncelle

            # Alanları temizle (isteğe bağlı)
            self.film_dizi_ad_entry.delete(0, "end")
            self.tur_sec.set('')
            self.durum_sec.set('')
            self.yildiz_var.set('')
            self.notlar_textbox.delete("1.0", "end")