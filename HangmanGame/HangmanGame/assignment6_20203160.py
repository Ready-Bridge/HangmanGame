import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.scdb = []
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.readScoreDB()
        self.showScoreDB(self.scdb, 'Name')


    def initUI(self):

        Name = QLabel('Name:')
        Age = QLabel('Age:')
        Score = QLabel('Score:')

        self.NameEdit = QLineEdit()
        self.AgeEdit = QLineEdit()
        self.ScoreEdit = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(Name)
        hbox1.addWidget(self.NameEdit)
        hbox1.addWidget(Age)
        hbox1.addWidget(self.AgeEdit)
        hbox1.addWidget(Score)
        hbox1.addWidget(self.ScoreEdit)

        Amount = QLabel('Amont:')
        Key = QLabel('Key:')

        self.AmountEdit = QLineEdit()
        self.KeyEdit = QComboBox()
        self.KeyEdit.addItem('Name')
        self.KeyEdit.addItem('Age')
        self.KeyEdit.addItem('Score')

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(Amount)
        hbox2.addWidget(self.AmountEdit)
        hbox2.addWidget(Key)
        hbox2.addWidget(self.KeyEdit)

        AddButton = QPushButton("Add")
        AddButton.clicked.connect(self.buttonClicked)
        DelButton = QPushButton("Del")
        DelButton.clicked.connect(self.buttonClicked)
        FindButton = QPushButton("Find")
        FindButton.clicked.connect(self.buttonClicked)
        IncButton = QPushButton("Inc")
        IncButton.clicked.connect(self.buttonClicked)
        showButton = QPushButton("show")
        showButton.clicked.connect(self.buttonClicked)


        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(AddButton)
        hbox3.addWidget(DelButton)
        hbox3.addWidget(FindButton)
        hbox3.addWidget(IncButton)
        hbox3.addWidget(showButton)

        self.Result = QLabel('Result: ')
        self.ResultEdit = QTextEdit()


        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.Result)
        vbox.addWidget(self.ResultEdit)

        self.setLayout(vbox)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):


        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.ResultEdit.append("New DB: " + self.dbfilename)
            return []

        scdb = []
        try:
            self.scdb = pickle.load(fH)
        except:
            self.ResultEdit.append("Empty DB: " + self.dbfilename)
        else:
            pass
        fH.close()
        return self.scdb


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()


    def showScoreDB(self, scdb, keyName):
        try :
            self.ResultEdit.clear()
            for p in sorted(scdb, key=lambda person: person[keyName]):
                result = ""
                for attr in sorted(p):
                    result += (attr + "=" + str(p[attr]) + "      ")
                self.ResultEdit.append(result)

        except :
            self.ResultEdit.append("Error!")

    def addScoreDB(self):
        try :
            record = {'Name': self.NameEdit.text(), 'Age': int(self.AgeEdit.text()), 'Score': int(self.ScoreEdit.text())}
            self.scdb += [record]
            self.AgeEdit.clear()
            self.ScoreEdit.clear()
            self.NameEdit.clear()

        except :
            self.ResultEdit.append("Error!")

    def delScoreDB(self):
        try :
            for p in self.scdb[:]:
                if p['Name'] == self.NameEdit.text():
                    self.scdb.remove(p)
        except :
            self.ResultEdit.append("Error!")

    def findScoreDB(self):
        try :
            self.ResultEdit.clear()

            for i in self.scdb:
                result = ""
                if i['Name'] == self.NameEdit.text():
                    for k in i:
                        result += (k + "=" + str(i[k]) + "      ")
                self.ResultEdit.append(result)

        except :
            self.ResultEdit.append("Error!")

    def incScoreDB(self, scdb, name, amount):
        try :
            for i in scdb:
                if i['Name'] == name:
                    i['Score'] += int(amount)
        except :
            self.ResultEdit.append("Error!")

    def buttonClicked(self):
        try :
            sender = self.sender
            if sender().text() == "Add" :
                self.addScoreDB()
                self.showScoreDB(self.scdb, 'Name')

            elif sender().text() == "show" :
                self.showScoreDB(self.scdb, self.KeyEdit.currentText())

            elif sender().text() == "Del" :
                self.delScoreDB()
                self.showScoreDB(self.scdb, "Name")

            elif sender().text() == "Find" :
                self.findScoreDB()

            else :
                self.incScoreDB(self.scdb, self.NameEdit.text(), self.AmountEdit.text())
                self.showScoreDB(self.scdb, 'Name')

        except :
            self.ResultEdit.append("Error!")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

