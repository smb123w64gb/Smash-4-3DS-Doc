# {enemy,fighter,assistpokemon/item_,stage}
import sys, struct, zlib, subprocess, os
#print 'Getting strings...'
outdir = sys.argv[2]
if not os.path.exists(outdir):
    os.mkdir(outdir)
by_crc = {}
def try_crc(str):
    crc = zlib.crc32(str.encode("utf-8")) & 0xffffffff
    by_crc.setdefault(crc, set()).add(str.encode("utf-8"))
    #print "This is by_crc from try_crc: ", by_crc

fp = open(sys.argv[1], 'rb') # opens cro.sarc
assert fp.read(4).decode("utf-8") == 'SARC' # confirms that cro.sarc is a sarc
num_files, = struct.unpack('<I', fp.read(4)) # reads the byte after magic?

for i in range(num_files):
    print(i)
    fp.seek(0x10 + 0x10 * i)
    crc, off, flags, size = struct.unpack('<IIII', fp.read(16))
    print( 'crc: ', crc, 'off: ', off, 'flags: ', flags, 'size: ', size)
    fp.seek(off)
    compressed = fp.read(size)
    data = zlib.decompress(compressed)
    offset = struct.unpack('<I', data[0xC0:0xC4])[0]
    name = data[offset:offset+data[offset:].decode("utf-8", "ignore").find('\0')].decode("utf-8") #gets offset of filename from header and file. Bytes C0-C4 determine the location of the string for the filename.
    
    try_crc('fighter/' + name)
    try_crc('stage/final/' + name)
    try_crc('stage/' + name)
    try_crc('menu/' + name)
    try_crc('enemy/' + name)
    try_crc('minigame/' + name)
    try_crc('assistpokemon/' + name)
    
    strings = by_crc.get(crc, set())
    print(strings)
    #continue
    if len(strings) >= 2:
        raise Exception('Multiple CRC possibilities for %08x' % crc)
    elif len(strings) == 1:
        fn = strings.pop()
        #print "This is fn: ", fn, "this is crc: ", hex(crc), "this is off: ", hex(off), "This is i: ", i
        assert not fn.decode("utf-8").startswith('/')
        outfn = os.path.join(outdir, fn.decode("utf-8"))
        if not os.path.exists(os.path.dirname(outfn)):
            os.makedirs(os.path.dirname(outfn))
    else:
        outfn = os.path.join(outdir, 'unkcrc-%08x-%s' % (crc, name))
 
    open(outfn, 'wb').write(data)
