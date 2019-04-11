#Made by Eliott Gandiolle / 20/05/2018

from tkinter import *
import tkinter.font as tfont

fenetre = Tk()
fenetre.geometry("500x505+500+70")
fenetre.resizable(width=False, height=False)

coin = 0
amelioration = 1
amlutin = 2
prix_lut = 100
prix_am = 10
mangerX = 0
qlutin = 2
prix_mou = 2000
ammouche = 20
mouche = 0
Oammouche = 20

################################# Cookie Cliquer ##################################

def Manger():
    
    global coin, amelioration

    coin += amelioration
    NPiece.set(str(coin)+"$")

def MangerPlus():

    global amelioration, prix_am, coin

    if coin >= prix_am :
      
      coin = coin - prix_am
      NPiece.set(str(coin)+"$")
      amelioration += 1
      prix_am += amelioration**2
      PAmeliorerr.set(str(prix_am)+"$ (+"+str(amelioration)+"/clic)")

def Lutin() :

    global coin, amlutin, prix_lut, mangerX, qlutin

    if mangerX == 0 and coin >= prix_lut :

        MangerAuto()
        coin = coin - prix_lut
        NPiece.set(str(coin)+"$")
        prix_lut = prix_lut * qlutin
        mangerX = 1
        amlutin += 3 * qlutin
        PLutin.set(str(prix_lut)+"$ (+"+str(amlutin)+"/auto)")
        qlutin += 1

    elif mangerX != 0 and coin >= prix_lut :

        coin = coin - prix_lut
        NPiece.set(str(coin)+"$")
        prix_lut = prix_lut * qlutin
        amlutin += 2 * qlutin
        PLutin.set(str(prix_lut)+"$ (+"+str(amlutin)+"/auto)")
        qlutin += 1

def Mouche():

    global coin, ammouche, prix_mou, mouche, Oammouche

    if coin >= prix_mou :

        coin = coin - prix_mou
        NPiece.set(str(coin)+"$")
        prix_mou += prix_mou
        Oammouche = ammouche
        ammouche = round(1.4 * ammouche)
        PMouche.set(str(prix_mou)+"$ (+"+str(ammouche)+"/auto)")
        mouche = 1
        
def MangerAuto() :

    global amlutin, ammouche, coin, mouche, Oammouche
    fenetre.after(200,MangerAuto)  

    if mouche == 0 :
      coin += amlutin - (2* qlutin)

    else :
      coin += amlutin - (2* qlutin) + ammouche -  round(1.4 * Oammouche)

    NPiece.set(str(coin)+"$")
    
IFondcookie = PhotoImage(file = "fondcookie.gif")
Fondcookie = Canvas(fenetre, width = 500, height = 500)
Fondcookie.create_image(200, 200, image = IFondcookie)
Fondcookie.pack()

ICookie = PhotoImage(file = "cookie.gif")
BCookie = Button(fenetre, image = ICookie, command = Manger)
BCookie = Fondcookie.create_window(250, 218, window = BCookie)

TRegle = tfont.Font(family = "Calibri", size = 27, weight ="bold")
LRegle = Label(fenetre, text = "CLIQUE SUR LE COOKIE", bg = "white", font = TRegle)
LRegle = Fondcookie.create_window(250,26, window = LRegle)

TCoin = tfont.Font(family = "Calibri", size = 40, weight ="bold")
NPiece = StringVar()
NPiece.set(str(coin)+"$")
LCoin = Label(fenetre, textvar = NPiece , bg = "white", font = TCoin)
LCoin = Fondcookie.create_window(430,440, window = LCoin)

TAmeliorer = tfont.Font(family = "Calibri", size = 11, weight ="bold")
BAmeliorer = Button(fenetre, text = "Pioche a cookie plus grosse", font = TAmeliorer, cursor = "hand1", command = MangerPlus, bg= "white")
BAmeliorer = Fondcookie.create_window(100,411, window = BAmeliorer)

PAmeliorer =tfont.Font(family = "Calibri", size = 16, weight ="bold")
PAmeliorerr = StringVar()
PAmeliorerr.set(str(prix_am)+"$ (+"+str(amelioration)+"/clic)")
LAmeliorer = Label(fenetre, textvar = PAmeliorerr, font = PAmeliorer, bg = "white")
LAmeliorer = Fondcookie.create_window(265,413, window = LAmeliorer)

BLutin = Button(fenetre, text = "Ce lutin sauras te servir", font = TAmeliorer, cursor = "hand1",command = Lutin, bg = "white", padx = 14)
BLutin = Fondcookie.create_window(100,447, window = BLutin)

PLutin = StringVar()
PLutin.set(str(prix_lut)+"$ (+"+str(amlutin)+"/auto)")
LLutin = Label(fenetre, textvar = PLutin, font = PAmeliorer, bg = "white")
LLutin = Fondcookie.create_window(275,448, window = LLutin)

BMouche = Button(fenetre, text = "Cette mouche a très faim", font = TAmeliorer, cursor = "hand1",command = Mouche, bg = "white", padx = 8)
BMouche = Fondcookie.create_window(100,484, window = BMouche)

PMouche = StringVar()
PMouche.set(str(prix_mou)+"$ (+"+str(ammouche)+"/auto)")
LMouche = Label(fenetre, textvar = PMouche, font = PAmeliorer, bg = "white")
LMouche = Fondcookie.create_window(275,483, window = LMouche)

fenetre.mainloop()

