import json
from record import Record
from config import getInfoPath

class Info:
    """docstring for RecordCollection."""
    list = None

    def __init__(self):
        self.list = []
        self.read();


    def read(self):
        data = ""
        with open(getInfoPath()) as f:
            data += "".join(f.readlines())

        if len(data) > 0:
            info = json.loads(data);
            self._extractRecords(info)

    def _extractRecords(self, info):
        if 'list' in info:
            for record in info['list']:
                self.list.append(Record.decoder(record))

    def addRecord(self, r):
        self.list.append(r)

    def exists(self, path):
        for rec in self.list:
            if path == rec.getPath():
                return True
        return False

    def getDict(self):
        return dict(list=[ r.getDict() for r in self.list ])

    def save(self):
        f = open(getInfoPath(), "w")
        f.write(json.dumps(self.getDict()))
        f.close()


    def display(self):
        count = 0
        for r in self.list:
            print(r.path + " -- (" + str(r.getDelta()) + "m) " + r.getKey())
            count+=1

        print(str(count) + " file" +(" is" if count == 1 else "s are") + " freezed.")


    def check(self):
        count = 0
        for r in self.list:
            count+=r.check()

        print(str(count) + " file" +(" is" if count == 1 else "s are") + " replaced.")
