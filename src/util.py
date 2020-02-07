import hashlib
from collections import OrderedDict as od

def getFileHash(filepath):
    od_hash = od()
    od_hash['md5sum'] = hashlib.md5()
    od_hash['sha1sum'] = hashlib.sha1()
    od_hash['sha224sum'] = hashlib.sha224()
    od_hash['sha256sum'] = hashlib.sha256()
    od_hash['sha384sum'] = hashlib.sha384()
    od_hash['sha512sum'] = hashlib.sha512()

    with open(filepath, 'rb') as fd:
        data_chunk = fd.read(1024)
        while data_chunk:
              for hashsum in od_hash.keys():
                  od_hash[hashsum].update(data_chunk)
              data_chunk = fd.read(1024)

    hash = []
    for key,value in od_hash.items():
         hash.append(key + ":" + value.hexdigest())

    return ";".join(hash)
