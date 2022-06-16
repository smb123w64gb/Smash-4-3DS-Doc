import struct,binascii,sys

import os.path
def readByte(file):
    return struct.unpack("B", file.read(1))[0]
 
def readu16be(file):
    return struct.unpack(">H", file.read(2))[0]
 
def readu16le(file):
    return struct.unpack("<H", file.read(2))[0]
    
def readu32be(file):
    return struct.unpack(">I", file.read(4))[0]
 
def readu32le(file):
    return struct.unpack("<I", file.read(4))[0]

def getString(f, term=b'\0'):
    result = ""
    tmpChar = f.read(1).decode("ASCII")
    while ord(tmpChar) != 0:
        result += tmpChar
        tmpChar = f.read(1).decode("ASCII")
    return result


def updateDamit(file):
    file.seek(0,1)

def write32(file,val):
    file.write(struct.pack("<I", val))
    updateDamit(file)
def write16(file,val):
    file.write(struct.pack("<H", val))
    updateDamit(file)
def writeS16(file,val):
    file.write(struct.pack("<h", val))
    updateDamit(file)
def writeByte(file,val):
    file.write(struct.pack("B", val))
    updateDamit(file)
def writeSByte(file,val):
    file.write(struct.pack("b", val))
    updateDamit(file)
def writefloat(file,val):
    file.write(struct.pack("<f", val))
    updateDamit(file)


def fillIN(file):
    currentPOS = file.tell()
    val = 0
    while(currentPOS % 0x20):
        val += 1
        writeByte(file,0xFF)
        currentPOS = file.tell()

class mbnBone(object):
    def __init__(self,bonez):
        self.boneID = [2]
        self.boneScan = bonez
    def addBone(self,string):
        outID = 0
        notAvalable = True
        hashID = self.boneScan.getBone(string)
        if(len(self.boneID) == 0):
            notAvalable = False
            self.boneID.append(hashID)
        else:
            for b,boneHash in enumerate(self.boneID):
                if hashID == boneHash:
                    outID = b 
                    notAvalable = False
        if(notAvalable):
            self.boneID.append(hashID)
            outID = len(self.boneID) - 1
        return outID
    def writeNodes(self,file):
        if(len(self.boneID)):
            write32(file,len(self.boneID))
            for ids in  self.boneID:
                write32(file,ids)
        else:
            write32(file,1)
            write32(file,2)
        
                
        
class Bone(object):
    def __init__(self):
        self.curID = 0
        self.IDarray = []
        self.nameArray = []
        self.totalBones = 0
    def addBone(self, string):
        self.nameArray.append(string)
        self.IDarray.append(self.curID)
        self.curID += 1
    def getBone(self, string):
        ID = 0
        for b,boneName in enumerate(self.nameArray):
            if string == boneName:
                    ID = self.IDarray[b]
        if(ID == 0):
            print("%s is not in the table" % string)
        return ID

def parseBCH():
    bonez = Bone()
    f = open("normal.bch", 'rb')
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

    for modelIndex in range(modelsPointerTableEntries):
        f.seek(modelsPointerTableOffset + (modelIndex * 4))
        objectsHeaderOffset = readu32le(f) + mainHeaderOffset
        f.seek(objectsHeaderOffset + 0x70)
        skeletonOffset =readu32le(f) + mainHeaderOffset
        skeletonEntries =readu32le(f)
        skeletonNameOffset =readu32le(f) + mainHeaderOffset
        f.seek(skeletonOffset)
        bonez.totalBones = skeletonEntries
        for index in range(skeletonEntries):
            f.seek(0x5C,1)
            rtn = f.tell() + 8
            f.seek(readu32le(f) + stringTableOffset)
            bonez.addBone(getString(f))
            f.seek(rtn)
    f.close
    return bonez



    
class poly(object):
        def __init__(self,boneMan):
                self.verts = []
                self.normals = []
                self.colors =[]
                self.uv0 = []
                self.uv1 = []
                self.uv2 = []
                self.uv3 = []
                self.faces = []
                self.boneIDs = []
                self.boneWgts = []
                self.boneManage = boneMan
        def addBone(self,string):
            return self.boneManage.addBone(string)

BoneBCH = parseBCH()
   
cvsIn = open(sys.argv[1], "rb")

polys = []
ii = 0
for line in cvsIn:
    if line.startswith("Obj Name"):
            if(ii > 0):
                polys.append(data)
            data = poly(mbnBone(BoneBCH))
            ii += 1
            SubType = 0
    elif line.startswith("tex_Array:"):
        pass
    elif line.startswith("Color_Suport"):
        colorEnable = True
    elif line.startswith("UV_Num:"):
        numUVs = int(line.split(":")[1].replace("\n", ""))
    elif line.startswith("vert_Array"):
        Type = 1
    elif line.startswith("face_Array"):
        Type = 2
    elif line.startswith("Bone_Suport"):
        pass
    elif line.startswith("bone_Array"):
        Type = 3
    else:
        line = line.replace("\n", "").replace("\r", "").split(",")
        if(Type == 1):
            if(SubType == 0):
                data.verts.append(line)
                SubType += 1
            elif(SubType == 1):
                data.normals.append(line)
                SubType += 1
            elif(SubType == 2):
                data.colors.append(line)
                SubType += 1
            elif(SubType == 3):
                data.uv0.append(line)
                if(numUVs == 1):SubType = 0
                else:SubType += 1
            elif(SubType == 4):
                data.uv1.append(line)
                if(numUVs == 2):SubType = 0
                else:SubType += 1
            elif(SubType == 5):
                data.uv2.append(line)
                if(numUVs == 3):SubType = 0
                else:SubType += 1
            elif(SubType == 6):
                data.uv3.append(line)
                SubType = 0
        elif(Type == 2):
            data.faces.append(line)
        elif(Type == 3):
            flip = False
            if(len(line)%2):line.pop()
            count = 0
            IDS = []
            WGT = []
            for e in line:
                if(count < 2):
                    if(flip):
                        count += 1
                        WGT.append(e)
                        flip = False
                    else:
                        IDS.append(data.addBone(e))
                        flip = True
            data.boneIDs.append(IDS)
            data.boneWgts.append(WGT)
                
                    
polys.append(data)

f = open("normal.mbn", "wb")            

TotalVertCount = 0

for p in polys:TotalVertCount+=len(p.verts)

write16(f,6)
write16(f,0xFFFF)
write32(f,0)
write32(f,1)
write32(f,len(polys))

write32(f,5)

write32(f,0)
write32(f,0)
writefloat(f,1.0)

write32(f,1)
write32(f,2)
writefloat(f,0.007874)

#write32(f,2)
#write32(f,1)
#writefloat(f,1)

write32(f,3)
write32(f,3)
writefloat(f,0.000089)

write32(f,5)
write32(f,1)
writefloat(f,1)

write32(f,6)
write32(f,1)
writefloat(f,0.010000)

write32(f,TotalVertCount*0x18)

for p in polys:
    write32(f,1)
    p.boneManage.writeNodes(f)
    write32(f,len(p.faces)*3)
fillIN(f)
for p in polys:
    for v in range(len(p.verts)):
        for vp in p.verts[v]:
            #writeS16(f,int(float(vp)/0.000778))
            writefloat(f,float(vp))
        for vp in p.normals[v]:
            writeSByte(f,int(float(vp)/0.007874))
        writeByte(f,0)
        #for vp in p.colors[v]:
            #writeByte(f,int(float(vp)))
        for vp in p.uv0[v]:
            writeS16(f,int(float(vp)/0.000089))
        if(len(p.boneIDs)):
            for vp in p.boneIDs[v]:
                if(len(p.boneIDs[v]) == 1):
                    writeByte(f,0)
                writeByte(f,int(vp))
                
                    
            wghTime = p.boneWgts[v]
            size = int(float(wghTime[0])*100)
            writeByte(f,100-size)
            writeByte(f,size)
        else:
            write32(f,0)
fillIN(f)
addPolyVal = 0
for p in polys:
    for b in p.faces:
        for pp in b:
            write16(f,int(float(pp))-1+addPolyVal)
    addPolyVal += len(p.verts)
    fillIN(f)
