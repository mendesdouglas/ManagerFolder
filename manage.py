
import tkinter as tk
from tkinter import ttk
import shutil
import os
import time
import datetime

# import matplotlib
# matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2TkAgg #serve para oferecer as opções de navegacao e para o canvas do grafico
#from matplotlib.figure import Figure

LARGE_FONT = ("Verdana", 14)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Copyvic - Gerenciamento de Documentos")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for framess in (StartPage, PageOne, PageTwo, PageThree):
            frame = framess(container,self)
            self.frames[framess] = frame
            frame.grid(row=0, column=0, sticky="nsew")



        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    #inicialization of page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame2 = tk.Frame.__init(self, parent)

        label = ttk.Label(self,text="Pagina Inicial", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        ## botoes
        button1 = ttk.Button(self, text="Pagina Um", command=lambda : controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Pagina Dois", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Pagina Tres", command=lambda: controller.show_frame(PageThree))
        button3.pack()

    def ListarDiretorio(self):
        path = "c:\PDF Files"

        somatotal=0
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
        cvintetres = 0
        cvintequatro = 0

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
                vintetres = 23
                vintequatro = 24

                if timestFile.day == datetime.date.today().day:
                    somatotal += 1
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


            dict = {'8:00':str(coito)}
            print(dict)

            print("TOTAL HOJE "+str(somatotal)+" Nesta Pasta")
            print("TOTAL 8:00 "+str(coito)+" Nesta Pasta")
            print("TOTAL 9:00 "+str(cnove)+" Nesta Pasta")
            print("TOTAL 10:00 "+str(cdez)+" Nesta Pasta")
            print("TOTAL 11:00 "+str(conze)+" Nesta Pasta")
            print("TOTAL 12:00 "+str(cdoze)+" Nesta Pasta")
            print("TOTAL 13:00 "+str(ctreze)+" Nesta Pasta")
            print("TOTAL 14:00 "+str(cquartoze)+" Nesta Pasta")
            print("TOTAL 15:00 "+str(cquinze)+" Nesta Pasta")
            print("TOTAL 16:00 "+str(cdezesseis)+" Nesta Pasta")
            print("TOTAL 17:00 "+str(cdezessete)+" Nesta Pasta")
            print("TOTAL 18:00 "+str(cdezoito)+" Nesta Pasta")

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Pagina Um", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button1 = ttk.Button(self, text="Pagina Dois", command=lambda: controller.show_frame(PageTwo))
        button1.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Pagina Dois", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Voltar Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Voltar Um", command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Pagina do Grafico", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Voltar Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = SeaofBTCapp()
app.mainloop()