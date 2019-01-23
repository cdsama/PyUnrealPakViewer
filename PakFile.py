class PakFileSepFile:
    def __init__(self, path, offset, size, sha1):
        self.path = path
        self.offset = offset
        self.size = size
        self.sha1 = sha1


class PakFile:
    def __init__(self):
        self.files = dict()
