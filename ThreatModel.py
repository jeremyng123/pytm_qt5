from main import *
from enum_types import *
from pytm import TM, Actor, Boundary, Dataflow, Datastore, Lambda, Server


class ThreatModel:
    def __init__(self, name, allComponents, allBoundaries, description="My TM", isOrdered=True, mergeResponses=True):
        self.tm = TM(name)
        self.tm.description=description
        self.tm.isOrdered = isOrdered
        self.tm.mergeResponses = mergeResponses
        self.components = allComponents
        self.boundaries = allBoundaries

    def start(self):
        self.tm.process()

class Components(ThreatModel):
    def __init__(self, type, name, allComponents, boundary=None, attributes={}, children=[], **kwargs):
        self.type = type
        self.name = name
        self.children=children
        self.attributes=attributes
        self.allComponents=allComponents
        self.boundary=boundary
        self.kwargs = kwargs
        if self.name not in allComponents.keys() or not attributes:
            if type==ComponentType.ACTOR.value:
                self.name = name
                self.type = "Actor"
                self.obj = Actor(name)
                self.attributes['name'] = self.name
                self.attributes['type'] = self.type
                if boundary is not None:
                    self.obj.inBoundary = boundary.obj
                    self.attributes['obj'] = {'header': self.obj,
                                              'inBoundary': boundary.name}
                else:
                    self.attributes['obj'] = {'header': self.obj}
                if 'actor' not in self.allComponents.keys():
                    self.allComponents['actor'] = {self.name : self}
                else:
                    self.allComponents['actor'][self.name] = self
            elif type==ComponentType.SERVER.value:
                self.name = name
                self.type = "Server"
                self.obj = Server(name)
                if 'OS' in kwargs.keys():
                    self.obj.OS = kwargs['OS']
                self.obj.isHardened = kwargs['isHardened']
                self.obj.sanitizesInput = kwargs['sanitizesInput']
                self.obj.encodesOutput = kwargs['encodesOutput']
                self.obj.authorizesSource = kwargs['authorizesSource']
                self.attributes['name'] = self.name
                self.attributes['type'] = self.type
                if boundary is not None:
                    self.obj.inBoundary = boundary
                    self.attributes['obj'] = {'header': self.obj,
                                              'OS': self.obj.OS,
                                              'isHardened': self.obj.isHardened,
                                              'sanitizesInput': self.obj.sanitizesInput,
                                              'encodesOutput': self.obj.encodesOutput,
                                              'authorizesSource': self.obj.authorizesSource,
                                              'inBoundary': boundary.name}
                else:
                    self.attributes['obj'] = {'header': self.obj,
                                              'OS': self.obj.OS,
                                              'isHardened': self.obj.isHardened,
                                              'sanitizesInput': self.obj.sanitizesInput,
                                              'encodesOutput': self.obj.encodesOutput,
                                              'authorizesSource': self.obj.authorizesSource}

                if 'server' not in self.allComponents.keys():
                    self.allComponents['server'] = {self.name : self}
                else:
                    self.allComponents['server'][self.name] = self
            elif type==ComponentType.DATASTORE.value:
                self.name = name
                self.type = "Datastore"
                self.obj = Datastore(name)
                self.obj.OS = kwargs['OS']
                self.obj.isHardened = kwargs['isHardened']
                self.obj.isSQL = kwargs['isSQL']
                self.obj.inScope = kwargs['inScope']
                if boundary is not None:
                    self.obj.inBoundary = boundary
                    self.attributes['obj'] = {'header': self.obj,
                                              'OS': self.obj.OS,
                                              'isHardened': self.obj.isHardened,
                                              'isSQL': self.obj.isSQL,
                                              'inScope': self.obj.inScope,
                                              'inBoundary': boundary.name}
                else:
                    self.attributes['obj'] = {'header': self.obj,
                                              'OS': self.obj.OS,
                                              'isHardened': self.obj.isHardened,
                                              'isSQL': self.obj.isSQL,
                                              'inScope': self.obj.inScope}

                self.attributes['name'] = self.name
                self.attributes['type'] = self.type

                if 'datastore' not in self.allComponents.keys():
                    self.allComponents['datastore'] = {self.name : self}
                else:
                    self.allComponents['datastore'][self.name] = self
            elif type==ComponentType.LAMBDA.value:
                self.name = name
                self.type = "Lambda"
                self.obj = Lambda(name)
                if boundary is not None:
                    self.obj.inBoundary = boundary
                    self.attributes['obj'] = {'inBoundary' : boundary.name}
                self.obj.hasAccessControl = kwargs['hasAccessControl']
                self.attributes['obj'] = {'header': self.obj,
                                          'hasAccessControl' : self.obj.hasAccessControl}
                if 'lambda' not in self.allComponents.keys():
                    self.allComponents['lambda'] = {self.name : self}
                else:
                    self.allComponents['lambda'][self.name] = self
            else:
                print("type is not found")
                return


    def __str__(self):
        """
        this is to return a readable component for component list view
        :return:
        """
        return_str = self.name
        if len(self.children) > 0:
            return_str += "dataflow to: "
            for child in self.children:
                return_str += child + " "
        return return_str

    def makeChild(self, component):
        if component not in self.children:
            self.children.append(component)


class Boundaries(ThreatModel):
    def __init__(self, name, componentsInSelf, allBoundaries):
        self.name = name
        self.obj = Boundary(name)
        self.componentsInSelf = componentsInSelf    # this is a list
        self.allBoundaries = allBoundaries          # this is a dict containing Boundaries object as values and boundary.name as keys

    def __repr__(self):
        return self.obj

    def __str__(self):
        return self.name

    def __getitem__(self, name):
        return self.allBoundaries[name]

    def getComponentsInBoundary(self):
        return self.components

    def addComponent(self, component):
        self.componentsInSelf.append(component)

    def getAllBoundariesName(self):
        str_b_dict = []
        for name, boundary in self.allBoundaries.items():
            str_b_dict.append(name)
        return str_b_dict

    def getAllBoundaries(self):
        return self.allBoundaries