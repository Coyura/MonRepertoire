import sys, json
from PySide2.QtWidgets import QLineEdit, QPushButton, QApplication, QVBoxLayout, QWidget, QLabel, QInputDialog, QListWidget
from PySide2 import QtCore, QtUiTools
from ui_designFichier import Ui_Form

filename = "repertoire.data"

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        global filename
        self.monRepertoire = {}

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pBModif.clicked.connect(self.ModifClient)
        self.ui.pBAjout.clicked.connect(self.AjoutClient)

        self.ui.listWClients.itemClicked.connect(self.clientSelected)

        self.monRepertoire = self.lireJSON(filename)

        self.updateListw()

    def updateListw(self):
        self.ui.listWClients.clear()
        for fiche in self.monRepertoire["repertoire"]:
            self.ui.listWClients.addItem(fiche["nom"])

    def AjoutClient (self):
        print("Ajout fait")
        retour = QInputDialog().getText(self, "Ajout Utilisateut", "Nom")
        if retour[0] == "":
            return

        fiche={}
        fiche["nom"]=retour[0]
        fiche["prenom"]=""
        fiche["tel"]=""

        self.monRepertoire["repertoire"].append(fiche)
        self.updateListw()

        self.sauveJSON(filename)

    def clientSelected(self):
        print("dfghj")
        rowSelected = self.ui.listWClients.currentRow()
        fiche = self.monRepertoire["repertoire"][rowSelected]
        self.ui.editName.setText(fiche["nom"])
        self.ui.editPrenom.setText(fiche["prenom"])
        self.ui.editTel.setText(fiche["tel"])
    #
    def ModifClient(self):
        print("Modif faite")
        rowSelected = self.ui.listWClients.currentRow()
        print(self.ui.editName.text())
        self.monRepertoire["repertoire"][rowSelected]["nom"]=self.ui.editName.text()
        self.monRepertoire["repertoire"][rowSelected]["prenom"]=self.ui.editPrenom.text()
        self.monRepertoire["repertoire"][rowSelected]["tel"]=self.ui.editTel.text()
        self.updateListw()
        self.sauveJSON(filename)

    def lireJSON(self,fileName):
        with open(fileName) as json_file:
            dico = json.load(json_file)
            return dico
        return None

    def sauveJSON (self, filename):
        jsonClasse=json.dumps(self.monRepertoire, sort_keys=True, indent=4)
        f=open(filename, 'w')
        f.write(jsonClasse)

    #
    # def updateListw(self):
    #     self.ui.lwListeNoms.clear()
    #     for fiche in self.monRepertoire["repertoire"]:
    #         self.ui.lwListeNoms.addItem(fiche["nom"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = Form()
    fenetre.show()
    sys.exit(app.exec_())