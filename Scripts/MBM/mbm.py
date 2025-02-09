import struct
def vec3(file):
    return struct.unpack("fff", file.read(12))[0:3]
def u32(file):
    return struct.unpack("<I", file.read(4))[0]
def u16(file):
    return struct.unpack("<H", file.read(2))[0]

class MBM(object):
    class Header(object):
        def __init__(self):
            self.MAGIC = "MBM\0"
            self.vertexCount1 = 0
            self.vertexCount2 = 0
            self.faceCount = 0
            self.startOfHeader = 0
            self.vertexBuff1 = 0
            self.vertexBuff2 = 0
            self.polygonBuff = 0
        def read(self,f):
            self.MAGIC = f.read(4)
            self.vertexCount1 = u32(f)
            self.vertexCount2  = u32(f)
            self.faceCount  = u32(f)
            self.startOfHeader  = u32(f)
            self.vertexBuff1  = u32(f)
            self.vertexBuff2  = u32(f)
            self.polygonBuff  = u32(f)
    def __init__(self):
        self.header = self.Header()
        self.positions = []
        self.normals = []
        self.poly = []
    def read(self,f):
        self.header.read(f)
        for x in range(self.header.vertexCount1):
            self.positions.append(vec3(f))
        for x in range(self.header.vertexCount2):
            self.normals.append(vec3(f))
        for x in range(self.header.vertexCount1):
            self.poly.append(u16(f))