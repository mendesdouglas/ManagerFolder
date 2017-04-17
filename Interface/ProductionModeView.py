# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductionModeView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


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

class Ui_Frame(QtGui.QWidget):
    def setupUi(self, Frame):
        print("estou no pmv ui frame")
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(605, 210)
        Frame.move(500,500)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayoutWidget = QtGui.QWidget(Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 139, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.list_productionView = QtGui.QListWidget(Frame)
        self.list_productionView.setGeometry(QtCore.QRect(140, 30, 171, 161))
        self.list_productionView.setObjectName(_fromUtf8("list_productionView"))
        item = QtGui.QListWidgetItem()
        self.list_productionView.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_productionView.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_productionView.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_productionView.addItem(item)
        self.vSB_listProduction = QtGui.QScrollBar(Frame)
        self.vSB_listProduction.setGeometry(QtCore.QRect(310, 30, 16, 160))
        self.vSB_listProduction.setOrientation(QtCore.Qt.Vertical)
        self.vSB_listProduction.setObjectName(_fromUtf8("vSB_listProduction"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(Frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 141, 81))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(150, 0, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(90, 0, 61, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.graphicsView = QtGui.QGraphicsView(Frame)
        self.graphicsView.setGeometry(QtCore.QRect(340, 30, 256, 161))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayoutWidget.raise_()
        self.list_productionView.raise_()
        self.vSB_listProduction.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.graphicsView.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.pushButton.setText(_translate("Frame", "Limpar ScanPro", None))
        self.pushButton_2.setText(_translate("Frame", "Gerar Produção", None))
        self.checkBox.setText(_translate("Frame", "Visualização Automático", None))
        __sortingEnabled = self.list_productionView.isSortingEnabled()
        self.list_productionView.setSortingEnabled(False)
        item = self.list_productionView.item(0)
        item.setText(_translate("Frame", "05:00 = 100", None))
        item = self.list_productionView.item(1)
        item.setText(_translate("Frame", "06:00 = 50", None))
        item = self.list_productionView.item(2)
        item.setText(_translate("Frame", "07:00 = 80", None))
        item = self.list_productionView.item(3)
        item.setText(_translate("Frame", "08:00 = 90", None))
        self.list_productionView.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("Frame", "Usuário", None))
        self.label_6.setText(_translate("Frame", "Data:", None))
        self.label_7.setText(_translate("Frame", "Dia", None))
        self.label.setText(_translate("Frame", "Total Geral: 500", None))
        self.label_2.setText(_translate("Frame", "17:00:00", None))
        self.label_3.setText(_translate("Frame", "PF: 400", None))
        self.label_4.setText(_translate("Frame", "PG: 100", None))

def run_pmv():

        import sys
        app = QtGui.QApplication(sys.argv)
        Frame = QtGui.QFrame()
        ui = Ui_Frame()
        ui.setupUi(Frame)
        Frame.show()
        #sys.exit(app.exec_())
run_pmv()
