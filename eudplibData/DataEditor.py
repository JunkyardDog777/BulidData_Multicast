from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x66450C, Add, -524288),# units:Graphics  index:22    from 86 To 78
        SetMemory(0x664514, Add, 14848),# units:Graphics  index:29    from 70 To 128
        SetMemory(0x664530, Add, 0),# units:Graphics  index:57    from 12 To 12
        SetMemory(0x664540, Add, 2293760),# units:Graphics  index:74    from 46 To 81
        SetMemory(0x664550, Add, 2181038080),# units:Graphics  index:91    from 43 To 173
        SetMemory(0x664554, Add, 85),# units:Graphics  index:92    from 43 To 128
        SetMemory(0x664554, Add, -4096),# units:Graphics  index:93    from 198 To 182
        SetMemory(0x664554, Add, 1006632960),# units:Graphics  index:95    from 114 To 174
        SetMemory(0x664558, Add, -4980736),# units:Graphics  index:98    from 191 To 115
        SetMemory(0x66456C, Add, 2483027968),# units:Graphics  index:119    from 43 To 191
        SetMemory(0x664570, Add, 11520),# units:Graphics  index:121    from 43 To 88
        SetMemory(0x664574, Add, 503316480),# units:Graphics  index:127    from 99 To 129
        SetMemory(0x664578, Add, -126),# units:Graphics  index:128    from 207 To 81
        SetMemory(0x664578, Add, -20480),# units:Graphics  index:129    from 208 To 128
        SetMemory(0x6645C0, Add, -18),# units:Graphics  index:200    from 196 To 178
        SetMemory(0x6645C4, Add, 256),# units:Graphics  index:205    from 173 To 174
        SetMemory(0x6645C4, Add, 196608),# units:Graphics  index:206    from 174 To 177
        SetMemory(0x6607EC, Add, -1179648),# units:Subunit 1  index:23    from 24 To 6
        SetMemory(0x66128C, Add, -325),# units:Construction Animation  index:119    from 325 To 0
        SetMemory(0x661294, Add, -325),# units:Construction Animation  index:121    from 325 To 0
        SetMemory(0x6612AC, Add, -104),# units:Construction Animation  index:127    from 104 To 0
        SetMemory(0x6613E4, Add, 0),# units:Construction Animation  index:205    from 0 To 0
        SetMemory(0x660628, Add, -1280),# units:Unit Direction  index:57    from 13 To 8
        SetMemory(0x660664, Add, 536870912),# units:Unit Direction  index:119    from 0 To 32
        SetMemory(0x660668, Add, 8192),# units:Unit Direction  index:121    from 0 To 32
        SetMemory(0x66066C, Add, 0),# units:Unit Direction  index:127    from 0 To 0
        SetMemory(0x660670, Add, 32),# units:Unit Direction  index:128    from 0 To 32
        SetMemory(0x660670, Add, 8192),# units:Unit Direction  index:129    from 0 To 32
        SetMemory(0x6606BC, Add, 0),# units:Unit Direction  index:204    from 0 To 0
        SetMemory(0x6606BC, Add, 8192),# units:Unit Direction  index:205    from 0 To 32
        SetMemory(0x6647F8, Add, -65536),# units:Shield Enable  index:74    from 1 To 0
        SetMemory(0x664808, Add, 16777216),# units:Shield Enable  index:91    from 0 To 1
        SetMemory(0x66480C, Add, 1),# units:Shield Enable  index:92    from 0 To 1
        SetMemory(0x66480C, Add, 256),# units:Shield Enable  index:93    from 0 To 1
        SetMemory(0x66480C, Add, 16777216),# units:Shield Enable  index:95    from 0 To 1
        SetMemory(0x664810, Add, -65536),# units:Shield Enable  index:98    from 1 To 0
        SetMemory(0x66482C, Add, 0),# units:Shield Enable  index:127    from 0 To 0
        SetMemory(0x664830, Add, 0),# units:Shield Enable  index:129    from 0 To 0
        SetMemory(0x66487C, Add, 256),# units:Shield Enable  index:205    from 0 To 1
        SetMemory(0x660E94, Add, 20),# units:Shield Amount  index:74    from 80 To 100
        SetMemory(0x660EB4, Add, 9830400),# units:Shield Amount  index:91    from 100 To 250
        SetMemory(0x660EB8, Add, 300),# units:Shield Amount  index:92    from 100 To 400
        SetMemory(0x660EB8, Add, 9830400),# units:Shield Amount  index:93    from 100 To 250
        SetMemory(0x660EBC, Add, 19660800),# units:Shield Amount  index:95    from 100 To 400
        SetMemory(0x660EC4, Add, 40),# units:Shield Amount  index:98    from 60 To 100
        SetMemory(0x660EFC, Add, 0),# units:Shield Amount  index:127    from 100 To 100
        SetMemory(0x660F00, Add, -6553600),# units:Shield Amount  index:129    from 100 To 0
        SetMemory(0x660F98, Add, 19660800),# units:Shield Amount  index:205    from 100 To 400
        SetMemory(0x6623A0, Add, -25600),# units:Hit Points  index:20    from 51200 To 25600
        SetMemory(0x6623A8, Add, -179200),# units:Hit Points  index:22    from 204800 To 25600
        SetMemory(0x6623AC, Add, -6400),# units:Hit Points  index:23    from 102400 To 96000
        SetMemory(0x6623C4, Add, -148480),# units:Hit Points  index:29    from 179200 To 30720
        SetMemory(0x6623E4, Add, -8192),# units:Hit Points  index:37    from 8960 To 768
        SetMemory(0x662478, Add, 35840),# units:Hit Points  index:74    from 10240 To 46080
        SetMemory(0x6624B4, Add, 240384),# units:Hit Points  index:89    from 15360 To 255744
        SetMemory(0x6624BC, Add, 32000),# units:Hit Points  index:91    from 32000 To 64000
        SetMemory(0x6624C0, Add, 19200),# units:Hit Points  index:92    from 32000 To 51200
        SetMemory(0x6624C4, Add, 48640),# units:Hit Points  index:93    from 15360 To 64000
        SetMemory(0x6624CC, Add, 87040),# units:Hit Points  index:95    from 15360 To 102400
        SetMemory(0x6624D8, Add, 230144),# units:Hit Points  index:98    from 25600 To 255744
        SetMemory(0x66252C, Add, 20479),# units:Hit Points  index:119    from 1 To 20480
        SetMemory(0x662534, Add, 20479),# units:Hit Points  index:121    from 1 To 20480
        SetMemory(0x66254C, Add, -481280),# units:Hit Points  index:127    from 512000 To 30720
        SetMemory(0x662550, Add, -2544640),# units:Hit Points  index:128    from 2560000 To 15360
        SetMemory(0x662554, Add, 253439744),# units:Hit Points  index:129    from 2560000 To 255999744
        SetMemory(0x662610, Add, -25599744),# units:Hit Points  index:176    from 25600000 To 256
        SetMemory(0x662670, Add, 25395200),# units:Hit Points  index:200    from 204800 To 25600000
        SetMemory(0x662684, Add, -25497600),# units:Hit Points  index:205    from 25600000 To 102400
        SetMemory(0x6626D8, Add, -204544),# units:Hit Points  index:226    from 204800 To 256
        SetMemory(0x6626DC, Add, -204544),# units:Hit Points  index:227    from 204800 To 256
        SetMemory(0x663164, Add, -786432),# units:Elevation Level  index:22    from 16 To 4
        SetMemory(0x66316C, Add, 512),# units:Elevation Level  index:29    from 16 To 18
        SetMemory(0x663188, Add, -2816),# units:Elevation Level  index:57    from 16 To 5
        SetMemory(0x6631A8, Add, -67108864),# units:Elevation Level  index:91    from 18 To 14
        SetMemory(0x6631AC, Add, -14),# units:Elevation Level  index:92    from 18 To 4
        SetMemory(0x6631AC, Add, 2560),# units:Elevation Level  index:93    from 4 To 14
        SetMemory(0x6631AC, Add, 234881024),# units:Elevation Level  index:95    from 4 To 18
        SetMemory(0x6631B0, Add, -917504),# units:Elevation Level  index:98    from 18 To 4
        SetMemory(0x6631CC, Add, 234881024),# units:Elevation Level  index:127    from 4 To 18
        SetMemory(0x6631D0, Add, 3584),# units:Elevation Level  index:129    from 4 To 18
        SetMemory(0x663218, Add, 8),# units:Elevation Level  index:200    from 4 To 12
        SetMemory(0x66321C, Add, 11),# units:Elevation Level  index:204    from 1 To 12
        SetMemory(0x66321C, Add, 3584),# units:Elevation Level  index:205    from 4 To 18
        SetMemory(0x66321C, Add, 524288),# units:Elevation Level  index:206    from 4 To 12
        SetMemory(0x663228, Add, -67108864),# units:Elevation Level  index:219    from 4 To 0
        SetMemory(0x660FDC, Add, -8650752),# units:Unknown (old Movement)  index:22    from 197 To 65
        SetMemory(0x660FDC, Add, 2147483648),# units:Unknown (old Movement)  index:23    from 65 To 193
        SetMemory(0x661010, Add, 8388608),# units:Unknown (old Movement)  index:74    from 65 To 193
        SetMemory(0x661020, Add, 0),# units:Unknown (old Movement)  index:91    from 197 To 197
        SetMemory(0x661024, Add, -132),# units:Unknown (old Movement)  index:92    from 197 To 65
        SetMemory(0x661024, Add, 33792),# units:Unknown (old Movement)  index:93    from 65 To 197
        SetMemory(0x661024, Add, 2214592512),# units:Unknown (old Movement)  index:95    from 65 To 197
        SetMemory(0x661028, Add, -8650752),# units:Unknown (old Movement)  index:98    from 197 To 65
        SetMemory(0x66103C, Add, 3238002688),# units:Unknown (old Movement)  index:119    from 0 To 193
        SetMemory(0x661040, Add, 49408),# units:Unknown (old Movement)  index:121    from 0 To 193
        SetMemory(0x661044, Add, 3305111552),# units:Unknown (old Movement)  index:127    from 0 To 197
        SetMemory(0x661048, Add, -4),# units:Unknown (old Movement)  index:128    from 197 To 193
        SetMemory(0x661094, Add, 50432),# units:Unknown (old Movement)  index:205    from 0 To 197
        SetMemory(0x663DD0, Add, -1),# units:Rank/Sublabel  index:0    from 2 To 1
        SetMemory(0x663DD4, Add, 0),# units:Rank/Sublabel  index:7    from 1 To 1
        SetMemory(0x663DE4, Add, -16),# units:Rank/Sublabel  index:20    from 17 To 1
        SetMemory(0x663DE4, Add, -917504),# units:Rank/Sublabel  index:22    from 15 To 1
        SetMemory(0x663DE4, Add, -301989888),# units:Rank/Sublabel  index:23    from 19 To 1
        SetMemory(0x663DEC, Add, -2816),# units:Rank/Sublabel  index:29    from 21 To 10
        SetMemory(0x663E18, Add, -720896),# units:Rank/Sublabel  index:74    from 12 To 1
        SetMemory(0x663E28, Add, 201326592),# units:Rank/Sublabel  index:91    from 0 To 12
        SetMemory(0x663E2C, Add, 12),# units:Rank/Sublabel  index:92    from 0 To 12
        SetMemory(0x663E2C, Add, 3072),# units:Rank/Sublabel  index:93    from 0 To 12
        SetMemory(0x663E2C, Add, 201326592),# units:Rank/Sublabel  index:95    from 0 To 12
        SetMemory(0x663E30, Add, -524288),# units:Rank/Sublabel  index:98    from 8 To 0
        SetMemory(0x663E44, Add, 100663296),# units:Rank/Sublabel  index:119    from 0 To 6
        SetMemory(0x663E48, Add, 1536),# units:Rank/Sublabel  index:121    from 0 To 6
        SetMemory(0x663E4C, Add, 167772160),# units:Rank/Sublabel  index:127    from 0 To 10
        SetMemory(0x663E50, Add, 1),# units:Rank/Sublabel  index:128    from 0 To 1
        SetMemory(0x663E50, Add, 512),# units:Rank/Sublabel  index:129    from 0 To 2
        SetMemory(0x663E9C, Add, 3072),# units:Rank/Sublabel  index:205    from 0 To 12
        SetMemory(0x662EF8, Add, -256),# units:Comp AI Idle  index:89    from 2 To 1
        SetMemory(0x662EF8, Add, -352321536),# units:Comp AI Idle  index:91    from 23 To 2
        SetMemory(0x662EFC, Add, 35),# units:Comp AI Idle  index:92    from 23 To 58
        SetMemory(0x662F00, Add, -65536),# units:Comp AI Idle  index:98    from 2 To 1
        SetMemory(0x662F14, Add, -2600468480),# units:Comp AI Idle  index:119    from 156 To 1
        SetMemory(0x662F18, Add, -39680),# units:Comp AI Idle  index:121    from 156 To 1
        SetMemory(0x662F1C, Add, -2583691264),# units:Comp AI Idle  index:127    from 156 To 2
        SetMemory(0x662F20, Add, -95),# units:Comp AI Idle  index:128    from 97 To 2
        SetMemory(0x662F20, Add, -18944),# units:Comp AI Idle  index:129    from 97 To 23
        SetMemory(0x662F68, Add, -154),# units:Comp AI Idle  index:200    from 156 To 2
        SetMemory(0x662F6C, Add, -21),# units:Comp AI Idle  index:204    from 23 To 2
        SetMemory(0x662F6C, Add, -5376),# units:Comp AI Idle  index:205    from 23 To 2
        SetMemory(0x662F6C, Add, -1376256),# units:Comp AI Idle  index:206    from 23 To 2
        SetMemory(0x662F6C, Add, 1962934272),# units:Comp AI Idle  index:207    from 23 To 140
        SetMemory(0x662F78, Add, -1241513984),# units:Comp AI Idle  index:219    from 97 To 23
        SetMemory(0x6622C0, Add, -42240),# units:Human AI Idle  index:89    from 166 To 1
        SetMemory(0x6622C0, Add, -352321536),# units:Human AI Idle  index:91    from 23 To 2
        SetMemory(0x6622C4, Add, 35),# units:Human AI Idle  index:92    from 23 To 58
        SetMemory(0x6622C4, Add, -41984),# units:Human AI Idle  index:93    from 166 To 2
        SetMemory(0x6622C4, Add, -2399141888),# units:Human AI Idle  index:95    from 166 To 23
        SetMemory(0x6622C8, Add, -65536),# units:Human AI Idle  index:98    from 2 To 1
        SetMemory(0x6622DC, Add, -369098752),# units:Human AI Idle  index:119    from 23 To 1
        SetMemory(0x6622E0, Add, -5632),# units:Human AI Idle  index:121    from 23 To 1
        SetMemory(0x6622E4, Add, -352321536),# units:Human AI Idle  index:127    from 23 To 2
        SetMemory(0x6622E8, Add, -95),# units:Human AI Idle  index:128    from 97 To 2
        SetMemory(0x6622E8, Add, -18944),# units:Human AI Idle  index:129    from 97 To 23
        SetMemory(0x662330, Add, 164),# units:Human AI Idle  index:200    from 23 To 187
        SetMemory(0x662334, Add, -21),# units:Human AI Idle  index:204    from 23 To 2
        SetMemory(0x662334, Add, -1376256),# units:Human AI Idle  index:206    from 23 To 2
        SetMemory(0x662340, Add, -1241513984),# units:Human AI Idle  index:219    from 97 To 23
        SetMemory(0x6648F0, Add, -42240),# units:Return to Idle  index:89    from 166 To 1
        SetMemory(0x6648F0, Add, -352321536),# units:Return to Idle  index:91    from 23 To 2
        SetMemory(0x6648F4, Add, 35),# units:Return to Idle  index:92    from 23 To 58
        SetMemory(0x6648F4, Add, -41984),# units:Return to Idle  index:93    from 166 To 2
        SetMemory(0x6648F4, Add, -2399141888),# units:Return to Idle  index:95    from 166 To 23
        SetMemory(0x6648F8, Add, -65536),# units:Return to Idle  index:98    from 2 To 1
        SetMemory(0x66490C, Add, -369098752),# units:Return to Idle  index:119    from 23 To 1
        SetMemory(0x664910, Add, -5632),# units:Return to Idle  index:121    from 23 To 1
        SetMemory(0x664914, Add, -352321536),# units:Return to Idle  index:127    from 23 To 2
        SetMemory(0x664918, Add, -95),# units:Return to Idle  index:128    from 97 To 2
        SetMemory(0x664918, Add, -18944),# units:Return to Idle  index:129    from 97 To 23
        SetMemory(0x664960, Add, 164),# units:Return to Idle  index:200    from 23 To 187
        SetMemory(0x664964, Add, -21),# units:Return to Idle  index:204    from 23 To 2
        SetMemory(0x664964, Add, -1376256),# units:Return to Idle  index:206    from 23 To 2
        SetMemory(0x664970, Add, -1241513984),# units:Return to Idle  index:219    from 97 To 23
        SetMemory(0x663378, Add, -47872),# units:Attack Unit  index:89    from 188 To 1
        SetMemory(0x663378, Add, -218103808),# units:Attack Unit  index:91    from 23 To 10
        SetMemory(0x66337C, Add, 36),# units:Attack Unit  index:92    from 23 To 59
        SetMemory(0x66337C, Add, -45568),# units:Attack Unit  index:93    from 188 To 10
        SetMemory(0x66337C, Add, -2986344448),# units:Attack Unit  index:95    from 188 To 10
        SetMemory(0x663380, Add, -589824),# units:Attack Unit  index:98    from 10 To 1
        SetMemory(0x663394, Add, -218103808),# units:Attack Unit  index:119    from 23 To 10
        SetMemory(0x663398, Add, -3328),# units:Attack Unit  index:121    from 23 To 10
        SetMemory(0x66339C, Add, -218103808),# units:Attack Unit  index:127    from 23 To 10
        SetMemory(0x6633A0, Add, -13),# units:Attack Unit  index:128    from 23 To 10
        SetMemory(0x6633A0, Add, 0),# units:Attack Unit  index:129    from 23 To 23
        SetMemory(0x6633E8, Add, -13),# units:Attack Unit  index:200    from 23 To 10
        SetMemory(0x6633EC, Add, -13),# units:Attack Unit  index:204    from 23 To 10
        SetMemory(0x6633EC, Add, -3328),# units:Attack Unit  index:205    from 23 To 10
        SetMemory(0x6633EC, Add, -851968),# units:Attack Unit  index:206    from 23 To 10
        SetMemory(0x663AA8, Add, -47872),# units:Attack Move  index:89    from 188 To 1
        SetMemory(0x663AA8, Add, -352321536),# units:Attack Move  index:91    from 23 To 2
        SetMemory(0x663AAC, Add, 35),# units:Attack Move  index:92    from 23 To 58
        SetMemory(0x663AAC, Add, -47616),# units:Attack Move  index:93    from 188 To 2
        SetMemory(0x663AAC, Add, -3120562176),# units:Attack Move  index:95    from 188 To 2
        SetMemory(0x663AB0, Add, -65536),# units:Attack Move  index:98    from 2 To 1
        SetMemory(0x663AC4, Add, -369098752),# units:Attack Move  index:119    from 23 To 1
        SetMemory(0x663AC8, Add, -5632),# units:Attack Move  index:121    from 23 To 1
        SetMemory(0x663ACC, Add, -352321536),# units:Attack Move  index:127    from 23 To 2
        SetMemory(0x663AD0, Add, -21),# units:Attack Move  index:128    from 23 To 2
        SetMemory(0x663AD0, Add, 0),# units:Attack Move  index:129    from 23 To 23
        SetMemory(0x663B18, Add, -21),# units:Attack Move  index:200    from 23 To 2
        SetMemory(0x663B1C, Add, -21),# units:Attack Move  index:204    from 23 To 2
        SetMemory(0x663B1C, Add, -5376),# units:Attack Move  index:205    from 23 To 2
        SetMemory(0x663B1C, Add, -1376256),# units:Attack Move  index:206    from 23 To 2
        SetMemory(0x6636CC, Add, -1),# units:Ground Weapon  index:20    from 1 To 0
        SetMemory(0x6636CC, Add, -8519680),# units:Ground Weapon  index:22    from 130 To 0
        SetMemory(0x6636D4, Add, -1280),# units:Ground Weapon  index:29    from 21 To 16
        SetMemory(0x663700, Add, -4784128),# units:Ground Weapon  index:74    from 86 To 13
        SetMemory(0x663710, Add, -268435456),# units:Ground Weapon  index:91    from 130 To 114
        SetMemory(0x663714, Add, -4096),# units:Ground Weapon  index:93    from 130 To 114
        SetMemory(0x663714, Add, -922746880),# units:Ground Weapon  index:95    from 130 To 75
        SetMemory(0x66372C, Add, -184549376),# units:Ground Weapon  index:119    from 130 To 119
        SetMemory(0x663730, Add, -3072),# units:Ground Weapon  index:121    from 130 To 118
        SetMemory(0x663734, Add, 0),# units:Ground Weapon  index:127    from 130 To 130
        SetMemory(0x663738, Add, -117),# units:Ground Weapon  index:128    from 130 To 13
        SetMemory(0x663784, Add, -14080),# units:Ground Weapon  index:205    from 130 To 75
        SetMemory(0x6645F4, Add, 65536),# units:Max Ground Hits  index:22    from 0 To 1
        SetMemory(0x664638, Add, 16777216),# units:Max Ground Hits  index:91    from 0 To 1
        SetMemory(0x66463C, Add, 256),# units:Max Ground Hits  index:93    from 0 To 1
        SetMemory(0x66463C, Add, 16777216),# units:Max Ground Hits  index:95    from 0 To 1
        SetMemory(0x664654, Add, 16777216),# units:Max Ground Hits  index:119    from 0 To 1
        SetMemory(0x664658, Add, 256),# units:Max Ground Hits  index:121    from 0 To 1
        SetMemory(0x66465C, Add, 16777216),# units:Max Ground Hits  index:127    from 0 To 1
        SetMemory(0x664660, Add, 1),# units:Max Ground Hits  index:128    from 0 To 1
        SetMemory(0x6646AC, Add, 256),# units:Max Ground Hits  index:205    from 0 To 1
        SetMemory(0x6616F4, Add, -1),# units:Air Weapon  index:20    from 1 To 0
        SetMemory(0x6616F4, Add, -8519680),# units:Air Weapon  index:22    from 130 To 0
        SetMemory(0x6616FC, Add, 27648),# units:Air Weapon  index:29    from 22 To 130
        SetMemory(0x661738, Add, -251658240),# units:Air Weapon  index:91    from 130 To 115
        SetMemory(0x66173C, Add, -3840),# units:Air Weapon  index:93    from 130 To 115
        SetMemory(0x66173C, Add, -905969664),# units:Air Weapon  index:95    from 130 To 76
        SetMemory(0x661740, Add, 1966080),# units:Air Weapon  index:98    from 100 To 130
        SetMemory(0x661754, Add, -184549376),# units:Air Weapon  index:119    from 130 To 119
        SetMemory(0x66175C, Add, -167772160),# units:Air Weapon  index:127    from 130 To 120
        SetMemory(0x6617AC, Add, -13824),# units:Air Weapon  index:205    from 130 To 76
        SetMemory(0x65FC2C, Add, 65536),# units:Max Air Hits  index:22    from 0 To 1
        SetMemory(0x65FC70, Add, 16777216),# units:Max Air Hits  index:91    from 0 To 1
        SetMemory(0x65FC74, Add, 256),# units:Max Air Hits  index:93    from 0 To 1
        SetMemory(0x65FC74, Add, 16777216),# units:Max Air Hits  index:95    from 0 To 1
        SetMemory(0x65FC78, Add, -65536),# units:Max Air Hits  index:98    from 1 To 0
        SetMemory(0x65FC8C, Add, 16777216),# units:Max Air Hits  index:119    from 0 To 1
        SetMemory(0x65FC94, Add, 33554432),# units:Max Air Hits  index:127    from 0 To 2
        SetMemory(0x65FCE4, Add, 256),# units:Max Air Hits  index:205    from 0 To 1
        SetMemory(0x66018C, Add, -3),# units:AI Internal  index:20    from 3 To 0
        SetMemory(0x66018C, Add, -196608),# units:AI Internal  index:22    from 3 To 0
        SetMemory(0x66018C, Add, 0),# units:AI Internal  index:23    from 3 To 3
        SetMemory(0x660194, Add, -768),# units:AI Internal  index:29    from 3 To 0
        SetMemory(0x6601D0, Add, 50331648),# units:AI Internal  index:91    from 0 To 3
        SetMemory(0x6601D4, Add, 3),# units:AI Internal  index:92    from 0 To 3
        SetMemory(0x6601D8, Add, 196608),# units:AI Internal  index:98    from 0 To 3
        SetMemory(0x6601EC, Add, -50331648),# units:AI Internal  index:119    from 3 To 0
        SetMemory(0x6601F0, Add, -768),# units:AI Internal  index:121    from 3 To 0
        SetMemory(0x6601F4, Add, -50331648),# units:AI Internal  index:127    from 3 To 0
        SetMemory(0x66409C, Add, 0),# units:Special Ability Flags  index:7    from 1476460552 To 1476460552
        SetMemory(0x6640D0, Add, -64),# units:Special Ability Flags  index:20    from 402718784 To 402718720
        SetMemory(0x6640D8, Add, -1109360964),# units:Special Ability Flags  index:22    from 1512079684 To 402718720
        SetMemory(0x6640DC, Add, -33554432),# units:Special Ability Flags  index:23    from 1509949504 To 1476395072
        SetMemory(0x6640F4, Add, -33553984),# units:Special Ability Flags  index:29    from 1545601092 To 1512047108
        SetMemory(0x6641A8, Add, 1069547592),# units:Special Ability Flags  index:74    from 406913024 To 1476460616
        SetMemory(0x6641AC, Add, -64),# units:Special Ability Flags  index:75    from 406913088 To 406913024
        SetMemory(0x6641C0, Add, -64),# units:Special Ability Flags  index:80    from 1509949508 To 1509949444
        SetMemory(0x6641E4, Add, -49148),# units:Special Ability Flags  index:89    from 402718720 To 402669572
        SetMemory(0x6641EC, Add, 134217728),# units:Special Ability Flags  index:91    from 0 To 134217728
        SetMemory(0x6641F0, Add, 1543520320),# units:Special Ability Flags  index:92    from 0 To 1543520320
        SetMemory(0x6641F4, Add, -268500988),# units:Special Ability Flags  index:93    from 402718720 To 134217732
        SetMemory(0x6641FC, Add, 1107230724),# units:Special Ability Flags  index:95    from 402718720 To 1509949444
        SetMemory(0x664208, Add, -1109377088),# units:Special Ability Flags  index:98    from 1512046660 To 402669572
        SetMemory(0x664238, Add, -1073741824),# units:Special Ability Flags  index:110    from 1140858881 To 67117057
        SetMemory(0x66425C, Add, 1275068419),# units:Special Ability Flags  index:119    from 67108865 To 1342177284
        SetMemory(0x664264, Add, 201326593),# units:Special Ability Flags  index:121    from 1140850691 To 1342177284
        SetMemory(0x664278, Add, -1),# units:Special Ability Flags  index:126    from 1140850689 To 1140850688
        SetMemory(0x66427C, Add, 908067331),# units:Special Ability Flags  index:127    from 1140850689 To 2048918020
        SetMemory(0x664280, Add, 939587592),# units:Special Ability Flags  index:128    from 536872960 To 1476460552
        SetMemory(0x664284, Add, 939540480),# units:Special Ability Flags  index:129    from 536872960 To 1476413440
        SetMemory(0x664320, Add, -1),# units:Special Ability Flags  index:168    from 1140850689 To 1140850688
        SetMemory(0x664340, Add, -536870913),# units:Special Ability Flags  index:176    from 603987969 To 67117056
        SetMemory(0x6643A0, Add, -100663293),# units:Special Ability Flags  index:200    from 1140850689 To 1040187396
        SetMemory(0x6643B0, Add, 503316484),# units:Special Ability Flags  index:204    from 536870912 To 1040187396
        SetMemory(0x6643B4, Add, 973078596),# units:Special Ability Flags  index:205    from 536870912 To 1509949508
        SetMemory(0x6643B8, Add, 503316484),# units:Special Ability Flags  index:206    from 536870912 To 1040187396
        SetMemory(0x6643EC, Add, -4194304),# units:Special Ability Flags  index:219    from 545261568 To 541067264
        SetMemory(0x662DCC, Add, -1),# units:Target Acquisition Range  index:20    from 5 To 4
        SetMemory(0x662DCC, Add, 262144),# units:Target Acquisition Range  index:22    from 0 To 4
        SetMemory(0x662DD4, Add, -256),# units:Target Acquisition Range  index:29    from 6 To 5
        SetMemory(0x662E00, Add, -131072),# units:Target Acquisition Range  index:74    from 3 To 1
        SetMemory(0x662E10, Add, 65280),# units:Target Acquisition Range  index:89    from 0 To 255
        SetMemory(0x662E10, Add, -67108864),# units:Target Acquisition Range  index:91    from 8 To 4
        SetMemory(0x662E14, Add, 4),# units:Target Acquisition Range  index:92    from 4 To 8
        SetMemory(0x662E14, Add, 1024),# units:Target Acquisition Range  index:93    from 0 To 4
        SetMemory(0x662E14, Add, 67108864),# units:Target Acquisition Range  index:95    from 0 To 4
        SetMemory(0x662E18, Add, 16121856),# units:Target Acquisition Range  index:98    from 9 To 255
        SetMemory(0x662E2C, Add, 4278190080),# units:Target Acquisition Range  index:119    from 0 To 255
        SetMemory(0x662E30, Add, 65280),# units:Target Acquisition Range  index:121    from 0 To 255
        SetMemory(0x662E34, Add, 150994944),# units:Target Acquisition Range  index:127    from 0 To 9
        SetMemory(0x662E38, Add, 1),# units:Target Acquisition Range  index:128    from 0 To 1
        SetMemory(0x662E84, Add, 1024),# units:Target Acquisition Range  index:205    from 0 To 4
        SetMemory(0x66324C, Add, -196608),# units:Sight Range  index:22    from 10 To 7
        SetMemory(0x663254, Add, -1024),# units:Sight Range  index:29    from 11 To 7
        SetMemory(0x663290, Add, -1536),# units:Sight Range  index:89    from 7 To 1
        SetMemory(0x663290, Add, 33554432),# units:Sight Range  index:91    from 8 To 10
        SetMemory(0x663294, Add, 3),# units:Sight Range  index:92    from 7 To 10
        SetMemory(0x663294, Add, -1536),# units:Sight Range  index:93    from 7 To 1
        SetMemory(0x663294, Add, 50331648),# units:Sight Range  index:95    from 7 To 10
        SetMemory(0x663298, Add, -524288),# units:Sight Range  index:98    from 9 To 1
        SetMemory(0x6632AC, Add, -117440512),# units:Sight Range  index:119    from 8 To 1
        SetMemory(0x6632B0, Add, -1792),# units:Sight Range  index:121    from 8 To 1
        SetMemory(0x6632B4, Add, -16777216),# units:Sight Range  index:127    from 8 To 7
        SetMemory(0x6632B8, Add, 2),# units:Sight Range  index:128    from 5 To 7
        SetMemory(0x6632B8, Add, 1024),# units:Sight Range  index:129    from 5 To 9
        SetMemory(0x663300, Add, -1),# units:Sight Range  index:200    from 8 To 7
        SetMemory(0x663304, Add, 2304),# units:Sight Range  index:205    from 1 To 10
        SetMemory(0x663304, Add, 393216),# units:Sight Range  index:206    from 1 To 7
        SetMemory(0x663310, Add, 117440512),# units:Sight Range  index:219    from 5 To 12
        SetMemory(0x6635E4, Add, 0),# units:Armor Upgrade  index:20    from 0 To 0
        SetMemory(0x6635E4, Add, -131072),# units:Armor Upgrade  index:22    from 2 To 0
        SetMemory(0x663618, Add, -327680),# units:Armor Upgrade  index:74    from 5 To 0
        SetMemory(0x663628, Add, -905969664),# units:Armor Upgrade  index:91    from 60 To 6
        SetMemory(0x66362C, Add, -55),# units:Armor Upgrade  index:92    from 60 To 5
        SetMemory(0x66362C, Add, -13824),# units:Armor Upgrade  index:93    from 60 To 6
        SetMemory(0x66362C, Add, -905969664),# units:Armor Upgrade  index:95    from 60 To 6
        SetMemory(0x663630, Add, 3538944),# units:Armor Upgrade  index:98    from 6 To 60
        SetMemory(0x663644, Add, -989855744),# units:Armor Upgrade  index:119    from 60 To 1
        SetMemory(0x663648, Add, -15104),# units:Armor Upgrade  index:121    from 60 To 1
        SetMemory(0x66364C, Add, -973078528),# units:Armor Upgrade  index:127    from 60 To 2
        SetMemory(0x663650, Add, -60),# units:Armor Upgrade  index:128    from 60 To 0
        SetMemory(0x663650, Add, -3840),# units:Armor Upgrade  index:129    from 60 To 45
        SetMemory(0x66369C, Add, -13824),# units:Armor Upgrade  index:205    from 60 To 6
        SetMemory(0x662194, Add, -131072),# units:Unit Size  index:22    from 3 To 1
        SetMemory(0x6621D8, Add, 16777216),# units:Unit Size  index:91    from 2 To 3
        SetMemory(0x6621DC, Add, 1),# units:Unit Size  index:92    from 2 To 3
        SetMemory(0x6621DC, Add, 512),# units:Unit Size  index:93    from 1 To 3
        SetMemory(0x6621DC, Add, 33554432),# units:Unit Size  index:95    from 1 To 3
        SetMemory(0x6621E0, Add, -65536),# units:Unit Size  index:98    from 2 To 1
        SetMemory(0x6621F4, Add, 33554432),# units:Unit Size  index:119    from 0 To 2
        SetMemory(0x6621F8, Add, -256),# units:Unit Size  index:121    from 3 To 2
        SetMemory(0x6621FC, Add, 0),# units:Unit Size  index:127    from 3 To 3
        SetMemory(0x662200, Add, 1),# units:Unit Size  index:128    from 0 To 1
        SetMemory(0x662200, Add, 256),# units:Unit Size  index:129    from 0 To 1
        SetMemory(0x662248, Add, -2),# units:Unit Size  index:200    from 3 To 1
        SetMemory(0x66224C, Add, 1),# units:Unit Size  index:204    from 0 To 1
        SetMemory(0x66224C, Add, 768),# units:Unit Size  index:205    from 0 To 3
        SetMemory(0x66224C, Add, 65536),# units:Unit Size  index:206    from 0 To 1
        SetMemory(0x65FEDC, Add, 0),# units:Armor  index:20    from 3 To 3
        SetMemory(0x65FEDC, Add, 1441792),# units:Armor  index:22    from 4 To 26
        SetMemory(0x65FEDC, Add, -16777216),# units:Armor  index:23    from 3 To 2
        SetMemory(0x65FEE4, Add, -1024),# units:Armor  index:29    from 4 To 0
        SetMemory(0x65FF20, Add, 65280),# units:Armor  index:89    from 0 To 255
        SetMemory(0x65FF20, Add, 33554432),# units:Armor  index:91    from 1 To 3
        SetMemory(0x65FF24, Add, 2),# units:Armor  index:92    from 1 To 3
        SetMemory(0x65FF24, Add, 768),# units:Armor  index:93    from 0 To 3
        SetMemory(0x65FF24, Add, 50331648),# units:Armor  index:95    from 0 To 3
        SetMemory(0x65FF28, Add, 16711680),# units:Armor  index:98    from 0 To 255
        SetMemory(0x65FF3C, Add, -16777216),# units:Armor  index:119    from 1 To 0
        SetMemory(0x65FF40, Add, -256),# units:Armor  index:121    from 1 To 0
        SetMemory(0x65FF44, Add, -16777216),# units:Armor  index:127    from 1 To 0
        SetMemory(0x65FF90, Add, -1),# units:Armor  index:200    from 1 To 0
        SetMemory(0x65FF94, Add, 768),# units:Armor  index:205    from 0 To 3
        SetMemory(0x6620AC, Add, -65536),# units:Right-click Action  index:22    from 2 To 1
        SetMemory(0x6620E0, Add, 262144),# units:Right-click Action  index:74    from 1 To 5
        SetMemory(0x6620F0, Add, -256),# units:Right-click Action  index:89    from 2 To 1
        SetMemory(0x6620F0, Add, 16777216),# units:Right-click Action  index:91    from 0 To 1
        SetMemory(0x6620F4, Add, 1),# units:Right-click Action  index:92    from 0 To 1
        SetMemory(0x6620F4, Add, -256),# units:Right-click Action  index:93    from 2 To 1
        SetMemory(0x6620F4, Add, -16777216),# units:Right-click Action  index:95    from 2 To 1
        SetMemory(0x66210C, Add, 16777216),# units:Right-click Action  index:119    from 0 To 1
        SetMemory(0x662110, Add, 256),# units:Right-click Action  index:121    from 0 To 1
        SetMemory(0x662114, Add, 16777216),# units:Right-click Action  index:127    from 0 To 1
        SetMemory(0x662118, Add, 5),# units:Right-click Action  index:128    from 0 To 5
        SetMemory(0x662118, Add, 1536),# units:Right-click Action  index:129    from 0 To 6
        SetMemory(0x662160, Add, 1),# units:Right-click Action  index:200    from 0 To 1
        SetMemory(0x662164, Add, 1),# units:Right-click Action  index:204    from 0 To 1
        SetMemory(0x662164, Add, 256),# units:Right-click Action  index:205    from 0 To 1
        SetMemory(0x662164, Add, 65536),# units:Right-click Action  index:206    from 0 To 1
        SetMemory(0x661FE8, Add, 275),# units:Ready Sound  index:20    from 0 To 275
        SetMemory(0x661FEC, Add, -57),# units:Ready Sound  index:22    from 332 To 275
        SetMemory(0x661FEC, Add, 20709376),# units:Ready Sound  index:23    from 0 To 316
        SetMemory(0x661FF8, Add, 16777216),# units:Ready Sound  index:29    from 0 To 256
        SetMemory(0x662054, Add, -360),# units:Ready Sound  index:74    from 728 To 368
        SetMemory(0x662074, Add, 0),# units:Ready Sound  index:91    from 0 To 0
        SetMemory(0x662078, Add, 637),# units:Ready Sound  index:92    from 0 To 637
        SetMemory(0x662084, Add, -1041),# units:Ready Sound  index:98    from 1041 To 0
        SetMemory(0x65FFD8, Add, -124),# units:What Sound Start  index:20    from 411 To 287
        SetMemory(0x65FFDC, Add, -53),# units:What Sound Start  index:22    from 340 To 287
        SetMemory(0x65FFDC, Add, -7340032),# units:What Sound Start  index:23    from 436 To 324
        SetMemory(0x65FFE8, Add, -12058624),# units:What Sound Start  index:29    from 449 To 265
        SetMemory(0x660044, Add, -356),# units:What Sound Start  index:74    from 733 To 377
        SetMemory(0x660064, Add, 74448896),# units:What Sound Start  index:91    from 0 To 1136
        SetMemory(0x660068, Add, 642),# units:What Sound Start  index:92    from 0 To 642
        SetMemory(0x660068, Add, 10747904),# units:What Sound Start  index:93    from 972 To 1136
        SetMemory(0x66006C, Add, 32112640),# units:What Sound Start  index:95    from 50 To 540
        SetMemory(0x660074, Add, -990),# units:What Sound Start  index:98    from 1044 To 54
        SetMemory(0x66009C, Add, 22609920),# units:What Sound Start  index:119    from 15 To 360
        SetMemory(0x6600A0, Add, -2686976),# units:What Sound Start  index:121    from 401 To 360
        SetMemory(0x6600AC, Add, -8257536),# units:What Sound Start  index:127    from 391 To 265
        SetMemory(0x6600B0, Add, 362),# units:What Sound Start  index:128    from 15 To 377
        SetMemory(0x6600B0, Add, -983040),# units:What Sound Start  index:129    from 15 To 0
        SetMemory(0x660140, Add, -366),# units:What Sound Start  index:200    from 396 To 30
        SetMemory(0x660148, Add, 33816576),# units:What Sound Start  index:205    from 24 To 540
        SetMemory(0x66014C, Add, 4),# units:What Sound Start  index:206    from 26 To 30
        SetMemory(0x662C18, Add, -124),# units:What Sound End  index:20    from 414 To 290
        SetMemory(0x662C1C, Add, -53),# units:What Sound End  index:22    from 343 To 290
        SetMemory(0x662C1C, Add, -7340032),# units:What Sound End  index:23    from 439 To 327
        SetMemory(0x662C28, Add, -12058624),# units:What Sound End  index:29    from 452 To 268
        SetMemory(0x662C84, Add, -356),# units:What Sound End  index:74    from 736 To 380
        SetMemory(0x662CA4, Add, 74645504),# units:What Sound End  index:91    from 0 To 1139
        SetMemory(0x662CA8, Add, 645),# units:What Sound End  index:92    from 0 To 645
        SetMemory(0x662CA8, Add, 10813440),# units:What Sound End  index:93    from 974 To 1139
        SetMemory(0x662CAC, Add, 32178176),# units:What Sound End  index:95    from 52 To 543
        SetMemory(0x662CB4, Add, -991),# units:What Sound End  index:98    from 1047 To 56
        SetMemory(0x662CDC, Add, 22806528),# units:What Sound End  index:119    from 15 To 363
        SetMemory(0x662CE0, Add, -2490368),# units:What Sound End  index:121    from 401 To 363
        SetMemory(0x662CEC, Add, -8060928),# units:What Sound End  index:127    from 391 To 268
        SetMemory(0x662CF0, Add, 365),# units:What Sound End  index:128    from 15 To 380
        SetMemory(0x662CF0, Add, -983040),# units:What Sound End  index:129    from 15 To 0
        SetMemory(0x662D80, Add, -365),# units:What Sound End  index:200    from 396 To 31
        SetMemory(0x662D88, Add, 33947648),# units:What Sound End  index:205    from 25 To 543
        SetMemory(0x662D8C, Add, 4),# units:What Sound End  index:206    from 27 To 31
        SetMemory(0x663B60, Add, -127),# units:Piss Sound Start  index:20    from 407 To 280
        SetMemory(0x663B64, Add, -53),# units:Piss Sound Start  index:22    from 333 To 280
        SetMemory(0x663B64, Add, -7274496),# units:Piss Sound Start  index:23    from 431 To 320
        SetMemory(0x663B70, Add, -12189696),# units:Piss Sound Start  index:29    from 444 To 258
        SetMemory(0x663BCC, Add, -359),# units:Piss Sound Start  index:74    from 729 To 370
        SetMemory(0x663BEC, Add, 74055680),# units:Piss Sound Start  index:91    from 0 To 1130
        SetMemory(0x663BF0, Add, 639),# units:Piss Sound Start  index:92    from 0 To 639
        SetMemory(0x663BF0, Add, 74055680),# units:Piss Sound Start  index:93    from 0 To 1130
        SetMemory(0x663BFC, Add, -1052),# units:Piss Sound Start  index:98    from 1052 To 0
        SetMemory(0x661F10, Add, -124),# units:Piss Sound End  index:20    from 410 To 286
        SetMemory(0x661F14, Add, -53),# units:Piss Sound End  index:22    from 339 To 286
        SetMemory(0x661F14, Add, -7340032),# units:Piss Sound End  index:23    from 435 To 323
        SetMemory(0x661F20, Add, -12058624),# units:Piss Sound End  index:29    from 448 To 264
        SetMemory(0x661F7C, Add, -356),# units:Piss Sound End  index:74    from 732 To 376
        SetMemory(0x661F9C, Add, 74383360),# units:Piss Sound End  index:91    from 0 To 1135
        SetMemory(0x661FA0, Add, 641),# units:Piss Sound End  index:92    from 0 To 641
        SetMemory(0x661FA0, Add, 74383360),# units:Piss Sound End  index:93    from 0 To 1135
        SetMemory(0x661FAC, Add, -1058),# units:Piss Sound End  index:98    from 1058 To 0
        SetMemory(0x663C38, Add, -124),# units:Yes Sound Start  index:20    from 415 To 291
        SetMemory(0x663C3C, Add, -53),# units:Yes Sound Start  index:22    from 344 To 291
        SetMemory(0x663C3C, Add, -7340032),# units:Yes Sound Start  index:23    from 440 To 328
        SetMemory(0x663C48, Add, -12058624),# units:Yes Sound Start  index:29    from 453 To 269
        SetMemory(0x663CA4, Add, -356),# units:Yes Sound Start  index:74    from 737 To 381
        SetMemory(0x663CC4, Add, 74711040),# units:Yes Sound Start  index:91    from 0 To 1140
        SetMemory(0x663CC8, Add, 646),# units:Yes Sound Start  index:92    from 0 To 646
        SetMemory(0x663CC8, Add, 74711040),# units:Yes Sound Start  index:93    from 0 To 1140
        SetMemory(0x663CD4, Add, -1048),# units:Yes Sound Start  index:98    from 1048 To 0
        SetMemory(0x661468, Add, -124),# units:Yes Sound End  index:20    from 418 To 294
        SetMemory(0x66146C, Add, -53),# units:Yes Sound End  index:22    from 347 To 294
        SetMemory(0x66146C, Add, -7340032),# units:Yes Sound End  index:23    from 443 To 331
        SetMemory(0x661478, Add, -12058624),# units:Yes Sound End  index:29    from 456 To 272
        SetMemory(0x6614D4, Add, -356),# units:Yes Sound End  index:74    from 740 To 384
        SetMemory(0x6614F4, Add, 74907648),# units:Yes Sound End  index:91    from 0 To 1143
        SetMemory(0x6614F8, Add, 649),# units:Yes Sound End  index:92    from 0 To 649
        SetMemory(0x6614F8, Add, 74907648),# units:Yes Sound End  index:93    from 0 To 1143
        SetMemory(0x661504, Add, -1051),# units:Yes Sound End  index:98    from 1051 To 0
        SetMemory(0x6628B0, Add, -1),# units:StarEdit Placement Box Width  index:20    from 18 To 17
        SetMemory(0x6628B8, Add, -48),# units:StarEdit Placement Box Width  index:22    from 65 To 17
        SetMemory(0x6628D4, Add, -74),# units:StarEdit Placement Box Width  index:29    from 75 To 1
        SetMemory(0x662944, Add, -50),# units:StarEdit Placement Box Width  index:57    from 50 To 0
        SetMemory(0x662988, Add, -1),# units:StarEdit Placement Box Width  index:74    from 24 To 23
        SetMemory(0x6629C4, Add, -31),# units:StarEdit Placement Box Width  index:89    from 32 To 1
        SetMemory(0x6629CC, Add, -31),# units:StarEdit Placement Box Width  index:91    from 32 To 1
        SetMemory(0x6629D0, Add, -31),# units:StarEdit Placement Box Width  index:92    from 32 To 1
        SetMemory(0x6629D4, Add, -31),# units:StarEdit Placement Box Width  index:93    from 32 To 1
        SetMemory(0x6629DC, Add, -31),# units:StarEdit Placement Box Width  index:95    from 32 To 1
        SetMemory(0x6629E8, Add, -48),# units:StarEdit Placement Box Width  index:98    from 49 To 1
        SetMemory(0x662A3C, Add, -64),# units:StarEdit Placement Box Width  index:119    from 96 To 32
        SetMemory(0x662A44, Add, -64),# units:StarEdit Placement Box Width  index:121    from 96 To 32
        SetMemory(0x662A58, Add, -95),# units:StarEdit Placement Box Width  index:126    from 96 To 1
        SetMemory(0x662A5C, Add, -95),# units:StarEdit Placement Box Width  index:127    from 96 To 1
        SetMemory(0x662A60, Add, -9),# units:StarEdit Placement Box Width  index:128    from 32 To 23
        SetMemory(0x662A64, Add, -31),# units:StarEdit Placement Box Width  index:129    from 32 To 1
        SetMemory(0x662B00, Add, -127),# units:StarEdit Placement Box Width  index:168    from 128 To 1
        SetMemory(0x662B20, Add, -56),# units:StarEdit Placement Box Width  index:176    from 64 To 8
        SetMemory(0x662B80, Add, -118),# units:StarEdit Placement Box Width  index:200    from 128 To 10
        SetMemory(0x662B8C, Add, -64),# units:StarEdit Placement Box Width  index:203    from 64 To 0
        SetMemory(0x662B90, Add, -246),# units:StarEdit Placement Box Width  index:204    from 256 To 10
        SetMemory(0x662B94, Add, -135),# units:StarEdit Placement Box Width  index:205    from 136 To 1
        SetMemory(0x662B98, Add, -126),# units:StarEdit Placement Box Width  index:206    from 136 To 10
        SetMemory(0x662BCC, Add, -31),# units:StarEdit Placement Box Width  index:219    from 32 To 1
        SetMemory(0x6628B0, Add, -131072),# units:StarEdit Placement Box Height  index:20    from 22 To 20
        SetMemory(0x6628B8, Add, -1966080),# units:StarEdit Placement Box Height  index:22    from 50 To 20
        SetMemory(0x6628D4, Add, -3801088),# units:StarEdit Placement Box Height  index:29    from 59 To 1
        SetMemory(0x662944, Add, -3276800),# units:StarEdit Placement Box Height  index:57    from 50 To 0
        SetMemory(0x662988, Add, -458752),# units:StarEdit Placement Box Height  index:74    from 30 To 23
        SetMemory(0x6629C4, Add, -2031616),# units:StarEdit Placement Box Height  index:89    from 32 To 1
        SetMemory(0x6629CC, Add, -2031616),# units:StarEdit Placement Box Height  index:91    from 32 To 1
        SetMemory(0x6629D0, Add, -2031616),# units:StarEdit Placement Box Height  index:92    from 32 To 1
        SetMemory(0x6629D4, Add, -2031616),# units:StarEdit Placement Box Height  index:93    from 32 To 1
        SetMemory(0x6629DC, Add, -2031616),# units:StarEdit Placement Box Height  index:95    from 32 To 1
        SetMemory(0x6629E8, Add, -2359296),# units:StarEdit Placement Box Height  index:98    from 37 To 1
        SetMemory(0x662A3C, Add, -2097152),# units:StarEdit Placement Box Height  index:119    from 64 To 32
        SetMemory(0x662A44, Add, -4194304),# units:StarEdit Placement Box Height  index:121    from 96 To 32
        SetMemory(0x662A58, Add, -4128768),# units:StarEdit Placement Box Height  index:126    from 64 To 1
        SetMemory(0x662A5C, Add, -4128768),# units:StarEdit Placement Box Height  index:127    from 64 To 1
        SetMemory(0x662A60, Add, -589824),# units:StarEdit Placement Box Height  index:128    from 32 To 23
        SetMemory(0x662A64, Add, -2031616),# units:StarEdit Placement Box Height  index:129    from 32 To 1
        SetMemory(0x662B00, Add, -6225920),# units:StarEdit Placement Box Height  index:168    from 96 To 1
        SetMemory(0x662B20, Add, -1572864),# units:StarEdit Placement Box Height  index:176    from 32 To 8
        SetMemory(0x662B80, Add, -5636096),# units:StarEdit Placement Box Height  index:200    from 96 To 10
        SetMemory(0x662B8C, Add, -4194304),# units:StarEdit Placement Box Height  index:203    from 64 To 0
        SetMemory(0x662B90, Add, -7733248),# units:StarEdit Placement Box Height  index:204    from 128 To 10
        SetMemory(0x662B94, Add, -8847360),# units:StarEdit Placement Box Height  index:205    from 136 To 1
        SetMemory(0x662B98, Add, -8257536),# units:StarEdit Placement Box Height  index:206    from 136 To 10
        SetMemory(0x662BCC, Add, -2031616),# units:StarEdit Placement Box Height  index:219    from 32 To 1
        SetMemory(0x661878, Add, -24),# units:Unit Size Left  index:22    from 32 To 8
        SetMemory(0x6618B0, Add, -36),# units:Unit Size Left  index:29    from 37 To 1
        SetMemory(0x661990, Add, -25),# units:Unit Size Left  index:57    from 25 To 0
        SetMemory(0x661A18, Add, -1),# units:Unit Size Left  index:74    from 12 To 11
        SetMemory(0x661A90, Add, -15),# units:Unit Size Left  index:89    from 16 To 1
        SetMemory(0x661AA0, Add, -14),# units:Unit Size Left  index:91    from 15 To 1
        SetMemory(0x661AA8, Add, -14),# units:Unit Size Left  index:92    from 15 To 1
        SetMemory(0x661AB0, Add, -15),# units:Unit Size Left  index:93    from 16 To 1
        SetMemory(0x661AC0, Add, -15),# units:Unit Size Left  index:95    from 16 To 1
        SetMemory(0x661AD8, Add, -23),# units:Unit Size Left  index:98    from 24 To 1
        SetMemory(0x661B80, Add, -32),# units:Unit Size Left  index:119    from 48 To 16
        SetMemory(0x661B90, Add, -32),# units:Unit Size Left  index:121    from 48 To 16
        SetMemory(0x661BB8, Add, -47),# units:Unit Size Left  index:126    from 48 To 1
        SetMemory(0x661BC0, Add, -47),# units:Unit Size Left  index:127    from 48 To 1
        SetMemory(0x661BC8, Add, -5),# units:Unit Size Left  index:128    from 16 To 11
        SetMemory(0x661BD0, Add, -15),# units:Unit Size Left  index:129    from 16 To 1
        SetMemory(0x661D08, Add, -63),# units:Unit Size Left  index:168    from 64 To 1
        SetMemory(0x661D48, Add, -28),# units:Unit Size Left  index:176    from 32 To 4
        SetMemory(0x661E08, Add, -46),# units:Unit Size Left  index:200    from 56 To 10
        SetMemory(0x661E20, Add, -32),# units:Unit Size Left  index:203    from 32 To 0
        SetMemory(0x661E28, Add, -118),# units:Unit Size Left  index:204    from 128 To 10
        SetMemory(0x661E30, Add, -24),# units:Unit Size Left  index:205    from 25 To 1
        SetMemory(0x661E38, Add, -34),# units:Unit Size Left  index:206    from 44 To 10
        SetMemory(0x661EA0, Add, -15),# units:Unit Size Left  index:219    from 16 To 1
        SetMemory(0x661878, Add, -1572864),# units:Unit Size Up  index:22    from 33 To 9
        SetMemory(0x6618B0, Add, -1835008),# units:Unit Size Up  index:29    from 29 To 1
        SetMemory(0x661990, Add, -1638400),# units:Unit Size Up  index:57    from 25 To 0
        SetMemory(0x661A18, Add, 327680),# units:Unit Size Up  index:74    from 6 To 11
        SetMemory(0x661A90, Add, -983040),# units:Unit Size Up  index:89    from 16 To 1
        SetMemory(0x661AA0, Add, -917504),# units:Unit Size Up  index:91    from 15 To 1
        SetMemory(0x661AA8, Add, -917504),# units:Unit Size Up  index:92    from 15 To 1
        SetMemory(0x661AB0, Add, -983040),# units:Unit Size Up  index:93    from 16 To 1
        SetMemory(0x661AC0, Add, -983040),# units:Unit Size Up  index:95    from 16 To 1
        SetMemory(0x661AD8, Add, -983040),# units:Unit Size Up  index:98    from 16 To 1
        SetMemory(0x661B80, Add, -1048576),# units:Unit Size Up  index:119    from 32 To 16
        SetMemory(0x661B90, Add, -2097152),# units:Unit Size Up  index:121    from 48 To 16
        SetMemory(0x661BB8, Add, -2031616),# units:Unit Size Up  index:126    from 32 To 1
        SetMemory(0x661BC0, Add, -2031616),# units:Unit Size Up  index:127    from 32 To 1
        SetMemory(0x661BC8, Add, -327680),# units:Unit Size Up  index:128    from 16 To 11
        SetMemory(0x661BD0, Add, -983040),# units:Unit Size Up  index:129    from 16 To 1
        SetMemory(0x661D08, Add, -3080192),# units:Unit Size Up  index:168    from 48 To 1
        SetMemory(0x661D48, Add, -786432),# units:Unit Size Up  index:176    from 16 To 4
        SetMemory(0x661E08, Add, -1179648),# units:Unit Size Up  index:200    from 28 To 10
        SetMemory(0x661E20, Add, -2097152),# units:Unit Size Up  index:203    from 32 To 0
        SetMemory(0x661E28, Add, -3538944),# units:Unit Size Up  index:204    from 64 To 10
        SetMemory(0x661E30, Add, -1048576),# units:Unit Size Up  index:205    from 17 To 1
        SetMemory(0x661E38, Add, -458752),# units:Unit Size Up  index:206    from 17 To 10
        SetMemory(0x661EA0, Add, -983040),# units:Unit Size Up  index:219    from 16 To 1
        SetMemory(0x66187C, Add, -24),# units:Unit Size Right  index:22    from 32 To 8
        SetMemory(0x6618B4, Add, -36),# units:Unit Size Right  index:29    from 37 To 1
        SetMemory(0x661994, Add, -24),# units:Unit Size Right  index:57    from 24 To 0
        SetMemory(0x661A94, Add, -14),# units:Unit Size Right  index:89    from 15 To 1
        SetMemory(0x661AA4, Add, -15),# units:Unit Size Right  index:91    from 16 To 1
        SetMemory(0x661AAC, Add, -15),# units:Unit Size Right  index:92    from 16 To 1
        SetMemory(0x661AB4, Add, -14),# units:Unit Size Right  index:93    from 15 To 1
        SetMemory(0x661AC4, Add, -14),# units:Unit Size Right  index:95    from 15 To 1
        SetMemory(0x661ADC, Add, -23),# units:Unit Size Right  index:98    from 24 To 1
        SetMemory(0x661B84, Add, -32),# units:Unit Size Right  index:119    from 47 To 15
        SetMemory(0x661B94, Add, -32),# units:Unit Size Right  index:121    from 47 To 15
        SetMemory(0x661BBC, Add, -46),# units:Unit Size Right  index:126    from 47 To 1
        SetMemory(0x661BC4, Add, -46),# units:Unit Size Right  index:127    from 47 To 1
        SetMemory(0x661BCC, Add, -4),# units:Unit Size Right  index:128    from 15 To 11
        SetMemory(0x661BD4, Add, -14),# units:Unit Size Right  index:129    from 15 To 1
        SetMemory(0x661D0C, Add, -62),# units:Unit Size Right  index:168    from 63 To 1
        SetMemory(0x661D4C, Add, -27),# units:Unit Size Right  index:176    from 31 To 4
        SetMemory(0x661E0C, Add, -53),# units:Unit Size Right  index:200    from 63 To 10
        SetMemory(0x661E24, Add, -31),# units:Unit Size Right  index:203    from 31 To 0
        SetMemory(0x661E2C, Add, -117),# units:Unit Size Right  index:204    from 127 To 10
        SetMemory(0x661E34, Add, -43),# units:Unit Size Right  index:205    from 44 To 1
        SetMemory(0x661E3C, Add, -15),# units:Unit Size Right  index:206    from 25 To 10
        SetMemory(0x661EA4, Add, -14),# units:Unit Size Right  index:219    from 15 To 1
        SetMemory(0x66187C, Add, -393216),# units:Unit Size Down  index:22    from 16 To 10
        SetMemory(0x6618B4, Add, -1835008),# units:Unit Size Down  index:29    from 29 To 1
        SetMemory(0x661994, Add, -1572864),# units:Unit Size Down  index:57    from 24 To 0
        SetMemory(0x661A1C, Add, -524288),# units:Unit Size Down  index:74    from 19 To 11
        SetMemory(0x661A94, Add, -917504),# units:Unit Size Down  index:89    from 15 To 1
        SetMemory(0x661AA4, Add, -983040),# units:Unit Size Down  index:91    from 16 To 1
        SetMemory(0x661AAC, Add, -983040),# units:Unit Size Down  index:92    from 16 To 1
        SetMemory(0x661AB4, Add, -917504),# units:Unit Size Down  index:93    from 15 To 1
        SetMemory(0x661AC4, Add, -917504),# units:Unit Size Down  index:95    from 15 To 1
        SetMemory(0x661ADC, Add, -1245184),# units:Unit Size Down  index:98    from 20 To 1
        SetMemory(0x661B84, Add, -1048576),# units:Unit Size Down  index:119    from 31 To 15
        SetMemory(0x661B94, Add, -2097152),# units:Unit Size Down  index:121    from 47 To 15
        SetMemory(0x661BBC, Add, -1966080),# units:Unit Size Down  index:126    from 31 To 1
        SetMemory(0x661BC4, Add, -1966080),# units:Unit Size Down  index:127    from 31 To 1
        SetMemory(0x661BCC, Add, -262144),# units:Unit Size Down  index:128    from 15 To 11
        SetMemory(0x661BD4, Add, -917504),# units:Unit Size Down  index:129    from 15 To 1
        SetMemory(0x661D0C, Add, -3014656),# units:Unit Size Down  index:168    from 47 To 1
        SetMemory(0x661D4C, Add, -720896),# units:Unit Size Down  index:176    from 15 To 4
        SetMemory(0x661E0C, Add, -2162688),# units:Unit Size Down  index:200    from 43 To 10
        SetMemory(0x661E24, Add, -2031616),# units:Unit Size Down  index:203    from 31 To 0
        SetMemory(0x661E2C, Add, -3473408),# units:Unit Size Down  index:204    from 63 To 10
        SetMemory(0x661E34, Add, -1245184),# units:Unit Size Down  index:205    from 20 To 1
        SetMemory(0x661E3C, Add, -655360),# units:Unit Size Down  index:206    from 20 To 10
        SetMemory(0x661EA4, Add, -917504),# units:Unit Size Down  index:219    from 15 To 1
        SetMemory(0x662FB0, Add, -13),# units:Portrait  index:20    from 13 To 0
        SetMemory(0x662FB4, Add, -9),# units:Portrait  index:22    from 9 To 0
        SetMemory(0x662FB4, Add, -524288),# units:Portrait  index:23    from 14 To 6
        SetMemory(0x662FC0, Add, -393216),# units:Portrait  index:29    from 14 To 8
        SetMemory(0x66301C, Add, -42),# units:Portrait  index:74    from 49 To 7
        SetMemory(0x66303C, Add, -4288675840),# units:Portrait  index:91    from 65535 To 95
        SetMemory(0x663040, Add, -65479),# units:Portrait  index:92    from 65535 To 56
        SetMemory(0x663040, Add, -393216),# units:Portrait  index:93    from 101 To 95
        SetMemory(0x663044, Add, -1245184),# units:Portrait  index:95    from 64 To 45
        SetMemory(0x66304C, Add, -34),# units:Portrait  index:98    from 96 To 62
        SetMemory(0x663074, Add, -917504),# units:Portrait  index:119    from 17 To 3
        SetMemory(0x663078, Add, -917504),# units:Portrait  index:121    from 17 To 3
        SetMemory(0x663084, Add, -589824),# units:Portrait  index:127    from 17 To 8
        SetMemory(0x663088, Add, -97),# units:Portrait  index:128    from 104 To 7
        SetMemory(0x663088, Add, -5767168),# units:Portrait  index:129    from 105 To 17
        SetMemory(0x663118, Add, 65518),# units:Portrait  index:200    from 17 To 65535
        SetMemory(0x663120, Add, -4291952640),# units:Portrait  index:205    from 65535 To 45
        SetMemory(0x663888, Add, -49),# units:Mineral Cost  index:0    from 50 To 1
        SetMemory(0x663888, Add, -1572864),# units:Mineral Cost  index:1    from 25 To 1
        SetMemory(0x66388C, Add, -6488064),# units:Mineral Cost  index:3    from 100 To 1
        SetMemory(0x663890, Add, -9764864),# units:Mineral Cost  index:5    from 150 To 1
        SetMemory(0x6638B0, Add, -49),# units:Mineral Cost  index:20    from 50 To 1
        SetMemory(0x6638B4, Add, -49),# units:Mineral Cost  index:22    from 50 To 1
        SetMemory(0x6638C0, Add, -52428800),# units:Mineral Cost  index:29    from 800 To 0
        SetMemory(0x6638C8, Add, -49),# units:Mineral Cost  index:32    from 50 To 1
        SetMemory(0x6638CC, Add, -49),# units:Mineral Cost  index:34    from 50 To 1
        SetMemory(0x66390C, Add, -125),# units:Mineral Cost  index:66    from 125 To 0
        SetMemory(0x66391C, Add, -100),# units:Mineral Cost  index:74    from 150 To 50
        SetMemory(0x66391C, Add, -6553600),# units:Mineral Cost  index:75    from 100 To 0
        SetMemory(0x663928, Add, -600),# units:Mineral Cost  index:80    from 600 To 0
        SetMemory(0x663934, Add, -50),# units:Mineral Cost  index:86    from 50 To 0
        SetMemory(0x663934, Add, -6553600),# units:Mineral Cost  index:87    from 100 To 0
        SetMemory(0x663938, Add, -65536),# units:Mineral Cost  index:89    from 1 To 0
        SetMemory(0x66393C, Add, -1),# units:Mineral Cost  index:90    from 1 To 0
        SetMemory(0x66393C, Add, 32768000),# units:Mineral Cost  index:91    from 100 To 600
        SetMemory(0x663940, Add, 300),# units:Mineral Cost  index:92    from 100 To 400
        SetMemory(0x663940, Add, 39256064),# units:Mineral Cost  index:93    from 1 To 600
        SetMemory(0x663944, Add, 39256064),# units:Mineral Cost  index:95    from 1 To 600
        SetMemory(0x66394C, Add, -150),# units:Mineral Cost  index:98    from 150 To 0
        SetMemory(0x663964, Add, -99),# units:Mineral Cost  index:110    from 100 To 1
        SetMemory(0x663964, Add, -9175040),# units:Mineral Cost  index:111    from 150 To 10
        SetMemory(0x663968, Add, -149),# units:Mineral Cost  index:112    from 150 To 1
        SetMemory(0x663968, Add, -13041664),# units:Mineral Cost  index:113    from 200 To 1
        SetMemory(0x663974, Add, 4849664),# units:Mineral Cost  index:119    from 1 To 75
        SetMemory(0x663978, Add, 4849664),# units:Mineral Cost  index:121    from 1 To 75
        SetMemory(0x663984, Add, -3276800),# units:Mineral Cost  index:127    from 200 To 150
        SetMemory(0x663988, Add, 49),# units:Mineral Cost  index:128    from 1 To 50
        SetMemory(0x663988, Add, 1572864),# units:Mineral Cost  index:129    from 1 To 25
        SetMemory(0x6639C0, Add, -99),# units:Mineral Cost  index:156    from 100 To 1
        SetMemory(0x6639C8, Add, -149),# units:Mineral Cost  index:160    from 150 To 1
        SetMemory(0x663A18, Add, -199),# units:Mineral Cost  index:200    from 200 To 1
        SetMemory(0x663A20, Add, 39256064),# units:Mineral Cost  index:205    from 1 To 600
        SetMemory(0x65FD00, Add, -4915200),# units:Vespene Cost  index:1    from 75 To 0
        SetMemory(0x65FD04, Add, -3276800),# units:Vespene Cost  index:3    from 50 To 0
        SetMemory(0x65FD08, Add, -6553600),# units:Vespene Cost  index:5    from 100 To 0
        SetMemory(0x65FD2C, Add, -600),# units:Vespene Cost  index:22    from 600 To 0
        SetMemory(0x65FD38, Add, -39321600),# units:Vespene Cost  index:29    from 600 To 0
        SetMemory(0x65FD40, Add, -25),# units:Vespene Cost  index:32    from 25 To 0
        SetMemory(0x65FD44, Add, -25),# units:Vespene Cost  index:34    from 25 To 0
        SetMemory(0x65FD84, Add, -50),# units:Vespene Cost  index:66    from 50 To 0
        SetMemory(0x65FD94, Add, -150),# units:Vespene Cost  index:74    from 150 To 0
        SetMemory(0x65FD94, Add, -19660800),# units:Vespene Cost  index:75    from 300 To 0
        SetMemory(0x65FDA0, Add, -300),# units:Vespene Cost  index:80    from 300 To 0
        SetMemory(0x65FDAC, Add, -1000),# units:Vespene Cost  index:86    from 1000 To 0
        SetMemory(0x65FDAC, Add, -19660800),# units:Vespene Cost  index:87    from 300 To 0
        SetMemory(0x65FDB0, Add, -65536),# units:Vespene Cost  index:89    from 1 To 0
        SetMemory(0x65FDB4, Add, -1),# units:Vespene Cost  index:90    from 1 To 0
        SetMemory(0x65FDB4, Add, 13107200),# units:Vespene Cost  index:91    from 100 To 300
        SetMemory(0x65FDB8, Add, 100),# units:Vespene Cost  index:92    from 100 To 200
        SetMemory(0x65FDB8, Add, 19595264),# units:Vespene Cost  index:93    from 1 To 300
        SetMemory(0x65FDBC, Add, 19595264),# units:Vespene Cost  index:95    from 1 To 300
        SetMemory(0x65FDC4, Add, -100),# units:Vespene Cost  index:98    from 100 To 0
        SetMemory(0x65FDE0, Add, -6553600),# units:Vespene Cost  index:113    from 100 To 0
        SetMemory(0x65FDEC, Add, -65536),# units:Vespene Cost  index:119    from 1 To 0
        SetMemory(0x65FDF0, Add, -65536),# units:Vespene Cost  index:121    from 1 To 0
        SetMemory(0x65FDFC, Add, 6553600),# units:Vespene Cost  index:127    from 0 To 100
        SetMemory(0x65FE00, Add, -1),# units:Vespene Cost  index:128    from 1 To 0
        SetMemory(0x65FE00, Add, 4849664),# units:Vespene Cost  index:129    from 1 To 75
        SetMemory(0x65FE90, Add, -49),# units:Vespene Cost  index:200    from 50 To 1
        SetMemory(0x65FE98, Add, 19595264),# units:Vespene Cost  index:205    from 1 To 300
        SetMemory(0x660428, Add, -357),# units:Build Time  index:0    from 360 To 3
        SetMemory(0x660428, Add, -47841280),# units:Build Time  index:1    from 750 To 20
        SetMemory(0x66042C, Add, -38928384),# units:Build Time  index:3    from 600 To 6
        SetMemory(0x660430, Add, -48496640),# units:Build Time  index:5    from 750 To 10
        SetMemory(0x660450, Add, 2),# units:Build Time  index:20    from 1 To 3
        SetMemory(0x660454, Add, -2397),# units:Build Time  index:22    from 2400 To 3
        SetMemory(0x660454, Add, -97648640),# units:Build Time  index:23    from 1500 To 10
        SetMemory(0x660460, Add, -255590400),# units:Build Time  index:29    from 4800 To 900
        SetMemory(0x660468, Add, -359),# units:Build Time  index:32    from 360 To 1
        SetMemory(0x66046C, Add, -440),# units:Build Time  index:34    from 450 To 10
        SetMemory(0x6604AC, Add, -749),# units:Build Time  index:66    from 750 To 1
        SetMemory(0x6604BC, Add, -450),# units:Build Time  index:74    from 750 To 300
        SetMemory(0x6604BC, Add, -94699520),# units:Build Time  index:75    from 1500 To 55
        SetMemory(0x6604C8, Add, -2398),# units:Build Time  index:80    from 2400 To 2
        SetMemory(0x6604D4, Add, -4790),# units:Build Time  index:86    from 4800 To 10
        SetMemory(0x6604D4, Add, -97648640),# units:Build Time  index:87    from 1500 To 10
        SetMemory(0x6604D8, Add, 589824),# units:Build Time  index:89    from 1 To 10
        SetMemory(0x6604DC, Add, 9),# units:Build Time  index:90    from 1 To 10
        SetMemory(0x6604DC, Add, 117964800),# units:Build Time  index:91    from 600 To 2400
        SetMemory(0x6604E0, Add, 1200),# units:Build Time  index:92    from 600 To 1800
        SetMemory(0x6604E0, Add, 157220864),# units:Build Time  index:93    from 1 To 2400
        SetMemory(0x6604E4, Add, 157220864),# units:Build Time  index:95    from 1 To 2400
        SetMemory(0x6604EC, Add, -740),# units:Build Time  index:98    from 750 To 10
        SetMemory(0x660504, Add, -590),# units:Build Time  index:110    from 600 To 10
        SetMemory(0x660504, Add, -77856768),# units:Build Time  index:111    from 1200 To 12
        SetMemory(0x660508, Add, -1190),# units:Build Time  index:112    from 1200 To 10
        SetMemory(0x660508, Add, -77856768),# units:Build Time  index:113    from 1200 To 12
        SetMemory(0x660514, Add, 29425664),# units:Build Time  index:119    from 1 To 450
        SetMemory(0x660518, Add, 29425664),# units:Build Time  index:121    from 1 To 450
        SetMemory(0x660524, Add, 0),# units:Build Time  index:127    from 900 To 900
        SetMemory(0x660528, Add, 299),# units:Build Time  index:128    from 1 To 300
        SetMemory(0x660528, Add, 39256064),# units:Build Time  index:129    from 1 To 600
        SetMemory(0x660560, Add, -449),# units:Build Time  index:156    from 450 To 1
        SetMemory(0x660568, Add, -899),# units:Build Time  index:160    from 900 To 1
        SetMemory(0x6605B8, Add, -2399),# units:Build Time  index:200    from 2400 To 1
        SetMemory(0x6605C0, Add, 157220864),# units:Build Time  index:205    from 1 To 2400
        SetMemory(0x6637E8, Add, -131072),# units:Staredit Group Flags  index:74    from 12 To 10
        SetMemory(0x6637E8, Add, -67108864),# units:Staredit Group Flags  index:75    from 12 To 8
        SetMemory(0x6637F8, Add, 50331648),# units:Staredit Group Flags  index:91    from 9 To 12
        SetMemory(0x6637FC, Add, 3),# units:Staredit Group Flags  index:92    from 9 To 12
        SetMemory(0x6637FC, Add, -31744),# units:Staredit Group Flags  index:93    from 136 To 12
        SetMemory(0x6637FC, Add, -2080374784),# units:Staredit Group Flags  index:95    from 136 To 12
        SetMemory(0x663800, Add, 8126464),# units:Staredit Group Flags  index:98    from 12 To 136
        SetMemory(0x663814, Add, -134217728),# units:Staredit Group Flags  index:119    from 18 To 10
        SetMemory(0x663818, Add, -2048),# units:Staredit Group Flags  index:121    from 18 To 10
        SetMemory(0x66381C, Add, -134217728),# units:Staredit Group Flags  index:127    from 18 To 10
        SetMemory(0x663820, Add, -118),# units:Staredit Group Flags  index:128    from 128 To 10
        SetMemory(0x663820, Add, -29696),# units:Staredit Group Flags  index:129    from 128 To 12
        SetMemory(0x663868, Add, 110),# units:Staredit Group Flags  index:200    from 18 To 128
        SetMemory(0x66386C, Add, -29696),# units:Staredit Group Flags  index:205    from 128 To 12
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663CFC, Add, 2),# units:Supply Required  index:20    from 0 To 2
        SetMemory(0x663CFC, Add, 131072),# units:Supply Required  index:22    from 0 To 2
        SetMemory(0x663CFC, Add, 67108864),# units:Supply Required  index:23    from 0 To 4
        SetMemory(0x663D04, Add, 0),# units:Supply Required  index:29    from 0 To 0
        SetMemory(0x663D40, Add, 0),# units:Supply Required  index:91    from 0 To 0
        SetMemory(0x663D5C, Add, 67108864),# units:Supply Required  index:119    from 0 To 4
        SetMemory(0x663D60, Add, 1024),# units:Supply Required  index:121    from 0 To 4
        SetMemory(0x663D64, Add, 0),# units:Supply Required  index:127    from 0 To 0
        SetMemory(0x663D68, Add, 2),# units:Supply Required  index:128    from 0 To 2
        SetMemory(0x663D68, Add, 512),# units:Supply Required  index:129    from 0 To 2
        SetMemory(0x664424, Add, -16646144),# units:Space Required  index:22    from 255 To 1
        SetMemory(0x664458, Add, -65536),# units:Space Required  index:74    from 2 To 1
        SetMemory(0x664468, Add, 0),# units:Space Required  index:91    from 255 To 255
        SetMemory(0x66446C, Add, -251),# units:Space Required  index:92    from 255 To 4
        SetMemory(0x664484, Add, -4244635648),# units:Space Required  index:119    from 255 To 2
        SetMemory(0x664488, Add, -64768),# units:Space Required  index:121    from 255 To 2
        SetMemory(0x66448C, Add, 0),# units:Space Required  index:127    from 255 To 255
        SetMemory(0x664490, Add, -254),# units:Space Required  index:128    from 255 To 1
        SetMemory(0x660988, Add, 0),# units:Space Provided  index:0    from 0 To 0
        SetMemory(0x663430, Add, 50),# units:Build Score  index:20    from 0 To 50
        SetMemory(0x663434, Add, 50),# units:Build Score  index:22    from 0 To 50
        SetMemory(0x663434, Add, 655360),# units:Build Score  index:23    from 0 To 10
        SetMemory(0x663440, Add, 26214400),# units:Build Score  index:29    from 0 To 400
        SetMemory(0x66349C, Add, 50),# units:Build Score  index:74    from 0 To 50
        SetMemory(0x6634BC, Add, 0),# units:Build Score  index:91    from 0 To 0
        SetMemory(0x6634F4, Add, 4915200),# units:Build Score  index:119    from 0 To 75
        SetMemory(0x6634F8, Add, 4915200),# units:Build Score  index:121    from 0 To 75
        SetMemory(0x663504, Add, 26214400),# units:Build Score  index:127    from 0 To 400
        SetMemory(0x663508, Add, 50),# units:Build Score  index:128    from 0 To 50
        SetMemory(0x663508, Add, 14745600),# units:Build Score  index:129    from 0 To 225
        SetMemory(0x663EE0, Add, -100),# units:Destroy Score  index:20    from 200 To 100
        SetMemory(0x663EE4, Add, -2400),# units:Destroy Score  index:22    from 2500 To 100
        SetMemory(0x663EF0, Add, -262144000),# units:Destroy Score  index:29    from 4800 To 800
        SetMemory(0x663F4C, Add, -300),# units:Destroy Score  index:74    from 400 To 100
        SetMemory(0x663F58, Add, -2600),# units:Destroy Score  index:80    from 2600 To 0
        SetMemory(0x663F6C, Add, 157286400),# units:Destroy Score  index:91    from 0 To 2400
        SetMemory(0x663F70, Add, 1600),# units:Destroy Score  index:92    from 0 To 1600
        SetMemory(0x663F70, Add, 156631040),# units:Destroy Score  index:93    from 10 To 2400
        SetMemory(0x663F74, Add, 169738240),# units:Destroy Score  index:95    from 10 To 2600
        SetMemory(0x663F7C, Add, -1290),# units:Destroy Score  index:98    from 1300 To 10
        SetMemory(0x663FA4, Add, 9830400),# units:Destroy Score  index:119    from 0 To 150
        SetMemory(0x663FA8, Add, 9830400),# units:Destroy Score  index:121    from 0 To 150
        SetMemory(0x663FB4, Add, -275251200),# units:Destroy Score  index:127    from 5000 To 800
        SetMemory(0x663FB8, Add, 100),# units:Destroy Score  index:128    from 0 To 100
        SetMemory(0x663FB8, Add, 29491200),# units:Destroy Score  index:129    from 0 To 450
        SetMemory(0x664048, Add, -590),# units:Destroy Score  index:200    from 600 To 10
        SetMemory(0x664050, Add, 169738240),# units:Destroy Score  index:205    from 10 To 2600
        SetMemory(0x660730, Add, 16777216),# units:Broodwar Unit Flag  index:91    from 0 To 1
        SetMemory(0x660758, Add, -1),# units:Broodwar Unit Flag  index:128    from 1 To 0
        SetMemory(0x660758, Add, -256),# units:Broodwar Unit Flag  index:129    from 1 To 0
        SetMemory(0x6607A0, Add, -1),# units:Broodwar Unit Flag  index:200    from 1 To 0
        SetMemory(0x661540, Add, 8),# units:Staredit Availability Flags  index:20    from 455 To 463
        SetMemory(0x661544, Add, 8),# units:Staredit Availability Flags  index:22    from 455 To 463
        SetMemory(0x661544, Add, 0),# units:Staredit Availability Flags  index:23    from 455 To 455
        SetMemory(0x661550, Add, 524288),# units:Staredit Availability Flags  index:29    from 455 To 463
        SetMemory(0x6615AC, Add, 8),# units:Staredit Availability Flags  index:74    from 455 To 463
        SetMemory(0x6615AC, Add, 34078720),# units:Staredit Availability Flags  index:75    from 455 To 975
        SetMemory(0x6615B8, Add, 520),# units:Staredit Availability Flags  index:80    from 455 To 975
        SetMemory(0x6615C8, Add, 34144256),# units:Staredit Availability Flags  index:89    from 454 To 975
        SetMemory(0x6615CC, Add, 63373312),# units:Staredit Availability Flags  index:91    from 0 To 967
        SetMemory(0x6615D0, Add, 4559),# units:Staredit Availability Flags  index:92    from 0 To 4559
        SetMemory(0x6615D0, Add, 65536),# units:Staredit Availability Flags  index:93    from 966 To 967
        SetMemory(0x6615D4, Add, -3604480),# units:Staredit Availability Flags  index:95    from 454 To 399
        SetMemory(0x6615D8, Add, 25),# units:Staredit Availability Flags  index:96    from 966 To 991
        SetMemory(0x6615DC, Add, 971),# units:Staredit Availability Flags  index:98    from 4 To 975
        SetMemory(0x661604, Add, 30343168),# units:Staredit Availability Flags  index:119    from 0 To 463
        SetMemory(0x661608, Add, 30343168),# units:Staredit Availability Flags  index:121    from 0 To 463
        SetMemory(0x661614, Add, 8),# units:Staredit Availability Flags  index:126    from 455 To 463
        SetMemory(0x661614, Add, 524288),# units:Staredit Availability Flags  index:127    from 455 To 463
        SetMemory(0x661618, Add, -392),# units:Staredit Availability Flags  index:128    from 855 To 463
        SetMemory(0x661618, Add, -25690112),# units:Staredit Availability Flags  index:129    from 855 To 463
        SetMemory(0x661678, Add, 457),# units:Staredit Availability Flags  index:176    from 2 To 459
        SetMemory(0x6616A8, Add, -504),# units:Staredit Availability Flags  index:200    from 967 To 463
        SetMemory(0x6616B0, Add, 463),# units:Staredit Availability Flags  index:204    from 0 To 463
        SetMemory(0x6616B0, Add, 27721728),# units:Staredit Availability Flags  index:205    from 32 To 455
        SetMemory(0x6616B4, Add, 431),# units:Staredit Availability Flags  index:206    from 32 To 463
        SetMemory(0x6616CC, Add, 11010048),# units:Staredit Availability Flags  index:219    from 343 To 511
        SetMemory(0x6616DC, Add, 1023),# units:Staredit Availability Flags  index:226    from 0 To 1023
        SetMemory(0x6616DC, Add, 30081024),# units:Staredit Availability Flags  index:227    from 0 To 459
        SetMemory(0x6573C8, Add, 786432),# weapons:Label  index:117    from 229 To 241
        SetMemory(0x6573CC, Add, 26),# weapons:Label  index:118    from 229 To 255
        SetMemory(0x6573CC, Add, 11206656),# weapons:Label  index:119    from 229 To 400
        SetMemory(0x6573D0, Add, 28),# weapons:Label  index:120    from 229 To 257
        SetMemory(0x656E7C, Add, -1),# weapons:Graphics  index:117    from 142 To 141
        SetMemory(0x656E80, Add, 8),# weapons:Graphics  index:118    from 142 To 150
        SetMemory(0x656E84, Add, 34),# weapons:Graphics  index:119    from 142 To 176
        SetMemory(0x656E88, Add, 4),# weapons:Graphics  index:120    from 142 To 146
        SetMemory(0x657A80, Add, -65536),# weapons:Target Flags  index:117    from 3 To 2
        SetMemory(0x657A84, Add, -1),# weapons:Target Flags  index:118    from 3 To 2
        SetMemory(0x657A84, Add, 5177344),# weapons:Target Flags  index:119    from 3 To 82
        SetMemory(0x657A88, Add, -2),# weapons:Target Flags  index:120    from 3 To 1
        SetMemory(0x656BF0, Add, 0),# weapons:Minimum Range  index:118    from 0 To 0
        SetMemory(0x657644, Add, -96),# weapons:Maximum Range  index:117    from 128 To 32
        SetMemory(0x657648, Add, 7872),# weapons:Maximum Range  index:118    from 128 To 8000
        SetMemory(0x65764C, Add, 7872),# weapons:Maximum Range  index:119    from 128 To 8000
        SetMemory(0x657650, Add, 96),# weapons:Maximum Range  index:120    from 128 To 224
        SetMemory(0x657244, Add, 13568),# weapons:Damage Upgrade  index:117    from 7 To 60
        SetMemory(0x657244, Add, 65536),# weapons:Damage Upgrade  index:118    from 7 To 8
        SetMemory(0x657244, Add, 905969664),# weapons:Damage Upgrade  index:119    from 7 To 61
        SetMemory(0x657248, Add, 53),# weapons:Damage Upgrade  index:120    from 7 To 60
        SetMemory(0x6572CC, Add, 0),# weapons:Weapon Type  index:118    from 3 To 3
        SetMemory(0x6572CC, Add, -16777216),# weapons:Weapon Type  index:119    from 3 To 2
        SetMemory(0x6572D0, Add, -2),# weapons:Weapon Type  index:120    from 3 To 1
        SetMemory(0x6566E4, Add, 0),# weapons:Weapon Behavior  index:118    from 2 To 2
        SetMemory(0x6566E4, Add, 16777216),# weapons:Weapon Behavior  index:119    from 2 To 3
        SetMemory(0x6566E8, Add, -1),# weapons:Weapon Behavior  index:120    from 2 To 1
        SetMemory(0x6570B4, Add, -83886080),# weapons:Remove After  index:119    from 255 To 250
        SetMemory(0x65676C, Add, 65536),# weapons:Explosion Type  index:118    from 1 To 2
        SetMemory(0x65676C, Add, 16777216),# weapons:Explosion Type  index:119    from 1 To 2
        SetMemory(0x656770, Add, 0),# weapons:Explosion Type  index:120    from 1 To 1
        SetMemory(0x656974, Add, 10),# weapons:Inner Splash Range  index:118    from 0 To 10
        SetMemory(0x656974, Add, 786432),# weapons:Inner Splash Range  index:119    from 0 To 12
        SetMemory(0x656978, Add, 0),# weapons:Inner Splash Range  index:120    from 0 To 0
        SetMemory(0x6571B4, Add, 25),# weapons:Medium Splash Range  index:118    from 0 To 25
        SetMemory(0x6571B4, Add, 1310720),# weapons:Medium Splash Range  index:119    from 0 To 20
        SetMemory(0x6571B8, Add, 0),# weapons:Medium Splash Range  index:120    from 0 To 0
        SetMemory(0x65786C, Add, 40),# weapons:Outer Splash Range  index:118    from 0 To 40
        SetMemory(0x65786C, Add, 2162688),# weapons:Outer Splash Range  index:119    from 0 To 33
        SetMemory(0x657870, Add, 0),# weapons:Outer Splash Range  index:120    from 0 To 0
        SetMemory(0x656F98, Add, -65536),# weapons:Damage Amount  index:117    from 6 To 5
        SetMemory(0x656F9C, Add, 64),# weapons:Damage Amount  index:118    from 6 To 70
        SetMemory(0x656F9C, Add, 0),# weapons:Damage Amount  index:119    from 6 To 6
        SetMemory(0x656FA0, Add, 14),# weapons:Damage Amount  index:120    from 6 To 20
        SetMemory(0x657764, Add, 4),# weapons:Damage Bonus  index:118    from 1 To 5
        SetMemory(0x657764, Add, 0),# weapons:Damage Bonus  index:119    from 1 To 1
        SetMemory(0x657768, Add, -1),# weapons:Damage Bonus  index:120    from 1 To 0
        SetMemory(0x65702C, Add, -917504),# weapons:Weapon Cooldown  index:118    from 15 To 1
        SetMemory(0x65702C, Add, -234881024),# weapons:Weapon Cooldown  index:119    from 15 To 1
        SetMemory(0x657030, Add, 0),# weapons:Weapon Cooldown  index:120    from 15 To 15
        SetMemory(0x656558, Add, 0),# weapons:Damage Factor  index:120    from 1 To 1
        SetMemory(0x656A04, Add, 7340032),# weapons:Attack Angle  index:118    from 16 To 128
        SetMemory(0x656A04, Add, 0),# weapons:Attack Angle  index:119    from 16 To 16
        SetMemory(0x656A08, Add, 0),# weapons:Attack Angle  index:120    from 16 To 16
        SetMemory(0x6578FC, Add, 0),# weapons:Launch Spin  index:119    from 0 To 0
        SetMemory(0x657900, Add, 0),# weapons:Launch Spin  index:120    from 0 To 0
        SetMemory(0x657988, Add, 10),# weapons:Forward Offset  index:120    from 0 To 10
        SetMemory(0x656C98, Add, 20),# weapons:Upward Offset  index:120    from 0 To 20
        SetMemory(0x656868, Add, 393216),# weapons:Icon  index:117    from 323 To 329
        SetMemory(0x65686C, Add, 13),# weapons:Icon  index:118    from 323 To 336
        SetMemory(0x65686C, Add, -2949120),# weapons:Icon  index:119    from 323 To 278
        SetMemory(0x656870, Add, 14),# weapons:Icon  index:120    from 323 To 337
        SetMemory(0x6CA41C, Add, 129),# flingy:Sprite  index:130    from 291 To 420
        SetMemory(0x6CA470, Add, 0),# flingy:Sprite  index:173    from 381 To 381
        SetMemory(0x6CA474, Add, -37),# flingy:Sprite  index:174    from 382 To 345
        SetMemory(0x6CA0C4, Add, 1399),# flingy:Speed  index:115    from 1 To 1400
        SetMemory(0x6CA1AC, Add, 2550),# flingy:Speed  index:173    from 0 To 2550
        SetMemory(0x6CA1B0, Add, 9999),# flingy:Speed  index:174    from 0 To 9999
        SetMemory(0x6CA1BC, Add, 100),# flingy:Speed  index:177    from 0 To 100
        SetMemory(0x6CA1C0, Add, 100),# flingy:Speed  index:178    from 0 To 100
        SetMemory(0x6CA214, Add, -1280),# flingy:Speed  index:199    from 1280 To 0
        SetMemory(0x6C9D5C, Add, 45809664),# flingy:Acceleration  index:115    from 1 To 700
        SetMemory(0x6C9DD0, Add, 65470464),# flingy:Acceleration  index:173    from 0 To 999
        SetMemory(0x6C9DD4, Add, 999),# flingy:Acceleration  index:174    from 0 To 999
        SetMemory(0x6C9DD8, Add, 1507328),# flingy:Acceleration  index:177    from 0 To 23
        SetMemory(0x6C9DDC, Add, 100),# flingy:Acceleration  index:178    from 0 To 100
        SetMemory(0x6C9A78, Add, 0),# flingy:Halt Distance  index:82    from 1 To 1
        SetMemory(0x6C9AFC, Add, 6999),# flingy:Halt Distance  index:115    from 1 To 7000
        SetMemory(0x6C9BE4, Add, 92229),# flingy:Halt Distance  index:173    from 0 To 92229
        SetMemory(0x6C9BE8, Add, 136352),# flingy:Halt Distance  index:174    from 0 To 136352
        SetMemory(0x6C9BF4, Add, 23),# flingy:Halt Distance  index:177    from 0 To 23
        SetMemory(0x6C9BF8, Add, 100),# flingy:Halt Distance  index:178    from 0 To 100
        SetMemory(0x6C9E90, Add, 1056964608),# flingy:Turn Radius  index:115    from 27 To 90
        SetMemory(0x6C9EA0, Add, 60),# flingy:Turn Radius  index:128    from 0 To 60
        SetMemory(0x6C9EA0, Add, 25600),# flingy:Turn Radius  index:129    from 0 To 100
        SetMemory(0x6C9ECC, Add, 15360),# flingy:Turn Radius  index:173    from 0 To 60
        SetMemory(0x6C9ECC, Add, 6488064),# flingy:Turn Radius  index:174    from 0 To 99
        SetMemory(0x6C9ED0, Add, 5888),# flingy:Turn Radius  index:177    from 0 To 23
        SetMemory(0x6C9ED0, Add, -1769472),# flingy:Turn Radius  index:178    from 127 To 100
        SetMemory(0x6C98C8, Add, -33554432),# flingy:Movement Control  index:115    from 2 To 0
        SetMemory(0x6C98D8, Add, -512),# flingy:Movement Control  index:129    from 2 To 0
        SetMemory(0x6C9904, Add, -512),# flingy:Movement Control  index:173    from 2 To 0
        SetMemory(0x6C9904, Add, -131072),# flingy:Movement Control  index:174    from 2 To 0
        SetMemory(0x6C9908, Add, -512),# flingy:Movement Control  index:177    from 2 To 0
        SetMemory(0x6C9908, Add, -131072),# flingy:Movement Control  index:178    from 2 To 0
        SetMemory(0x666340, Add, 0),# sprites:Image File  index:241    from 251 To 251
        SetMemory(0x666388, Add, 7667712),# sprites:Image File  index:277    from 340 To 457
        SetMemory(0x6663A0, Add, 33357824),# sprites:Image File  index:289    from 394 To 903
        SetMemory(0x6663C4, Add, 227),# sprites:Image File  index:306    from 740 To 967
        SetMemory(0x666458, Add, -32309248),# sprites:Image File  index:381    from 742 To 249
        SetMemory(0x66645C, Add, -14483456),# sprites:Image File  index:383    from 750 To 529
        SetMemory(0x666460, Add, 151),# sprites:Image File  index:384    from 751 To 902
        SetMemory(0x666460, Add, -27328512),# sprites:Image File  index:385    from 754 To 337
        SetMemory(0x6664A8, Add, -220),# sprites:Image File  index:420    from 803 To 583
        SetMemory(0x6698B8, Add, -142),# images:GRP File  index:902    from 858 To 716
        SetMemory(0x66E9B0, Add, 256),# images:Gfx Turns  index:337    from 0 To 1
        SetMemory(0x66EBE4, Add, 16777216),# images:Gfx Turns  index:903    from 0 To 1
        SetMemory(0x66C318, Add, 0),# images:Clickable  index:457    from 0 To 0
        SetMemory(0x66D660, Add, 16777216),# images:Use Full Iscript  index:395    from 0 To 1
        SetMemory(0x66D6E8, Add, -256),# images:Use Full Iscript  index:529    from 1 To 0
        SetMemory(0x66D71C, Add, 16777216),# images:Use Full Iscript  index:583    from 0 To 1
        SetMemory(0x66D85C, Add, 65536),# images:Use Full Iscript  index:902    from 0 To 1
        SetMemory(0x66D85C, Add, 16777216),# images:Use Full Iscript  index:903    from 0 To 1
        SetMemory(0x669F28, Add, -512),# images:Draw Function  index:257    from 10 To 8
        SetMemory(0x669F78, Add, 2048),# images:Draw Function  index:337    from 9 To 17
        SetMemory(0x669FB0, Add, 134217728),# images:Draw Function  index:395    from 0 To 8
        SetMemory(0x669FC8, Add, -512),# images:Draw Function  index:417    from 10 To 8
        SetMemory(0x66A06C, Add, -184549376),# images:Draw Function  index:583    from 15 To 4
        SetMemory(0x66A1AC, Add, 524288),# images:Draw Function  index:902    from 0 To 8
        SetMemory(0x66A1AC, Add, -33554432),# images:Draw Function  index:903    from 10 To 8
        SetMemory(0x66F04C, Add, -25),# images:Iscript ID  index:257    from 275 To 250
        SetMemory(0x66F18C, Add, -76),# images:Iscript ID  index:337    from 299 To 223
        SetMemory(0x66F274, Add, -136),# images:Iscript ID  index:395    from 218 To 82
        SetMemory(0x66F2CC, Add, 35),# images:Iscript ID  index:417    from 215 To 250
        SetMemory(0x66F36C, Add, -105),# images:Iscript ID  index:457    from 322 To 217
        SetMemory(0x66F48C, Add, -23),# images:Iscript ID  index:529    from 240 To 217
        SetMemory(0x66FA60, Add, -101),# images:Iscript ID  index:902    from 337 To 236
        SetMemory(0x66FA64, Add, -189),# images:Iscript ID  index:903    from 275 To 86
        SetMemory(0x6557A0, Add, -9764864),# upgrades:Mineral Cost Base  index:49    from 150 To 1
        SetMemory(0x6558A0, Add, -9830400),# upgrades:Vespene Cost Base  index:49    from 150 To 0
        SetMemory(0x655BE0, Add, -163184640),# upgrades:Research Time Base  index:49    from 2500 To 10
        SetMemory(0x655B18, Add, 262144),# upgrades:Icon  index:45    from 0 To 4
        SetMemory(0x655B24, Add, 384),# upgrades:Icon  index:50    from 0 To 384
        SetMemory(0x655A98, Add, 8519680),# upgrades:Label  index:45    from 0 To 130
        SetMemory(0x655AA4, Add, 1275),# upgrades:Label  index:50    from 0 To 1275
        SetMemory(0x655C2C, Add, 256),# upgrades:Race  index:49    from 2 To 3
        SetMemory(0x655C2C, Add, -131072),# upgrades:Race  index:50    from 3 To 1
        SetMemory(0x655730, Add, 65536),# upgrades:Max. Repeats  index:50    from 0 To 1
        SetMemory(0x656278, Add, -13107200),# techdata:Mineral Cost  index:25    from 200 To 0
        SetMemory(0x65627C, Add, -140),# techdata:Mineral Cost  index:26    from 150 To 10
        SetMemory(0x65627C, Add, -13107200),# techdata:Mineral Cost  index:27    from 200 To 0
        SetMemory(0x656288, Add, 65536),# techdata:Mineral Cost  index:33    from 0 To 1
        SetMemory(0x656220, Add, -13107200),# techdata:Vespene Cost  index:25    from 200 To 0
        SetMemory(0x656224, Add, -150),# techdata:Vespene Cost  index:26    from 150 To 0
        SetMemory(0x656224, Add, -13107200),# techdata:Vespene Cost  index:27    from 200 To 0
        SetMemory(0x656408, Add, -78381056),# techdata:Resarch Time  index:25    from 1200 To 4
        SetMemory(0x65640C, Add, -1790),# techdata:Resarch Time  index:26    from 1800 To 10
        SetMemory(0x656418, Add, 655360),# techdata:Resarch Time  index:33    from 0 To 10
        SetMemory(0x656380, Add, -6553600),# techdata:Energy Required  index:1    from 100 To 0
        SetMemory(0x656384, Add, -100),# techdata:Energy Required  index:2    from 100 To 0
        SetMemory(0x656388, Add, -50),# techdata:Energy Required  index:4    from 50 To 0
        SetMemory(0x656390, Add, -150),# techdata:Energy Required  index:8    from 150 To 0
        SetMemory(0x6563BC, Add, -74),# techdata:Energy Required  index:30    from 75 To 1
        SetMemory(0x6563C0, Add, 4915200),# techdata:Energy Required  index:33    from 0 To 75
        SetMemory(0x656464, Add, 366),# techdata:Icon  index:26    from 0 To 366
        SetMemory(0x656470, Add, 15859712),# techdata:Icon  index:33    from 0 To 242
        SetMemory(0x6562D4, Add, 1243),# techdata:Label  index:26    from 0 To 1243
        SetMemory(0x6562E0, Add, 68878336),# techdata:Label  index:33    from 0 To 1051
        SetMemory(0x6564A0, Add, 256),# techdata:Race  index:25    from 2 To 3
        SetMemory(0x6564A0, Add, -131072),# techdata:Race  index:26    from 3 To 1
        SetMemory(0x6564A0, Add, 16777216),# techdata:Race  index:27    from 2 To 3
        SetMemory(0x6564A8, Add, -512),# techdata:Race  index:33    from 3 To 1
    ])

