from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPalette, QColor
from main import *
from enum_types import *
from dialogs_stacked import *

# to return multiple values back to mainwindow. check out https://stackoverflow.com/questions/25250684/how-to-return-values-from-a-qdialog-instance-in-python
class AddComponent(QDialog):
    FIXED_LENGTH = 420
    ACTOR_HEIGHT = 150
    SERVER_HEIGHT = 320
    DATASTORE_HEIGHT = 290
    LAMBDA_HEIGHT = 195

    def __init__(self, allComponents=None, allBoundaries=None):
        super(AddComponent, self).__init__()
        self.setWindowTitle("Add new component")
        self.stackedlayout = QStackedLayout()
        self.resize(self.FIXED_LENGTH, self.ACTOR_HEIGHT)

        v_window = QVBoxLayout()

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        # buttonBox
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # comboBox for all component Types
        componentsBox = QComboBox()
        componentsBox.addItems(ComponentType.getAllTypes())
        componentsBox.currentIndexChanged.connect(self.index_changed)
        componentsBox.setCurrentIndex(ComponentType.ACTOR.value)
        self.index = ComponentType.ACTOR.value

        # stacked widgets for each types
        self.wactor = WActor(allComponents, allBoundaries)
        self.wserver = WServer(allComponents, allBoundaries)
        self.wdatastore = WDatastore(allComponents, allBoundaries)
        self.wlambda = WLambda(allComponents, allBoundaries)




        self.stackedlayout.addWidget(self.wactor)
        self.stackedlayout.addWidget(self.wserver)
        self.stackedlayout.addWidget(self.wdatastore)
        self.stackedlayout.addWidget(self.wlambda)
        stackedWidget = QWidget()
        stackedWidget.setLayout(self.stackedlayout)

        v_window.addWidget(componentsBox)
        v_window.addWidget(stackedWidget)
        v_window.addWidget(buttonBox)
        self.setLayout(v_window)

    def index_changed(self, i): # i is an int
        self.stackedlayout.setCurrentIndex(i)
        self.index = i
        currentlength = self.size().width()
        print(currentlength)
        if i == ComponentType.ACTOR.value:
            self.resize(currentlength,self.ACTOR_HEIGHT)
        elif i == ComponentType.SERVER.value:
            self.resize(currentlength,self.SERVER_HEIGHT)
        elif i == ComponentType.DATASTORE.value:
            self.resize(currentlength, self.DATASTORE_HEIGHT)
        elif i == ComponentType.LAMBDA.value:
            self.resize(currentlength, self.LAMBDA_HEIGHT)
        else:
            print("index_changed received weird index")

