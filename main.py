# coding: utf8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from time import sleep
from os.path import exists
from gtts import gTTS
from playsound import playsound

setInterval = 0
op = 0
execStatus = 0
text = ''
sleepTime = 0
audioBreak='docs/coffe-break.mp3'
audioWork='docs/return-to-job.mp3'
_lang='en-us'

def createAudio(fileName, _text):
    sp = gTTS(
        text=_text,
        lang=_lang
    )
    sp.save(fileName)

if not exists(audioBreak):
    createAudio(audioBreak, 'Make a coffe break')

if not exists(audioWork):
    createAudio(audioWork, 'Return to job')

class run_longTask(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    intervalFinished = pyqtSignal()

    def setIntervalCounter(self):
        global setInterval;

        time = int(self.getConfigVariables(prop='sleep'))

        for i in range(1, setInterval+1):
            sleep(time)
            self.progress.emit(i)
        self.intervalFinished.emit()
        self.showMessageBox()

    def showMessageBox(self):
        global execStatus, text;

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Success")
        msg.setText(text)
        msg.setMinimumWidth(350)
        msg.addButton('Encerrar execução', QMessageBox.YesRole)
        msg.addButton(QMessageBox.Ok)

        bttn = msg.exec_()

        if bttn == QMessageBox.Ok:
            execStatus = 0
            self.setIntervalCounter()
        else:
            self.finished.emit()
            execStatus = 1

    def getConfigVariables(self, prop):
        try:
            with open('docs/conf.txt', 'r') as config_file:
                for i in config_file:
                    val = i.split()
                    if val[0] == prop:
                        return val[1]
                config_file.close()
        except:
            print('except')

class Ui_MainWindow(object):

    def run(self, MainWindow):
        global sleepTime
        try:
            with open('docs/conf.txt', 'r') as ref_file:
                ref_file.close()
        except:
            with open('docs/conf.txt', 'w+') as ref_file:
                ref_file.writelines('lang en_US\n'
                                    'sleep 60')
                ref_file.close()
        finally:
            self.setupUi(MainWindow)

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
        self.progressBar.setStyleSheet("QProgressBar {\n"
            "    background-color: #cecfcf;\n"
            "    text-align: center;\n"
            "    color: #fff;\n"
            "    border: none;\n"
            "    border-radius: none;\n"
            "    font-size: 14px;\n"
            "}\n"
            "QProgressBar::chunk {\n"
            "    border-radius: none;\n"
            "    border: none;\n"
            "    background-color: rgb(62, 100, 254);\n"
            "}")
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.workTime = QtWidgets.QLineEdit(self.centralwidget)
        self.workTime.setGeometry(QtCore.QRect(20, 100, 261, 31))
        self.workTime.setStyleSheet("background-color: #cecfcf;\n"
            "border-color: rgb(99, 99, 99);\n"
            "color: #000;\n"
            "border-radius: 0;")
        self.workTime.setText("")
        self.workTime.setObjectName("workTime")
        self.intervalTime = QtWidgets.QLineEdit(self.centralwidget)
        self.intervalTime.setGeometry(QtCore.QRect(20, 190, 261, 31))
        self.intervalTime.setStyleSheet("background-color: #cecfcf;\n"
            "border-color: rgb(99, 99, 99);\n"
            "color: #000;\n"
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
        global setInterval, text;

        try:
            setInterval = int(self.workTime.text())
            text = self.finishWorkTime
            self.startFirstThread()
        except:
            print('não utilizar valor nulo')


    def reportProgress(self, n):
        global setInterval
        progress = (float(n) / float(setInterval)) * 100
        self.progressBar.setValue(int(progress))


    def startFirstThread(self):
        global execStatus;

        self.thread = QThread()
        self.run_longTask = run_longTask()
        self.run_longTask.moveToThread(self.thread)
        self.thread.started.connect(self.run_longTask.setIntervalCounter)
        self.run_longTask.finished.connect(self.thread.quit)
        self.run_longTask.finished.connect(self.run_longTask.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.run_longTask.progress.connect(self.reportProgress)
        self.thread.start()

        self.run_longTask.intervalFinished.connect(self.changeOperation)

        self.disableTemplate()
        self.run_longTask.finished.connect(self.setDefaultTemplate)

    def disableTemplate(self):
        self.startButton.setEnabled(False)
        self.startButton.setStyleSheet("border: 0;\n"
           "background-color: #cecfcf;\n"
           "color: #000;")
        self.workTime.setEnabled(False)
        self.intervalTime.setEnabled(False)

    def setDefaultTemplate(self):
        lambda: self.startButton.setEnabled(True)
        lambda: self.startButton.setStyleSheet("border: 0;\n"
           "background-color: rgb(62, 100, 254);\n"
           "color: #fff;")
        lambda: self.workTime.setEnabled(True)
        lambda: self.intervalTime.setEnabled(True)

    def changeOperation(self):
        global setInterval, execStatus, op, text, audioBreak, audioWork;

        if execStatus == 0:
            if op == 0:
                setInterval = int(self.intervalTime.text())
                text = self.finishIntervalTime
                op = 1
                playsound(audioBreak)
            else:
                setInterval = int(self.workTime.text())
                text = self.finishWorkTime
                op = 0
                playsound(audioWork)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.run_longTask = run_longTask()
        lang = self.run_longTask.getConfigVariables(prop='lang')
        if lang == 'pt_BR':
            MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro Tech"))
            MainWindow.setWindowIcon(QtGui.QIcon('docs/pomodoro-tech.png'))
            self.startButton.setText(_translate("MainWindow", "Iniciar"))
            self.finishButton.setText(_translate("MainWindow", "Encerrar"))
            self.label.setText(_translate("MainWindow", "Tempo de Trabalho"))
            self.label_2.setText(_translate("MainWindow", "Tempo de Intervalo"))
            self.finishWorkTime = 'Tempo de trabalho/estudo encerrado, hora do intervalo'
            self.finishIntervalTime = 'Tempo de intervalo encerrado, hora e trabalhar/estudar'
        else:
            MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro Tech"))
            MainWindow.setWindowIcon(QtGui.QIcon('docs/pomodoro-tech.png'))
            self.startButton.setText(_translate("MainWindow", "Start"))
            self.finishButton.setText(_translate("MainWindow", "Finish"))
            self.label.setText(_translate("MainWindow", "Work Time"))
            self.label_2.setText(_translate("MainWindow", "Interval Time"))
            self.finishWorkTime = 'End of work/study time, break time'
            self.finishIntervalTime = 'Break time ended, time to work/study'

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.run(Principal)
    Principal.show()
    sys.exit(app.exec_())
