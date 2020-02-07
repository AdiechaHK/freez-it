import json
from record import Record
from config import getInfoPath

class RecordCollection:
    """docstring for RecordCollection."""
    list = None

    def __init__(self):
        self.list = []
        self.read();

    def read(self):
        data = ""
        with open(getInfoPath()) as f:
            data += "".join(f.readlines())

        info = json.loads(data);

        for record in info['list']:
            # print(record)
            self.list.append(Record.decoder(record))
            pass

    def addRecord(self, r):
        self.list.append(r)


    def write(self):
        data = ""
        with open(getInfoPath()) as f:
            data += "".join(f.readlines())

        info = json.loads(data);
        lst = []
        for record in self.list:
            lst.append(record.encode())

        info['list'] = lst
        f = open(getInfoPath(), "w")
        f.write(json.dumps(info))
        f.close()
