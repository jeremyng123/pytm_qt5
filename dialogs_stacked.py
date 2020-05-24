from main import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget

from ui.WActor import Ui_Actor
from ui.WServer import Ui_Server
from ui.WDatastore import Ui_Datastore
from ui.WLambda import Ui_Lambda

class WActor(QWidget, Ui_Actor):
    def __init__(self, allComponents={}, allBoundaries={}):
        super(WActor, self).__init__()
        self.setupUi(self)
        self.boundaries.addItems(allBoundaries.keys())
        self.boundaries.addItem("None")

        # row1 = QHBoxLayout()
        #
        # self.setLayout()

class WServer(QWidget, Ui_Server):
    def __init__(self, allComponents=[], allBoundaries=[]):
        super(WServer, self).__init__()
        self.setupUi(self)
        self.boundaries.addItems(allBoundaries.keys())
        self.boundaries.addItem("None")

class WDatastore(QWidget, Ui_Datastore):
    def __init__(self, allComponents=[], allBoundaries=[]):
        super(WDatastore, self).__init__()
        self.setupUi(self)
        self.boundaries.addItems(allBoundaries.keys())
        self.boundaries.addItem("None")

class WLambda(QWidget, Ui_Lambda):
    def __init__(self, allComponents=[], allBoundaries=[]):
        super(WLambda, self).__init__()
        self.setupUi(self)
        self.boundaries.addItems(allBoundaries.keys())
        self.boundaries.addItem("None")