from random import randint
import tkinter as tk
from tkinter import *
from ctypes import windll
from math import ceil
def roll6(n):
    m = 0
    roll = 0
    while (m < n):
        roll += randint(1,6)
        m += 1
    return roll

def rolls6(n, m):
    first = roll6(n)
    second = roll6(m)
    result = first - second
    if(result < 0):
        result = 0
    return result
    
def roll66():
    one = roll6(1)
    ten = roll6(1) * 10
    roll = ten + one
    return roll

def getWorld(clicked):
    print(clicked.get())
    
def calcPsgWert(staClicked, zieClicked, mil, pop):
    #                         Agr    Ast       Oed      Wue     Liq    Gar    Dic     Eis    Ind    Due     NAgr   NInd     Arm      Rei    Was    Gel     Rot
    Passagierverkehrswert = ['0,0', '1,-1', '-5, -5', '-1,-1', '0,0', '2,2', '0,4', '1,-1', '2,1', '0,-4', '0,0', '0,-1', '-2,-1', '-1,2', '0,0', '2,-2', '4,-4']
    Welten = ['Agrarwelt', 'Asteroid', 'Ödwelt', ' Wüstenwelt', 'Liquidwelt', 'Gartenwelt', 'Dicht besiedelte Welt', 'Eiskappenwelt', 'Industriewelt', 'Dünn besiedelte Welt', 'Nicht-Agrarwelt', 'Nicht-Industriewelt', 'Arme Welt', 'Reiche Welt', 'Wasserwelt', 'Gelbe Zone', 'Rote Zone']
    #sammeln der einzelnen Werte
    milWert = mil.get()
    popWert = pop.get()
    staWelt = staClicked.get()
    zieWelt = zieClicked.get()

    #wenn nichts eingetragen, dann 0
    if(milWert == ""):
        milWert = 0
    if(popWert == ""):
        popWert = 0

    #festlegen der Welt-Werte
    staTmp = Passagierverkehrswert[Welten.index(staWelt)]
    zieTmp = Passagierverkehrswert[Welten.index(zieWelt)]
    staWert = staTmp.split(',')[0]
    zieWert = zieTmp.split(',')[1]

    PsgWert = int(popWert) + ceil(int(milWert)/2) + int(staWert) + int(zieWert)
    return PsgWert

def verPsg(staClicked, zieClicked, mil, pop, UpsgNum, MpsgNum, OpsgNum):
    PsgWert = calcPsgWert(staClicked, zieClicked, mil, pop)
    if(PsgWert <= 0):
        psg = [0, 0, 0]
    if(PsgWert == 1):
        tmpU = roll6(2) - 6
        if(tmpU < 0):
            tmpU = 0
        tmpM = roll6(1) - 2
        if(tmpM < 0):
            tmpM = 0
        psg = [tmpU, tmpM, 0]
    if(PsgWert == 2):
        tmpU = roll6(2)
        tmpM = roll6(1)
        tmpO = rolls6(1, 1)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 3):
        tmpU = roll6(2)
        tmpM = rolls6(2, 1)
        tmpO = rolls6(2, 2)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 4):
        tmpU = rolls6(3, 1)
        tmpM = rolls6(2, 1)
        tmpO = rolls6(2, 1)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 5):
        tmpU = rolls6(3, 1)
        tmpM = rolls6(3, 2)
        tmpO = rolls6(2, 1)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 6):
        tmpU = roll6(3)
        tmpM = rolls6(3, 2)
        tmpO = rolls6(3, 2)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 7):
        tmpU = roll6(3)
        tmpM = rolls6(3, 1)
        tmpO = rolls6(3, 2)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 8):
        tmpU = roll6(4)
        tmpM = rolls6(3, 1)
        tmpO = rolls6(3, 1)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 9):
        tmpU = roll6(4)
        tmpM = roll6(3)
        tmpO = rolls6(3, 1)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 10):
        tmpU = roll6(5)
        tmpM = roll6(3)
        tmpO = rolls6(3, 1)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 11):
        tmpU = roll6(5)
        tmpM = roll6(4)
        tmpO = roll6(3)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 12):
        tmpU = roll6(6)
        tmpM = roll6(4)
        tmpO = roll6(3)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 13):
        tmpU = roll6(6)
        tmpM = roll6(4)
        tmpO = roll6(4)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 14):
        tmpU = roll6(7)
        tmpM = roll6(5)
        tmpO = roll6(4)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert == 15):
        tmpU = roll6(8)
        tmpM = roll6(5)
        tmpO = roll6(4)
        psg = [tmpU, tmpM, tmpO]
    if(PsgWert >= 16):
        tmpU = roll6(9)
        tmpM = roll6(6)
        tmpO = roll6(5)
        psg = [tmpU, tmpM, tmpO]
    UpsgNum.config(text=psg[0])
    MpsgNum.config(text=psg[1])
    OpsgNum.config(text=psg[2])
    return

def Passagierverkehr():
    for widget in root.winfo_children():
        widget.destroy()
    #                         Agr    Ast       Oed      Wue     Liq    Gar    Dic     Eis    Ind    Due     NAgr   NInd     Arm      Rei    Was    Gel     Rot
    Passagierverkehrswert = ['0,0', '1,-1', '-5, -5', '-1,-1', '0,0', '2,2', '0,4', '1,-1', '2,1', '0,-4', '0,0', '0,-1', '-2,-1', '-1,2', '0,0', '2,-2', '4,-4']
    #Abfragen der Welt
    Welten = ['Agrarwelt', 'Asteroid', 'Ödwelt', ' Wüstenwelt', 'Liquidwelt', 'Gartenwelt', 'Dicht besiedelte Welt', 'Eiskappenwelt', 'Industriewelt', 'Dünn besiedelte Welt', 'Nicht-Agrarwelt', 'Nicht-Industriewelt', 'Arme Welt', 'Reiche Welt', 'Wasserwelt', 'Gelbe Zone', 'Rote Zone']
    #Abfragen der Startwelt
    staClicked = tk.StringVar()
    staLabel = tk.Label(root, text="Startwelt")
    staLabel.grid(row=0, column=0)
    staDrop = tk.OptionMenu(root, staClicked, *Welten)
    staDrop.grid(row=0, column=1)
    #Abfragen der Zielwelt
    zieClicked = tk.StringVar()
    zieLabel = tk.Label(root, text="Zielwelt")
    zieLabel.grid(row=1, column=0)
    zieDrop = tk.OptionMenu(root, zieClicked, *Welten)
    zieDrop.grid(row=1, column=1)


    #Abfragen des Millieu
    milLabel = tk.Label(root, text="Gesseligkeit-/Millieuwurf?")
    milLabel.grid(row=2, column=0)
    milEntry = tk.Entry(root)
    milEntry.grid(row=2,column=1)

    #Abfragen des Populationswert
    popLabel = tk.Label(root, text="Populationswert der aktuellen Welt")
    popLabel.grid(row=3, column=0)
    popEntry = tk.Entry(root)
    popEntry.grid(row=3, column=1)

    # #Berechnung des PsgWertes sowie Darstellung
    # psgLabel = tk.Label(root, text="")
    # psgLabel.grid(row=4, column=1)
    # psgbutton = tk.Button(root, text="Berechnung des Passagierwertes", command= lambda: calcPsgWert(staClicked, zieClicked, milEntry, popEntry, psgLabel))
    # psgbutton.grid(row=4, column=0)
    
    #Berechnung der verfügbaren Passagiere
    UpsgLabel = tk.Label(root, text="Unterdeckpassagiere:")
    UpsgLabel.grid(row=6, column=0)
    UpsgNum = tk.Label(root, text="0")
    UpsgNum.grid(row=6, column=1)
    MpsgLabel = tk.Label(root, text="Mitteldeckpassagiere:")
    MpsgLabel.grid(row=7, column=0)
    MpsgNum = tk.Label(root, text="0")
    MpsgNum.grid(row=7, column=1)
    OpsgLabel = tk.Label(root, text="Oberdeckpassagiere:")
    OpsgLabel.grid(row=8, column=0)
    OpsgNum = tk.Label(root, text="0")
    OpsgNum.grid(row=8, column=1)
    berButton = tk.Button(root, text="Berechnung der verfügbaren Passagiere", command= lambda: verPsg(staClicked, zieClicked, milEntry, popEntry, UpsgNum, MpsgNum, OpsgNum))
    berButton.grid(row=5, column=0)

    exitButton = tk.Button(root, text="Exit", command=start)
    exitButton.grid(row=9, column=0)

#Berechne den Güterverkehrswert
def calcGutWert(staClicked, zieClicked, pop, tlD):
    
    #                      Agr     Ast    Oed      Wue     Liq    Gar     Dic     Eis    Ind     Due    NAgr    NInd     Arm      Rei    Was    Gel     Rot
    Gueterverkehrswert = ['2,1', '-3,1', '0, -5', '-3,0', '-3,0', '2,1', '2,0', '-3,0', '3,2', '-5,0', '-3,1', '-3,1', '-3,-3', '2,2', '-3,0', '5,-5', '-5,0']
    Welten = ['Agrarwelt', 'Asteroid', 'Ödwelt', ' Wüstenwelt', 'Liquidwelt', 'Gartenwelt', 'Dicht besiedelte Welt', 'Eiskappenwelt', 'Industriewelt', 'Dünn besiedelte Welt', 'Nicht-Agrarwelt', 'Nicht-Industriewelt', 'Arme Welt', 'Reiche Welt', 'Wasserwelt', 'Gelbe Zone', 'Rote Zone']    

    staWelt = staClicked.get()
    zieWelt = zieClicked.get()
    popWert = pop.get()
    tlDWert = tlD.get()

    #Wenn Startwelt = Ödwelt oder Zielwelt = Rote Zone, dann sofort auf 0 setzen
    if(staWelt == 'Ödwelt' or zieWelt == 'Rote Zone'):
        return 0

    #Wenn kein Pop oder TL-Differenzwert eingetragen wurde, setze ihn auf 0
    if(popWert == ''):
        popWert = 0
    if(tlDWert == ''):
        tlDWert = 0
    
    #Ermitteln der Start- und Zielwerte
    staTmp = Gueterverkehrswert[Welten.index(staWelt)]
    zieTmp = Gueterverkehrswert[Welten.index(zieWelt)]
    staWert = staTmp.split(',')[0]
    zieWert = zieTmp.split(',')[1] 
    #Ausrechnen des Güterverkehrswerts
    gutWert = int(popWert) - int(tlDWert) + int(staWert) + int(zieWert)
    return gutWert

def post(staClicked, zieClicked, pop, tlD, shipweapon, scrEntry, sozEntry, tl5, postLabel):
    gutWert = calcGutWert(staClicked, zieClicked, pop, tlD)
    gutWM = 0
    if(gutWert <=-10):
        gutWm = -2
    elif(gutWert <= -5):
        gutWM = -1
    elif(gutWert <= 4):
        gutWM = 0
    elif(gutWert <= 9):
        gutWM = 1
    else:
        gutWM = 2

    scr = scrEntry.get()
    soz = sozEntry.get()

#falls nichts eingetreagen wurde, setze auf 0
    if(scr == ''):
        scr = 0
    if(soz == ''):
        soz = 0

    if(shipweapon == 1):
        gutWM += 2
    if(tl5 == 1):
        gutWM -= 4
    gutWM = gutWM + int(soz) + int(scr)
    roll = roll6(2) + gutWM
    if(roll >= 12):
        postLabel.config(text="Es ist Post verfügbar")
    else:
        postLabel.config(text="Es ist leider keine Post verfügbar")
    return

def verGut(staClicked, zieClicked, pop, tlD, BGutNum, KGutNum, GGutNum):
    gutWert = calcGutWert(staClicked, zieClicked, pop, tlD)
    if(gutWert <= 0):
        gut = [0, 0, 0]
    if(gutWert == 1):
        tmpK = roll6(1) - 4
        if(tmpK < 0):
            tmpK = 0
        tmpG = roll6(1) - 4
        if(tmpG < 0):
            tmpG = 0
        gut = [0, tmpK, tmpG]
    if(gutWert == 2):
        tmpK = roll6(1) - 1
        tmpG = roll6(1) - 2
        if(tmpG < 0):
            tmpG = 0
        gut = [0, tmpK, tmpG]
    if(gutWert == 3):
        tmpK = roll6(1)
        tmpG = roll6(1) - 1
        gut = [0, tmpK, tmpG]
    if(gutWert == 4):
        tmpK = roll6(1) + 1
        tmpG = roll6(1)
        gut = [0, tmpK, tmpG]
    if(gutWert == 5):
        tmpK = roll6(1) + 2
        tmpG = roll6(1) +1
        gut = [0, tmpK, tmpG]
    if(gutWert == 6):
        tmpK = roll6(1) + 3
        tmpG = roll6(1) + 2
        gut = [0, tmpK, tmpG]
    if(gutWert == 7):
        tmpK = roll6(1) + 4
        tmpG = roll6(1) +3
        gut = [0, tmpK, tmpG]
    if(gutWert == 8):
        tmpK = roll6(1) + 5
        tmpG = roll6(1) + 4
        gut = [0, tmpK, tmpG]
    if(gutWert == 9):
        tmpB = roll6(1) - 2
        if(tmpB < 0):
            tmpB = 0
        tmpK = roll6(1) + 6
        tmpG = roll6(1) + 5
        gut = [tmpB, tmpK, tmpG]
    if(gutWert == 10):
        tmpB = roll6(1)
        tmpK = roll6(1) + 7
        tmpG = roll6(1) + 6
        gut = [tmpB, tmpK, tmpG]
    if(gutWert == 11):
        tmpB = roll6(1) + 1 
        tmpK = roll6(1) + 8
        tmpG = roll6(1) + 7
        gut = [tmpB, tmpK, tmpG]
    if(gutWert == 12):
        tmpB = roll6(1) + 2
        tmpK = roll6(1) + 9
        tmpG = roll6(1) + 8
        gut = [tmpB, tmpK, tmpG]
    if(gutWert == 13):
        tmpB = roll6(1) + 3
        tmpK = roll6(1) + 10
        tmpG = roll6(1) + 9
        gut = [tmpB, tmpK, tmpG]
    if(gutWert == 14):
        tmpB = roll6(1) + 4
        tmpK = roll6(1) + 12
        tmpG = roll6(1) + 10
        gut = [tmpB, tmpK, tmpG]
    if(gutWert == 15):
        tmpB = roll6(1) + 5
        tmpK = roll6(1) + 14
        tmpG = roll6(1) + 11
        gut = [tmpB, tmpK, tmpG]
    if(gutWert >= 16):
        tmpB = roll6(1) + 6
        tmpK = roll6(1) + 16
        tmpG = roll6(1) + 12
        gut = [tmpB, tmpK, tmpG]
    BGutNum.config(text=gut[0])
    KGutNum.config(text=gut[1])
    GGutNum.config(text=gut[2])
    return

def Gueterverkehr():
    Welten = ['Agrarwelt', 'Asteroid', 'Ödwelt', ' Wüstenwelt', 'Liquidwelt', 'Gartenwelt', 'Dicht besiedelte Welt', 'Eiskappenwelt', 'Industriewelt', 'Dünn besiedelte Welt', 'Nicht-Agrarwelt', 'Nicht-Industriewelt', 'Arme Welt', 'Reiche Welt', 'Wasserwelt', 'Gelbe Zone', 'Rote Zone']
    for widget in root.winfo_children():
        widget.destroy()

    #Abfragen der Startwelt
    staClicked = tk.StringVar()
    staLabel = tk.Label(root, text="Startwelt")
    staLabel.grid(row=0, column=0)
    staDrop = tk.OptionMenu(root, staClicked, *Welten)
    staDrop.grid(row=0, column=1)
    #Abfragen der Zielwelt
    zieClicked = tk.StringVar()
    zieLabel = tk.Label(root, text="Startwelt")
    zieLabel.grid(row=1, column=0)
    zieDrop = tk.OptionMenu(root, zieClicked, *Welten)
    zieDrop.grid(row=1, column=1)

    #Abfragen des Populationswert
    popLabel = tk.Label(root, text="Populationswert der aktuellen Welt")
    popLabel.grid(row=2, column=0)
    popEntry = tk.Entry(root)
    popEntry.grid(row=2, column=1)

    #Abfragen des TL-Unterschieds
    tlLabel = tk.Label(root, text="Unterschied im TL-Level")
    tlLabel.grid(row=3, column=0)
    tlEntry = tk.Entry(root)
    tlEntry.grid(row=3, column=1)

    ## POST ##
    #Abfrage Schiffsbewaffnung
    shipweapon = IntVar()
    SchLabel = tk.Label(root, text="Schiffsbewaffnung?")
    SchLabel.grid(row=4, column=0)
    SchCheck = tk.Checkbutton(root, variable=shipweapon)
    SchCheck.grid(row=4, column=1)
    
    #Abfrage nach hoechstem Scout oder Raumflotterang
    scrLabel = tk.Label(root, text="Höchster Scout-/Raumflottenrang?")
    scrLabel.grid(row=5, column=0)
    scrEntry = tk.Entry(root)
    scrEntry.grid(row=5, column=1)

    #Abfrage nach hoechstem Sozialstatus
    sozLabel = tk.Label(root, text="Höchster Sozialstatus-WM")
    sozLabel.grid(row=6, column=0)
    sozEntry = tk.Entry(root)
    sozEntry.grid(row=6, column=1)

    #Abfrage TL <= 5
    tl5 = IntVar()
    tl5Label = tk.Label(root, text="Ist TL 5 oder weniger?")
    tl5Label.grid(row=7, column=0)
    tl5Check = tk.Checkbutton(root, variable=tl5)
    tl5Check.grid(row=7, column=1)

    #Berechnung der Güter
    BGutLabel = tk.Label(root, text="Beiläufige Güter")
    BGutLabel.grid(row=9, column=0)
    BGutNum = tk.Label(root, text="0")
    BGutNum.grid(row=9, column=1)
    KGutLabel = tk.Label(root, text="Kleine Güter")
    KGutLabel.grid(row=10, column= 0)
    KGutNum = tk.Label(root, text="0")
    KGutNum.grid(row=10, column=1)
    GGutLabel = tk.Label(root, text="Große Güter")
    GGutLabel.grid(row=11, column=0)
    GGutNum = tk.Label(root, text="0")
    GGutNum.grid(row=11, column=1)

    gutButton = tk.Button(root, text="Berechnung der Gütermengen", command= lambda: verGut(staClicked, zieClicked, popEntry, tlEntry, BGutNum, KGutNum, GGutNum))
    gutButton.grid(row=8, column= 0)

    postLabel = tk.Label(root, text="")
    postLabel.grid(row=12, column=1)
    postButton = tk.Button(root, text="Postverfügbarkeit", command= lambda: post(staClicked, zieClicked, popEntry, tlEntry, shipweapon, scrEntry, sozEntry, tl5, postLabel))
    postButton.grid(row=12, column=0)

    exitButton = tk.Button(root, text="Exit", command=start)
    exitButton.grid(row=15, column=0)


def start():
    for widget in root.winfo_children():
        widget.destroy()
    #Button for selecting Passengertravel
    pasButton = Button(root, text='Passagierverkehr', command=Passagierverkehr)
    pasButton.pack()
    gutButton = Button(root, text="Güterverkehr", command=Gueterverkehr).pack()
    exitButton = tk.Button(root, text="Exit", command=exit)
    exitButton.pack()
    




#initiate tkinter
root =tk.Tk()
#setting the title -> Name of the window
root.title('Test')

#Size of the window
wwidth = 600
wheight = 400

#Centering window in the middle of the screen
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()

centerx = int(swidth/2 - wwidth/2)
centery = int(sheight/2 - wheight/2)
root.geometry(f'{wwidth}x{wheight}+{centerx}+{centery}')


start()


#solve textblur and set the mainloop
windll.shcore.SetProcessDpiAwareness(1)
root.mainloop()

