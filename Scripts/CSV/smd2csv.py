import sys
import struct
import array
import binascii

smd = open(sys.argv[1], "r")
cvs = open(sys.argv[1].replace(".smd",".csv"), "w")

class poly(object):
        def __init__(self,name = ""):
                self.name = name
                self.verts = []
                self.normals = []
                self.uv0 = []
                self.faces = []
                self.boneName = []
                self.boneWeght = []
                self.raw = []
        def genFaces(self):
                faceArray = []
                
                for b in self.raw:
                        if(not b in faceArray):
                                faceArray.append(b)
                                raw = b.split(" ")
                                raw.pop(0)
                                raw[-1] = raw[-1].strip()
                                raw = filter(None,raw)
                                Vert = []
                                Norm = []
                                UV = []
                                BoneName = []
                                BoneWeght = []
                                for idx,x in enumerate(raw):
                                        if(idx < 3):
                                                Vert.append(x)
                                        elif(idx<6):
                                                Norm.append(x)
                                        elif(idx<8):
                                                UV.append(x)
                                        elif(idx==8):
                                                bmode = 0
                                        else:
                                                if(bmode == 0):
                                                        bmode = 1
                                                        BoneName.append(boneNameArray[int(x)])
                                                elif(bmode == 1):
                                                        BoneWeght.append(x)
                                                        bmode = 0
                                self.verts.append(Vert)
                                self.normals.append(Norm)
                                self.uv0.append(UV)
                                self.boneName.append(BoneName)
                                self.boneWeght.append(BoneWeght)
                print ("FaceCouB4 = %i" % len(self.raw))
                print ("FaceCount = %i" % len(faceArray))
                #print self.name
                #print("VertCount = %i" % len(self.verts))
                #print("FaceCount = %i" % (len(self.verts)/3))
                CurFace = 0
                for x in range((len(self.raw)/3)):
                        face = []
                        for y in range(3):
                                face.append(1 + faceArray.index(self.raw[CurFace]))
                                CurFace +=1
                        self.faces.append(face)
                         

polys = {}
boneNameArray =[]
Mode = 0
globName = ""
for line in smd:
        
        if line.startswith("end"):
                Mode = 0 #Dont want to break anything
        elif line.startswith("nodes"):
                Mode = 1
        elif line.startswith("triangles"):
                Mode = 2
                inx = 0
        elif Mode == 1:
                boneNameArray.append(line.split(" ")[1].replace("\"", "").strip())
        elif Mode == 2:
                if inx == 0:
                        if(not polys.has_key(line)):
                                polys[line] = poly(line.strip())
                                print "NAME:"+line
                                globName = line
                        else:
                                globName = line
                        inx+=1
                else:
                        
                        polys[globName].raw.append(line)
                        #print line
                        inx+= 1
                        if(inx == 4):inx = 0
                        
        else:
                pass
for pol in polys:
        polys[pol].genFaces()
for pol in polys:
        obj = polys[pol]
        cvs.write(str("Obj Name:%s\nBone_Suport\nUV_Num:1\nvert_Array\n" % obj.name))
        for idx,v in enumerate(obj.verts):
                n = obj.normals[idx]
                u = obj.uv0[idx]
                
                cvs.write(str("%s,%s,%s\n" % (v[0],v[1],v[2])))
                cvs.write(str("%s,%s,%s\n" % (n[0],n[1],n[2])))
                cvs.write(str("127.0,127.0,127.0,127.0\n"))
                cvs.write(str("%s,%s\n" % (u[0],u[1])))
        cvs.write(str("face_Array\n"))
        for f in obj.faces:
                cvs.write(str("%i,%i,%i\n" % (f[0],f[1],f[2])))
        cvs.write(str("bone_Array\n"))
        
        for z in range(len(obj.boneName)):
                bnName = ""
                i = obj.boneName[z]
                w = obj.boneWeght[z]
                for f in range(len(i)):
                        bnName+=i[f] + "," + w[f] + ","
                cvs.write(bnName + " \n")
'''       

















#Read in obj and other cleaning
for line in objs:
        if line.startswith("o "):
                if(ii > 0):
                        polys.append(data)
                data = obj()
                data.name = line.split(" ")[1].replace("\n", "")

                ii += 1
        if line.startswith("v "):
                v = line.split(" ")
                v.pop(0)
                v.append(v.pop().replace("\n", ""))
                VERTS.append(v)
        if line.startswith("vt "):
                vt = line.split(" ")
                vt.pop(0)
                vt.append(vt.pop().replace("\n", ""))
                UVS.append(vt)
        if line.startswith("vn "):
                nr = line.split(" ")
                nr.pop(0)
                nr.append(nr.pop().replace("\n", ""))
                NORMS.append(nr)
        if line.startswith("f "):
                f = line.split(" ")
                f.pop(0)
                if(len(f) > 3):
                        print("Get your untriangled Swine out of here")
                f.append(f.pop().replace("\n", ""))
                data.faces.append(f)
polys.append(data)

cleanedCSV = []

#No convert it to be sain
for o in polys:
        polyClean = poly()
        cleanedCSV.append(polyClean)
        polyClean.name = o.name
        print(o.name)
        cleanFaces = []
        for fac in o.faces:
                madeFace = []
                for fid in fac:
                        freePass = True
                        for indx,ft in enumerate(cleanFaces):
                                if ft == fid:
                                        madeFace.append(indx + 1)
                                        freePass = False
                        if(freePass):
                                cleanFaces.append(fid)
                                madeFace.append(len(cleanFaces))
                polyClean.faces.append(madeFace)
        for ddd in cleanFaces:
                vals = ddd.split("/")
                polyClean.verts.append(VERTS[int(vals[0])])
                if(vals[1] == ""):
                        polyClean.uv0.append([0,0])
                else:
                        polyClean.uv0.append(UVS[int(vals[1])])
                polyClean.normals.append(NORMS[int(vals[2])])
        print("\tVertCount:%i" % (len(polyClean.verts)))
        print("\tFaceCount:%i" % len(polyClean.faces))
        
for obj in cleanedCSV:
        cvs.write(str("Obj Name:%s\nUV_Num:1\nvert_Array\n" % obj.name))
        for idx,v in enumerate(obj.verts):
                n = obj.normals[idx]
                u = obj.uv0[idx]
                cvs.write(str("%s,%s,%s\n" % (v[0],v[1],v[2])))
                cvs.write(str("%s,%s,%s\n" % (n[0],n[1],n[2])))
                cvs.write(str("127.0,127.0,127.0,127.0\n"))
                cvs.write(str("%s,%s\n" % (u[0],u[1])))
        cvs.write(str("face_Array\n"))
        for f in obj.faces:
                cvs.write(str("%i,%i,%i\n" % (f[0],f[1],f[2])))
                                
'''           
                         
                                        
                        
                
                

