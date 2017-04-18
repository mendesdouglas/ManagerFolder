import sys
from PyQt4 import QtGui, QtCore

##EXECUTANDO APARTIR DO PYQT E DEIXANDO DE LADO O TKINTER

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(796,600)
        self.setWindowTitle("Gerenciador de Produção")

        #criando um wid principal
        self.mainwidget = QtGui.QWidget(self)

        #criando um gridLayout Wid
        self.gridLayoutWid = QtGui.QWidget(self.mainwidget)
        self.gridLayoutWid.setGeometry(QtCore.QRect(-1,60,451,221)) #criando grid lay

        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWid)

        self.lb_ttlSemanal = QtGui.QLabel(self.gridLayoutWid)
        self.lb_ttlSemanal.setText("Label")

        # extractAction = QtGui.QAction("&Sair", self)
        # extractAction.setShortcut("Ctrl+Q")
        # extractAction.setStatusTip('Sair do Programa')
        # extractAction.triggered.connect(self.close_app)

        # self.statusBar()
        # mainMenu = self.menuBar()
        # progMenu = mainMenu.addMenu('&Programa')
        # progMenu.addAction(extractAction)




        self.overView()

    def overView(self):
        # btn = QtGui.QPushButton("Quit", self)
        # btn.clicked.connect(self.close_app)
        # btn.resize(btn.minimumSizeHint())
        #
        # extractAct = QtGui.QAction(QtGui.QIcon('img.png'), "Flee the scene",self)
        # extractAct.triggered.connect(self.close_app)
        #
        # self.toolBar =self.addToolBar("extracao")
        # self.toolBar.addAction(extractAct)

        #btn.move(100,100)
        self.show()

    def close_app(self):
        sys.exit()







def run():
        app = QtGui.QApplication(sys.argv)
        GUI = Window()
        sys.exit(app.exec_())

run()

