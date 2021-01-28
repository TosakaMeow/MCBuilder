# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import createCommand
import keyboardOutput

class deploy(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Minecraft方块部署小工具 Beta V1.0")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startPoint = QtWidgets.QLabel(self.centralwidget)
        self.startPoint.setGeometry(QtCore.QRect(30, 50, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.startPoint.setFont(font)
        self.startPoint.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint.setObjectName("startPoint")
        self.sx = QtWidgets.QTextEdit(self.centralwidget)
        self.sx.setGeometry(QtCore.QRect(160, 50, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sx.setFont(font)
        self.sx.setObjectName("sx")
        self.sy = QtWidgets.QTextEdit(self.centralwidget)
        self.sy.setGeometry(QtCore.QRect(250, 50, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sy.setFont(font)
        self.sy.setObjectName("sy")
        self.sz = QtWidgets.QTextEdit(self.centralwidget)
        self.sz.setGeometry(QtCore.QRect(340, 50, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sz.setFont(font)
        self.sz.setObjectName("sz")
        self.startPoint_3 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_3.setGeometry(QtCore.QRect(180, 10, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.startPoint_3.setFont(font)
        self.startPoint_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_3.setObjectName("startPoint_3")
        self.startPoint_4 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_4.setGeometry(QtCore.QRect(270, 10, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.startPoint_4.setFont(font)
        self.startPoint_4.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_4.setObjectName("startPoint_4")
        self.startPoint_5 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_5.setGeometry(QtCore.QRect(360, 10, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.startPoint_5.setFont(font)
        self.startPoint_5.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_5.setObjectName("startPoint_5")
        self.startPoint_2 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_2.setGeometry(QtCore.QRect(530, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.startPoint_2.setFont(font)
        self.startPoint_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_2.setObjectName("startPoint_2")
        self.source = QtWidgets.QComboBox(self.centralwidget)
        self.source.setGeometry(QtCore.QRect(510, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.source.setFont(font)
        self.source.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.source.addItem("")
        self.source.addItem("")
        self.source.addItem("")
        self.startPoint_6 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_6.setGeometry(QtCore.QRect(360, 120, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.startPoint_6.setFont(font)
        self.startPoint_6.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_6.setObjectName("startPoint_6")
        self.ey = QtWidgets.QTextEdit(self.centralwidget)
        self.ey.setGeometry(QtCore.QRect(250, 160, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ey.setFont(font)
        self.ey.setObjectName("ey")
        self.ez = QtWidgets.QTextEdit(self.centralwidget)
        self.ez.setGeometry(QtCore.QRect(340, 160, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ez.setFont(font)
        self.ez.setObjectName("ez")
        self.endPoint = QtWidgets.QLabel(self.centralwidget)
        self.endPoint.setGeometry(QtCore.QRect(30, 160, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.endPoint.setFont(font)
        self.endPoint.setTextFormat(QtCore.Qt.MarkdownText)
        self.endPoint.setObjectName("endPoint")
        self.ex = QtWidgets.QTextEdit(self.centralwidget)
        self.ex.setGeometry(QtCore.QRect(160, 160, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ex.setFont(font)
        self.ex.setObjectName("ex")
        self.startPoint_8 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_8.setGeometry(QtCore.QRect(180, 120, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.startPoint_8.setFont(font)
        self.startPoint_8.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_8.setObjectName("startPoint_8")
        self.startPoint_9 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_9.setGeometry(QtCore.QRect(270, 120, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.startPoint_9.setFont(font)
        self.startPoint_9.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_9.setObjectName("startPoint_9")
        self.deploy = QtWidgets.QPushButton(self.centralwidget)
        self.deploy.setGeometry(QtCore.QRect(110, 290, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.deploy.setFont(font)
        self.deploy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deploy.setObjectName("deploy")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(440, 250, 341, 192))
        self.log.setObjectName("log")
        self.startPoint_10 = QtWidgets.QLabel(self.centralwidget)
        self.startPoint_10.setGeometry(QtCore.QRect(500, 190, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.startPoint_10.setFont(font)
        self.startPoint_10.setTextFormat(QtCore.Qt.MarkdownText)
        self.startPoint_10.setObjectName("startPoint_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.deploy.clicked.connect(MainWindow.test)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startPoint.setText(_translate("MainWindow", "起始坐标："))
        self.startPoint_3.setText(_translate("MainWindow", "X"))
        self.startPoint_4.setText(_translate("MainWindow", "Y"))
        self.startPoint_5.setText(_translate("MainWindow", "Z"))
        self.startPoint_2.setText(_translate("MainWindow", "选择材质："))
        self.source.setItemText(0, _translate("MainWindow", "石头"))
        self.source.setItemText(1, _translate("MainWindow", "萤石"))
        self.source.setItemText(2, _translate("MainWindow", "丛林木"))
        self.source.setItemText(3, _translate("MainWindow", "原石"))
        self.startPoint_6.setText(_translate("MainWindow", "Z"))
        self.endPoint.setText(_translate("MainWindow", "结束坐标："))
        self.startPoint_8.setText(_translate("MainWindow", "X"))
        self.startPoint_9.setText(_translate("MainWindow", "Y"))
        self.deploy.setText(_translate("MainWindow", "准备部署"))
        self.startPoint_10.setText(_translate("MainWindow", "命令执行日志："))


    def test(self):
        sx = self.sx.toPlainText()
        sy = self.sy.toPlainText()
        sz = self.sz.toPlainText()
        ex = self.ex.toPlainText()
        ey = self.ey.toPlainText()
        ez = self.ez.toPlainText()

        source = self.source.currentText()
        source = createCommand.translate(str(source))
        source = str(source)

        cmd = "/fill " + sx + " " + sy + " " + sz + " " + ex + " " + ey + " " + ez + " minecraft:" + source.lower()
        self.log.setText(cmd)
        keyboardOutput.main(cmd)

