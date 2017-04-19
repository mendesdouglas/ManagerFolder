import sys
from PyQt4 import QtGui, QtCore

##EXECUTANDO APARTIR DO PYQT E DEIXANDO DE LADO O TKINTER

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(796, 600)
        self.setWindowTitle("Gerenciador de Produção")

        self.centralWidget = QtGui.QWidget(self)
        self.centralWidget.setObjectName("centralwidget")
        # inicializando
        frame = QtGui.QFrame()
        pmv = ProductionModelView(frame)

        action_programa = QtGui.QAction("&Sair", self.centralWidget)
        action_programa.setShortcut("Ctrl+Q")
        action_programa.triggered.connect(pmv.productionView)






        self.statusBar()

        self.statusBar()
        mainMenu = self.menuBar()
        progMenu = mainMenu.addMenu('&Programa')
        progMenu.addAction(action_programa)




        #criando um wid principal



        # extractAction = QtGui.QAction("&Sair", self)
        # extractAction.setShortcut("Ctrl+Q")
        # extractAction.setStatusTip('Sair do Programa')
        # extractAction.triggered.connect(self.close_app)

        # self.statusBar()
        # mainMenu = self.menuBar()
        # progMenu = mainMenu.addMenu('&Programa')
        # progMenu.addAction(extractAction)
        self.mainGrid = QtGui.QGridLayout()



        self.overView()

    def overView(self):

        self.gridLay = QtGui.QWidget(self.centralWidget)
        self.gridLay.move(500,500)
        label1 = QtGui.QLabel(self.gridLay)
        label1.setText("Q444h")


       # btn = QtGui.QPushButton("Quit", self)

        # label = QtGui.QLabel(self.mainGrid)
        # label.setText("Qeheh")
        #self.mainGrid.addWidget(label)



        #btn.move(100,100)
        self.show()

    def close_app(self):
        sys.exit()

class ProductionModelView(QtGui.QFrame):
    def __init__(self):
        super(ProductionModelView, self).__init__()
        self.resize(796, 600)
        self.setWindowTitle("Gerenciador de Produção")

        self.centralWidget = QtGui.QWidget(self)
        self.centralWidget.setObjectName("centralwidget")

        action_programa = QtGui.QAction("&Sair", self.centralWidget)
        action_programa.setShortcut("Ctrl+Q")







    def productionView(self):
        print("estou passando")

        self.gridLay = QtGui.QWidget(self.centralWidget)
        self.gridLay.move(500,500)
        label1 = QtGui.QLabel(self.gridLay)
        label1.setText("Q444h")


        btn = QtGui.QPushButton("Quit",self.gridLay)

        # label = QtGui.QLabel(self.mainGrid)
        # label.setText("Qeheh")
        #self.mainGrid.addWidget(label)



        #btn.move(100,100)
        self.show()











def run():
        app = QtGui.QApplication(sys.argv)
        GUI = Window()
        sys.exit(app.exec_())

run()

