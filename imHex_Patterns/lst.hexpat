enum AtlasFlag : u32{
 None = 0,
 Dynamic = 1
};
u16 StringOffset = 0;


struct Header{
char MAGIC[4];
u16 unk0;
u16 numAtlases;
u16 numTextures;
u16 flagsOffset;
u16 entriesOffset;
u16 stringsOffset;
};
struct Texture{
u32 nameOffset;
u32 nameOffset2;
char name[] @ StringOffset+nameOffset;

float topx;
float topy;

float botx;
float boty;

u16 width;
u16 height;

u16 atlasId;

u16 unk0;

}[[name(name)]];

struct LST{
Header HDR;

StringOffset = HDR.stringsOffset;
AtlasFlag atlases[HDR.numAtlases] @ HDR.flagsOffset;
Texture textures[HDR.numTextures] @ HDR.entriesOffset;

};

LST list @ 0;