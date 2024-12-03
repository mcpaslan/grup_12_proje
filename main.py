import tkinter
import GUI  # GUI.py'deki FilmDiziArayuz sınıfını import ediyoruz

if __name__ == "__main__":
    window = tkinter.Tk()  # Ana pencereyi oluştur
    app = GUI.FilmDiziArayuz(window)  # GUI.py'deki sınıfı başlat
    window.mainloop()  # Pencereyi sürekli çalıştır
