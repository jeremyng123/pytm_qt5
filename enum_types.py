from enum import Enum

class ComponentType(Enum):
    ACTOR = 0
    SERVER = 1
    DATASTORE = 2
    LAMBDA = 3

    @classmethod
    def getAllTypes(cls):
        return ['Actor', 'Server', 'Datastore', 'Lambda']