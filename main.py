from tkinter import Tk
import LoginEkrani

ad = ""
if __name__ == "__main__":
    ana_pencere = Tk()
    obj=LoginEkrani.LoginEkrani(ana_pencere)
    ana_pencere.mainloop()
def set_ad(isim):
    global ad
    ad=isim

