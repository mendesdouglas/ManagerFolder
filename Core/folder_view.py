import json
import os
import time
import datetime
import configs


class Folders:
    def __init__(self):
        self.listDirectory()


    def listDirectory(self):
        #BUSCANDO DA PASTA CONFIG
        path = configs.PATH
        path_track = configs.PATH_TRACK
        path_system = configs.PATH_SYSTEM
        # path = (r'\\scanserver\folder')
        # path=(r'\\scanserver\folder')
        # open(path, 'w+')
        # path=input("Entre com o Local do Diretorio para Listar: ")
        # sortlist=Files_json.sort(os.listdir(path))

        # cvintetres = 0
        # cvintequatro = 0

        print("root")
        print()
        path_files = configs.PATH_FILES
        print(path_files)

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
                ola = dtt.strftime('%Y-%m-%d')

                timestFile = datetime.date.fromtimestamp(getctime)
                timestToday = datetime.datetime.fromtimestamp(getctime)
                print(ola == timestToday.date())
                print(getsize)
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
                # vintetres = 23
                # vintequatro = 24

                ### VERIFICA A CONTAGEM DE PRONTUARIO GROSSO OU FINO
                # conta todas os documentos dentro do pdffiles, sem verificar a data atual
                # if getsize < 5000000:
                #     cprontFino += 1
                # else:
                #     cprontGrosso +=1
                ### VERIFICA A CONTAGEM DO DIA
                if timestFile.day == datetime.date.today().day:
                    somatotal += 1
                    # verifica a pasta atual e verifica se é abaixo de 5mb
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
            'pGrosso': cprontGrosso,
            'pFino': cprontFino,
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

        return dict














