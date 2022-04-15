from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep

setWorkTime = 0
setInterval = 0
op = 0

class intervalCounter(QObject):
    finished = pyqtSignal()
    # progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        global setWorkTime, setInterval, op;
        for i in range(setWorkTime):
            sleep(1)
            print(f'Counter: {i}')
            # self.progress.emit(i + 1)
        print('finished taks')
        self.finished.emit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        MainWindow.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(20, 340, 125, 35))
        self.startButton.setMinimumSize(QtCore.QSize(125, 35))
        self.startButton.setMaximumSize(QtCore.QSize(125, 35))
        self.startButton.setStyleSheet("border: 0;\n"
"background-color: rgb(62, 100, 254);\n"
"color: #fff;")
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(False)
        self.startButton.setFlat(False)
        self.startButton.setObjectName("startButton")
        self.finishButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishButton.setGeometry(QtCore.QRect(150, 340, 125, 35))
        self.finishButton.setMinimumSize(QtCore.QSize(125, 35))
        self.finishButton.setMaximumSize(QtCore.QSize(125, 35))
        self.finishButton.setStyleSheet("border: 0;\n"
"background-color: rgb(62, 100, 254);\n"
"color: #fff;")
        self.finishButton.setAutoDefault(False)
        self.finishButton.setDefault(False)
        self.finishButton.setFlat(False)
        self.finishButton.setObjectName("finishButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 300, 251, 21))
        self.progressBar.setStatusTip("")
        self.progressBar.setStyleSheet("border: 0;\n"
"background-color: #cecfcf;\n"
"text-align: center;\n"
"color: #fff;")
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.worTime = QtWidgets.QLineEdit(self.centralwidget)
        self.worTime.setGeometry(QtCore.QRect(20, 100, 261, 31))
        self.worTime.setStyleSheet("background-color: #cecfcf;\n"
"border-color: rgb(99, 99, 99);\n"
"color: #3e64fe;\n"
"border-radius: 0;")
        self.worTime.setText("")
        self.worTime.setObjectName("worTime")
        self.intervalTime = QtWidgets.QLineEdit(self.centralwidget)
        self.intervalTime.setGeometry(QtCore.QRect(20, 190, 261, 31))
        self.intervalTime.setStyleSheet("background-color: #cecfcf;\n"
"border-color: rgb(99, 99, 99);\n"
"color: #3e64fe;\n"
"border-radius: 0;")
        self.intervalTime.setText("")
        self.intervalTime.setObjectName("intervalTime")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #3e64fe;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #3e64fe;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.finishButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startButton.clicked.connect(self.startWorkCycle)

    def startWorkCycle(self):
        global setWorkTime, setInterval, op;
        setWorkTime = int(self.worTime.text())
        setInterval = int(self.intervalTime.text())
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a intervalCounter object
        self.intervalCounter = intervalCounter()
        # Step 4: Move intervalCounter to the thread
        self.intervalCounter.moveToThread(self.thread)

        # Step 5: Connect signals and slots
        self.thread.started.connect(self.intervalCounter.run)

        # Step 6: Finish thread when recive signal for finish
        self.intervalCounter.finished.connect(self.thread.quit)

        # Step 7: Delete work and objects
        self.intervalCounter.finished.connect(self.intervalCounter.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # self.intervalCounter.progress.connect(self.reportProgress)

        # Step 8: Start the thread
        self.thread.start()

        # Final resets
        # self.longRunningBtn.setEnabled(False)
        # self.thread.finished.connect(
        #     lambda: self.longRunningBtn.setEnabled(True)
        # )
        # self.thread.finished.connect(
        #     lambda: self.stepLabel.setText("Long-Running Step: 0")
        # )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.finishButton.setText(_translate("MainWindow", "Finish"))
        self.label.setText(_translate("MainWindow", "Tempo de Trabalho"))
        self.label_2.setText(_translate("MainWindow", "Tempo de Intervalo"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())