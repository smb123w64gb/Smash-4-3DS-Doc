import sys
import os
import struct


def readByte(file):
	return struct.unpack("B", file.read(1))[0]

def readSByte(file):
	return struct.unpack("b", file.read(1))[0]

def readu16be(file):
	return struct.unpack(">H", file.read(2))[0]

def readu16le(file):
	return struct.unpack("<H", file.read(2))[0]

def reads16le(file):
	return struct.unpack("<h", file.read(2))[0]
	
def readu32be(file):
	return struct.unpack(">I", file.read(4))[0]

def readu32le(file):
	return struct.unpack("<I", file.read(4))[0]

def readFloatle(file):
        return struct.unpack("<f", file.read(4))[0]

	
def getString(file):
	result = ""
	tmpChar = file.read(1)
	while ord(tmpChar) != 0:
		result += tmpChar.decode("utf-8")
		tmpChar =file.read(1)
	return result

def align(al,file):
    currentPOS = file.tell()
    while(currentPOS % al):
        file.seek(1,1)
        currentPOS = file.tell()

class bone(object):
        def __init__(self):
                self.parentId = 0
                self.name = ""
                self.rotation = []
                self.transform = []
class mbn(object):
    def __init__(self):
        self.name = ""
        self.vct = 0
        self.smd = []
        self.idn = []
class Descriptor(object):
    def __init__(self):
        self.type = []
        self.format = []
        self.scale = []
        self.lenth = 0
        self.pos = []
        self.nrm = []
        self.uv0 = []
        self.bix = []
        self.bwt = []
    def read(self,f):
        length = readu32le(f)
        for i in range(length):
            self.type.append(readu32le(f))
            self.format.append(readu32le(f))
            self.scale.append(readFloatle(f))
        self.lenth = readu32le(f)
    def readBuffer(self,file):
        cur = file.tell()
        while(file.tell() < cur + self.lenth):
            for fm in range(len(self.type)):
                t = self.type[fm]
                f = self.format[fm]
                s = self.scale[fm]
                if(t == 0):self.pos.append([readType(file,f,s),readType(file,f,s),readType(file,f,s)])
                if(t == 1):self.nrm.append([readType(file,f,s),readType(file,f,s),readType(file,f,s)])
                if(t == 3):self.uv0.append([readType(file,f,s),readType(file,f,s)])
                if(t == 5):self.bix.append([readType(file,f,s),readType(file,f,s)])
                if(t == 6):self.bwt.append([readType(file,f,s),readType(file,f,s)])
                align(2,file)
    def printD(self):
        for i in range(len(self.type)):
            if(self.type[i] == 0):print("pos")
            if(self.type[i] == 1):print("nor")
            if(self.type[i] == 2):print("col")
            if(self.type[i] == 3):print("uv0")
            if(self.type[i] == 4):print("uv1")
            if(self.type[i] == 5):print("bID")
            if(self.type[i] == 6):print("bWG")
            if(self.type[i] == 7):print("unk")
            if(self.format[i] == 0):print("Float")
            if(self.format[i] == 1):print("Byte")
            if(self.format[i] == 2):print("SByte")
            if(self.format[i] == 3):print("SShort")
            print("Scale:%f"%self.scale[i])
            
def readType(f,format,scale):
    if(format == 0):return readFloatle(f)*scale
    elif(format == 1):return float(readByte(f))*scale
    elif(format == 2):return float(readSByte(f))*scale
    elif(format == 3):return float(reads16le(f))*scale
    else:return 0
        
f = open(sys.argv[1].replace(".mbn",".bch"), 'rb')
f.seek(8)

mainHeaderOffset = readu32le(f)
stringTableOffset = readu32le(f)
gpuCommandOffset= readu32le(f)
dataOffset= readu32le(f)
dataExtendOffset= readu32le(f)
relocationTableOffset= readu32le(f)

mainHeaderLength= readu32le(f)
stringTableLength= readu32le(f)
gpuCommandLength= readu32le(f)
dataLength= readu32le(f)
dataExtendLength= readu32le(f)
relocationTableLength= readu32le(f)
datsSecLength= readu32le(f)
desSecLength= readu32le(f)
flags= readu16le(f)
addressCount= readu16le(f)


f.seek(mainHeaderOffset)
modelsPointerTableOffset = readu32le(f) + mainHeaderOffset
modelsPointerTableEntries = readu32le(f)
modelsNameOffset = readu32le(f) + mainHeaderOffset

Bonez = []


for modelIndex in range(modelsPointerTableEntries):
    f.seek(modelsPointerTableOffset + (modelIndex * 4))
    objectsHeaderOffset = readu32le(f) + mainHeaderOffset
    f.seek(objectsHeaderOffset + 0x70)
    skeletonOffset =readu32le(f) + mainHeaderOffset
    skeletonEntries =readu32le(f)
    skeletonNameOffset =readu32le(f) + mainHeaderOffset
    f.seek(skeletonOffset)
    for index in range(skeletonEntries):
        f.seek(4,1)
        Bonez.append(bone())
        Bonez[index].parentId = reads16le(f)#6
        f.seek(0xE,1)#0x14
        for flt in range(3):
            Bonez[index].rotation.append(readFloatle(f))
        for flt in range(3):
            Bonez[index].transform.append(readFloatle(f))
        f.seek(0x30,1)
        rtn = f.tell() + 8
        f.seek(readu32le(f) + stringTableOffset)
        Bonez[index].name = getString(f)
        f.seek(rtn)
f.close()

f = open(sys.argv[1], 'rb')

fmt = readu16le(f)

isDataWithinHeader = fmt == 4
f.seek(2,1)
contentFlags = readu32le(f)
hasNameTable = (contentFlags & 2) > 0
mode = readu32le(f)
meshCount = readu32le(f)

mbnModels = []


des = Descriptor()
des.read(f)
idxMBN = 0
for i in range(meshCount):
    facesCount = readu32le(f)
    for j in range(facesCount):
        mbnModels.append(mbn())
        mbnModels[idxMBN].name = str("%d:%d" % (i,j))
        nodesCount = readu32le(f)
        for k in range(nodesCount):
            mbnModels[idxMBN].idn.append(readu32le(f))
        mbnModels[idxMBN].vct = (readu32le(f))
        idxMBN+=1

align(32,f)

print(hex(f.tell()))
des.readBuffer(f)
print(hex(f.tell()))
align(32,f)
print(hex(f.tell()))
for mb in mbnModels:
    for a in range(mb.vct):
        idx = readu16le(f)
        mb.smd.append(str("0 %.6f %.6f %.6f %.6f %.6f %.6f %.6f %.6f 2 %i %f %i %f\n" %
                          (des.pos[idx][0],des.pos[idx][1],des.pos[idx][2],
                           des.nrm[idx][0],des.nrm[idx][1],des.nrm[idx][2],
                           des.uv0[idx][0],des.uv0[idx][1],
                           mb.idn[int(des.bix[idx][1])],des.bwt[idx][1],
                           mb.idn[int(des.bix[idx][0])],des.bwt[idx][0])))
    align(32,f)
print(hex(f.tell()))

f.close()

f = open(sys.argv[1].replace(".mbn",".smd"), 'w')
f.write("version 1\nnodes\n")
nIDX = 0
for Bn in Bonez:
    f.write(str("%i \"%s\" %i\n" % (nIDX,Bn.name,Bn.parentId)))
    nIDX+=1
f.write("end\nskeleton\ntime 0\n")
nIDX = 0
for Bn in Bonez:
    f.write(str("%i %f %f %f %f %f %f\n" % (nIDX,
                                                        Bn.transform[0],Bn.transform[1],Bn.transform[2],
                                                        Bn.rotation[0],Bn.rotation[1],Bn.rotation[2])))
    nIDX+=1
f.write("end\ntriangles\n")
for mb in mbnModels:
    for msh in range(int(len(mb.smd)/3)):
        f.write(mb.name + "\n")
        for mmm in range(3):
            f.write(mb.smd[(msh*3)+mmm])
