from mbm import MBM

import sys


fileIn = open(sys.argv[1], "rb")
mBm_in = MBM()
mBm_in.read(fileIn)
fileOut = open(sys.argv[1] + ".obj","w")
for x in mBm_in.positions:
    fileOut.write(str("v %f %f %f\n" %(x[0],x[1],x[2])))
for x in mBm_in.normals:
    fileOut.write(str("vn %f %f %f\n" %(x[0],x[1],x[2])))
for indx,x in enumerate(mBm_in.poly):
    if(not indx % 3):
        fileOut.write(str("\nf"))
        print(indx)
    fileOut.write(str(" %i//%i" % (x+1,x+1)))
