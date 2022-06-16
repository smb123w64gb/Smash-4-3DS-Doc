.3ds
.arm.little
.open "code117.bin","code.bin",0x100000

.org 0x03BF934 				;redirecting the table. All of these are necessary to expand the stage table without real bound.
.dcd 0x0C0E698

.org 0x05CAAAC 				;redirecting the table
.dcd 0x0C0E698

.org 0x05CAAF4 				;redirecting the table
.dcd 0x0C0E698

.org 0x05CAB10 				;redirecting the table
.dcd 0x0C0E698


.org 0x05CAA94 				;max stage count. These are necessary so that the game does not assume values above stage id 106 are just battlefield. 
cmp r0, #0xFF

.org 0x06D61F8 				;max stage count
cmp r0, #0xFF

.org 0x0B716D8				;erasing old stage table. Just a bit of cleanup. Anything that is (107*3) or less dwords is probably safe to be moved here.  
.area 0xB71BD8-.,0x00
.endarea


.org 0x0C0E698				;moving the stage table
.arm.big
.area 0x0C0EB9C-.,0x00
	.dcd        0xF702C000, 0xCB54C000, 0x00000000, 0x0503C000, 0xE954C000, 0x00000000, 0x2205C000, 0xFF55C000, 0x00000000, 0x23F9BF00, 0x7054C000, 0x00000000, 0x8804C000, 0xDE55C000, 0x00000000, 0x6200C000, 0x6F00C000, 0x00000000, 0xB612C000, 0x4156C000, 0x00000000, 0xFE16C000, 0x7656C000, 0x00000000, 0x8914C000, 0xA914C000, 0x00000000, 0x5005C000, 0x0656C000, 0x00000000, 0x9654C000, 0x0656C000, 0x00000000, 0x3E05C000, 0x4905C000, 0x00000000, 0xC812C000, 0x4756C000, 0x00000000, 0x960BC000, 0x2056C000, 0x00000000, 0xA503C000, 0xD555C000, 0x00000000, 0x1320C000, 0xA856C000, 0x00000000, 0x441AC000, 0xB81AC000, 0x00000000, 0x640DC000, 0x6E0DC000, 0x00000000, 0x851CC000, 0x9B1CC000, 0x00000000, 0x311FC000, 0x9A56C000, 0x00000000, 0x901DC000, 0x8656C000, 0x00000000, 0xC11EC000, 0x9156C000, 0x00000000, 0x9E09C000, 0x1856C000, 0x00000000, 0x35F9BF00, 0x7A54C000, 0x00000000, 0x0B03C000, 0xEF54C000, 0x00000000, 0x8203C000, 0xBF55C000, 0x00000000, 0xB054C000, 0xBF55C000, 0x00000000, 0xAA20C000, 0xB156C000, 0x00000000, 0x4214C000, 0x5156C000, 0x00000000, 0x2A1CC000, 0x7D56C000, 0x00000000, 0x4816C000, 0x6D56C000, 0x00000000, 0xCCFFBF00, 0xA454C000, 0x00000000, 0xE714C000, 0x6456C000, 0x00000000, 0xF523C000, 0xBD56C000, 0x00000000, 0xC614C000, 0x5B56C000, 0x00000000, 0x2E11C000, 0x3556C000, 0x00000000, 0xF702C000, 0xCB54C000, 0x01000000, 0x2205C000, 0xFF55C000, 0x01000000, 0x23F9BF00, 0x7054C000, 0x01000000, 0x8804C000, 0xDE55C000, 0x01000000, 0x6200C000, 0x6F00C000, 0x01000000, 0xB612C000, 0x4156C000, 0x01000000, 0xFE16C000, 0x7656C000, 0x01000000, 0x8914C000, 0xA914C000, 0x01000000, 0x5005C000, 0x0656C000, 0x01000000, 0x9654C000, 0x0656C000, 0x01000000, 0x3E05C000, 0x4905C000, 0x01000000, 0xC812C000, 0x4756C000, 0x01000000, 0x960BC000, 0x2056C000, 0x01000000, 0xA503C000, 0xD555C000, 0x01000000, 0x1320C000, 0xA856C000, 0x01000000, 0x441AC000, 0xB81AC000, 0x01000000, 0x640DC000, 0x6E0DC000, 0x01000000, 0x851CC000, 0x9B1CC000, 0x01000000, 0x311FC000, 0x9A56C000, 0x01000000, 0x901DC000, 0x8656C000, 0x01000000, 0xC11EC000, 0x9156C000, 0x01000000, 0x9E09C000, 0x1856C000, 0x01000000, 0x35F9BF00, 0x7A54C000, 0x01000000, 0x0B03C000, 0xEF54C000, 0x01000000, 0x8203C000, 0xBF55C000, 0x01000000, 0xB054C000, 0xBF55C000, 0x01000000, 0xAA20C000, 0xB156C000, 0x01000000, 0x4214C000, 0x5156C000, 0x01000000, 0x2A1CC000, 0x7D56C000, 0x01000000, 0x4816C000, 0x6D56C000, 0x01000000, 0xCCFFBF00, 0xA454C000, 0x01000000, 0xE714C000, 0x6456C000, 0x01000000, 0xF523C000, 0xBD56C000, 0x01000000, 0xC614C000, 0x5B56C000, 0x01000000, 0x2E11C000, 0x3556C000, 0x01000000, 0xEA55C000, 0xF455C000, 0x02000000, 0xC208C000, 0x1156C000, 0x02000000, 0x4154C000, 0x38B3C000, 0x02000000, 0x5354C000, 0x38B3C000, 0x02000000, 0x4854C000, 0x00000000, 0x02000000, 0x5A54C000, 0x00000000, 0x02000000, 0x6554C000, 0x00000000, 0x02000000, 0x8054C000, 0x00000000, 0x02000000, 0x8B54C000, 0x00000000, 0x02000000, 0x3803C000, 0x4855C000, 0x03000000, 0x98D5BF00, 0x8C55C000, 0x03000000, 0x4703C000, 0x7955C000, 0x03000000, 0xF002C000, 0xC454C000, 0x03000000, 0x3A55C000, 0x4155C000, 0x03000000, 0x2703C000, 0x2855C000, 0x03000000, 0x8D03C000, 0xCA55C000, 0x03000000, 0xFB54C000, 0x0355C000, 0x03000000, 0x5955C000, 0x6955C000, 0x03000000, 0x6703C000, 0xA455C000, 0x00000000, 0x6703C000, 0xA455C000, 0x01000000, 0xBE02C000, 0xD954C000, 0x00000000, 0xBE02C000, 0xD954C000, 0x01000000, 0xCD02C000, 0x0B55C000, 0x00000000, 0xCD02C000, 0x0B55C000, 0x01000000, 0xDD02C000, 0x1C55C000, 0x00000000, 0xDD02C000, 0x1C55C000, 0x01000000, 0x5A03C000, 0x9655C000, 0x00000000, 0x5A03C000, 0x9655C000, 0x01000000, 0x8F59C000, 0x8F59C000, 0x00000000, 0x8F59C000, 0x8F59C000, 0x01000000, 0x7703C000, 0xB455C000, 0x00000000, 0x7703C000, 0xB455C000, 0x01000000, 0x5103C000, 0x8355C000, 0x00000000, 0x5103C000, 0x8355C000, 0x01000000, 0xE802C000, 0xBC54C000, 0x00000000, 0xE802C000, 0xBC54C000, 0x01000000
.endarea

.arm.little
.org 0x0C0EB9C
.area 0x0C0FD4C-., 0x00		;table for new ids. Note: this does not actually use up the entire region that I am writing to. There is probably about 200 more dwords of free space left over.
	.dcd        0x00bb1668, 0x00000000, 0x00000000, 0x00bb166C, 0x00000000, 0x00000000, 0x00bb1670, 0x00000000, 0x00000000, 0x00bb1674, 0x00000000, 0x00000000, 0x00bb1678, 0x00000000, 0x00000000, 0x00bb167C, 0x00000000, 0x00000000, 0x00bb1680, 0x00000000, 0x00000000, 0x00bb1684, 0x00000000, 0x00000000, 0x00bb1688, 0x00000000, 0x00000000, 0x00bb168C, 0x00000000, 0x00000000, 0x00bb1690, 0x00000000, 0x00000000, 0x00bb1694, 0x00000000, 0x00000000, 0x00bb1698, 0x00000000, 0x00000000, 0x00bb169C, 0x00000000, 0x00000000, 0x00bb16A0, 0x00000000, 0x00000000, 0x00bb16A4, 0x00000000, 0x00000000, 0x00bb16A8, 0x00000000, 0x00000000, 0x00bb16AC, 0x00000000, 0x00000000, 0x00bb16B0, 0x00000000, 0x00000000, 0x00bb16B4, 0x00000000, 0x00000000, 0x00bb16B8, 0x00000000, 0x00000000, 0x00bb16BC, 0x00000000, 0x00000000, 0x00bb16C0, 0x00000000, 0x00000000, 0x00bb16C4, 0x00000000, 0x00000000, 0x00bb16C8, 0x00000000, 0x00000000, 0x00bb16CC, 0x00000000, 0x00000000, 0x00bb16D0, 0x00000000, 0x00000000, 0x00bb16D4, 0x00000000, 0x00000000, 0x00bb16D8, 0x00000000, 0x00000000, 0x00bb16DC, 0x00000000, 0x00000000, 0x00bb16E0, 0x00000000, 0x00000000, 0x00bb16E4, 0x00000000, 0x00000000, 0x00bb16E8, 0x00000000, 0x00000000, 0x00bb16EC, 0x00000000, 0x00000000, 0x00bb16F0, 0x00000000, 0x00000000, 0x00bb16F4, 0x00000000, 0x00000000, 0x00bb16F8, 0x00000000, 0x00000000, 0x00bb16FC, 0x00000000, 0x00000000, 0x00bb1700, 0x00000000, 0x00000000, 0x00bb1704, 0x00000000, 0x00000000, 0x00bb1708, 0x00000000, 0x00000000, 0x00bb170C, 0x00000000, 0x00000000, 0x00bb1710, 0x00000000, 0x00000000, 0x00bb1714, 0x00000000, 0x00000000, 0x00bb1718, 0x00000000, 0x00000000, 0x00bb171C, 0x00000000, 0x00000000, 0x00bb1720, 0x00000000, 0x00000000, 0x00bb1724, 0x00000000, 0x00000000, 0x00bb1728, 0x00000000, 0x00000000, 0x00bb172C, 0x00000000, 0x00000000, 0x00bb1730, 0x00000000, 0x00000000, 0x00bb1734, 0x00000000, 0x00000000, 0x00bb1738, 0x00000000, 0x00000000, 0x00bb173C, 0x00000000, 0x00000000, 0x00bb1740, 0x00000000, 0x00000000, 0x00bb1744, 0x00000000, 0x00000000, 0x00bb1748, 0x00000000, 0x00000000, 0x00bb174C, 0x00000000, 0x00000000, 0x00bb1750, 0x00000000, 0x00000000, 0x00bb1754, 0x00000000, 0x00000000, 0x00bb1758, 0x00000000, 0x00000000, 0x00bb175C, 0x00000000, 0x00000000, 0x00bb1760, 0x00000000, 0x00000000, 0x00bb1764, 0x00000000, 0x00000000, 0x00bb1768, 0x00000000, 0x00000000, 0x00bb176C, 0x00000000, 0x00000000, 0x00bb1770, 0x00000000, 0x00000000, 0x00bb1774, 0x00000000, 0x00000000, 0x00bb1778, 0x00000000, 0x00000000, 0x00bb177C, 0x00000000, 0x00000000, 0x00bb1780, 0x00000000, 0x00000000, 0x00bb1784, 0x00000000, 0x00000000, 0x00bb1788, 0x00000000, 0x00000000, 0x00bb178C, 0x00000000, 0x00000000, 0x00bb1790, 0x00000000, 0x00000000, 0x00bb1794, 0x00000000, 0x00000000, 0x00bb1798, 0x00000000, 0x00000000, 0x00bb179C, 0x00000000, 0x00000000, 0x00bb17A0, 0x00000000, 0x00000000, 0x00bb17A4, 0x00000000, 0x00000000, 0x00bb17A8, 0x00000000, 0x00000000, 0x00bb17AC, 0x00000000, 0x00000000, 0x00bb17B0, 0x00000000, 0x00000000, 0x00bb17B4, 0x00000000, 0x00000000, 0x00bb17B8, 0x00000000, 0x00000000, 0x00bb17BC, 0x00000000, 0x00000000, 0x00bb17C0, 0x00000000, 0x00000000, 0x00bb17C4, 0x00000000, 0x00000000, 0x00bb17C8, 0x00000000, 0x00000000, 0x00bb17CC, 0x00000000, 0x00000000, 0x00bb17D0, 0x00000000, 0x00000000, 0x00bb17D4, 0x00000000, 0x00000000, 0x00bb17D8, 0x00000000, 0x00000000, 0x00bb17DC, 0x00000000, 0x00000000, 0x00bb17E0, 0x00000000, 0x00000000, 0x00bb17E4, 0x00000000, 0x00000000, 0x00bb17E8, 0x00000000, 0x00000000, 0x00bb17EC, 0x00000000, 0x00000000, 0x00bb17F0, 0x00000000, 0x00000000, 0x00bb17F4, 0x00000000, 0x00000000, 0x00bb17F8, 0x00000000, 0x00000000, 0x00bb17FC, 0x00000000, 0x00000000, 0x00bb1800, 0x00000000, 0x00000000, 0x00bb1804, 0x00000000, 0x00000000, 0x00bb1808, 0x00000000, 0x00000000, 0x00bb180C, 0x00000000, 0x00000000, 0x00bb1810, 0x00000000, 0x00000000, 0x00bb1814, 0x00000000, 0x00000000, 0x00bb1818, 0x00000000, 0x00000000, 0x00bb181C, 0x00000000, 0x00000000, 0x00bb1820, 0x00000000, 0x00000000, 0x00bb1824, 0x00000000, 0x00000000, 0x00bb1828, 0x00000000, 0x00000000, 0x00bb182C, 0x00000000, 0x00000000, 0x00bb1830, 0x00000000, 0x00000000, 0x00bb1834, 0x00000000, 0x00000000, 0x00bb1838, 0x00000000, 0x00000000, 0x00bb183C, 0x00000000, 0x00000000, 0x00bb1840, 0x00000000, 0x00000000, 0x00bb1844, 0x00000000, 0x00000000, 0x00bb1848, 0x00000000, 0x00000000, 0x00bb184C, 0x00000000, 0x00000000, 0x00bb1850, 0x00000000, 0x00000000, 0x00bb1854, 0x00000000, 0x00000000, 0x00bb1858, 0x00000000, 0x00000000, 0x00bb185C, 0x00000000, 0x00000000, 0x00bb1860, 0x00000000, 0x00000000, 0x00bb1864, 0x00000000, 0x00000000, 0x00bb1868, 0x00000000, 0x00000000, 0x00bb186C, 0x00000000, 0x00000000, 0x00bb1870, 0x00000000, 0x00000000, 0x00bb1874, 0x00000000, 0x00000000, 0x00bb1878, 0x00000000, 0x00000000, 0x00bb187C, 0x00000000, 0x00000000, 0x00bb1880, 0x00000000, 0x00000000, 0x00bb1884, 0x00000000, 0x00000000, 0x00bb1888, 0x00000000, 0x00000000, 0x00bb188C, 0x00000000, 0x00000000, 0x00bb1890, 0x00000000, 0x00000000, 0x00bb1894, 0x00000000, 0x00000000, 0x00bb1898, 0x00000000, 0x00000000, 0x00bb189C, 0x00000000, 0x00000000, 0x00bb18A0, 0x00000000, 0x00000000, 0x00bb18A4, 0x00000000, 0x00000000, 0x00bb18A8, 0x00000000, 0x00000000, 0x00bb18AC, 0x00000000, 0x00000000, 0x00bb18B0, 0x00000000, 0x00000000, 0x00bb18B4, 0x00000000, 0x00000000, 0x00bb18B8, 0x00000000, 0x00000000
	
.endarea

.org 0x0bb1668				;stage names overwriting literally useless strings in rodata. There's probably another 100 bytes or so of strings that can be overwritten in this area. I don't feel like doing math.
.db "107", 0x0, "108", 0x0, "109", 0x0, "110", 0x0, "111", 0x0, "112", 0x0, "113", 0x0, "114", 0x0, "115", 0x0, "116", 0x0, "117", 0x0, "118", 0x0, "119", 0x0, "120", 0x0, "121", 0x0, "122", 0x0, "123", 0x0, "124", 0x0, "125", 0x0, "126", 0x0, "127", 0x0, "128", 0x0, "129", 0x0, "130", 0x0, "131", 0x0, "132", 0x0, "133", 0x0, "134", 0x0, "135", 0x0, "136", 0x0, "137", 0x0, "138", 0x0, "139", 0x0, "140", 0x0, "141", 0x0, "142", 0x0, "143", 0x0, "144", 0x0, "145", 0x0, "146", 0x0, "147", 0x0, "148", 0x0, "149", 0x0, "150", 0x0, "151", 0x0, "152", 0x0, "153", 0x0, "154", 0x0, "155", 0x0, "156", 0x0, "157", 0x0, "158", 0x0, "159", 0x0, "160", 0x0, "161", 0x0, "162", 0x0, "163", 0x0, "164", 0x0, "165", 0x0, "166", 0x0, "167", 0x0, "168", 0x0, "169", 0x0, "170", 0x0, "171", 0x0, "172", 0x0, "173", 0x0, "174", 0x0, "175", 0x0, "176", 0x0, "177", 0x0, "178", 0x0, "179", 0x0, "180", 0x0, "181", 0x0, "182", 0x0, "183", 0x0, "184", 0x0, "185", 0x0, "186", 0x0, "187", 0x0, "188", 0x0, "189", 0x0, "190", 0x0, "191", 0x0, "192", 0x0, "193", 0x0, "194", 0x0, "195", 0x0, "196", 0x0, "197", 0x0, "198", 0x0, "199", 0x0, "200", 0x0, "201", 0x0, "202", 0x0, "203", 0x0, "204", 0x0, "205", 0x0, "206", 0x0, "207", 0x0, "208", 0x0, "209", 0x0, "210", 0x0, "211", 0x0, "212", 0x0, "213", 0x0, "214", 0x0, "215", 0x0, "216", 0x0, "217", 0x0, "218", 0x0, "219", 0x0, "220", 0x0, "221", 0x0, "222", 0x0, "223", 0x0, "224", 0x0, "225", 0x0, "226", 0x0, "227", 0x0, "228", 0x0, "229", 0x0, "230", 0x0, "231", 0x0, "232", 0x0, "233", 0x0, "234", 0x0, "235", 0x0, "236", 0x0, "237", 0x0, "238", 0x0, "239", 0x0, "240", 0x0, "241", 0x0, "242", 0x0, "243", 0x0, "244", 0x0, "245", 0x0, "246", 0x0, "247", 0x0, "248", 0x0, "249", 0x0, "250", 0x0, "251", 0x0, "252", 0x0, "253", 0x0, "254", 0x0, "255"

.close