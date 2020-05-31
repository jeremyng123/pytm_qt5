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
    def __init__(self, type, name, allComponents, getNamesFromType, getTypeFromName, boundary=None, attributes={}, children=[], **kwargs):
        self.type = type
        self.name = name
        self.children=children
        self.attributes=attributes
        self.boundary=boundary
        self.kwargs = kwargs
        self.getTypeFromName = getTypeFromName
        self.allComponents = allComponents
        self.df = DataFlows(self, allComponents)
        if type==ComponentType.ACTOR.value:
            self.name = name
            self.type = "Actor"
            self.obj = Actor(name)
            self.attributes['name'] = self.name
            self.attributes['type'] = self.type
            if boundary is not None:
                print(f'boundary in component: {boundary}')
                self.obj.inBoundary = boundary.obj
                self.attributes['obj'] = {'header': self.obj,
                                          'inBoundary': boundary.name}
            else:
                self.attributes['obj'] = {'header': self.obj}
            if 'actor' not in allComponents.keys():
                allComponents['actor'] = {self.name : self}
                getNamesFromType['actor'] = [self.name]
            else:
                allComponents['actor'][self.name] = self
                getNamesFromType['actor'].append(self.name)
            getTypeFromName[self.name] = 'actor'
        elif type==ComponentType.SERVER.value:
            self.name = name
            self.type = "Server"
            self.obj = Server(name)
            if 'OS' in kwargs.keys():
                self.obj.OS = kwargs['OS']
            self.obj.isHardened = kwargs['isHardened']
            self.obj.sanitizesInput = kwargs['sanitizesInput']
            self.obj.encodesOutput = kwargs['encodesOutput']
            self.obj.authorizesSources = kwargs['authorizesSource']
            self.attributes['name'] = self.name
            self.attributes['type'] = self.type
            if boundary is not None:
                self.obj.inBoundary = boundary.obj
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

            if 'server' not in allComponents.keys():
                allComponents['server'] = {self.name : self}
                getNamesFromType['server'] = [self.name]
            else:
                allComponents['server'][self.name] = self
                getNamesFromType['server'].append(self.name)
            getTypeFromName[self.name] = 'server'
        elif type==ComponentType.DATASTORE.value:
            self.name = name
            self.type = "Datastore"
            self.obj = Datastore(name)
            self.obj.OS = kwargs['OS']
            self.obj.isHardened = kwargs['isHardened']
            self.obj.isSQL = kwargs['isSQL']
            self.obj.inScope = kwargs['inScope']
            if boundary is not None:
                self.obj.inBoundary = boundary.obj
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

            if 'datastore' not in allComponents.keys():
                allComponents['datastore'] = {self.name : self}
                getNamesFromType['datastore'] = [self.name]
            else:
                allComponents['datastore'][self.name] = self
                getNamesFromType['datastore'].append(self.name)
            getTypeFromName[self.name] = 'datastore'
        elif type==ComponentType.LAMBDA.value:
            self.name = name
            self.type = "Lambda"
            self.obj = Lambda(name)
            if boundary is not None:
                self.obj.inBoundary = boundary.obj
                self.attributes['obj'] = {'inBoundary' : boundary.name}
            self.obj.hasAccessControl = kwargs['hasAccessControl']
            self.attributes['obj'] = {'header': self.obj,
                                      'hasAccessControl' : self.obj.hasAccessControl}
            if 'lambda' not in allComponents.keys():
                allComponents['lambda'] = {self.name : self}
                getNamesFromType['lambda'] = [self.name]
            else:
                allComponents['lambda'][self.name] = self
                getNamesFromType['lambda'].append(self.name)
            getTypeFromName[self.name] = 'lambda'
        else:
            print("type is not found")
            del self.kwargs
            return

        del self.kwargs

    def __getitem__(self, item):
        # item is component name
        typeOfItem = self.getTypeFromName(item)
        return self.allComponents[typeOfItem][item]


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

    def addBoundary(self, boundary):
        self.obj.inBoundary = boundary.obj


class Boundaries(ThreatModel):
    def __init__(self, name, allBoundaries):
        self.name = name
        self.obj = Boundary(name)
        self.componentsInSelf = []    # this is a list containing strings of component names
        self.allBoundaries = allBoundaries          # this is a dict containing Boundaries object as values and boundary.name as keys
        self.componentsInBoundaries = {}            # this is a dict where the values is a list of all components found inside a boundary-key (str datatype)
        if self.name not in allBoundaries.keys():
            self.allBoundaries[self.name] = self
            self.componentsInBoundaries[self.name] = []
        else:
            print("TODO: should not allow user to use same name. future dev.")

    def addComponentsToSelf(self, components):
        """
        :param components: this is a list containing string of the component's name
        :return:
        """
        for component in components:
            self.componentsInSelf.append(component)
            self.componentsInBoundaries[self.name].append(component)

    def addComponentToSelf(self, component):
        """
        :param component: this is a string of the component's name
        :return:
        """
        self.componentsInSelf.append(component)
        self.componentsInBoundaries[self.name].append(component)

    def removeComponentFromSelf(self, component):
        self.componentsInSelf.remove(component)

    def updateComponentsInBoundaries(self):
        if self.allBoundaries:
            for boundaries_obj in self.allBoundaries.values():
                self.componentsInBoundaries[boundaries_obj.name] = boundaries_obj.componentsInSelf

    # def __repr__(self):
    #     return self.obj

    def __str__(self):
        return self.name

    def __getitem__(self, name):
        return self.allBoundaries[name]

    def getComponentsInBoundary(self):
        return self.components

    def addComponent(self, component):
        self.componentsInSelf.append(component)

    def addComponents(self, components):
        for component in components:
            self.componentsInSelf.append(component)

    def getAllBoundariesName(self):
        str_b_dict = []
        for name, boundary in self.allBoundaries.items():
            str_b_dict.append(name)
        return str_b_dict

    def getAllBoundaries(self):
        return self.allBoundaries


class DataFlows(ThreatModel):
    def __init__(self, component, allComponents = {}, allDataflows={}):
        """
        component is the Components object
        """
        self.src = component
        self.name = self.src.name
        print(f"type of name: {(str(self.name))}")
        self.obj = None
        self.sink_flowName = None
        self.attributes = {}
        self.allComponents = allComponents
        self.allDataflows = allDataflows
        if self.name not in self.allDataflows.keys():
            self.allDataflows[self.name] = []


    def flowTo(self, sink, dataflowname, kwargs):
        """
        other should be the Components object
        kwargs contains notes/keys such as protocol, dstPort, data, note.
        responseTo is another dataflow object. this is filled if an existing dataflow is present and this
            dataflow only happens if the responseTo dataflow happens firstw
        """
        if self.obj is None:
            self.obj = Dataflow(self.src.obj, sink.obj, dataflowname)
            print(dataflowname, "dataflowname here")
            self.allDataflows[self.name].append(self)
            self.sink_flowName = sink.name, dataflowname
            for k,v in kwargs.items():
                if k == 'protocol':
                    self.obj.protocol = v
                    self.attributes[k] = v
                elif k == 'dstPort':
                    self.obj.dstPort = v
                    self.attributes[k] = v
                elif k == 'data':
                    self.obj.data = v
                    self.attributes[k] = v
                ## TODO: the rest of the attributes that are available in the Dataflow class
                elif k == 'authenticatedWith':
                    self.obj.authenticatedWith = v
                    self.attributes[k] = v
                elif k == 'authorizesSource':
                    self.obj.authorizesSource = v
                    self.attributes[k] = v
                elif k == 'definesConnectionTimeout':
                    self.obj.definesConnectionTimeout = v
                    self.attributes[k] = v
                elif k == 'responseTo':
                    self.obj.responseTo = v
                    self.attributes[k] = v
