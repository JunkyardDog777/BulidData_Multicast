from eudplib import *
try:
    InitialWireframe
except NameError:

    def init_wireframe():
        WireFrameDataEditor.WireFrameInit()
        WireFrameDataEditor.ChangeWireframe(5, 5)
        WireFrameDataEditor.ChangeTranframe(5, 30)
        WireFrameDataEditor.ChangeGrpframe(5, 30)
        WireFrameDataEditor.ChangeWireframe(20, 0)
        WireFrameDataEditor.ChangeTranframe(20, 0)
        WireFrameDataEditor.ChangeGrpframe(20, 0)
        WireFrameDataEditor.ChangeWireframe(22, 0)
        WireFrameDataEditor.ChangeTranframe(22, 0)
        WireFrameDataEditor.ChangeGrpframe(22, 0)
        WireFrameDataEditor.ChangeWireframe(29, 8)
        WireFrameDataEditor.ChangeTranframe(29, 8)
        WireFrameDataEditor.ChangeGrpframe(29, 8)
        WireFrameDataEditor.ChangeWireframe(74, 7)
        WireFrameDataEditor.ChangeTranframe(74, 7)
        WireFrameDataEditor.ChangeGrpframe(74, 7)
        WireFrameDataEditor.ChangeWireframe(91, 88)
        WireFrameDataEditor.ChangeTranframe(91, 88)
        WireFrameDataEditor.ChangeGrpframe(91, 88)
        WireFrameDataEditor.ChangeWireframe(92, 81)
        WireFrameDataEditor.ChangeTranframe(92, 81)
        WireFrameDataEditor.ChangeGrpframe(92, 81)
        WireFrameDataEditor.ChangeWireframe(93, 88)
        WireFrameDataEditor.ChangeTranframe(93, 88)
        WireFrameDataEditor.ChangeGrpframe(93, 88)
        WireFrameDataEditor.ChangeWireframe(95, 80)
        WireFrameDataEditor.ChangeTranframe(95, 0)
        WireFrameDataEditor.ChangeGrpframe(95, 0)
        WireFrameDataEditor.ChangeWireframe(98, 89)
        WireFrameDataEditor.ChangeTranframe(98, 89)
        WireFrameDataEditor.ChangeGrpframe(98, 89)
        WireFrameDataEditor.ChangeWireframe(119, 2)
        WireFrameDataEditor.ChangeGrpframe(119, 2)
        WireFrameDataEditor.ChangeWireframe(121, 2)
        WireFrameDataEditor.ChangeGrpframe(121, 2)
        WireFrameDataEditor.ChangeWireframe(127, 8)
        WireFrameDataEditor.ChangeGrpframe(127, 8)
        WireFrameDataEditor.ChangeWireframe(128, 7)
        WireFrameDataEditor.ChangeGrpframe(128, 7)
        WireFrameDataEditor.ChangeWireframe(129, 182)
        WireFrameDataEditor.ChangeGrpframe(129, 129)
        WireFrameDataEditor.ChangeWireframe(176, 220)
        WireFrameDataEditor.ChangeWireframe(200, 204)
        WireFrameDataEditor.ChangeWireframe(205, 80)
        WireFrameDataEditor.ChangeWireframe(206, 204)

else:
    InitialWireframe.wirefram(5, 5)
    InitialWireframe.tranwire(5, 30)
    InitialWireframe.grpwire(5, 30)
    InitialWireframe.wirefram(20, 0)
    InitialWireframe.tranwire(20, 0)
    InitialWireframe.grpwire(20, 0)
    InitialWireframe.wirefram(22, 0)
    InitialWireframe.tranwire(22, 0)
    InitialWireframe.grpwire(22, 0)
    InitialWireframe.wirefram(29, 8)
    InitialWireframe.tranwire(29, 8)
    InitialWireframe.grpwire(29, 8)
    InitialWireframe.wirefram(74, 7)
    InitialWireframe.tranwire(74, 7)
    InitialWireframe.grpwire(74, 7)
    InitialWireframe.wirefram(91, 88)
    InitialWireframe.tranwire(91, 88)
    InitialWireframe.grpwire(91, 88)
    InitialWireframe.wirefram(92, 81)
    InitialWireframe.tranwire(92, 81)
    InitialWireframe.grpwire(92, 81)
    InitialWireframe.wirefram(93, 88)
    InitialWireframe.tranwire(93, 88)
    InitialWireframe.grpwire(93, 88)
    InitialWireframe.wirefram(95, 80)
    InitialWireframe.tranwire(95, 0)
    InitialWireframe.grpwire(95, 0)
    InitialWireframe.wirefram(98, 89)
    InitialWireframe.tranwire(98, 89)
    InitialWireframe.grpwire(98, 89)
    InitialWireframe.wirefram(119, 2)
    InitialWireframe.grpwire(119, 2)
    InitialWireframe.wirefram(121, 2)
    InitialWireframe.grpwire(121, 2)
    InitialWireframe.wirefram(127, 8)
    InitialWireframe.grpwire(127, 8)
    InitialWireframe.wirefram(128, 7)
    InitialWireframe.grpwire(128, 7)
    InitialWireframe.wirefram(129, 182)
    InitialWireframe.grpwire(129, 129)
    InitialWireframe.wirefram(176, 220)
    InitialWireframe.wirefram(200, 204)
    InitialWireframe.wirefram(205, 80)
    InitialWireframe.wirefram(206, 204)


def onPluginStart():
    try:
        init_wireframe()
    except NameError:
        pass
    DoActions([ # 스테이터스인포메이션
        SetMemory(0x5197E8, SetTo, 4344192),
        SetMemory(0x5197EC, SetTo, 4353872),
        SetMemory(0x5197F4, SetTo, 4344656),
        SetMemory(0x5197F8, SetTo, 4355232),
        SetMemory(0x51993C, SetTo, 4353872),
        SetMemory(0x519950, SetTo, 4344192),
        SetMemory(0x519954, SetTo, 4353872),
        SetMemory(0x519998, SetTo, 4344192),
        SetMemory(0x51999C, SetTo, 4353872),
        SetMemory(0x5199A4, SetTo, 4344192),
        SetMemory(0x5199A8, SetTo, 4353872),
        SetMemory(0x5199B0, SetTo, 4344192),
        SetMemory(0x5199B4, SetTo, 4353872),
        SetMemory(0x519D04, SetTo, 4344192),
        SetMemory(0x519D08, SetTo, 4353872),
        SetMemory(0x519D34, SetTo, 4344192),
        SetMemory(0x519D38, SetTo, 4353872),
        SetMemory(0x519D40, SetTo, 4344192),
        SetMemory(0x519D44, SetTo, 4353872),
        SetMemory(0x519D4C, SetTo, 4344192),
        SetMemory(0x519D50, SetTo, 4353872),
        SetMemory(0x519DE8, SetTo, 4344192),
        SetMemory(0x519DEC, SetTo, 4353872),
    ])
    # 버튼셋
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr0 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,81,1,96,142,66,0,176,52,66,0,96,0,87,0,79,5,1,0,2,0,128,1,96,142,66,0,176,52,66,0,95,0,86,0,78,5,1,0,3,0,37,1,96,142,66,0,176,52,66,0,90,0,90,0,80,5,1,0,4,0,80,1,96,142,66,0,176,52,66,0,94,0,89,0,81,5,28,4,5,0,128,0,208,130,66,0,240,51,66,0,0,0,0,0,68,5,1,0,6,0,93,1,208,130,66,0,176,52,66,0,96,0,90,0,76,5,1,0])
    btnptr4 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,96,136,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,96,136,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,96,136,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,245,0,192,145,66,0,80,52,66,0,5,0,5,0,82,1,93,1,7,0,246,0,112,145,66,0,112,52,66,0,5,0,0,0,83,1,0,0])
    btnptr5 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,79,1,96,142,66,0,176,52,66,0,86,0,86,0,74,5,1,0,2,0,38,1,96,142,66,0,176,52,66,0,87,0,87,0,75,5,1,0,3,0,36,1,96,142,66,0,176,52,66,0,90,0,90,0,69,5,1,0,5,0,128,0,208,130,66,0,240,51,66,0,0,0,0,0,68,5,1,0,6,0,93,1,208,130,66,0,176,52,66,0,96,0,90,0,76,5,1,0])
    btnptr6 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,112,134,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,134,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,16,134,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,232,0,224,133,66,0,208,59,66,0,0,0,0,0,165,2,0,0,5,0,231,0,160,133,66,0,112,59,66,0,0,0,0,0,163,2,0,0,6,0,233,0,96,133,66,0,96,55,66,0,0,0,0,0,164,2,0,0,7,0,234,0,16,138,66,0,240,154,69,0,0,0,239,0,166,2,0,0,8,0,235,0,144,137,66,0,240,154,69,0,0,0,242,0,167,2,0,0,9,0,236,0,16,131,66,0,240,51,66,0,0,0,0,0,188,2,0,0])
    btnptr7 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,6,0,79,1,208,130,66,0,240,51,66,0,86,0,86,0,82,5,1,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr10 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,81,1,96,142,66,0,176,52,66,0,96,0,87,0,79,5,1,0,2,0,128,1,96,142,66,0,176,52,66,0,95,0,86,0,78,5,1,0,3,0,45,1,96,142,66,0,176,52,66,0,90,0,90,0,82,5,1,0,4,0,70,1,96,142,66,0,176,52,66,0,94,0,89,0,82,5,28,4,5,0,128,0,208,130,66,0,240,51,66,0,0,0,0,0,68,5,1,0,6,0,93,1,208,130,66,0,176,52,66,0,96,0,90,0,76,5,1,0])
    btnptr13 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,6,0,80,1,208,130,66,0,112,63,66,0,31,0,3,0,149,4,25,4,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr17 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,6,0,80,1,224,148,66,0,112,63,66,0,32,0,3,0,150,4,25,4,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr18 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,243,0,224,148,66,0,112,63,66,0,3,0,3,0,80,1,92,1])
    btnptr19 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,96,136,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,96,136,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,96,136,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,245,0,192,145,66,0,80,52,66,0,5,0,5,0,82,1,93,1,7,0,246,0,112,145,66,0,112,52,66,0,5,0,0,0,83,1,0,0])
    btnptr23 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,6,0,80,1,208,130,66,0,112,63,66,0,32,0,3,0,150,4,25,4,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr24 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,6,0,80,1,208,130,66,0,112,63,66,0,32,0,3,0,151,4,25,4,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr26 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,6,0,242,0,224,148,66,0,112,63,66,0,25,0,3,0,152,4,24,4,7,0,109,1,224,148,66,0,224,57,66,0,34,0,34,0,223,4,0,0,8,0,111,1,224,148,66,0,112,63,66,0,24,0,24,0,224,4,226,4,9,0,117,1,224,148,66,0,112,63,66,0,30,0,30,0,225,4,227,4])
    btnptr34 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,32,132,66,0,64,68,66,0,0,0,0,0,152,2,0,0,1,0,7,0,96,142,66,0,176,52,66,0,7,0,7,0,80,2,0,0,2,0,229,0,32,132,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,195,0,208,130,66,0,176,52,66,0,7,0,75,0,154,4,0,0,6,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,7,0,107,0,96,142,66,0,16,61,66,0,107,0,107,0,146,2,196,2,8,0,108,0,96,142,66,0,16,61,66,0,108,0,108,0,147,2,197,2,9,0,27,1,240,131,66,0,48,60,66,0,0,0,106,0,158,2,0,0,9,0,26,1,208,135,66,0,48,50,66,0,0,0,0,0,159,2,0,0,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,0,0,9,0,236,0,32,137,66,0,208,50,66,0,0,0,0,0,182,2,0,0])
    btnptr106 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,32,132,66,0,64,68,66,0,0,0,0,0,152,2,0,0,1,0,0,0,96,142,66,0,176,52,66,0,0,0,0,0,74,2,0,0,2,0,229,0,32,132,66,0,240,51,66,0,0,0,0,0,153,2,0,0,2,0,32,0,96,142,66,0,176,52,66,0,32,0,32,0,76,2,190,2,3,0,1,0,96,142,66,0,176,52,66,0,1,0,1,0,75,2,189,2,4,0,34,0,96,142,66,0,176,52,66,0,34,0,34,0,10,5,14,5,6,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,9,0,27,1,240,131,66,0,48,60,66,0,0,0,111,0,158,2,0,0,9,0,26,1,208,135,66,0,48,50,66,0,91,0,0,0,159,2,0,0,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,0,0,9,0,236,0,32,137,66,0,208,50,66,0,0,0,0,0,182,2,0,0])
    btnptr111 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,238,0,80,148,66,0,16,51,66,0,16,0,16,0,216,1,0,0,2,0,237,0,0,149,66,0,80,51,66,0,0,0,0,0,68,1,0,0,4,0,110,1,0,149,66,0,80,51,66,0,24,0,24,0,221,4,0,0,5,0,117,1,0,149,66,0,80,51,66,0,30,0,30,0,222,4,0,0,6,0,128,1,80,148,66,0,16,51,66,0,51,0,51,0,1,5,0,0,8,0,242,0,0,149,66,0,80,51,66,0,25,0,25,0,77,5,0,0,9,0,236,0,224,136,66,0,48,51,66,0,0,0,0,0,180,2,0,0,9,0,236,0,0,137,66,0,240,50,66,0,0,0,0,0,179,2,0,0])
    btnptr112 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,35,0,208,130,66,0,48,57,66,0,0,0,0,0,162,2,0,0,2,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,3,0,3,1,0,149,66,0,80,51,66,0,11,0,11,0,108,1,0,0,7,0,132,0,96,142,66,0,96,56,66,0,132,0,132,0,112,2,234,2,8,0,194,0,208,130,66,0,240,154,69,0,7,0,195,0,154,4,0,0,9,0,236,0,224,136,66,0,48,51,66,0,0,0,0,0,180,2,0,0])
    btnptr131 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,35,0,208,130,66,0,48,57,66,0,0,0,0,0,162,2,0,0,2,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,3,0,3,1,0,149,66,0,80,51,66,0,11,0,11,0,108,1,0,0,4,0,5,1,80,148,66,0,16,51,66,0,24,0,24,0,224,1,0,0,5,0,6,1,80,148,66,0,16,51,66,0,25,0,25,0,225,1,0,0,6,0,40,1,80,148,66,0,16,51,66,0,26,0,26,0,226,1,0,0,7,0,133,0,96,142,66,0,96,56,66,0,133,0,133,0,113,2,235,2,8,0,194,0,208,130,66,0,240,154,69,0,7,0,195,0,154,4,0,0,9,0,236,0,224,136,66,0,48,51,66,0,0,0,0,0,180,2,0,0,9,0,236,0,0,137,66,0,240,50,66,0,0,0,0,0,179,2,0,0])
    btnptr132 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,35,0,208,130,66,0,48,57,66,0,0,0,0,0,162,2,0,0,2,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,3,0,3,1,0,149,66,0,80,51,66,0,11,0,11,0,108,1,0,0,4,0,5,1,80,148,66,0,16,51,66,0,24,0,24,0,224,1,0,0,5,0,6,1,80,148,66,0,16,51,66,0,25,0,25,0,225,1,0,0,6,0,40,1,80,148,66,0,16,51,66,0,26,0,26,0,226,1,0,0,8,0,194,0,208,130,66,0,240,154,69,0,7,0,195,0,154,4,0,0,9,0,236,0,224,136,66,0,48,51,66,0,0,0,0,0,180,2,0,0,9,0,236,0,0,137,66,0,240,50,66,0,0,0,0,0,179,2,0,0])
    btnptr133 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,64,0,96,142,66,0,176,52,66,0,64,0,64,0,87,2,0,0,3,0,196,0,208,130,66,0,240,154,69,0,7,0,195,0,154,4,0,0,6,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,0,0])
    btnptr154 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,112,134,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,134,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,16,134,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,232,0,224,133,66,0,208,59,66,0,0,0,0,0,165,2,0,0,5,0,231,0,160,133,66,0,112,59,66,0,0,0,0,0,163,2,0,0,6,0,233,0,96,133,66,0,96,55,66,0,0,0,0,0,164,2,0,0,7,0,234,0,16,138,66,0,240,154,69,0,0,0,239,0,166,2,0,0,8,0,235,0,144,137,66,0,240,154,69,0,0,0,242,0,167,2,0,0,9,0,236,0,16,131,66,0,240,51,66,0,0,0,0,0,188,2,0,0,9,0,133,1,208,130,66,0,176,52,66,0,0,0,76,0,60,4,0,0])
    btnptr176 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,136,4,1,0,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,176,52,66,0,75,0,75,0,192,3,146,4])
    btnptr194 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,137,4,1,0,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,176,52,66,0,75,0,75,0,192,3,146,4])
    btnptr195 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,138,4,1,0,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,176,52,66,0,75,0,75,0,192,3,146,4])
    btnptr196 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,139,4,1,0,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,176,52,66,0,75,0,75,0,192,3,146,4])
    btnptr197 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,140,4,1,0,2,0,233,0,208,130,66,0,176,52,66,0,75,0,75,0,147,4,146,4,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,240,154,69,0,7,0,106,0,192,3,0,0])
    btnptr198 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,141,4,1,0,2,0,233,0,208,130,66,0,176,52,66,0,75,0,75,0,147,4,146,4,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,240,154,69,0,7,0,106,0,192,3,0,0])
    btnptr199 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,142,4,1,0,2,0,233,0,208,130,66,0,176,52,66,0,75,0,75,0,147,4,146,4,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,240,154,69,0,7,0,106,0,192,3,0,0])
    btnptr200 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,218,0,208,130,66,0,176,52,66,0,0,0,76,0,143,4,1,0,2,0,233,0,208,130,66,0,176,52,66,0,75,0,75,0,147,4,146,4,7,0,107,1,208,130,66,0,240,51,66,0,7,0,106,0,155,4,0,0,9,0,236,0,208,130,66,0,240,154,69,0,7,0,106,0,192,3,0,0])
    btnptr201 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,67,1,96,142,66,0,176,52,66,0,96,0,86,0,82,5,1,0,2,0,38,1,96,142,66,0,176,52,66,0,87,0,87,0,72,5,1,0,3,0,36,1,96,142,66,0,176,52,66,0,99,0,90,0,65,5,1,0,4,0,67,1,96,142,66,0,176,52,66,0,100,0,86,0,83,5,82,4,5,0,128,0,208,130,66,0,240,51,66,0,0,0,0,0,68,5,1,0,6,0,80,1,96,142,66,0,176,52,66,0,99,0,90,0,73,5,153,4,7,0,67,1,96,142,66,0,176,52,66,0,100,0,86,0,84,5,83,4,9,0,93,1,208,130,66,0,176,52,66,0,96,0,90,0,76,5,1,0])
    btnptr226 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,68,1,96,142,66,0,176,52,66,0,95,0,86,0,73,5,1,0,2,0,252,0,96,142,66,0,176,52,66,0,87,0,87,0,72,5,1,0,3,0,36,1,96,142,66,0,176,52,66,0,90,0,90,0,69,5,1,0,4,0,68,1,96,142,66,0,176,52,66,0,96,0,86,0,73,5,1,0,5,0,128,0,208,130,66,0,240,51,66,0,0,0,0,0,68,5,1,0])
    btnptr227 = Db(bytebuffer)
    bytebuffer = bytearray([9,0,236,0,208,130,66,0,112,151,66,0,0,0,0,0,176,2,0,0])
    btnptr229 = Db(bytebuffer)
    bytebuffer = bytearray([9,0,236,0,208,130,66,0,128,151,66,0,0,0,0,0,176,2,0,0])
    btnptr230 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,67,1,96,142,66,0,176,52,66,0,96,0,86,0,82,5,1,0,2,0,38,1,96,142,66,0,176,52,66,0,87,0,87,0,72,5,1,0,3,0,36,1,96,142,66,0,176,52,66,0,95,0,90,0,69,5,1,0,4,0,67,1,96,142,66,0,176,52,66,0,100,0,87,0,83,5,82,4,5,0,128,0,208,130,66,0,240,51,66,0,0,0,0,0,68,5,1,0,6,0,80,1,96,142,66,0,176,52,66,0,99,0,90,0,73,5,153,4,7,0,67,1,96,142,66,0,176,52,66,0,100,0,86,0,84,5,83,4,9,0,93,1,208,130,66,0,176,52,66,0,96,0,90,0,76,5,1,0])
    btnptr248 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,73,1,96,142,66,0,176,52,66,0,95,0,86,0,71,5,1,0,3,0,37,1,96,142,66,0,176,52,66,0,90,0,90,0,69,5,1,0,4,0,69,1,96,142,66,0,176,52,66,0,96,0,87,0,70,5,1,0,5,0,128,0,208,130,66,0,240,51,66,0,0,0,0,0,68,5,1,0,6,0,51,1,96,142,66,0,176,52,66,0,94,0,89,0,67,5,1,0])
    btnptr249 = Db(bytebuffer)
    DoActions([
        SetMemory(0x5187EC, SetTo, btnptr0),
        SetMemory(0x5187E8, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x51881C, SetTo, btnptr4),
        SetMemory(0x518818, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x518828, SetTo, btnptr5),
        SetMemory(0x518824, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518834, SetTo, btnptr6),
        SetMemory(0x518830, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518840, SetTo, btnptr7),
        SetMemory(0x51883C, SetTo, 9),
    ])
    DoActions([
        SetMemory(0x518864, SetTo, btnptr10),
        SetMemory(0x518860, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518888, SetTo, 0),
        SetMemory(0x518884, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x5188B8, SetTo, btnptr17),
        SetMemory(0x5188B4, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188C4, SetTo, btnptr18),
        SetMemory(0x5188C0, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188D0, SetTo, btnptr19),
        SetMemory(0x5188CC, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x5188DC, SetTo, btnptr0),
        SetMemory(0x5188D8, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x5188F4, SetTo, btnptr0),
        SetMemory(0x5188F0, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x518900, SetTo, btnptr23),
        SetMemory(0x5188FC, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x51890C, SetTo, btnptr24),
        SetMemory(0x518908, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518924, SetTo, btnptr26),
        SetMemory(0x518920, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518948, SetTo, 5340440),
        SetMemory(0x518944, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518984, SetTo, btnptr34),
        SetMemory(0x518980, SetTo, 8),
    ])
    DoActions([
        SetMemory(0x518B64, SetTo, btnptr7),
        SetMemory(0x518B60, SetTo, 9),
    ])
    DoActions([
        SetMemory(0x518C30, SetTo, 5332432),
        SetMemory(0x518C2C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518C3C, SetTo, 5337144),
        SetMemory(0x518C38, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518C48, SetTo, 5332432),
        SetMemory(0x518C44, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518C60, SetTo, 0),
        SetMemory(0x518C5C, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C84, SetTo, 5332432),
        SetMemory(0x518C80, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518CE4, SetTo, btnptr106),
        SetMemory(0x518CE0, SetTo, 11),
    ])
    DoActions([
        SetMemory(0x518D20, SetTo, btnptr111),
        SetMemory(0x518D1C, SetTo, 11),
    ])
    DoActions([
        SetMemory(0x518D2C, SetTo, btnptr112),
        SetMemory(0x518D28, SetTo, 8),
    ])
    DoActions([
        SetMemory(0x518D80, SetTo, btnptr0),
        SetMemory(0x518D7C, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x518D98, SetTo, btnptr0),
        SetMemory(0x518D94, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x518DEC, SetTo, btnptr7),
        SetMemory(0x518DE8, SetTo, 9),
    ])
    DoActions([
        SetMemory(0x518E10, SetTo, btnptr131),
        SetMemory(0x518E0C, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x518E1C, SetTo, btnptr132),
        SetMemory(0x518E18, SetTo, 10),
    ])
    DoActions([
        SetMemory(0x518E28, SetTo, btnptr133),
        SetMemory(0x518E24, SetTo, 9),
    ])
    DoActions([
        SetMemory(0x518F24, SetTo, btnptr154),
        SetMemory(0x518F20, SetTo, 4),
    ])
    DoActions([
        SetMemory(0x51902C, SetTo, btnptr176),
        SetMemory(0x519028, SetTo, 10),
    ])
    DoActions([
        SetMemory(0x519104, SetTo, btnptr194),
        SetMemory(0x519100, SetTo, 3),
    ])
    DoActions([
        SetMemory(0x519110, SetTo, btnptr195),
        SetMemory(0x51910C, SetTo, 3),
    ])
    DoActions([
        SetMemory(0x51911C, SetTo, btnptr196),
        SetMemory(0x519118, SetTo, 3),
    ])
    DoActions([
        SetMemory(0x519128, SetTo, btnptr197),
        SetMemory(0x519124, SetTo, 3),
    ])
    DoActions([
        SetMemory(0x519134, SetTo, btnptr198),
        SetMemory(0x519130, SetTo, 4),
    ])
    DoActions([
        SetMemory(0x519140, SetTo, btnptr199),
        SetMemory(0x51913C, SetTo, 4),
    ])
    DoActions([
        SetMemory(0x51914C, SetTo, btnptr200),
        SetMemory(0x519148, SetTo, 4),
    ])
    DoActions([
        SetMemory(0x519158, SetTo, btnptr201),
        SetMemory(0x519154, SetTo, 4),
    ])
    DoActions([
        SetMemory(0x51917C, SetTo, btnptr0),
        SetMemory(0x519178, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x519284, SetTo, btnptr226),
        SetMemory(0x519280, SetTo, 8),
    ])
    DoActions([
        SetMemory(0x519290, SetTo, btnptr227),
        SetMemory(0x51928C, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x5192A8, SetTo, btnptr229),
        SetMemory(0x5192A4, SetTo, 1),
    ])
    DoActions([
        SetMemory(0x5192B4, SetTo, btnptr230),
        SetMemory(0x5192B0, SetTo, 1),
    ])
    DoActions([
        SetMemory(0x51938C, SetTo, btnptr248),
        SetMemory(0x519388, SetTo, 8),
    ])
    DoActions([
        SetMemory(0x519398, SetTo, btnptr249),
        SetMemory(0x519394, SetTo, 5),
    ])
    inputData = open('../temp/RequireData', 'rb').read()
    inputData_db = Db(inputData)
    inputDwordN = (len(inputData) + 3) // 4

    addrEPD = EPD(0x514178)
    f_repmovsd_epd(addrEPD, EPD(inputData_db), inputDwordN)


def beforeTriggerExec():
    DoActions([
        SetMemory(0x660A70 + 0, SetTo, 393217),
        SetMemory(0x660A70 + 4, SetTo, 786439),
        SetMemory(0x660A70 + 8, SetTo, 851968),
        SetMemory(0x660A70 + 12, SetTo, 917504),
        SetMemory(0x660A70 + 16, SetTo, 1441809),
        SetMemory(0x660A70 + 20, SetTo, 1966080),
        SetMemory(0x660A70 + 24, SetTo, 37),
        SetMemory(0x660A70 + 28, SetTo, 45),
        SetMemory(0x660A70 + 32, SetTo, 0),
        SetMemory(0x660A70 + 36, SetTo, 0),
        SetMemory(0x660A70 + 40, SetTo, 50),
        SetMemory(0x660A70 + 44, SetTo, 55),
        SetMemory(0x660A70 + 48, SetTo, 0),
        SetMemory(0x660A70 + 52, SetTo, 0),
        SetMemory(0x660A70 + 56, SetTo, 3932160),
        SetMemory(0x660A70 + 60, SetTo, 0),
        SetMemory(0x660A70 + 64, SetTo, 61),
        SetMemory(0x660A70 + 68, SetTo, 62),
        SetMemory(0x660A70 + 72, SetTo, 4521984),
        SetMemory(0x660A70 + 76, SetTo, 5046345),
        SetMemory(0x660A70 + 80, SetTo, 5308416),
        SetMemory(0x660A70 + 84, SetTo, 5701716),
        SetMemory(0x660A70 + 88, SetTo, 6422622),
        SetMemory(0x660A70 + 92, SetTo, 6946918),
        SetMemory(0x660A70 + 96, SetTo, 0),
        SetMemory(0x660A70 + 100, SetTo, 113),
        SetMemory(0x660A70 + 104, SetTo, 0),
        SetMemory(0x660A70 + 108, SetTo, 0),
        SetMemory(0x660A70 + 112, SetTo, 0),
        SetMemory(0x660A70 + 116, SetTo, 117),
        SetMemory(0x660A70 + 120, SetTo, 8519806),
        SetMemory(0x660A70 + 124, SetTo, 135),
        SetMemory(0x660A70 + 128, SetTo, 9437324),
        SetMemory(0x660A70 + 132, SetTo, 9699475),
        SetMemory(0x660A70 + 136, SetTo, 9961472),
        SetMemory(0x660A70 + 140, SetTo, 10354843),
        SetMemory(0x660A70 + 144, SetTo, 10879138),
        SetMemory(0x660A70 + 148, SetTo, 11534509),
        SetMemory(0x660A70 + 152, SetTo, 177),
        SetMemory(0x660A70 + 156, SetTo, 0),
        SetMemory(0x660A70 + 160, SetTo, 178),
        SetMemory(0x660A70 + 164, SetTo, 11730944),
        SetMemory(0x660A70 + 168, SetTo, 12255415),
        SetMemory(0x660A70 + 172, SetTo, 12779714),
        SetMemory(0x660A70 + 176, SetTo, 12976128),
        SetMemory(0x660A70 + 180, SetTo, 13107399),
        SetMemory(0x660A70 + 184, SetTo, 13238473),
        SetMemory(0x660A70 + 188, SetTo, 13500619),
        SetMemory(0x660A70 + 192, SetTo, 209),
        SetMemory(0x660A70 + 196, SetTo, 13959380),
        SetMemory(0x660A70 + 200, SetTo, 215),
        SetMemory(0x660A70 + 204, SetTo, 14286848),
        SetMemory(0x660A70 + 208, SetTo, 0),
        SetMemory(0x660A70 + 212, SetTo, 15139040),
        SetMemory(0x660A70 + 216, SetTo, 15925485),
        SetMemory(0x660A70 + 220, SetTo, 16449783),
        SetMemory(0x660A70 + 224, SetTo, 17301763),
        SetMemory(0x660A70 + 228, SetTo, 17957133),
        SetMemory(0x660A70 + 232, SetTo, 18612503),
        SetMemory(0x660A70 + 236, SetTo, 289),
        SetMemory(0x660A70 + 240, SetTo, 294),
        SetMemory(0x660A70 + 244, SetTo, 19923243),
        SetMemory(0x660A70 + 248, SetTo, 20578613),
        SetMemory(0x660A70 + 252, SetTo, 20971839),
        SetMemory(0x660A70 + 256, SetTo, 21102913),
        SetMemory(0x660A70 + 260, SetTo, 21168128),
        SetMemory(0x660A70 + 264, SetTo, 21758279),
        SetMemory(0x660A70 + 268, SetTo, 22413649),
        SetMemory(0x660A70 + 272, SetTo, 23069019),
        SetMemory(0x660A70 + 276, SetTo, 23920997),
        SetMemory(0x660A70 + 280, SetTo, 24969592),
        SetMemory(0x660A70 + 284, SetTo, 26214789),
        SetMemory(0x660A70 + 288, SetTo, 404),
        SetMemory(0x660A70 + 292, SetTo, 408),
        SetMemory(0x660A70 + 296, SetTo, 27000832),
        SetMemory(0x660A70 + 300, SetTo, 0),
        SetMemory(0x660A70 + 304, SetTo, 0),
        SetMemory(0x660A70 + 308, SetTo, 27394463),
        SetMemory(0x660A70 + 312, SetTo, 27853222),
        SetMemory(0x660A70 + 316, SetTo, 28049408),
        SetMemory(0x660A70 + 320, SetTo, 432),
        SetMemory(0x660A70 + 324, SetTo, 28836276),
        SetMemory(0x660A70 + 328, SetTo, 29360572),
        SetMemory(0x660A70 + 332, SetTo, 29884868),
        SetMemory(0x660A70 + 336, SetTo, 30212556),
        SetMemory(0x660A70 + 340, SetTo, 30802385),
        SetMemory(0x660A70 + 344, SetTo, 474),
        SetMemory(0x660A70 + 348, SetTo, 0),
        SetMemory(0x660A70 + 352, SetTo, 478),
        SetMemory(0x660A70 + 356, SetTo, 0),
        SetMemory(0x660A70 + 360, SetTo, 0),
        SetMemory(0x660A70 + 364, SetTo, 0),
        SetMemory(0x660A70 + 368, SetTo, 0),
        SetMemory(0x660A70 + 372, SetTo, 0),
        SetMemory(0x660A70 + 376, SetTo, 0),
        SetMemory(0x660A70 + 380, SetTo, 0),
        SetMemory(0x660A70 + 384, SetTo, 0),
        SetMemory(0x660A70 + 388, SetTo, 0),
        SetMemory(0x660A70 + 392, SetTo, 0),
        SetMemory(0x660A70 + 396, SetTo, 0),
        SetMemory(0x660A70 + 400, SetTo, 0),
        SetMemory(0x660A70 + 404, SetTo, 0),
        SetMemory(0x660A70 + 408, SetTo, 31457759),
        SetMemory(0x660A70 + 412, SetTo, 481),
        SetMemory(0x660A70 + 416, SetTo, 0),
        SetMemory(0x660A70 + 420, SetTo, 0),
        SetMemory(0x660A70 + 424, SetTo, 0),
        SetMemory(0x660A70 + 428, SetTo, 0),
        SetMemory(0x660A70 + 432, SetTo, 0),
        SetMemory(0x660A70 + 436, SetTo, 31588352),
        SetMemory(0x660A70 + 440, SetTo, 0),
        SetMemory(0x660A70 + 444, SetTo, 0),
        SetMemory(0x660A70 + 448, SetTo, 0),
        SetMemory(0x660A70 + 452, SetTo, 31653888),
        SetMemory(0x6558C0 + 0, SetTo, 851969),
        SetMemory(0x6558C0 + 4, SetTo, 2424857),
        SetMemory(0x6558C0 + 8, SetTo, 4456499),
        SetMemory(0x6558C0 + 12, SetTo, 5898319),
        SetMemory(0x6558C0 + 16, SetTo, 7471206),
        SetMemory(0x6558C0 + 20, SetTo, 9175166),
        SetMemory(0x6558C0 + 24, SetTo, 11206810),
        SetMemory(0x6558C0 + 28, SetTo, 12648630),
        SetMemory(0x6558C0 + 32, SetTo, 13697228),
        SetMemory(0x6558C0 + 36, SetTo, 14024704),
        SetMemory(0x6558C0 + 40, SetTo, 14680283),
        SetMemory(0x6558C0 + 44, SetTo, 15335653),
        SetMemory(0x6558C0 + 48, SetTo, 16122095),
        SetMemory(0x6558C0 + 52, SetTo, 17039613),
        SetMemory(0x6558C0 + 56, SetTo, 17629448),
        SetMemory(0x6558C0 + 60, SetTo, 18153745),
        SetMemory(0x6558C0 + 64, SetTo, 18678041),
        SetMemory(0x6558C0 + 68, SetTo, 19202337),
        SetMemory(0x6558C0 + 72, SetTo, 19726633),
        SetMemory(0x6558C0 + 76, SetTo, 20250929),
        SetMemory(0x6558C0 + 80, SetTo, 20775225),
        SetMemory(0x6558C0 + 84, SetTo, 21299521),
        SetMemory(0x6558C0 + 88, SetTo, 329),
        SetMemory(0x6558C0 + 92, SetTo, 21823488),
        SetMemory(0x6558C0 + 96, SetTo, 22151168),
        SetMemory(0x6558C0 + 100, SetTo, 22544724),
        SetMemory(0x6558C0 + 104, SetTo, 23265630),
        SetMemory(0x6558C0 + 108, SetTo, 360),
        SetMemory(0x6558C0 + 112, SetTo, 0),
        SetMemory(0x6558C0 + 116, SetTo, 0),
        SetMemory(0x656198 + 0, SetTo, 393217),
        SetMemory(0x656198 + 4, SetTo, 786443),
        SetMemory(0x656198 + 8, SetTo, 851968),
        SetMemory(0x656198 + 12, SetTo, 1179648),
        SetMemory(0x656198 + 16, SetTo, 1572887),
        SetMemory(0x656198 + 20, SetTo, 2228253),
        SetMemory(0x656198 + 24, SetTo, 2883584),
        SetMemory(0x656198 + 28, SetTo, 3145728),
        SetMemory(0x656198 + 32, SetTo, 3670068),
        SetMemory(0x656198 + 36, SetTo, 4194364),
        SetMemory(0x656198 + 40, SetTo, 4718660),
        SetMemory(0x656198 + 44, SetTo, 76),
        SetMemory(0x656198 + 48, SetTo, 5636176),
        SetMemory(0x656198 + 52, SetTo, 6094935),
        SetMemory(0x656198 + 56, SetTo, 6291456),
        SetMemory(0x656198 + 60, SetTo, 6684773),
        SetMemory(0x656198 + 64, SetTo, 7536747),
        SetMemory(0x656198 + 68, SetTo, 0),
        SetMemory(0x656198 + 72, SetTo, 0),
        SetMemory(0x656198 + 76, SetTo, 0),
        SetMemory(0x656198 + 80, SetTo, 0),
        SetMemory(0x656198 + 84, SetTo, 0),
        SetMemory(0x6562F8 + 0, SetTo, 1048577),
        SetMemory(0x6562F8 + 4, SetTo, 1179665),
        SetMemory(0x6562F8 + 8, SetTo, 1310739),
        SetMemory(0x6562F8 + 12, SetTo, 2555937),
        SetMemory(0x6562F8 + 16, SetTo, 3211312),
        SetMemory(0x6562F8 + 20, SetTo, 5177402),
        SetMemory(0x6562F8 + 24, SetTo, 7536749),
        SetMemory(0x6562F8 + 28, SetTo, 8585340),
        SetMemory(0x6562F8 + 32, SetTo, 10289293),
        SetMemory(0x6562F8 + 36, SetTo, 11534506),
        SetMemory(0x6562F8 + 40, SetTo, 12910780),
        SetMemory(0x6562F8 + 44, SetTo, 14090446),
        SetMemory(0x6562F8 + 48, SetTo, 14549210),
        SetMemory(0x6562F8 + 52, SetTo, 14942432),
        SetMemory(0x6562F8 + 56, SetTo, 15335654),
        SetMemory(0x6562F8 + 60, SetTo, 15597805),
        SetMemory(0x6562F8 + 64, SetTo, 16187634),
        SetMemory(0x6562F8 + 68, SetTo, 249),
        SetMemory(0x6562F8 + 72, SetTo, 0),
        SetMemory(0x6562F8 + 76, SetTo, 0),
        SetMemory(0x6562F8 + 80, SetTo, 0),
        SetMemory(0x6562F8 + 84, SetTo, 0),
        SetMemory(0x665580 + 0, SetTo, 327682),
        SetMemory(0x665580 + 4, SetTo, 786440),
        SetMemory(0x665580 + 8, SetTo, 1310736),
        SetMemory(0x665580 + 12, SetTo, 1835032),
        SetMemory(0x665580 + 16, SetTo, 2621476),
        SetMemory(0x665580 + 20, SetTo, 3145772),
        SetMemory(0x665580 + 24, SetTo, 3670068),
        SetMemory(0x665580 + 28, SetTo, 4194364),
        SetMemory(0x665580 + 32, SetTo, 0),
        SetMemory(0x665580 + 36, SetTo, 5308484),
        SetMemory(0x665580 + 40, SetTo, 7405677),
        SetMemory(0x665580 + 44, SetTo, 7929973),
        SetMemory(0x665580 + 48, SetTo, 8126464),
        SetMemory(0x665580 + 52, SetTo, 8650880),
        SetMemory(0x665580 + 56, SetTo, 9568395),
        SetMemory(0x665580 + 60, SetTo, 10158233),
        SetMemory(0x665580 + 64, SetTo, 10682527),
        SetMemory(0x665580 + 68, SetTo, 11075749),
        SetMemory(0x665580 + 72, SetTo, 173),
        SetMemory(0x665580 + 76, SetTo, 11468800),
        SetMemory(0x665580 + 80, SetTo, 11862194),
        SetMemory(0x665580 + 84, SetTo, 0),
        SetMemory(0x665580 + 88, SetTo, 0),
        SetMemory(0x665580 + 92, SetTo, 188),
        SetMemory(0x665580 + 96, SetTo, 12648448),
        SetMemory(0x665580 + 100, SetTo, 13435077),
        SetMemory(0x665580 + 104, SetTo, 14876891),
        SetMemory(0x665580 + 108, SetTo, 15925483),
        SetMemory(0x665580 + 112, SetTo, 17367297),
        SetMemory(0x665580 + 116, SetTo, 18415889),
        SetMemory(0x665580 + 120, SetTo, 19464481),
        SetMemory(0x665580 + 124, SetTo, 305),
        SetMemory(0x665580 + 128, SetTo, 20840761),
        SetMemory(0x665580 + 132, SetTo, 20971520),
        SetMemory(0x665580 + 136, SetTo, 21233664),
        SetMemory(0x665580 + 140, SetTo, 21692743),
        SetMemory(0x665580 + 144, SetTo, 335),
        SetMemory(0x665580 + 148, SetTo, 339),
        SetMemory(0x665580 + 152, SetTo, 22413312),
        SetMemory(0x665580 + 156, SetTo, 23396699),
        SetMemory(0x665580 + 160, SetTo, 23789928),
        SetMemory(0x665580 + 164, SetTo, 366),
        SetMemory(0x665580 + 168, SetTo, 24379761),
        SetMemory(0x665580 + 172, SetTo, 375),
        SetMemory(0x665580 + 176, SetTo, 0),
        SetMemory(0x665580 + 180, SetTo, 378),
        SetMemory(0x665580 + 184, SetTo, 25166205),
        SetMemory(0x665580 + 188, SetTo, 25756038),
        SetMemory(0x665580 + 192, SetTo, 26017792),
        SetMemory(0x665580 + 196, SetTo, 0),
        SetMemory(0x665580 + 200, SetTo, 26411408),
        SetMemory(0x665580 + 204, SetTo, 27394464),
        SetMemory(0x665580 + 208, SetTo, 425),
        SetMemory(0x665580 + 212, SetTo, 28114944),
        SetMemory(0x665580 + 216, SetTo, 433),
        SetMemory(0x665580 + 220, SetTo, 28835840),
        SetMemory(0x665580 + 224, SetTo, 443),
        SetMemory(0x665580 + 228, SetTo, 0),
        SetMemory(0x665580 + 232, SetTo, 0),
        SetMemory(0x665580 + 236, SetTo, 0),
        SetMemory(0x665580 + 240, SetTo, 0),
        SetMemory(0x665580 + 244, SetTo, 29229056),
        SetMemory(0x665580 + 248, SetTo, 29491200),
        SetMemory(0x665580 + 252, SetTo, 30015942),
        SetMemory(0x665580 + 256, SetTo, 30540238),
        SetMemory(0x665580 + 260, SetTo, 31326678),
        SetMemory(0x665580 + 264, SetTo, 31784960),
        SetMemory(0x665580 + 268, SetTo, 32309736),
        SetMemory(0x665580 + 272, SetTo, 498),
        SetMemory(0x665580 + 276, SetTo, 0),
        SetMemory(0x665580 + 280, SetTo, 506),
        SetMemory(0x665580 + 284, SetTo, 0),
        SetMemory(0x665580 + 288, SetTo, 0),
        SetMemory(0x665580 + 292, SetTo, 0),
        SetMemory(0x665580 + 296, SetTo, 0),
        SetMemory(0x665580 + 300, SetTo, 0),
        SetMemory(0x665580 + 304, SetTo, 510),
        SetMemory(0x665580 + 308, SetTo, 33685504),
        SetMemory(0x665580 + 312, SetTo, 34340864),
        SetMemory(0x665580 + 316, SetTo, 0),
        SetMemory(0x665580 + 320, SetTo, 0),
        SetMemory(0x665580 + 324, SetTo, 0),
        SetMemory(0x665580 + 328, SetTo, 34603008),
        SetMemory(0x665580 + 332, SetTo, 36045330),
        SetMemory(0x665580 + 336, SetTo, 37945910),
        SetMemory(0x665580 + 340, SetTo, 40043088),
        SetMemory(0x665580 + 344, SetTo, 0),
        SetMemory(0x665580 + 348, SetTo, 41287680),
        SetMemory(0x665580 + 352, SetTo, 41812602),
        SetMemory(0x665580 + 356, SetTo, 642),
        SetMemory(0x665580 + 360, SetTo, 0),
        SetMemory(0x665580 + 364, SetTo, 646),
        SetMemory(0x665580 + 368, SetTo, 0),
        SetMemory(0x665580 + 372, SetTo, 0),
    ])
    

