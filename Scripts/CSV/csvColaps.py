import struct,binascii,sys

import os.path

    
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
                self.bones = []
                
cvsIn = open(sys.argv[1], "r")

colaps = poly()
ii = 0
addpoly = 0
curAddPoly = 0
for line in cvsIn:
    if line.startswith("Obj Name"):
            if(ii > 0):
                curAddPoly = addpoly
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
                addpoly += 1
                colaps.verts.append(line)
                SubType += 1
            elif(SubType == 1):
                colaps.normals.append(line)
                SubType += 1
            elif(SubType == 2):
                colaps.colors.append(line)
                SubType += 1
            elif(SubType == 3):
                colaps.uv0.append(line)
                if(numUVs == 1):SubType = 0
                else:SubType += 1
            elif(SubType == 4):
                colaps.uv1.append(line)
                if(numUVs == 2):SubType = 0
                else:SubType += 1
            elif(SubType == 5):
                colaps.uv2.append(line)
                if(numUVs == 3):SubType = 0
                else:SubType += 1
            elif(SubType == 6):
                colaps.uv3.append(line)
                SubType = 0
        elif(Type == 2):
            for e in line:
                colaps.faces.append(float(e) +curAddPoly)
        elif(Type == 3):
            line.pop()
            colaps.bones.append(line)


f = open("mush.csv", "w")            

f.write("Obj Name:MUSH\n")
f.write("UV_Num:1\n")
f.write("vert_Array\n")
for v in range(len(colaps.verts)):
    f.write("%s\n" % str(colaps.verts[v]).replace("'","").replace("[","").replace("]",""))
    f.write("%s\n" % str(colaps.normals[v]).replace("'","").replace("[","").replace("]",""))
    f.write("%s\n" % str(colaps.colors[v]).replace("'","").replace("[","").replace("]",""))
    f.write("%s\n" % str(colaps.uv0[v]).replace("'","").replace("[","").replace("]",""))
f.write("face_Array\n")
for p in range(0,len(colaps.faces),3):
    f.write("%.1f, %.1f, %.1f\n" %(colaps.faces[p],colaps.faces[p+1],colaps.faces[p+2]))
f.write("bone_Array\n")
for b in colaps.bones:
    f.write("%s\n" % str(b).replace("'","").replace("[","").replace("]",""))
