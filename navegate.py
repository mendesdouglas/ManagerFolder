import tkinter as tk
from tkinter import ttk, Menu
from tkinter.ttk import Style
from tkinter import *
from configs import *



import json
import os
import time
import datetime


LARGE_FONT = ("Verdana", 14)
NORMAL_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)



    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)
        self.style = Style()
        self.style.theme_use("default")

        frame = ttk.Frame(self, relief=SUNKEN, borderwidth=1)
        frame.pack(fill="both", side=LEFT, expand=True)

        frame4 = ttk.Frame(self, relief=GROOVE, borderwidth=1)
        frame4.pack(fill=BOTH, side=LEFT, expand=True)

        frame5 = ttk.Frame(self, relief=GROOVE, borderwidth=1)
        frame5.pack(fill=BOTH, side=RIGHT, expand=True)

        self.total = ttk.Label(frame, text="TOTAL HOJE", font=SMALL_FONT)
        self.total.pack()
        self.pfino = ttk.Label(frame, text="PRONTUÁRIO FINO", font=SMALL_FONT)
        self.pfino.pack()
        self.pgrosso = ttk.Label(frame, text="PRONTUÁRIO GROSSO", font=SMALL_FONT)
        self.pgrosso.pack()

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
        self.StartItens()

        #self.createFiles()

    def ListarDiretorio(self):
        #path = "c:\PDF Files"
        path = PATH
        path_track = PATH_TRACK

        path_system = PATH_SYSTEM
        path_files = PATH_SYSTEM+PATH_TRACK
        #path = (r'\\scanserver\folder')
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
        cprontGrosso = 0
        cprontFino = 0

        # cvintetres = 0
        # cvintequatro = 0

        print("root")
        print()

        print(path_files)


        for root, dirs, files in os.walk(path):

            print(dir)

            for file in files:

                pathname = os.path.join(root, file)
                getctime = os.path.getatime(pathname)
                getmtimee = os.path.getmtime(pathname)
                getatime = os.path.getatime(pathname)
                getsize = os.path.getsize(pathname)
                tictime = time.ctime(getmtimee)

                dtt = datetime.datetime.strptime(tictime, "%a %b %d %H:%M:%S %Y")
                nomeArquivo = dtt.strftime('%Y-%m-%d')
                #contador = dtt.strftime("%H:%M:%S.%f")
                #print("contador",contador)

                timestFile = datetime.date.fromtimestamp(getctime)
                timestToday = datetime.datetime.fromtimestamp(getctime)
                print(nomeArquivo == timestToday.date())
                print("dtt", dtt)
                print(file)

                print(timestToday.date())
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

                ### VERIFICA A CONTAGEM DE PRONTUARIO GROSSO OU FINO
                #conta todas os documentos dentro do pdffiles, sem verificar a data atual
                # if getsize < 5000000:
                #     cprontFino += 1
                # else:
                #     cprontGrosso +=1


                ### VERIFICA A CONTAGEM DO DIA
                if timestFile.day == datetime.date.today().day:
                    somatotal += 1
                    #verifica a pasta atual e verifica se é abaixo de 5mb
                    if getsize < 5000000:
                        cprontFino += 1
                    else:
                        cprontGrosso += 1
                    if timestToday.hour == cinco:
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
                'pGrosso':cprontGrosso,
                'pFino':cprontFino,
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

            print("grosso")
            print(cprontGrosso)
            print("fino")
            print(cprontFino)

            if ((nomeArquivo == datetime.date.today().day) and (timestFile.day == datetime.date.today().day)):
                json_str = json.dumps(dict, nomeArquivo)
                self.createFiles(nomeArquivo, json_str)
                print(json_str)


            # builditens = self.Update(dict)


            # print('8:00: ',dict['8'])
            # print('9:00: ', dict['9'])
            # if msg["text"] == "Mudar":
            #     msg["text"] ="Mudanca feita"

            # print(dict)


            return dict



    def createFiles(self, nomeArquivo,dict):
        path_files = PATH_FILES
        file = "\\"+nomeArquivo+".json"
        files = path_files+file
        arquivo = open(files, 'w', encoding='utf-8')
        arquivo.write(dict)
        arquivo.close()
        print(arquivo)

    def StartItens(self):
        dict = self.ListarDiretorio()
        if dict != None:
            self.BuildLabel(dict)
            print("Estou no StartItens -> if")
            # time.sleep(4)
            # self.Transition(dict)

            # self.after_idle(3000,self.printTest(dict))
            # self.Transition(dict)


    def Reprint(self):
        self.LimpezarGeral()
        dict = self.ListarDiretorio()
        self.BuildLabel(dict)
        print("Estou no Reprint")
        self.after(1000, self.Reprint)



    def LimpezarGeral(self):


        self.total.pack_forget()
        self.pfino.pack_forget()
        self.pgrosso.pack_forget()
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


    def BuildLabel(self, dict):

        # totalLabel2 = ttk.Label(frame3, text="TARDE")
        # totalLabel2.pack(side=TOP)

        self.total.pack()
        self.pfino.pack()
        self.pgrosso.pack()
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
        self.pfino["text"] = "PRONTUÁRIO", "FINO", dict['pFino']
        self.pgrosso["text"] = "PRONTUÁRIO", "GROSSO", dict['pGrosso']
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



class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)

    def ValidaDocs(self):
        path = "c:\PDF Files"
        #path=(r'\\scanserver\folder')
        # open(path, 'w+')
        # path=input("Entre com o Local do Diretorio para Listar: ")
        # sortlist=Files_json.sort(os.listdir(path))


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
                #
                # if timestFile.day == datetime.date.today().day:
                #     somatotal += 1
                #     if timestToday.hour == ccinco:
                #         ccinco += 1
                #     if timestToday.hour == seis:
                #         cseis += 1
                #     if timestToday.hour == sete:
                #         csete += 1
                #     if timestToday.hour == oito:
                #         coito += 1
                #     if timestToday.hour == nove:
                #         cnove += 1
                #     if timestToday.hour == dez:
                #         cdez += 1
                #     if timestToday.hour == onze:
                #         conze += 1
                #     if timestToday.hour == doze:
                #         cdoze += 1
                #     if timestToday.hour == treze:
                #         ctreze += 1
                #     if timestToday.hour == quartoze:
                #         cquartoze += 1
                #     if timestToday.hour == quinze:
                #         cquinze += 1
                #     if timestToday.hour == dezesseis:
                #         cdezesseis += 1
                #     if timestToday.hour == dezessete:
                #         cdezessete += 1
                #     if timestToday.hour == dezoito:
                #         cdezoito += 1
                #     if timestToday.hour == dezenove:
                #         cdezenove += 1
                #     if timestToday.hour == vinte:
                #         cvinte += 1
                #     if timestToday.hour == vinteum:
                #         cvinteum = + 1
                #     if timestToday.hour == vintedois:
                #         cvintedois = + 1
                #     # if timestToday.hour == vintetres:
                #     #     cvintetres = + 1
                #     # if timestToday.hour == vintequatro:
                #     #     cvintequatro = + 1

            # dict = {
            #     'total': somatotal,
            #     '5':ccinco,
            #     '6':cseis,
            #     '7': csete,
            #     '8': coito,
            #     '9': cnove,
            #     '10': cdez,
            #     '11': conze,
            #     '12': cdoze,
            #     '13': ctreze,
            #     '14': cquartoze,
            #     '15': cquinze,
            #     '16': cdezesseis,
            #     '17': cdezessete,
            #     '18': cdezoito,
            #     '19': cdezenove,
            #     '20': cvinte,
            #     '21': cvinteum,
            #     '22': cvintedois,
            #     # '23': cvintetres,
            #     # '24': cvintequatro,
            # }

            # builditens = self.Update(dict)


            # print('8:00: ',dict['8'])
            # print('9:00: ', dict['9'])
            # if msg["text"] == "Mudar":
            #     msg["text"] ="Mudanca feita"

            # print(dict)

            return None






class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):

    def __init__(self, *args, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = ttk.Button(buttonframe, text="Geral", command=p1.lift)
        b2 = ttk.Button(buttonframe, text="Modo Pasta", command=p2.lift)
        b3 = ttk.Button(buttonframe, text="Buscar", command=p3.lift)

        self.contador = ttk.Label(buttonframe, text="CONTADOR", font=SMALL_FONT)
        self.contador.pack()

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="right")

        p1.show() #mostrado a função
        # p1.Reprint() #chamado automaticamente a função de listar pasta




    def defineHora(self):
        #hora = datetime.datetime.utcnow().strftime('%H:%M:%S.%f')
        hora = datetime.datetime.now().strftime('%H:%M:%S')
        print(hora)
        self.contador["text"] = hora

    def adicionaHora(self):
        self.defineHora()
        self.after(1, self.adicionaHora)

    def teste(self):
        print("teste efetuado")


if __name__ == "__main__":
    root = tk.Tk()
    p1 = Page1()
    p2 = Page2()
    mv = MainView()


    ##adicionar menu
    menubar = tk.Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Novo", command=p2.lift)
    menubar.add_cascade(label="Arquivo", menu=filemenu)


    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    #main.adicionaHora()
    root.wm_geometry("440x180+845+20")
    root.wm_title("Visualizador de Produção")
    root.config(menu=menubar)
    root.mainloop()