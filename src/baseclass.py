from random import randint
from constants_name import getAllNames
from constants_continent import getContinents
from constants_programs import getPrograms
from constants_dropoffreasons import getDropOffReason

class ERObject:
    continent = getContinents()
    programs = getPrograms()
    normalReasons = getDropOffReason("normal")
    remoteReasons = getDropOffReason("remote")
    names = getAllNames()

    id = None
    def __init__(self, id):
        self.id = id
    
    def print(self):
        return {"id":self.id}