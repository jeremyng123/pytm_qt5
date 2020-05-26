from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPalette, QColor
from main import *
from enum_types import *
from dialogs_stacked import *
from ui.DAddBoundary import Ui_DAddBoundary

# to return multiple values back to mainwindow. check out https://stackoverflow.com/questions/25250684/how-to-return-values-from-a-qdialog-instance-in-python
class AddComponent(QDialog):
    FIXED_WIDTH = 420
    ACTOR_HEIGHT = 150
    SERVER_HEIGHT = 320
    DATASTORE_HEIGHT = 290
    LAMBDA_HEIGHT = 195

    def __init__(self, allComponents=None, allBoundaries=None, getNamesFromType=None, getTypesFromName=None):
        super(AddComponent, self).__init__()
        self.setWindowTitle("Add new component")
        self.stackedlayout = QStackedLayout()
        self.resize(self.FIXED_WIDTH, self.ACTOR_HEIGHT)

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


class AddBoundary(QDialog, Ui_DAddBoundary):
    FIXED_WIDTH = 420
    FIXED_HEIGHT = 150

    def __init__(self, allComponents=None, allBoundaries=None, getNamesFromType=None, getTypesFromName=None):
        super(AddBoundary,self).__init__()
        self.setWindowTitle("Add new boundary")
        self.setupUi(self)
        all_types = [component for component in allComponents.values()]
        all_types_name = []
        for component in all_types:
            for c_name in component.keys():
                all_types_name.append(c_name)

        """
        This block of # comments is for future development where we can classify components into their types.
        For now, all components will just be sorted by name.
        """
        # print(f"all_types_name: {all_types_name}")
        # found = []
        # if 'actor' in allComponents.keys():
        #     actors_name = [actor for actor in allComponents['actor'].keys()]
        #     found.append('actors_name: ')
        #     for i in actors_name:
        #         found.append(i + ", ")
        #     found.append('\n')
        # if 'server' in allComponents.keys():
        #     servers_name = [server for server in allComponents['server'].keys()]
        #     found.append('servers_name: ')
        #     for i in servers_name:
        #         found.append(i + ", ")
        #     found.append('\n')
        # if 'datastore' in allComponents.keys():
        #     datastores_name = [datastore for datastore in allComponents['datastore'].keys()]
        #     found.append('datastores_name: ')
        #     for i in datastores_name:
        #         found.append(i + ", ")
        #     found.append('\n')
        # if 'lambda' in allComponents.keys():
        #     lambdas_name = [l for l in allComponents['lambda'].keys()]
        #     found.append('lambdas_name: ')
        #     for i in lambdas_name:
        #         found.append(i + ", ")
        #     found.append('\n')
        #
        # # print(f"dict: {allComponents} \nvalues: {allComponents.values()}")
        # print_str = ""
        # for x in found:
        #     print(x)
        #     print_str += x
        # print(print_str)


        self.allComponents.addItems(all_types_name) # self.allComponents here is a listwidget
        # print(f"selected indexes: {self.allComponents.selectedIndexes()}")


