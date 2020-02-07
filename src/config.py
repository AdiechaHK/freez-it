import os


def dataPath(filename):
    cwd = os.getcwd()
    dir = os.path.dirname(__file__)
    return os.path.realpath(os.path.join(cwd, dir, "../data/" + filename))

def currPath(filename):
    cwd = os.getcwd()
    return os.path.realpath(os.path.join(cwd, filename))

def readData():
    path = dataPath('info')
    with open(path) as f:
        print(f.readlines())

def makeEntry():
    data = readData()
    # print(data)
    # writeData(data)


def getInfoPath():
    return dataPath('info.json')
