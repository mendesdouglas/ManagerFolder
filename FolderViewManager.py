import tkinter as tk
# from tkinter import Tk,LEFT,RIGHT,BOTH,RAISED, SOLID, GROOVE, BOTTOM,TOP, VERTICAL,RIDGE,SUNKEN, CENTER,Scrollbar, Y,X
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style, Frame, Button, Label, Entry

import shutil
import os
import time
import datetime


LARGE_FONT = ("Verdana", 14)
NORMAL_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)


class FV(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for framess in (StartPage, PageOne):
            frame = framess(container,self)
            self.frames[framess] = frame
            frame.grid(row=0, column=0, sticky="wsen")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




class StartPage(tk.Frame):
    def __init__(self,parent, controller):
        # cont = tk.Frame.__init__(self,parent)
        # cont.pack()

        tk.Frame.__init__(self, parent)
        cont = tk.Frame(self, relief=SUNKEN,borderwidth=1)
        cont.pack(side=LEFT,expand=True,fill=BOTH)
        self.pack(fill=BOTH, expand=True, side=BOTTOM)
        #self.parent = parent


        self.initUI()
        self.StartItens()


    def initUI(self):
        ("Gerenciador de Produção")
        self.style = Style()
        self.style.theme_use("default")


        frame = ttk.Frame(self, relief=SUNKEN,borderwidth=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.pack()




        #frame2 = ttk.Frame(self, relief=GROOVE, borderwidth=1)
        #frame2.pack(fill=BOTH,side=LEFT, expand=True)
        # frame3 = ttk.Frame(self, relief=GROOVE, borderwidth=1)
        # frame3.pack(fill=BOTH, side=RIGHT, expand=True)
        frame4 = ttk.Frame(self, relief=GROOVE, borderwidth=1)
        frame4.pack(fill=BOTH, side=LEFT, expand=True)

        frame5 = ttk.Frame(self, relief=GROOVE, borderwidth=1)
        frame5.pack(fill=BOTH, side=RIGHT, expand=True)


        updateButton = ttk.Button(frame, text="Atualizar")
        updateButton.bind("<Button-1>", self.AutoUpdate)
        updateButton.pack()
        gerarButton = ttk.Button(frame, text="Gerar", command=lambda: self.P ) #ridge,sunken
        gerarButton.pack()
        gerarButton = ttk.Button(frame, text="Buscar")  # ridge,sunken
        gerarButton.pack()


        ########
        self.total = ttk.Label(frame, text="TOTAL HOJE", font=SMALL_FONT)
        self.total.pack()
        self.lblcinco = ttk.Label(frame4, text="7:00", font=SMALL_FONT)
        self.lblcinco.pack()
        self.lblseis = ttk.Label(frame4, text="7:00", font=SMALL_FONT)
        self.lblseis.pack()
        self.lblsete = ttk.Label(frame4, text="7:00", font=SMALL_FONT)
        self.lblsete.pack()
        self.lbloito = ttk.Label(frame4, text="8:00", font=SMALL_FONT)
        self.lbloito.pack()
        self.lblnove = ttk.Label(frame4, text="8:00", font=SMALL_FONT)
        self.lblnove.pack()
        self.lbldez = ttk.Label(frame4, text="8:00", font=SMALL_FONT)
        self.lbldez.pack()
        self.lblonze = ttk.Label(frame4, text="8:00", font=SMALL_FONT)
        self.lblonze.pack()
        self.lbldoze = ttk.Label(frame4, text="8:00", font=SMALL_FONT)
        self.lbldoze.pack()
        self.lbltreze = ttk.Label(frame4, text="8:00", font=SMALL_FONT)
        self.lbltreze.pack()
        self.lblquartoze = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lblquartoze.pack()
        self.lblquinze = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lblquinze.pack()
        self.lbldezesseis = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lbldezesseis.pack()
        self.lbldezessete = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lbldezessete.pack()
        self.lbldezoito = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lbldezoito.pack()
        self.lbldezenove = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lbldezenove.pack()
        self.lblvinte = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lblvinte.pack()
        self.lblvinteum = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lblvinteum.pack()
        self.lblvintedois = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        self.lblvintedois.pack()
        # self.lblvintetres = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        # self.lblvintetres.pack()
        # self.lblvintequatro = ttk.Label(frame5, text="8:00", font=SMALL_FONT)
        # self.lblvintequatro.pack()

        ########



        # totalLabel = ttk.Label(frame2,text="MANHÃ")
        # totalLabel.pack(side=TOP)
        # totalLabel2 = ttk.Label(frame3, text="TARDE")
        # totalLabel2.pack(side=TOP)

    def ListarDiretorio(self):
        path = "c:\PDF Files"
        #path=(r'\\scanserver\folder')
        # open(path, 'w+')
        # path=input("Entre com o Local do Diretorio para Listar: ")
        # sortlist=Files_json.sort(os.listdir(path))

        somatotal = 0
        ccinco = 0
        cseis = 0
        csete = 0
        coito = 0
        cnove = 0
        cdez = 0
        conze = 0
        cdoze = 0
        ctreze = 0
        cquartoze = 0
        cquinze = 0
        cdezesseis = 0
        cdezessete = 0
        cdezoito = 0
        cdezenove = 0
        cvinte = 0
        cvinteum = 0
        cvintedois = 0
        # cvintetres = 0
        # cvintequatro = 0

        for root, dirs, files in os.walk(path):

            for file in files:

                pathname = os.path.join(root, file)
                getctime = os.path.getatime(pathname)
                getmtimee = os.path.getmtime(pathname)
                getatime = os.path.getatime(pathname)
                tictime = time.ctime(getmtimee)

                dtt = datetime.datetime.strptime(tictime, "%a %b %d %H:%M:%S %Y")
                ola = dtt.strftime('%d/%m/%Y')

                timestFile = datetime.date.fromtimestamp(getctime)
                timestToday = datetime.datetime.fromtimestamp(getctime)
                cinco = 5
                seis = 6
                sete = 7
                oito = 8
                nove = 9
                dez = 10
                onze = 11
                doze = 12
                treze = 13
                quartoze = 14
                quinze = 15
                dezesseis = 16
                dezessete = 17
                dezoito = 18
                dezenove = 19
                vinte = 20
                vinteum = 21
                vintedois = 22
                #vintetres = 23
                #vintequatro = 24

                if timestFile.day == datetime.date.today().day:
                    somatotal += 1
                    if timestToday.hour == ccinco:
                        ccinco += 1
                    if timestToday.hour == seis:
                        cseis += 1
                    if timestToday.hour == sete:
                        csete += 1
                    if timestToday.hour == oito:
                        coito += 1
                    if timestToday.hour == nove:
                        cnove += 1
                    if timestToday.hour == dez:
                        cdez += 1
                    if timestToday.hour == onze:
                        conze += 1
                    if timestToday.hour == doze:
                        cdoze += 1
                    if timestToday.hour == treze:
                        ctreze += 1
                    if timestToday.hour == quartoze:
                        cquartoze += 1
                    if timestToday.hour == quinze:
                        cquinze += 1
                    if timestToday.hour == dezesseis:
                        cdezesseis += 1
                    if timestToday.hour == dezessete:
                        cdezessete += 1
                    if timestToday.hour == dezoito:
                        cdezoito += 1
                    if timestToday.hour == dezenove:
                        cdezenove += 1
                    if timestToday.hour == vinte:
                        cvinte += 1
                    if timestToday.hour == vinteum:
                        cvinteum = + 1
                    if timestToday.hour == vintedois:
                        cvintedois = + 1
                    # if timestToday.hour == vintetres:
                    #     cvintetres = + 1
                    # if timestToday.hour == vintequatro:
                    #     cvintequatro = + 1

            dict = {
                'total': somatotal,
                '5':ccinco,
                '6':cseis,
                '7': csete,
                '8': coito,
                '9': cnove,
                '10': cdez,
                '11': conze,
                '12': cdoze,
                '13': ctreze,
                '14': cquartoze,
                '15': cquinze,
                '16': cdezesseis,
                '17': cdezessete,
                '18': cdezoito,
                '19': cdezenove,
                '20': cvinte,
                '21': cvinteum,
                '22': cvintedois,
                # '23': cvintetres,
                # '24': cvintequatro,
            }

            # builditens = self.Update(dict)


            # print('8:00: ',dict['8'])
            # print('9:00: ', dict['9'])
            # if msg["text"] == "Mudar":
            #     msg["text"] ="Mudanca feita"

            # print(dict)

            return dict

    def StartItens(self):
        dict = self.ListarDiretorio()
        if dict != None:
            self.BuildLabel(dict)
            print("Estou no StartItens -> if")
            # time.sleep(4)
            # self.Transition(dict)

            # self.after_idle(3000,self.printTest(dict))
            # self.Transition(dict)

    def printTest(self, dict):
        print("estou no printTest")
        time.sleep(60)
        print(dict)
        self.LimpezarGeral()
        print("Feito a Limpeza")

        self.after(3000, self.AutoUpdate())

    def print(self):
        print('teste')


    def AutoUpdate(self, event):
        self.LimpezarGeral()
        dict = self.ListarDiretorio()
        self.BuildLabel(dict)
        print("Estou no AutoUpdate")

    def LimpezarGeral(self):

        self.total.pack_forget()
        self.lblcinco.pack_forget()
        self.lblseis.pack_forget()
        self.lblsete.pack_forget()
        self.lbloito.pack_forget()
        self.lblnove.pack_forget()
        self.lbldez.pack_forget()
        self.lblonze.pack_forget()
        self.lbldoze.pack_forget()
        self.lbltreze.pack_forget()
        self.lblquartoze.pack_forget()
        self.lblquinze.pack_forget()
        self.lbldezesseis.pack_forget()
        self.lbldezessete.pack_forget()
        self.lbldezoito.pack_forget()
        self.lbldezenove.pack_forget()
        self.lblvinte.pack_forget()
        self.lblvinteum.pack_forget()
        self.lblvintedois.pack_forget()
        # self.lblvintetres.pack_forget()
        # self.lblvintequatro.pack_forget()

    def ClearItems(self, event):
        self.total.pack_forget()
        self.lblsete.pack_forget()
        self.lbloito.pack_forget()
        self.lblnove.pack_forget()
        self.lbldez.pack_forget()
        self.lblonze.pack_forget()
        self.lbldoze.pack_forget()
        self.lbltreze.pack_forget()
        self.lblquartoze.pack_forget()
        self.lblquinze.pack_forget()
        self.lbldezesseis.pack_forget()
        self.lbldezessete.pack_forget()
        self.lbldezoito.pack_forget()
        self.lbldezenove.pack_forget()
        self.lblvinte.pack_forget()
        self.lblvinteum.pack_forget()
        self.lblvintedois.pack_forget()
        # self.lblvintetres.pack_forget()
        # self.lblvintequatro.pack_forget()

    def BuildLabel(self, dict):

        # totalLabel2 = ttk.Label(frame3, text="TARDE")
        # totalLabel2.pack(side=TOP)
        self.total.pack()
        self.lblcinco.pack()
        self.lblseis.pack()
        self.lblsete.pack()
        self.lbloito.pack()
        self.lblnove.pack()
        self.lbldez.pack()
        self.lblonze.pack()
        self.lbldoze.pack()
        self.lbltreze.pack()
        self.lblquartoze.pack()
        self.lblquinze.pack()
        self.lbldezesseis.pack()
        self.lbldezessete.pack()
        self.lbldezoito.pack()
        self.lbldezenove.pack()
        self.lblvinte.pack()
        self.lblvinteum.pack()
        self.lblvintedois.pack()



        # totalLabel = ttk.Label(self, text="MANHÃ")
        # totalLabel.pack(side=TOP)



        self.total["text"] = "TOTAL", "HOJE", dict['total']
        self.lblcinco["text"] = "5:00", "=", dict['5']
        self.lblseis["text"] = "6:00", "=", dict['6']
        self.lblsete["text"] = "7:00", "=", dict['7']
        self.lbloito["text"] = "8:00", "=", dict['8']
        self.lblnove["text"] = "9:00", "=", dict['9']
        self.lbldez["text"] = "10:00", "=", dict['10']
        self.lblonze["text"] = "11:00", "=", dict['11']
        self.lbldoze["text"] = "12:00", "=", dict['12']
        self.lbltreze["text"] = "13:00", "=", dict['13']
        self.lblquartoze["text"] = "14:00", "=", dict['14']
        self.lblquinze["text"] = "15:00", "=", dict['15']
        self.lbldezesseis["text"] = "16:00", "=", dict['16']
        self.lbldezessete["text"] = "17:00", "=", dict['17']
        self.lbldezoito["text"] = "18:00", "=", dict['18']
        self.lbldezenove["text"] = "19:00", "=", dict['19']
        self.lblvinte["text"] = "20:00", "=", dict['20']
        self.lblvinteum["text"] = "21:00", "=", dict['21']
        self.lblvintedois["text"] = "22:00", "=", dict['22']

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Pagina Um", font=LARGE_FONT)
        label.pack(pady=10, padx=10)




def main():
    #root = Tk()
    #root.geometry("440x160+845+20")
    app = FV()
    #app = FolderView(root)
    app.geometry("440x160+845+20")
    app.mainloop()
    #root.mainloop()


if __name__=='__main__':
    main()