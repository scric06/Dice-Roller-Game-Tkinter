import random
from tkinter import *
from PIL import ImageTk, Image
import time

saldo = int(input("enter your balance: "))

tk = Tk()
tk.geometry("428x300")
tk.title("Roller Dice Game!")

dado_1_img = ImageTk.PhotoImage(Image.open("enter the path of the images"))
dado_2_img = ImageTk.PhotoImage(Image.open("enter the path of the images"))
dado_3_img = ImageTk.PhotoImage(Image.open("enter the path of the images"))
dado_4_img = ImageTk.PhotoImage(Image.open("enter the path of the images"))
dado_5_img = ImageTk.PhotoImage(Image.open("enter the path of the images"))
dado_6_img = ImageTk.PhotoImage(Image.open("enter the path of the images"))

dadi_immagini = [dado_1_img,dado_2_img,dado_3_img,dado_4_img,dado_5_img,dado_6_img]

dadi_dati={
    dado_1_img: 1,
    dado_2_img: 2,
    dado_3_img: 3,
    dado_4_img: 4,
    dado_5_img: 5,
    dado_6_img: 6}

label1 = Label(tk, image = dadi_immagini[0], text="SPIN!")
label1.grid(row=0,column=2, columnspan=1)
label2 = Label(tk, image = dadi_immagini[0], text="SPIN!")
label2.grid(row=0,column=3, columnspan=1)

def spin():
    global label1, saldo
    

    if int(entryPuntata.get()) <= saldo:
        if int(entryNumero.get()) >= 2 and int(entryNumero.get()) <= 12:
            for i in range(25):
                randomDado1 = random.choice(dadi_immagini)
                randomDado2 = random.choice(dadi_immagini)
                label1.configure(image=randomDado1)
                label1.grid(row=0,column=2, columnspan=1)
                label2.configure(image=randomDado2)
                label2.grid(row=0,column=3, columnspan=1)
                tk.update()
                time.sleep(0.05)

            if int(entryNumero.get()) == (dadi_dati[randomDado1] + dadi_dati[randomDado2]):
                saldo += int(entryPuntata.get())*2
                print("YOU WON!")
                print(saldo)
            else:
                saldo -= int(entryPuntata.get())
                print(saldo)
        else:
            numeroNonValido()
    else:
        saldoInsufficiente()
    
def saldoInsufficiente():
    saldoInsufficiente = Label(tk, text = 'insufficient balance', font=('calibre',10, 'bold'))
    saldoInsufficiente.grid(row=3, column=3)
    tk.update()
    time.sleep(1)
    saldoInsufficiente.destroy()

def numeroNonValido():
    NumeroNonValido = Label(tk, text = 'invalid number', font=('calibre',10, 'bold'))
    NumeroNonValido.grid(row=2, column=3)
    tk.update()
    time.sleep(1)
    NumeroNonValido.destroy()

indicazioniNumero = Label(tk, text = 'number', font=('calibre',10, 'bold'))
indicazioniNumero.grid(row=2, column=0, columnspan=3)
entryNumero = Entry(tk)
entryNumero.grid(row=2, column=1, columnspan=3)

indicazioniPuntata = Label(tk, text = 'bet', font=('calibre',10, 'bold'))
indicazioniPuntata.grid(row=3, column=0, columnspan=3)
entryPuntata = Entry(tk)
entryPuntata.grid(row=3, column=1, columnspan=3)

buttonSpin = Button(text="SPIN!", command=spin)
buttonSpin.grid(row=4, column=1, columnspan=3)

tk.mainloop()

