# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        canvas = QtGui.QPixmap(MainWindow.frameGeometry().width(), MainWindow.frameGeometry().height())
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        #self.drawrect([200, 285], [4, 2])
       # MainWindow.resize(size[0], size[1])
       # self.page = page
        #self.paper = paper
        #self.landscape = landscape
        #self.drawrect([page[0], page[1]], [paper[0], paper[1]])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))

    def __init__(self,  size, page, paper, monofyllo):
        MainWindow.resize(size[0], size[1])
        self.page = page
        self.paper = paper
        self.monofyllo = monofyllo
        self.setupUi(MainWindow)
        self.drawrect([page[0], page[1]], [paper[0], paper[1], paper[2]], True)


    def drawrect(self, page, paper, monofyllo):
        #x = int (MainWindow.geometry().width()*0.6)
       # y = int (MainWindow.geometry().height()*0.6)
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor("#EB5160"))
        painter.setPen(pen)
        #z =
        if monofyllo:
            if paper[2] == 0:
                hgap = (MainWindow.geometry().width() - page[0] * paper[0]) // ((paper[0]) + 1)
                vgap = (MainWindow.geometry().height() - page[1] * paper[1]) // (paper[1] + 1)
                #for p in range(0, paper[0]):

            else:
                hgap = (MainWindow.geometry().width() - page[0]*paper[1])//((paper[1]) + 1)
                vgap = (MainWindow.geometry().height() - page[1] * paper[0]) // (paper[0] + 1)
        else:
            if paper[2] == 0:
                hgap = (MainWindow.geometry().width() - page[0]*paper[0]*2 )//((paper[0] *2) - 1)
                #print(MainWindow.geometry().width())
                #vgap = (MainWindow.geometry().height() - page[1]*paper[1])//3

                for p in range(0,paper[0] * 2):
                    vgap = (MainWindow.geometry().height() - page[1] * paper[1]) // (paper[1] + 1)
                    print(page[1] * paper[1])
                    #hgap += hgap
                    for m in range(0,paper[1]):
                        painter.drawRect(int(hgap), int(vgap), int(page[0]), int(page[1]))
                        vgap += vgap + page[1]
                        #vgap = ((MainWindow.geometry().height() - page[1] * 0.6 * paper[1]) // 3) + page[1] * 0.6
                    if ((p+1) % 2 == 0):
                        hgap += (MainWindow.geometry().width() - page[0]*paper[0]*2)//(paper[0] + 1)
                        print(hgap)
                    hgap += page[0]
                    print(hgap)
                    #painter.drawRect(10, 70, 100, 60)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow([1000, 700], [230, 330], [2, 2, 0], True)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
