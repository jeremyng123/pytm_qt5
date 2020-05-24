from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPalette, QColor
import sys
import random
from dialogs import *
from ThreatModel import *
from enum_types import *




class MainWindow(QMainWindow):
    def __init__(self, name, allComponents = {}, allBoundaries = {}, df = {}, tm = ThreatModel("example",[],[])):
        super(MainWindow, self).__init__()

        self.name = name
        self.allComponents = allComponents
        self.allBoundaries = allBoundaries
        self.tm = tm

        self.setWindowTitle("Edit {0} Programming List".format(self.name))
        self.setWindowIcon(QIcon("icon.png"))

        self.componentList = QListWidget()
        self.boundaryList = QListWidget()
        if allComponents is not None:
            self.componentList.addItems(allComponents)
            self.componentList.setCurrentRow(0)
        if allBoundaries is not None:
            self.boundaryList.addItems(allBoundaries)
            self.boundaryList.setCurrentRow(0)

        h_buttons1 = QHBoxLayout()
        h_buttons2 = QHBoxLayout()


        for text, slot in (("Add", self.c_add),
                           ("Edit", self.c_edit),
                           ("Remove", self.c_remove),
                           ("Sort", self.c_sort),
                           ("Close", self.c_close)):
            button = QPushButton(text)

            h_buttons1.addWidget(button)
            button.clicked.connect(slot)

        for text, slot in (("Add", self.b_add),
                           ("Edit", self.b_edit),
                           ("Remove", self.b_remove),
                           ("Sort", self.b_sort),
                           ("Close", self.b_close)):
            button = QPushButton(text)

            h_buttons2.addWidget(button)
            button.clicked.connect(slot)

        v_components_box = QVBoxLayout()
        v_components_box.addWidget(QLabel("Components"))
        v_components_box.addWidget(self.componentList)
        v_components_box.addLayout(h_buttons1)

        v_boundary_box = QVBoxLayout()
        v_boundary_box.addWidget(QLabel("Boundaries"))
        v_boundary_box.addWidget(self.boundaryList)
        v_boundary_box.addLayout(h_buttons2)

        h_window = QHBoxLayout()

        h_window.addLayout(v_components_box)
        h_window.addLayout(v_boundary_box)

        window = QWidget()
        window.setLayout(h_window)

        self.setCentralWidget(window)
        print(self.size())


    def c_add(self):
        dlg = AddComponent(self.allComponents, self.allBoundaries)
        if dlg.exec_():
            index = dlg.index
            if index == ComponentType.ACTOR.value:
                name = dlg.wactor.name.text()
                b_text = None if dlg.wactor.boundaries.currentText() == 'None' else dlg.wactor.boundaries.currentText()
                print("b_text: " + str(b_text) + ".")
                if b_text != None:
                    Components(index,dlg.wactor.name.text(),allComponents=self.allComponents,boundary=self.allBoundaries[dlg.wactor.boundaries.currentText()])
                    # print(f"HI {self.allComponents}")
                else:
                    Components(index,dlg.wactor.name.text(),allComponents=self.allComponents)
                    # print(f"HI1 name: {name} {self.allComponents['actor']}")
                    # print(f"HI2 {self.allComponents['actor'][name].attributes}")


            elif index == ComponentType.SERVER.value:
                pass
            elif index == ComponentType.LAMBDA.value:
                pass
            elif index == ComponentType.DATASTORE.value:
                pass
            else:
                print("Bugged out here at c_add()")
        else:
            print("Cancel!")
        # row = self.componentList.currentRow()
        # title = "Add Component"
        # string, ok = QInputDialog.getText(self, title, title)
        # if ok and string != "":
        #     print(string)
        #     self.componentList.insertItem(row, string)


    def c_edit(self):
        row = self.componentList.currentRow()
        item = self.componentList.item(row)
        if item is not None:
            title = "Edit {0}".format(self.name)
            string, ok = QInputDialog.getText(self, title, title,
                    QLineEdit.Normal, item.text())
            if ok and string != "":
                item.setText(string)


    def c_remove(self):
        row = self.componentList.currentRow()
        item = self.componentList.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {0}".format(
                self.name), "Remove {0} `{1}'?".format(
                self.name, str(item.text())),
                QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.componentList.takeItem(row)
            del item

    def c_sort(self):
        self.componentList.sortItems()


    def c_close(self):
        self.close()


    def b_add(self):
        row = self.boundaryList.currentRow()
        title = "Add {0}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)
        if ok and string != "":
            print(string)
            self.boundaryList.insertItem(row, string)


    def b_edit(self):
        row = self.boundaryList.currentRow()
        item = self.boundaryList.item(row)
        if item is not None:
            title = "Edit {0}".format(self.name)
            string, ok = QInputDialog.getText(self, title, title,
                    QLineEdit.Normal, item.text())
            if ok and string != "":
                item.setText(string)


    def b_remove(self):
        row = self.boundaryList.currentRow()
        item = self.boundaryList.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {0}".format(
                self.name), "Remove {0} `{1}'?".format(
                self.name, str(item.text())),
                QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.boundaryList.takeItem(row)
            del item

    def b_sort(self):
        self.boundaryList.sortItems()


    def b_close(self):
        self.close()






if __name__ == "__main__":

    # TODO: Figure out how to save and load component and boundary lists
    allComponents = {}
    allBoundaries = {}
    df = {}

    # TODO: Once components and boundaries are loaded, create tm
    tm = ThreatModel("My test TM", allComponents, allBoundaries)

    app= QApplication(sys.argv)
    window = MainWindow("Threat Model", allComponents, allBoundaries, df, tm)
    window.show()

    app.exec_()