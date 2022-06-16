import struct,binascii,sys

import os.path

def updateDamit(file):
    file.seek(0,1)

def write32(file,val):
    file.write(struct.pack("<I", val))
    updateDamit(file)
def write16(file,val):
    file.write(struct.pack("<H", val))
    updateDamit(file)
def writeByte(file,val):
    file.write(struct.pack("B", val))
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
    
class poly(object):
        def __init__(self):
                self.verts = []
                self.normals = []
                self.colors =[]
                self.uv0 = []
                self.uv1 = []
                self.uv2 = []
                self.uv3 = []
                self.faces = []
                
cvsIn = open(sys.argv[1], "rb")

polys = []
ii = 0
for line in cvsIn:
    if line.startswith("Obj Name"):
            if(ii > 0):
                polys.append(data)
            data = poly()
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
            pass
polys.append(data)

f = open("normal.mbn", "wb")            

write16(f,6)
write16(f,0xFFFF)
write32(f,1)
write32(f,0)
write32(f,len(polys))
for p in polys:
    write32(f,1)
    write32(f,0)
    write32(f,len(p.faces)*3)
    write32(f,3)
    
    write32(f,0)
    write32(f,0)
    writefloat(f,1)

    #write32(f,1)
    #write32(f,0)
    #writefloat(f,1)
    
    write32(f,2)
    write32(f,1)
    writefloat(f,1)

    write32(f,3)
    write32(f,0)
    writefloat(f,1)

    write32(f,len(p.verts)*0x18)
fillIN(f)
for p in polys:
    for v in range(len(p.verts)):
        for vp in p.verts[v]:
            writefloat(f,float(vp))
        #for vp in p.normals[v]:
            #writefloat(f,float(vp))
        for vp in p.colors[v]:
            writeByte(f,int(float(vp)))
        for vp in p.uv0[v]:
            writefloat(f,float(vp))
    fillIN(f)
    for p in p.faces:
        for pp in p:
            write16(f,int(float(pp))-1)
    fillIN(f)
