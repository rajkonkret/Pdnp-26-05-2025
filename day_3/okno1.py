import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Kurs")

        self.label = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label.pack(side="left")

        tkinter.mainloop()


my_gui = MyGui()

print("To jest koniec programu")
# To jest koniec programu
# napisz funkcje wypisujaca tekst
def wypisz_tekst(tekst):
    print(tekst)