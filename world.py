def init():
    global world
    world = []

def addEntity(entity):
    world.append(entity)

def removeEntity(entity):
    world.remove(entity)

def getEntitiesList(entity):
    result = world.copy()
    result.remove(entity)
    return result