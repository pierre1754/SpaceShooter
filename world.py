def init():
    global world, end
    world = []
    end = False

def addEntity(entity):
    world.append(entity)

def removeEntity(entity):
    world.remove(entity)

def getEntitiesList(entity):
    result = world.copy()
    result.remove(entity)
    return result

def update(time):
    for entity in world:
        entity.update(time)

def enemiesUpdate():
    for i in range(1, len(world)):
        world[i].movebad()
        world[i].shotbad()

def getVessel():
    return world[0]

def destroy():
    world.clear()