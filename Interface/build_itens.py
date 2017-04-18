from PyQt4 import QtGui

class MultiWindows(QtGui.QMainWindow):
    windowList = []

    def __init__(self, param):
        raise NotImplementedError()

    def addwindow(self, param):
        win = QtGui.MainWindow(param) # How to call the initializer of the subclass from here?
        self.windowList.append(win)

class PlanetApp(MultiWindows):
    def __init__(self, planet):
        pass

class AnimalApp(MultiWindows):
    def __init__(self, planet):
        pass

if __name__=="__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    app.exec_()