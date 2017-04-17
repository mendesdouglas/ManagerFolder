# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#import Interface.ProductionModeView
from PyQt4.QtGui import QMainWindow

from Interface import ProductionModeView

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):

        frame = QtGui.QFrame()
        pmv = ProductionModeView



        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(796, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, 60, 451, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lb_ttlSemanal = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_ttlSemanal.setObjectName(_fromUtf8("lb_ttlSemanal"))
        self.gridLayout.addWidget(self.lb_ttlSemanal, 5, 0, 1, 1)
        self.lb_metaDiaria = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_metaDiaria.setObjectName(_fromUtf8("lb_metaDiaria"))
        self.gridLayout.addWidget(self.lb_metaDiaria, 3, 0, 1, 1)
        self.lb_ttlMes = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_ttlMes.setObjectName(_fromUtf8("lb_ttlMes"))
        self.gridLayout.addWidget(self.lb_ttlMes, 6, 0, 1, 1)
        self.lb_metaMensal = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_metaMensal.setObjectName(_fromUtf8("lb_metaMensal"))
        self.gridLayout.addWidget(self.lb_metaMensal, 4, 0, 1, 1)
        self.lb_vl_metaDiaria = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_vl_metaDiaria.setObjectName(_fromUtf8("lb_vl_metaDiaria"))
        self.gridLayout.addWidget(self.lb_vl_metaDiaria, 3, 1, 1, 1)
        self.lb_vl_metaMensal = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_vl_metaMensal.setObjectName(_fromUtf8("lb_vl_metaMensal"))
        self.gridLayout.addWidget(self.lb_vl_metaMensal, 4, 1, 1, 1)
        self.lb_vl_ttlSemanal = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_vl_ttlSemanal.setObjectName(_fromUtf8("lb_vl_ttlSemanal"))
        self.gridLayout.addWidget(self.lb_vl_ttlSemanal, 5, 1, 1, 1)
        self.lb_vl_ttlMes = QtGui.QLabel(self.gridLayoutWidget)
        self.lb_vl_ttlMes.setObjectName(_fromUtf8("lb_vl_ttlMes"))
        self.gridLayout.addWidget(self.lb_vl_ttlMes, 6, 1, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 10, 451, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.clicked.connect(lambda: pmv.run_pmv())
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPrograma = QtGui.QMenu(self.menubar)
        self.menuPrograma.setObjectName(_fromUtf8("menuPrograma"))
        self.menuExibir = QtGui.QMenu(self.menubar)
        self.menuExibir.setObjectName(_fromUtf8("menuExibir"))
        self.menuGerar = QtGui.QMenu(self.menubar)
        self.menuGerar.setObjectName(_fromUtf8("menuGerar"))
        self.menuBuscar = QtGui.QMenu(self.menubar)
        self.menuBuscar.setObjectName(_fromUtf8("menuBuscar"))
        self.menuConfigura_es = QtGui.QMenu(self.menubar)
        self.menuConfigura_es.setObjectName(_fromUtf8("menuConfigura_es"))
        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName(_fromUtf8("menuAjuda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionModo_Geral = QtGui.QAction(MainWindow)
        self.actionModo_Geral.setObjectName(_fromUtf8("actionModo_Geral"))
        self.actionModo_Pasta = QtGui.QAction(MainWindow)
        self.actionModo_Pasta.setObjectName(_fromUtf8("actionModo_Pasta"))
        self.actionModo_Detalhe = QtGui.QAction(MainWindow)
        self.actionModo_Detalhe.setObjectName(_fromUtf8("actionModo_Detalhe"))
        self.actionPDF = QtGui.QAction(MainWindow)
        self.actionPDF.setObjectName(_fromUtf8("actionPDF"))
        self.actionBuscar_Produ_o = QtGui.QAction(MainWindow)
        self.actionBuscar_Produ_o.setObjectName(_fromUtf8("actionBuscar_Produ_o"))
        self.actionRelat_rios = QtGui.QAction(MainWindow)
        self.actionRelat_rios.setObjectName(_fromUtf8("actionRelat_rios"))
        self.actionGerais = QtGui.QAction(MainWindow)
        self.actionGerais.setObjectName(_fromUtf8("actionGerais"))
        self.actionDesenvolvimento = QtGui.QAction(MainWindow)
        self.actionDesenvolvimento.setObjectName(_fromUtf8("actionDesenvolvimento"))
        self.actionVers_o_do_Software = QtGui.QAction(MainWindow)
        self.actionVers_o_do_Software.setObjectName(_fromUtf8("actionVers_o_do_Software"))
        self.actionUsu_rios = QtGui.QAction(MainWindow)
        self.actionUsu_rios.setObjectName(_fromUtf8("actionUsu_rios"))
        self.menuPrograma.addAction(self.actionUsu_rios)
        self.menuExibir.addAction(self.actionModo_Geral)
        self.menuExibir.addAction(self.actionModo_Pasta)
        self.menuExibir.addAction(self.actionModo_Detalhe)
        self.menuGerar.addAction(self.actionPDF)
        self.menuGerar.addSeparator()
        self.menuGerar.addAction(self.actionRelat_rios)
        self.menuBuscar.addAction(self.actionBuscar_Produ_o)
        self.menuConfigura_es.addAction(self.actionGerais)
        self.menuAjuda.addAction(self.actionDesenvolvimento)
        self.menuAjuda.addAction(self.actionVers_o_do_Software)
        self.menubar.addAction(self.menuPrograma.menuAction())
        self.menubar.addAction(self.menuExibir.menuAction())
        self.menubar.addAction(self.menuGerar.menuAction())
        self.menubar.addAction(self.menuBuscar.menuAction())
        self.menubar.addAction(self.menuConfigura_es.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lb_ttlSemanal.setText(_translate("MainWindow", "Total Semanal", None))
        self.lb_metaDiaria.setText(_translate("MainWindow", "Meta Diária:", None))
        self.lb_ttlMes.setText(_translate("MainWindow", "Total Mês", None))
        self.lb_metaMensal.setText(_translate("MainWindow", "Meta Mensal", None))
        self.lb_vl_metaDiaria.setText(_translate("MainWindow", "850", None))
        self.lb_vl_metaMensal.setText(_translate("MainWindow", "15000", None))
        self.lb_vl_ttlSemanal.setText(_translate("MainWindow", "2000", None))
        self.lb_vl_ttlMes.setText(_translate("MainWindow", "8000", None))
        self.pushButton.setText(_translate("MainWindow", "Modo Produção", None))
        self.pushButton_2.setText(_translate("MainWindow", "Modo Pasta", None))
        self.menuPrograma.setTitle(_translate("MainWindow", "Programa", None))
        self.menuExibir.setTitle(_translate("MainWindow", "Exibir", None))
        self.menuGerar.setTitle(_translate("MainWindow", "Gerar", None))
        self.menuBuscar.setTitle(_translate("MainWindow", "Buscar", None))
        self.menuConfigura_es.setTitle(_translate("MainWindow", "Configurações", None))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda", None))
        self.actionModo_Geral.setText(_translate("MainWindow", "Modo Geral", None))
        self.actionModo_Pasta.setText(_translate("MainWindow", "Modo Pasta", None))
        self.actionModo_Detalhe.setText(_translate("MainWindow", "Modo Detalhe", None))
        self.actionPDF.setText(_translate("MainWindow", "PDF", None))
        self.actionBuscar_Produ_o.setText(_translate("MainWindow", "Buscar Produção", None))
        self.actionRelat_rios.setText(_translate("MainWindow", "Relatórios", None))
        self.actionGerais.setText(_translate("MainWindow", "Gerais", None))
        self.actionDesenvolvimento.setText(_translate("MainWindow", "Desenvolvimento", None))
        self.actionVers_o_do_Software.setText(_translate("MainWindow", "Versão do Software", None))
        self.actionUsu_rios.setText(_translate("MainWindow", "Mês", None))


    def call_ProductionModelView(self, frame):
        app = QtGui.QApplication(sys.argv)
        Frame = QtGui.QFrame()
        pmv = ProductionModeView.Ui_Frame()
        pmv.setupUi(Frame)
        Frame.showMaximized()







if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

