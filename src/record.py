import string
import random
import time
import json
import os
from datetime import datetime, timedelta
from shutil import copyfile
from config import dataPath
from json import JSONEncoder
from util import getFileHash

class Record(JSONEncoder):
    """docstring for record."""
    key = None
    path = None
    delta = None
    fileHash = None

    # Constructor
    def __init__(self, path, key=None):
        self.path = path
        self.delta = 60
        if key == None:
            self.autoSetKey()
        else:
            self.setKey(key)

    # Key Generator
    def autoSetKey(self, n=13):
        self.key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

    ###########################################################################
    ##   Getters
    ###########################################################################

    def getTimeDiff(self, td=0):
        return datetime.timestamp(datetime.now() + timedelta(hours=td))

    def getPath(self):
        return self.path

    def getKey(self):
        return self.key

    def getDelta(self):
        return self.delta

    def getTime(self):
        return datetime.fromtimestamp(self.expiry).strftime("%d-%m-%Y %I:%M %p")

    def encode(self):
        return json.dumps(self.__dict__)

    def setKey(self, k):
        self.key = k

    def setDelta(self, d):
        self.delta = d

    def setFileHash(self, k):
        self.fileHash = k

    def getDict(self):
        return self.__dict__

    def decoder(obj):
        r = Record(obj['path'], obj['key'])
        r.setFileHash(obj['fileHash'])
        r.setDelta(obj['delta'])
        return r

    def build(json_string):
        return json.loads(json_string, object_hook=Record.decoder)

    def updateHash(self):
        self.fileHash = getFileHash(dataPath(self.key))

    def backup(self):
        copyfile(self.path, dataPath(self.key))
        self.updateHash()


    def check(self):
        if os.path.isfile(self.path):
            hash = getFileHash(self.path)
            last_modified = datetime.fromtimestamp(os.stat(self.path).st_mtime)
            expected = (datetime.now() - timedelta(minutes=self.delta))
            if hash != self.fileHash and last_modified < expected:
                copyfile(dataPath(self.key), self.path)
                return 1
            else:
                print("no need to replace")
                return 0
        else:
            copyfile(dataPath(self.key), self.path)
            return 1



        # return datetime.timestamp(datetime.now() + timedelta(hours=td))
        # return datetime.fromtimestamp(self.expiry).strftime("%d-%m-%Y %I:%M %p")
