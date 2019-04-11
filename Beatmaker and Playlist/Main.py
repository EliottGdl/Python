# ISN Project 04/05/2018
# Gandiolle Eliott : Playlist and beatmaker
# Anthonin Vachez : Menu and beatmaker
# Jamey Antoine : Menu and beatmaker
from tkinter import *
import pygame
from tkinter.filedialog import *
from pygame import mixer
import random

def Fermeture():

    global AFenetre

    if AFenetre == 0 :

        mafenetre.destroy()
        quit()

    elif AFenetre == 1 :

      Beat.pack_forget()
      Accueil.pack()
      mafenetre.geometry("500x300+500+70")
      AFenetre = 0
    
    else :
        
      channel1.stop()
      Playlist.pack_forget()
      Accueil.pack()
      mafenetre.geometry("500x300+500+70")
      AFenetre = 0
      listbox.delete(0,END)

mafenetre =Tk()
mafenetre.title("BEATMAKER -Beta v2.0")
mafenetre.geometry("500x300+500+70")
mafenetre.resizable(width=False, height=False)
AFenetre = 0 #0 si c'est l'accueil, 1 si c'est le beat aléatoire, 2 si c'est la playlist


#---------------------------------------------------------------------------------------------------------------------------------------#



IAccueil = PhotoImage(file= "Assets/IAccueil.gif") #Photo par https://www.deviantart.com/art/Carmine-Rock-736895172
Accueil =Canvas(mafenetre, width = 600, height = 400)
Accueil.create_image(170,250, image = IAccueil)
Accueil.pack()

def beat () :
    
    global AFenetre
    
    Accueil.pack_forget()
    Beat.pack()
    mafenetre.geometry("600x400+500+70")
    AFenetre = 1

def playlist () :

    global AFenetre
    
    Accueil.pack_forget()
    Playlist.pack()
    mafenetre.geometry("170x250")
    AFenetre = 2
    

BEATMAKERLABEL = Label(mafenetre,text=' BEATMAKER ',fg='white',bg='black', font=('impact',38,'bold'))
BEATMAKERLABEL = Accueil.create_window(250, 95, window = BEATMAKERLABEL)

BBeat = Button(mafenetre,text=" Beat Aléatoire ",fg='black',bg='steelblue1', font=("impact",17),activebackground='steelblue4',activeforeground='black',command= beat)
BBeat.config(cursor="hand2")
BBeat = Accueil.create_window(140, 200, window = BBeat)

BPlaylist = Button(mafenetre,text=" Propre Playlist ",fg='black',bg='steelblue1', font=("impact",17),activebackground='steelblue4',activeforeground='black',command= playlist)
BPlaylist.config(cursor="hand2")
BPlaylist = Accueil.create_window(360, 200, window = BPlaylist)


#################################################################################################################################

x1 = 0

def choix_instru ():

    global Hat
    global Snare
    global Kick
    global Clap
    global Note

    mafenetre.after(50, choix_instru)
    
    if va1.get() == "1" :

        Kick = "Assets/Kick1.wav"

    elif va1.get() == "2" :
        
        Kick = "Assets/Kick2.wav"

    elif va1.get() == "3" :
        
        Kick = "Assets/Kick3.wav"

    elif va1.get() == "4" :

        Kick = "Assets/Kick4.wav"

    else :

        Kick = 0
        
    if va2.get() == "1" :

        Clap = "Assets/Clap1.wav"
        
    elif va2.get() == "2" :

        Clap = "Assets/Clap2.wav"

    elif va2.get() == "3" :

        Clap = "Assets/Clap3.wav"

    elif va2.get() == "4" :

        Clap = "Assets/Clap4.wav"

    else :

        Clap = 0

    if va3.get() == "1" :

        Hat = "Assets/Hat1.wav"

    elif va3.get() == "2" :

        Hat = "Assets/Hat2.wav"

    elif va3.get() == "3" :

        Hat = "Assets/Hat3.wav"

    elif va3.get() == "4" :

        Hat = "Assets/Hat4.wav"

    else :

        Hat = 0

    if va4.get() == "1" :

        Snare = "Assets/Snare1.wav"

    elif va4.get() == "2" :

        Snare = "Assets/Snare2.wav"

    elif va4.get() == "3" :

        Snare = "Assets/Snare3.wav"

    elif va4.get() == "4" :

        Snare = "Assets/Snare4.wav"

    else :

        Snare = 0

    if va5.get() == "1" :

        Note = 1        

    elif va5.get() == "2" :

        Note = 2

    elif va5.get() == "3" :

        Note = 3

    elif va5.get() == "4" :

        Note = 4

    else :

        Note = 0
        
    
def choixnote() :

    global Note
    choix = random.randint(0,3)
    
    if choix == 0 and Note != 0 :
            
          mi = pygame.mixer.Sound("Assets/Mi"+str(Note)+".wav").play()
          
    elif choix == 1 and Note != 0:
        
          do = pygame.mixer.Sound("Assets/Do"+str(Note)+".wav").play()
        
    elif choix == 2 and Note != 0:
        
          si = pygame.mixer.Sound("Assets/Si"+str(Note)+".wav").play()

    elif choix == 3 and Note != 0:
        
          la = pygame.mixer.Sound("Assets/La"+str(Note)+".wav").play()

    else :

        pass


def instru(x):

    global Snare
    global Hat
    global Clap
    global Kick
    
    kick = random.randint(0,10)
    clap = random.randint(0,20)
    hat = random.randint(0,10)
    snare = random.randint(0,10)
    
    if x == 1:
        
        if kick <= 8 and Kick != 0 :

            Kick1 = pygame.mixer.Sound(Kick).play()
        if clap <= 4 and Clap != 0 :

            Clap1 = pygame.mixer.Sound(Clap).play()
            
        if hat <= 7 and Hat != 0:

            Hat1 = pygame.mixer.Sound(Hat).play()

        if snare <= 8 and Snare != 0:

            Snare1 = pygame.mixer.Sound(Snare).play()

        choixnote()
        
        while pygame.mixer.get_busy():

            pygame.time.Clock().tick(1300)
           # lecture en cours
            pass
    else:
        
        pygame.mixer.unpause()
        
        if clap <= 2 and Clap != 0 :

            Clap1 = pygame.mixer.Sound(Clap).play()
            
        if hat <= 3 and Hat != 0:

            Hat1 = pygame.mixer.Sound(Hat).play()

        if snare <= 3 and Snare != 0:

            Snare1 = pygame.mixer.Sound(Snare).play()

        choixnote()


        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(1300)
           
            pass

def jouer() :

    for i in range(0,7):

        instru(1)
        instru(2)

mafenetre.after(5,choix_instru)           

IBeat = PhotoImage(file= "Assets/IBeat.gif") #Photo par https://www.deviantart.com/art/Misty-Bay-575512868
Beat = Canvas(mafenetre, width = 600, height = 400,bg="dimgray")
Beat.create_image(170,250, image = IBeat)


    
    #----------------------------------------------------------------
    
KICK = Label(mafenetre,text=' K I C K ',fg='white',bg='black', font=('impact',14,'bold'))
KICK = Beat.create_window(50, 165 ,window = KICK)
    
va1 = StringVar()
va1.set(0)
    
BoutonKick1 = Radiobutton(mafenetre,text= "Kick 1 ",font=("impact",10), value = "1", variable=va1)
BoutonKick1.config(cursor="hand2")
Boutonkick1 = Beat.create_window(50, 210, window = BoutonKick1)

    
BoutonKick2 = Radiobutton(mafenetre,text= "Kick 2",font=("impact",10), value = "2", variable=va1)
BoutonKick2.config(cursor="hand2")
Boutonkick2 = Beat.create_window(50, 240, window = BoutonKick2)

BoutonKick3 = Radiobutton(mafenetre,text= "Kick 3",font=("impact",10), value = "3", variable=va1)
BoutonKick3.config(cursor="hand2")
Boutonkick3 = Beat.create_window(50, 270, window = BoutonKick3)

BoutonKick4 = Radiobutton(mafenetre,text= "Kick 4",font=("impact",10), value = "4", variable=va1)
BoutonKick4.config(cursor="hand2")
Boutonkick4 = Beat.create_window(50, 300, window = BoutonKick4)

    #----------------------------------------------------------------
    
HAT = Label(mafenetre,text=' H A T ',fg='white',bg='black', font=('impact',14,'bold'))
HAT = Beat.create_window(150, 165, window = HAT)

va2 = StringVar()
va2.set(0)

BoutonHat1 = Radiobutton(mafenetre,text= "Hat 1 ",font=("impact",10), value = "1", variable=va2)
BoutonHat1.config(cursor="hand2")
BoutonHat1 = Beat.create_window(150, 210, window = BoutonHat1)
    
BoutonHat2 = Radiobutton(mafenetre,text= "Hat 2",font=("impact",10), value = "2", variable=va2)
BoutonHat2.config(cursor="hand2")
BoutonHat2 = Beat.create_window(150, 240, window = BoutonHat2)

BoutonHat3 = Radiobutton(mafenetre,text= "Hat 3",font=("impact",10), value = "3", variable=va2)
BoutonHat3.config(cursor="hand2")
BoutonHat3 = Beat.create_window(150, 270, window = BoutonHat3)

BoutonHat4 = Radiobutton(mafenetre,text= "Hat 4",font=("impact",10), value = "4", variable=va2)
BoutonHat4.config(cursor="hand2")
BoutonHat4 = Beat.create_window(150, 300, window = BoutonHat4)

    #----------------------------------------------------------------
                                      
SNARE = Label(mafenetre,text=' S N A R E ',fg='white',bg='black', font=('impact',14,'bold'))
SNARE = Beat.create_window(260, 165, window = SNARE)
    
va3 = StringVar()
va3.set(0)

BoutonSnare1 = Radiobutton(mafenetre,text= "Snare 1 ",font=("impact",10), value = "1", variable=va3)
BoutonSnare1.config(cursor="hand2")
BoutonSnare1 = Beat.create_window(260, 210, window = BoutonSnare1)
    
BoutonSnare2 = Radiobutton(mafenetre,text= "Snare 2",font=("impact",10), value = "2", variable=va3)
BoutonSnare2.config(cursor="hand2")
BoutonSnare2 = Beat.create_window(260, 240, window = BoutonSnare2)

BoutonSnare3 = Radiobutton(mafenetre,text= "Snare 3",font=("impact",10), value = "3", variable=va3)
BoutonSnare3.config(cursor="hand2")
BoutonSnare3 = Beat.create_window(260, 270, window = BoutonSnare3)

BoutonSnare4 = Radiobutton(mafenetre,text= "Snare 4",font=("impact",10), value = "4", variable=va3)
BoutonSnare4.config(cursor="hand2")
BoutonSnare4 = Beat.create_window(260, 300, window = BoutonSnare4)

    #----------------------------------------------------------------

CLAP = Label(mafenetre,text=' C L A P ',fg='white',bg='black', font=('impact',14,'bold'))
CLAP = Beat.create_window(375, 165, window = CLAP)
    
va4 = StringVar()
va4.set(0)
    
BoutonClap1 = Radiobutton(mafenetre,text= "Clap 1 ",font=("impact",10), value = "1", variable=va4)
BoutonClap1.config(cursor="hand2")
BoutonClap1 = Beat.create_window(375, 210, window = BoutonClap1)
    
BoutonClap2 = Radiobutton(mafenetre,text= "Clap 2",font=("impact",10), value = "2", variable=va4)
BoutonClap2.config(cursor="hand2")
BoutonClap2 = Beat.create_window(375, 240, window = BoutonClap2)

BoutonClap3 = Radiobutton(mafenetre,text= "Clap 3",font=("impact",10), value = "3", variable=va4)
BoutonClap3.config(cursor="hand2")
BoutonClap3 = Beat.create_window(375, 270, window = BoutonClap3)

BoutonClap4 = Radiobutton(mafenetre,text= "Clap 4",font=("impact",10), value = "4", variable=va4)
BoutonClap4.config(cursor="hand2")
BoutonClap4 = Beat.create_window(375, 300, window = BoutonClap4)

     #----------------------------------------------------------------

INSTRUMENT = Label(mafenetre,text=' I N S T R U  ',fg='white',bg='black', font=('impact',14,'bold'))
INSTRUMENT = Beat.create_window(500, 165, window = INSTRUMENT)
    
va5 = StringVar()
va5.set(0)
    
BoutonInstru1 = Radiobutton(mafenetre,text= "           Piano               ",font=("impact",10), value = "1", variable=va5)
BoutonInstru1.config(cursor="hand2")
BoutonInstru1 = Beat.create_window(500, 210, window = BoutonInstru1)
    
BoutonInstru2 = Radiobutton(mafenetre,text= "           Electro             ",font=("impact",10), value = "2", variable=va5)
BoutonInstru2.config(cursor="hand2")
BoutonInstru2 = Beat.create_window(500, 240, window = BoutonInstru2)

BoutonInstru3 = Radiobutton(mafenetre,text= "Piano  + Guitare",font=("impact",10), value = "3", variable=va5)
BoutonInstru3.config(cursor="hand2")
BoutonInstru3 = Beat.create_window(500, 270, window = BoutonInstru3)

BoutonInstru4 = Radiobutton(mafenetre,text= "Electro + Guitare",font=("impact",10), value = "4", variable=va5)
BoutonInstru4.config(cursor="hand2")
BoutonInstru4 = Beat.create_window(500, 300, window = BoutonInstru4)
    
BEATMAKERLABEL = Label(mafenetre,text=' BEATMAKER ',fg='white',bg='black', font=('impact',38,'bold'))
BEATMAKERLABEL = Beat.create_window(305, 80, window = BEATMAKERLABEL)

BoutonPlay = Button(mafenetre,text="    Play   ",fg='black',bg='steelblue1', font=("impact",17),activebackground='steelblue4',activeforeground='black', command = jouer)
BoutonPlay.config(cursor="hand2")
BoutonPlay = Beat.create_window(300, 350, window = BoutonPlay)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12) 
x = 1                                   #Si x = 0 ou 2 le morceau est en lecture, sinon il est en pause
mute = 0                                #Si mute = 0 le son est allumé, sinon il est coupé
n=0                                     #A quelle case de la listbox sommes nous
channel1 = pygame.mixer.Channel(0)      #On définit un channel pour jouer la musique

def ouvrir():        #Ici on ajoute un morceau dans la playlist             
    
    global x
    global lien1
    global n
    
    if len(listbox.get(0,END)) == 0:    #On charge le premier morceau s'il n'y en a pas d'autres

      lien = askopenfilename(title="Choisissez un ficher audio", filetypes = [( "wav files", ".wav")])
      son = pygame.mixer.Sound(lien)

      channel1.play(son)
      channel1.pause()

      listbox.insert(END, lien)
      musique.set("En cours : "+(listbox.get(n)))

      x = 0     #On met en pause
      n += 1    #Et on ajoute 1 a la listbox

    else:   #S'il y a déjà un morceau, on ajoute seulement le lien dans la listbox

       lien1 = askopenfilename(title="Choisissez un ficher audio", filetypes = [( "wav files", ".wav")])
       listbox.insert(END, lien1) 


def Vol() :   #Ici on regle le volume
    
    mafenetre.after(200,Vol)   #On vérifie 200 fois par seconde la valeur du bouton volume et on ajuste en fonction des changements le son du mixer
    vol1 = BVolume.get()
    channel1.set_volume(vol1*.01)

def BLect_Pause (o):   #Ici on définit les 2 apparences du bouton lecture/pause

    global BLecture
    global Blp

    if o == 1 :   #Si o = 1 alors on détruit le bouton lecture et on place un bouton pause a la place

       BLecture.destroy()
       Blp = PhotoImage(file="Assets/BPause.gif")
       BLecture = Button(mafenetre, text = "Play", command = Lecture_Pause, bg="grey", image = Blp, borderwidth = 0)
       BLecture_Playlist = Playlist.create_window(105, 224, window = BLecture)

    else :   #Si o = 2 alors on fait l'inverse

       Blp = PhotoImage(file = "Assets/BLancer.gif")
       BLecture = Button(mafenetre, text = "Play", command = Lecture_Pause, bg="grey", image = Blp, borderwidth = 0)
       Blecture_Playlist = Playlist.create_window(105, 224, window = BLecture)


def TestSuivante() :   #Ici on ajoute les musiques a la file d'attente 

    mafenetre.after(10,TestSuivante)                     #On vérifie régulièrement si les valeurs on changées
    global n
    global x
    
    if channel1.get_queue() == None and x != 1 and len(listbox.get(n)) != 0: #On vérifie qu'il n'y a pas encore de musique dans la queue, 
        #que le programme n'est pas en pause et qu'on a ajouté assez de musiques pour pouvoir en mettre une nouvelle en attente

        son = pygame.mixer.Sound(listbox.get(n))
        channel1.queue(son)      #On ajoute un son a la file d'attente
   
           
        musique.set("En cours : "+(listbox.get(n-1)))   #Si le son peut aller dans la file d'attente c'est que le son d'avant (celui qui est en lecture) qu'on affichera   
        n += 1 #On incrémente n pour la prochaine musique ajoutée, n est donc constamment de 2 au dessus
        #de la musique jouée
        
    else :
  
        pass
            

def Precedent ():   #Ici on recule d'une musique

    global n
    global x
    
    if n>= 2 :   #On vérifie qu'il y a une musique avant
        
      channel1.stop()    #On arrete la lecture
      n -= 2             #On passe a la musique précédente 
              #On met en pause
                         
      #Puis on prépare le son et la mise en page :
      
      son = pygame.mixer.Sound(listbox.get(n)) 
      channel1.play(son)
      channel1.pause()
      musique.set("En cours : "+(listbox.get(n)))
      BLect_Pause(2)
      x = 1
                   
    else :
      pass

def Passer():   #Ici on avance d'une musique

    global x 
    global n

    #On passe directement a la musique qui est dans la fille d'attente en diminuant n de 1     
    channel1.stop()
    BLect_Pause(2)
    son = pygame.mixer.Sound(listbox.get(n-1))
    channel1.play(son)
    channel1.pause()
    musique.set("En cours : "+(listbox.get(n-1)))
    x = 1

    
def Mute_Demute() :

    global mute

    if mute == 0 :

      BVolume.set(0)
      BVolume.config(state=DISABLED)
      mute = 1
      BMute_Demute(0)

    else :

      BVolume.config(state=NORMAL)
      BVolume.set(15)
      mute = 0
      BMute_Demute(1)
      
def BMute_Demute(mute):
    
    global IMute
    global BMute
    global Playlist

    if mute == 1 :
        
      IMute = PhotoImage(file = "Assets/BSonO.gif")
      BMute = Button(mafenetre, command = Mute_Demute, image = IMute, bg = "grey")
      BMute_Playlist = Playlist.create_window(140, 28, window = BMute)

    else :
        
      IMute = PhotoImage(file = "Assets/BSonC.gif")
      BMute = Button(mafenetre, command = Mute_Demute, image = IMute, bg = "grey")
      BMute_Playlist = Playlist.create_window(140, 28, window = BMute)
    

def Lecture_Pause() :

    global x
    global lien1
    
    if x == 0 :
        channel1.unpause()
        BLect_Pause(1)
        x = 2
        

    elif x == 2 :
        channel1.pause()
        BLect_Pause(2)
        x = 1

    else :
        channel1.unpause()
        BLect_Pause(1)
        x = 2
    
mafenetre.after(200,Vol)
mafenetre.after(50,TestSuivante)

IFond = PhotoImage(file= "Assets/IFond.gif")
Playlist = Canvas(mafenetre, width = 500, height=500)
Playlist.create_image(170,250, image = IFond)

Ba = PhotoImage(file="Assets/BAjouter.gif")
BAjouter = Button(mafenetre, command = ouvrir, image = Ba, borderwidth = 0, bg = "grey")
BAjouter_Playlist = Playlist.create_window(23, 224, window = BAjouter)

musique = StringVar()
Musique = Label(mafenetre, textvariable = musique, bg = "grey", fg = "black", width = 21)
musique.set("[Appuyez sur +]")
Musique = Playlist.create_window(85, 191, window = Musique)

Titres = Label(mafenetre, text = "Titres ajoutés :", bg = "grey", fg = "black", width = 21)
Titres = Playlist.create_window(85, 61, window = Titres)

BVolume = Scale(mafenetre,orient="horizontal", from_=0, to=100, fg="black", bg="grey", borderwidth = 0)
BVolume.set(100)
BVolume_Playlist = Playlist.create_window(62, 28, window = BVolume)

IPrecedent = PhotoImage(file= "Assets/BPrécédent.gif")
BPrecedent = Button(mafenetre, command = Precedent, image = IPrecedent, borderwidth = 0, bg = "grey")
BPrecedent = Playlist.create_window(64, 224, window = BPrecedent)

IPasser = PhotoImage(file= "Assets/BPasser.gif")
BPasser = Button(mafenetre, command = Passer, image = IPasser, borderwidth = 0, bg = "grey")
BPasser = Playlist.create_window(146, 224, window = BPasser)
 
mafenetre.protocol("WM_DELETE_WINDOW", Fermeture)

BMute_Demute(1)

BLect_Pause(0)

listbox = Listbox(mafenetre,width=25, height=6, relief = "groove")
listbox_Playlist = Playlist.create_window(85, 127, window = listbox)

mafenetre.mainloop()

