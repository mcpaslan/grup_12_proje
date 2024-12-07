import json
class VeriYonetimi:
    def __init__(self, dosya_adi="veriler.json"):
        self.dosya_adi = dosya_adi
    def veri_kaydet(self, film_dizi_listesi):
        try:
            with open(self.dosya_adi, "w", encoding="utf-8") as dosya:
                json.dump(film_dizi_listesi, dosya, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Veri kaydedilirken bir hata oluştu: {e}")
    def veri_yukle(self):
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
                return json.load(dosya)
        except FileNotFoundError:
            return []  # Dosya yoksa boş bir liste döndür
        except Exception as e:
            print(f"Veri yüklenirken bir hata oluştu: {e}")
            return []



































