import json
import shutil
import os
import time
from tkinter import *
import datetime

# tkFrame = tkinter.Frame(tela)
# tkFrame.pack()
# texto = tkinter.Label(tkFrame,text='ola mundo')
# texto.pack()
# tela.mainloop()

class ManagerFileExplorer:

    def Ler(self):
        path=input("Entre com o local do arquivo para Ler: ")
        file=open(path,"r")
        print(file.read())
        input('Pressione Enter...')
        file.close()

    def Escrever(self):
        path = input("Entre com o local do arquivo para escrever ou criar:")
        if os.path.isfile(path):
            print("Reconstruindo o arquivo existente")
        else:
            print("Criando novo arquivo")
            texto = input("Entre com o texto para o arquivo")
            file = open(path,"w")
            file.write(texto)

    def Adiciona(self):
        path=input("Entre com o local:")
        texto = input("Entre com o texto para Escrever: ")
        file=open(path,"a")
        file.write('\n'+texto)

    def Deletar(self):
        path=input("Entre com o local ou arquivo:")
        if os.path.exists(path):
            print("Arquivo Encontrado")
            os.remove(path)
            print("Arquivo foi deletado")
        else:
            print("Arquivo nao existe")

    def ListarDiretorio(self):
        path = "c:\PDF Files"
        # path=input("Entre com o Local do Diretorio para Listar: ")
        #sortlist=Files_json.sort(os.listdir(path))



        somatotal=0
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

        for root, dirs, files in os.walk(path):

            for file in files:

                pathname = os.path.join(root, file)
                getctime = os.path.getatime(pathname)
                getmtimee = os.path.getmtime(pathname)
                getatime = os.path.getatime(pathname)
                tictime = time.ctime(getmtimee)

                dtt = datetime.datetime.strptime(tictime, "%a %b %d %H:%M:%S %Y")
                ola = dtt.strftime('%d/%m/%Y')
                #teste = Files_json.sort(key=lambda x: os.path.getmtime(x))
               # print('getctime'+str(getctime))
                timestFile = datetime.date.fromtimestamp(getctime)
                timestToday = datetime.datetime.fromtimestamp(getctime)
                #print(timestFile.day)
                #print(datetime.date.today().day)
                #print(timestToday.hour)
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
                if timestFile.day == datetime.date.today().day:
                    somatotal += 1

                    #print('ola mundo')
                    if timestToday.hour == oito:
                        coito+=1
                    if timestToday.hour == nove:
                        cnove+=1
                    if timestToday.hour == dez:
                        cdez+=1
                    if timestToday.hour == onze:
                        conze+=1
                    if timestToday.hour == doze:
                        cdoze+=1
                    if timestToday.hour == treze:
                        ctreze+=1
                    if timestToday.hour == quartoze:
                        cquartoze+=1
                    if timestToday.hour == quinze:
                        cquinze+=1
                    if timestToday.hour == dezesseis:
                        cdezesseis+=1
                    if timestToday.hour == dezessete:
                        cdezessete+=1
                    if timestToday.hour == dezoito:
                        cdezoito+=1


                #contagem das horas




                #print(ola)
                #print(pathname)


            #print(root)
            #print(dirs)
            #print(Files_json)

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
        #i=0
        # while(i<len(sortlist)):
        #     info = os.path.getatime(sortlist[i])
        #     shorttime = time.ctime(info)
        #     #hour = datetime.datetime(shorttime)
        #     print(sortlist[i]+'\n')
        #     print(shorttime[i]+'\n')
        #     i+=1

    def Verifica(self):
        fp = int(input("Verificar a presença de um\n1.Arquivo\n2.Diretorio\n"))
        if fp==1:
            path = input("Etre com o local do arquivo")
            os.path.isfile(path)
            if os.path.isfile(path)==True:
                print("Arquivo Encontrado")
            else:
                print("Arquivo não encontrado")
        if fp==2:
            path=input("Entre com o local do Diretorio:")
            os.path.isdir(path)
            if os.path.isdir(path)==False:
                print("Diretorio Encontrado")
            else:
                print("Diretorio não encontrado")


    def Mover(self):
        path1=input("Entre com o local do arquivo para mover ou renomear")
        mr = int(input('1.Rename\n2.Mover\n'))
        if mr==1:
            path2 = input("Nome do Arquivo:")
            shutil.move(path1, path2)
            print("Arquivo Renomeado")
        if mr==2:
            path2=input("Entre com o local que deseja mover:")
            shutil.move(path1, path2)
            print("Arquivo movido")

    def Copiar(self):
        path1 = input('Entre com o nome do arquivo que deseja copiar ou renomear:')
        path2 = input('Entre com o local para copiar:')
        shutil.copy(path1, path2)
        print('Arquivo copiado')

    def ListarDiretorio(self):


        #path = "c:\PDF Files"
        #path=(r'\\scanserver\folder')
        path = "c:\PDF Files"
        path_track = "\Tracks"

        path_system = os.path.dirname(os.path.realpath(__file__))

        dirname_track = path_system+path_track
        print(dirname_track)
        # path = (r'\\scanserver\folder')
        # path=(r'\\scanserver\folder')
        # open(path, 'w+')
        # path=input("Entre com o Local do Diretorio para Listar: ")
        # sortlist=Files_json.sort(os.listdir(path))

        print("root")
        print()
        path_files = os.path.join(path_system, path_track)
        print(path_files)

        print(path)
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

        print("path", path)
        print(os.walk(path_system))

        for root, dirs, files in os.walk(dirname_track):
            print(root)
            print(dirs)
            print(files)


        for root, dirs, files in os.walk(path):


            #print("dir", dir)

            for file in files:

                pathname = os.path.join(root, file)
                print(pathname)
                getctime = os.path.getatime(pathname)
                getmtimee = os.path.getmtime(pathname)
                getatime = os.path.getatime(pathname)
                tictime = time.ctime(getmtimee)

                dtt = datetime.datetime.strptime(tictime, "%a %b %d %H:%M:%S %Y")
                ola = dtt.strftime('%d/%m/%Y')


                timestFile = datetime.date.fromtimestamp(getctime)
                timestToday = datetime.datetime.fromtimestamp(getctime)
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
                # vintetres = 23
                # vintequatro = 24

                if timestFile.day == datetime.date.today().day:
                    somatotal += 1
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
                'total': somatotal,
                '5': ccinco,
                '6': cseis,
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
            json_str = json.dumps(dict)
            print(json_str)

            # builditens = self.Update(dict)


            # print('8:00: ',dict['8'])
            # print('9:00: ', dict['9'])
            # if msg["text"] == "Mudar":
            #     msg["text"] ="Mudanca feita"

            # print(dict)

            return dict

    def ValidaDocs(self):
        path = "c:\PDF Files"
        #path = (r'\\scanserver\folder')

        # open(path, 'w+')
        # path=input("Entre com o Local do Diretorio para Listar: ")
        # sortlist=Files_json.sort(os.listdir(path))

        czeroum = 0
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

                dezessete = 1

                #print dos arquivos
                if timestFile.day == datetime.date.today().day:
                    if timestToday.minute == dezessete:
                        czeroum += 1
                        print(file)
                        print(timestToday)


            print("17:01: "+str(czeroum))







    def Criardir(self):
        path = input(
            "Entre com o nome do diretorio e o caminho para criar\neg. C:\\mundo\\NovoDiretorio \nOnde sera o novo diretorio:")
        os.makedirs(path)
        print('Diretorio Criado')


    def Removerdir(self):
        path = input('Entre com o local do diretorio:')
        treedir = int(input('1.Deletar o diretorio \n2.Deletar arvores de diretorios \n3.Sair \n'))
        if treedir == 1:
            os.rmdir(path)
        if treedir == 2:
            shutil.rmtree(path)
            print('Diretorio Deletado')
        if treedir == 3:
            exit()

    def criarDicionario(self):
        contato = {
            'Nome':'Douglas',
            'Sobrenome':'Mendes',
            'Apelido':'douglasm',
            'Celular':'90903333',
        }
        print(contato)
        for c in contato:
            print(c)


    def Abrirarquivo(self):
        path=input('Entre com o local:')
        try:
            os.startfile(path)
        except:
            print('Arquivo não encontrado')



# class Buttons:
#     def __init__(self, master):
#         manager = ManagerFileExplorer()
#         frame = Frame(master)
#         frame.pack()
#         bottomFrame = Frame(tela)
#         bottomFrame.pack(side=BOTTOM)
#         button1 = Button(frame, text="Atualizar", fg="green", command=manager.ListarDiretorio)
#         button2 = Button(bottomFrame, text="Button 1", fg="green")
#         button3 = Listbox(bottomFrame)
#         button1.pack()
#         button2.pack(side=LEFT)
#         button3.pack(side=RIGHT)


manager = ManagerFileExplorer()
#manager.ValidaDocs()
manager.criarDicionario()


#
# for i in range(1,100):
#     manager = ManagerFileExplorer()
#     time.sleep(3)
#
#     manager.ListarDiretorio()
#     print("   ")
#     print("   ")
#     print("   ")
#     print("   ")


#