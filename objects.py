# Copyright (c) Mathias Kaerlev 2012.

# This file is part of OpenSND.

# OpenSND is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# OpenSND is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with OpenSND.  If not, see <http://www.gnu.org/licenses/>.

from common import *
from images import *
from fonts import *
from sounds import *
from PySide.QtCore import Qt
import os

class String2_2(Text):
    name = 'String 2'
    width = 150
    height = 232
    font = font1
    color = (0, 0, 0)
    text = '[Data]\r\nName=Player\r\nMusic=1\r\nUp=Up\r\nDown=Down\r\nLeft=Left\r\nRight=Right\r\nReload=Shift\r\nSwitch=Control\r\nAimH=0 on numeric\r\nTurning=40\r\nStartweapon=0\r\nSkin=0\r\nMusicVolume=30\r\nGraphics=0\r\nFootsteps=1\r\n'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Object3(Backdrop):
    name = None
    obstacle_type = 'None'
    collision_mode = 'Fine'
    image = image776

class Title_4(ActivePicture):
    name = 'title'
    width = 800
    height = 600
    filename = 'title.jpg'

class Name_5(Edit):
    name = 'name'
    width = 241
    height = 24
    font = Font('Arial', 14, True, False, False)
    foreground = (255, 255, 255)
    background = None
    transparent = True
    border = False

class GlobalName_6(Text):
    name = 'Global Name'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Ini_7(INI):
    name = 'Ini'

class CheckVersion_8(Counter):
    name = 'Check version'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Ip2_9(Text):
    name = 'ip 2'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Ip'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Port2_10(Text):
    name = 'port 2'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Port'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Connect_11(Active):
    name = 'connect'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image232]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image529]
            },
        },
    }

class String2_12(Text):
    name = 'String 2'
    width = 326
    height = 20
    font = font20
    color = (8, 0, 0)
    text = 'Version 1.44'
    alignment = Qt.AlignLeft | Qt.AlignTop

class MooSock_13(Socket):
    name = 'MooSock'

class CheckUser_14(Counter):
    name = 'Check user'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class StringParser_15(StringParser):
    name = 'String Parser'

class Msg_16(Text):
    name = 'Msg'
    width = 316
    height = 31
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class String11_17(Text):
    name = 'String 11'
    width = 700
    height = 20
    font = font6
    color = (231, 0, 0)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class Timeout_18(Counter):
    name = 'Timeout'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = -1
    minimum = -1
    maximum = 999999999

class Edit_19(Edit):
    name = 'Edit'
    width = 216
    height = 149
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class RemoteIP_20(Text):
    name = 'remote IP'
    is_global = True
    width = 150
    height = 20
    font = font6
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class EigeneIP_21(Text):
    name = 'eigene IP'
    is_global = True
    width = 150
    height = 20
    font = font6
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class ValidChar_22(Text):
    name = 'Valid char'
    width = 480
    height = 20
    font = font1
    color = (0, 0, 0)
    text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-!$+*_'#[]/\\|"
    alignment = Qt.AlignLeft | Qt.AlignTop

class ScreenshotNr_23(Counter):
    name = 'screenshot nr'
    is_global = True
    initial = 0
    minimum = 0
    maximum = 999999999

class Edit2_24(Edit):
    name = 'Edit 2'
    width = 200
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class VerCheck_25(Text):
    name = 'VerCheck'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Version_26(Text):
    name = 'Version'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = '1.44'
    alignment = Qt.AlignLeft | Qt.AlignTop

class IrcNick_27(Text):
    name = 'irc nick'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Newid_28(Text):
    name = 'newid'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class SvrKills_29(Counter):
    name = 'svrKills'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = 0
    maximum = 999999999

class SvrDeaths_30(Counter):
    name = 'svrDeaths'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = 0
    maximum = 999999999

class SvrPoints_31(Counter):
    name = 'svrPoints'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = 0
    maximum = 999999999

class SvrKills2_32(Counter):
    name = 'svrKills 2'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = 0
    maximum = 999999999

class SvrDeaths2_33(Counter):
    name = 'svrDeaths 2'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = 0
    maximum = 999999999

class SvrPoints2_34(Counter):
    name = 'svrPoints 2'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = 0
    maximum = 999999999

class Channel1_36(Text):
    name = 'channel 1'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = '#sndo'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String12_37(Text):
    name = 'String 12'
    width = 700
    height = 20
    font = font6
    color = (8, 0, 0)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class BinaryObject_38(BinaryObject):
    name = 'Binary object'

class Zeilenumbruch_39(Text):
    name = 'Zeilenumbruch'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = '\r\n'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Lobby_40(ActivePicture):
    name = 'Lobby'
    width = 800
    height = 600
    filename = 'Lobby.jpg'

class Timeout_41(Counter):
    name = 'Timeout'
    initial = -1
    minimum = -1
    maximum = 10

class String_42(Text):
    name = 'String'
    is_global = True
    width = 141
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Version 1.44'
    alignment = Qt.AlignHCenter | Qt.AlignTop

class StringParser_43(StringParser):
    name = 'String Parser'

class ServerIPs_44(ListControl):
    name = 'Server IPs'
    width = 121
    height = 174
    font = Font('Arial', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class StatusServer_45(Text):
    name = 'Status Server'
    width = 553
    height = 20
    font = font10
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class Ip_46(Text):
    name = 'ip'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Ip'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Port_47(Text):
    name = 'port'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Port'
    alignment = Qt.AlignLeft | Qt.AlignTop

class SndKlein_48(Active):
    name = 'snd-klein'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image207]
            },
        },
    }

class Connect2_49(Active):
    name = 'connect 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image232]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image529]
            },
        },
    }

class GetServerList_50(Active):
    name = 'get server list'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image624]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image626]
            },
        },
    }

class HostAGame_51(Active):
    name = 'host a game'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image230]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image649]
            },
        },
    }

class ExitGame_52(Active):
    name = 'exit game'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image233]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image664]
            },
        },
    }

class Control_54(Counter):
    name = 'Control'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Ini_55(INI):
    name = 'Ini'
    filename = 'data.ini'

class Counter4_56(Counter):
    name = 'Counter 4'
    frames = {
        '0' : image650,
        '1' : image668,
        '2' : image669,
        '3' : image671,
        '4' : image676,
        '5' : image728,
        '6' : image730,
        '7' : image732,
        '8' : image734,
        '9' : image735,
        '-' : image744,
        '+' : image666,
        '.' : image745,
        'e' : image746,
    }
    initial = 2
    minimum = 1
    maximum = 99

class MooSock2_57(Socket):
    name = 'MooSock2'

class MessageOfDay_58(Text):
    name = 'message of day'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class WeaponAllowed_59(Text):
    name = 'weapon allowed'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class ServerError_60(Text):
    name = 'Server error'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class ServerInfo_61(Text):
    name = 'Server Info'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Edit2_62(Edit):
    name = 'Edit 2'
    width = 216
    height = 101
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Buffer_63(Text):
    name = 'buffer'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class SndKlein2_64(Active):
    name = 'snd-klein 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image288]
            },
        },
    }

class ClanTag_65(Text):
    name = 'clan tag'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Counter5_66(Counter):
    name = 'Counter 5'
    frames = {
        '0' : image650,
        '1' : image668,
        '2' : image669,
        '3' : image671,
        '4' : image676,
        '5' : image728,
        '6' : image730,
        '7' : image732,
        '8' : image734,
        '9' : image735,
        '-' : image744,
        '+' : image666,
        '.' : image745,
        'e' : image746,
    }
    initial = 100
    minimum = 0
    maximum = 100

class StringParser2_67(StringParser):
    name = 'String Parser 2'

class Edit3_68(Edit):
    name = 'Edit 3'
    width = 383
    height = 101
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Log_69(Edit):
    name = 'Log'
    width = 200
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class TextInputBox_70(Edit):
    name = 'text input box'
    width = 555
    height = 21
    font = Font('MS Sans Serif', 10, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class InputBoxModifier_71(Edit):
    name = 'input box modifier'
    width = 200
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class MooSock_72(Socket):
    name = 'MooSock'

class StingParserMotd_73(StringParser):
    name = 'sting parser motd'

class StringParse_74(StringParser):
    name = 'String Parse'

class StringParser3_75(StringParser):
    name = 'String Parser 3'

class InputBoxHandler_76(StringParser):
    name = 'input box handler'

class List_77(ListControl):
    name = 'List'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class UserList_78(ListControl):
    name = 'User list'
    width = 167
    height = 243
    font = Font('MS Sans Serif', 10, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class String2_79(Text):
    name = 'String 2'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String3_80(Text):
    name = 'String 3'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Nickname0_81(Text):
    name = 'nickname 0'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Server2_82(Text):
    name = 'server 2'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Flags_83(Active):
    name = 'flags'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image29]
            },
        },
    }

class Counter_84(Counter):
    name = 'Counter'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 1
    minimum = -999999999
    maximum = 999999999

class ChatLog_87(RichEdit):
    name = 'Chat log'
    width = 569
    height = 212
    font = Font('MS Sans Serif', 8, True, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    read_only = True
    text = ''

class IconListObject_88(IconList):
    name = 'IconList Object'
    width = 560
    height = 201
    list_type = 'Simple'
    icon_size = 16
    image = image387
    font = Font('Arial', 8, False, False, False)
    font_color = (0, 0, 0)

class Options_89(Active):
    name = 'Options'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image552]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image553]
            },
        },
    }

class JoinChat_90(Active):
    name = 'join chat'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image563]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image566]
            },
        },
    }

class SubApplication_91(SubApplication):
    name = 'Sub-Application'
    visible = False
    width = 300
    height = 350
    start_frame = 7

class Ctoip_92(Active):
    name = 'ctoip'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image247]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image777]
            },
        },
    }

class SubApplication2_93(SubApplication):
    name = 'Sub-Application 2'
    visible = False
    width = 300
    height = 250
    start_frame = 8

class Host_95(ActivePicture):
    name = 'host'
    width = 800
    height = 600
    filename = 'host.jpg'

class Serverinfo_96(Text):
    name = 'Serverinfo'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Serverinfo2_97(Text):
    name = 'Serverinfo 2'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Serverinfo3_98(Text):
    name = 'Serverinfo 3'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Map_99(Counter):
    name = 'Map'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class ServerName_100(Text):
    name = 'Server Name'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class JoinMap_101(Counter):
    name = 'Join Map'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class MaxPlayer_102(Counter):
    name = 'MaxPlayer'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class String2_103(Text):
    name = 'String 2'
    width = 107
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Server name:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class ServerName2_104(Edit):
    name = 'Server name 2'
    width = 200
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class String4_105(Text):
    name = 'String 4'
    width = 101
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Map:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String5_106(Text):
    name = 'String 5'
    width = 101
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Max players:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class MaxPl_107(Edit):
    name = 'max pl'
    width = 29
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class String6_108(Text):
    name = 'String 6'
    width = 111
    height = 20
    font = font7
    color = (255, 255, 255)
    text = '( 0 = No limit)'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Button_109(ButtonControl):
    name = 'Button'
    width = 13
    height = 12
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['']

class String7_110(Text):
    name = 'String 7'
    width = 145
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Dedicated Server:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String8_111(Text):
    name = 'String 8'
    width = 145
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Friendly Fire:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class FF_112(ButtonControl):
    name = 'FF'
    width = 13
    height = 12
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['']

class StartMap_113(Counter):
    name = 'start map'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class String9_114(Text):
    name = 'String 9'
    width = 145
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Score Limit:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class ScoreLimit_115(Edit):
    name = 'score limit'
    width = 33
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class String10_116(Text):
    name = 'String 10'
    width = 145
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Time Limit:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class TimeLimit_117(Edit):
    name = 'time limit'
    width = 33
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class String11_118(Text):
    name = 'String 11'
    width = 145
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Mapcycle:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class MapcycYesno_119(ButtonControl):
    name = 'Mapcyc yesno'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['']

class String12_120(Text):
    name = 'String 12'
    width = 145
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Host on port:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Port3_121(Edit):
    name = 'port 3'
    width = 39
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Active2_122(Active):
    name = 'Active 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image687]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image695]
            },
        },
    }

class Active3_123(Active):
    name = 'Active 3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image693]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image698]
            },
        },
    }

class MapList_124(ListControl):
    name = 'Map-List'
    width = 158
    height = 503
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class ChosedMap_125(Text):
    name = 'Chosed map'
    is_global = True
    width = 152
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class ChosedMapWithoutPath_126(Text):
    name = 'Chosed map without path'
    is_global = True
    width = 152
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Error_127(Text):
    name = 'Error'
    width = 150
    height = 20
    font = font10
    color = (255, 0, 0)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class LoadMap_128(ListControl):
    name = 'Load-Map'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class UserKills_130(Counter):
    name = 'User-Kills'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class UserDeaths_131(Counter):
    name = 'User-Deaths'
    is_global = True
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class GlobalPW_132(Text):
    name = 'Global PW'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String13_133(Text):
    name = 'String 13'
    width = 101
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'MOTD:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Motd_134(Edit):
    name = 'motd'
    width = 253
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class String14_135(Text):
    name = 'String 14'
    width = 113
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Weapons:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class DesertEagle_136(ButtonControl):
    name = 'Desert Eagle'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String15_137(Text):
    name = 'String 15'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'Desert Eagle'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String16_138(Text):
    name = 'String 16'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'Benelli M1'
    alignment = Qt.AlignLeft | Qt.AlignTop

class M1_139(ButtonControl):
    name = 'm1'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String17_140(Text):
    name = 'String 17'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'MP 5'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String18_141(Text):
    name = 'String 18'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'AK 47'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Mp5_142(ButtonControl):
    name = 'mp 5'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class Ak47_143(ButtonControl):
    name = 'ak 47'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String19_144(Text):
    name = 'String 19'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'Colt M4A1'
    alignment = Qt.AlignLeft | Qt.AlignTop

class M5_145(ButtonControl):
    name = 'm 5'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String20_146(Text):
    name = 'String 20'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'G3A3'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String21_147(Text):
    name = 'String 21'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'AW 50 Sniper'
    alignment = Qt.AlignLeft | Qt.AlignTop

class G3_148(ButtonControl):
    name = 'g3'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class Sniper_149(ButtonControl):
    name = 'sniper'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class HostIP_150(Text):
    name = 'Host IP'
    is_global = True
    width = 150
    height = 20
    font = font6
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class Edit2_151(Edit):
    name = 'Edit 2'
    width = 216
    height = 101
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class String23_152(Text):
    name = 'String 23'
    width = 113
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Password:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Pw_153(ButtonControl):
    name = 'pw?'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class Enterpw_154(Edit):
    name = 'enterpw'
    width = 89
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class SvrPw_155(Text):
    name = 'svr_pw'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String24_156(Text):
    name = 'String 24'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'SVD'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Xm8_157(ButtonControl):
    name = 'xm8'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String25_158(Text):
    name = 'String 25'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'Galil'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Uzi_159(ButtonControl):
    name = 'uzi'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String26_160(Text):
    name = 'String 26'
    width = 113
    height = 20
    font = font7
    color = (8, 0, 0)
    text = 'SR 60'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Sr60_161(ButtonControl):
    name = 'sr60'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String27_162(Text):
    name = 'String 27'
    width = 113
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Map Sending:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Mapd_163(ButtonControl):
    name = 'mapd'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['Desert Eagle']

class String28_164(Text):
    name = 'String 28'
    width = 113
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Map cycle:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class GlobalValues_165(Active):
    name = 'global values'
    is_global = True
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image29]
            },
        },
    }

class Obj2ndPort_166(Text):
    name = '2nd port'
    width = 145
    height = 20
    font = font10
    color = (255, 255, 255)
    text = 'and 1204'
    alignment = Qt.AlignLeft | Qt.AlignTop

class String29_167(Text):
    name = 'String 29'
    width = 113
    height = 20
    font = font7
    color = (255, 255, 255)
    text = 'Hide server:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Hideserver_168(ButtonControl):
    name = 'hideserver'
    width = 11
    height = 11
    type = 'Check'
    font = Font('Arial', 12, True, False, False)
    foreground = (0, 0, 0)
    background = (192, 192, 192)
    strings = ['']

class Connecting_169(ActivePicture):
    name = 'Connecting'
    width = 800
    height = 600
    filename = 'Connecting.jpg'

class Status_170(Text):
    name = 'Status'
    width = 414
    height = 127
    font = font12
    color = (255, 255, 0)
    text = 'Connecting'
    alignment = Qt.AlignHCenter | Qt.AlignTop

class CheckMap_171(ListControl):
    name = 'Check map'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class Info_173(Text):
    name = 'Info'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class VersionCheck_174(Text):
    name = 'Version check'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class CurrentPlayer_175(Counter):
    name = 'current player'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class CheckDaMap_176(Text):
    name = 'check da map'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Edit_177(Edit):
    name = 'Edit'
    width = 200
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Enterpw_179(Edit):
    name = 'enterpw'
    width = 200
    height = 20
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Rightpw_180(Text):
    name = 'rightpw'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Moo_181(Socket):
    name = 'Moo'

class XtraXtraCRC_182(ChecksumCalculator):
    name = 'Xtra Xtra CRC'

class Mapid_183(Text):
    name = 'mapid'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Mapid2_184(Text):
    name = 'mapid 2'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Sting_186(Text):
    name = 'sting'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Mapload_187(ListControl):
    name = 'mapload'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class MapTileCounter_188(Counter):
    name = 'map tile counter'
    initial = 0
    minimum = 0
    maximum = 999999999

class MapTileMax_189(Counter):
    name = 'map tile max'
    initial = 1
    minimum = 1
    maximum = 999999999

class Status2_190(Text):
    name = 'Status 2'
    width = 414
    height = 127
    font = font12
    color = (8, 0, 0)
    text = 'Connecting'
    alignment = Qt.AlignHCenter | Qt.AlignTop

class SpawnArea_192(Active):
    name = 'Spawn area'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image65]
            },
        },
    }

class Fusssoldat_193(Active):
    name = 'Fusssoldat'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image424]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image431]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image410]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image811]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image206]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image869]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image540]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image577]
            },
        },
        'Walking' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image424, image425, image426, image427, image428]
            },
            4 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image431, image432, image821, image433, image434]
            },
            8 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image409, image410, image411, image826, image413]
            },
            12 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image811, image271, image829, image830, image831]
            },
            16 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image206, image209, image237, image239, image252]
            },
            20 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image869, image415, image422, image842, image423]
            },
            24 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image540, image541, image569, image570, image876]
            },
            28 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image577, image578, image579, image581, image582]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image264]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image186]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image198]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image123]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image109]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image152]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image240]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image255]
            },
        },
        'User defined 2' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image264, image265, image266, image267, image268]
            },
            4 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image186, image188, image184, image192, image194]
            },
            8 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image196, image198, image200, image161, image202]
            },
            12 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image123, image120, image204, image121, image122]
            },
            16 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image109, image108, image103, image104, image111]
            },
            20 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image152, image154, image157, image278, image159]
            },
            24 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image240, image242, image485, image254, image253]
            },
            28 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image255, image261, image262, image263, image270]
            },
        },
        'User defined 3' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image390, image391, image392, image393, image395]
            },
            4 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image446, image445, image448, image440, image441]
            },
            8 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image416, image417, image396, image418, image420]
            },
            12 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image447, image421, image449, image349, image350]
            },
            16 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image289, image290, image291, image296, image293]
            },
            20 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image339, image340, image430, image371, image370]
            },
            24 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image408, image403, image404, image405, image407]
            },
            28 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image435, image436, image429, image443, image444]
            },
        },
        'User defined 4' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image390]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image446]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image417]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image447]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image289]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image339]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image408]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image435]
            },
        },
    }

class Fusssoldat2_194(Active):
    name = 'Fusssoldat 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image351]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image497]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image937]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image857]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image81]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image845]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image663]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image685]
            },
        },
        'Walking' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image351, image355, image356, image357, image358]
            },
            4 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image497, image498, image53, image499, image500]
            },
            8 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image487, image937, image488, image934, image489]
            },
            12 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image857, image332, image54, image894, image897]
            },
            16 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image81, image82, image83, image84, image85]
            },
            20 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image845, image490, image491, image884, image493]
            },
            24 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image663, image673, image674, image677, image939]
            },
            28 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image685, image690, image691, image1021, image692]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image167, image170, image172, image174, image176]
            },
            4 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image275, image276, image277, image279, image280]
            },
            8 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image180, image182, image190, image241, image222]
            },
            12 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image116, image125, image117, image118, image119]
            },
            16 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image91, image92, image93, image94, image95]
            },
            20 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image281, image259, image269, image272, image273]
            },
            24 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image319, image320, image331, image334, image333]
            },
            28 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image386, image388, image397, image398, image399]
            },
        },
        'User defined 2' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image167]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image275]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image182]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image116]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image91]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image281]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image319]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image381]
            },
        },
        'User defined 3' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image495, image940, image501, image941, image503]
            },
            4 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image534, image535, image536, image571, image572]
            },
            8 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image506, image505, image518, image504, image517]
            },
            12 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image470, image456, image457, image463, image466]
            },
            16 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image419, image936, image402, image938, image412]
            },
            20 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image526, image942, image600, image943, image531]
            },
            24 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image595, image590, image591, image592, image593]
            },
            28 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image610, image944, image604, image945, image614]
            },
        },
        'User defined 4' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image495]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image534]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image505]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image470]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image419]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image526]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image595]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image610]
            },
        },
    }

class Active7_195(Active):
    name = 'Active 7'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image224]
            },
        },
    }

class Active8_196(Active):
    name = 'Active 8'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image224]
            },
        },
    }

class Rauch_197(Active):
    name = 'Rauch'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image716]
            },
            1 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image236]
            },
            2 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image580]
            },
            3 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image625]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image717]
            },
            5 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image628]
            },
            6 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image630]
            },
            7 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image648]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image719]
            },
            9 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image651]
            },
            10 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image653]
            },
            11 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image655]
            },
            12 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image721]
            },
            13 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image662]
            },
            14 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image665]
            },
            15 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image667]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image725]
            },
            17 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image670]
            },
            18 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image672]
            },
            19 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image686]
            },
            20 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image727]
            },
            21 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image689]
            },
            22 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image694]
            },
            23 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image696]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image729]
            },
            25 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image699]
            },
            26 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image701]
            },
            27 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image703]
            },
            28 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image731]
            },
            29 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image706]
            },
            30 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image718]
            },
            31 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image722]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image149]
            },
            1 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image151]
            },
            2 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image153]
            },
            3 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image156]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image158]
            },
            5 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image160]
            },
            6 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image162]
            },
            7 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image164]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image166]
            },
            9 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image169]
            },
            10 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image171]
            },
            11 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image173]
            },
            12 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image175]
            },
            13 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image177]
            },
            14 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image179]
            },
            15 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image181]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image183]
            },
            17 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image185]
            },
            18 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image187]
            },
            19 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image189]
            },
            20 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image191]
            },
            21 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image193]
            },
            22 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image195]
            },
            23 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image197]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image199]
            },
            25 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image201]
            },
            26 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image203]
            },
            27 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image205]
            },
            28 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image208]
            },
            29 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image211]
            },
            30 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image235]
            },
            31 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image238]
            },
        },
    }

class HitBack_198(Active):
    name = 'HitBack'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 35,
                'max_speed' : 35,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image248, image249, image250, image251]
            },
        },
    }

class Obj2Die_199(Active):
    name = '2 Die'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image295, image297, image299]
            },
            8 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image538, image762, image304]
            },
            16 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image301, image307, image308]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image299, image471, image492, image522]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image304, image596, image599, image528]
            },
            16 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image585, image583, image576, image575]
            },
        },
    }

class String2_200(Text):
    name = 'String 2'
    visible = False
    width = 149
    height = 20
    font = font2
    color = (255, 0, 0)
    text = 'Respawn in'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Respawn_201(Counter):
    name = 'Respawn'
    visible = False
    frames = {
        '0' : image345,
        '1' : image346,
        '2' : image347,
        '3' : image348,
        '4' : image654,
        '5' : image660,
        '6' : image17,
        '7' : image18,
        '8' : image19,
        '9' : image20,
        '-' : image21,
        '+' : image22,
        '.' : image23,
        'e' : image24,
    }
    initial = 10
    minimum = 0
    maximum = 30

class Splitter_202Movement(Ball):
    speed = 20
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 0

class Splitter_202(Active):
    name = 'Splitter'
    movement_class = Splitter_202Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image336, image337, image338]
            },
        },
    }

class Killed_203(Text):
    name = 'Killed'
    visible = False
    width = 520
    height = 35
    font = font11
    color = (255, 0, 0)
    text = 'Text'
    alignment = Qt.AlignHCenter | Qt.AlignTop

class Chat_204(Edit):
    name = 'Chat'
    width = 437
    height = 23
    font = Font('Verdana', 10, True, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Message1_205(Text):
    name = 'Message1'
    width = 650
    height = 17
    font = font5
    color = (255, 251, 240)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Message2_206(Text):
    name = 'Message 2'
    width = 650
    height = 17
    font = font5
    color = (255, 251, 240)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Message3_207(Text):
    name = 'Message 3'
    width = 650
    height = 17
    font = font5
    color = (255, 251, 240)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class AmmoPack_208(Active):
    name = 'Ammo-Pack'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image366]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image469]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image468]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image366]
            },
            28 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image366]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image366, image450, image454, image643]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image469, image824, image828, image836]
            },
            4 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image468, image787, image807, image814]
            },
            24 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image366, image450, image454, image643]
            },
            28 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image366, image450, image454, image643]
            },
        },
    }

class Frags_209(Counter):
    name = 'Frags'
    frames = {
        '0' : image352,
        '1' : image353,
        '2' : image354,
        '3' : image365,
        '4' : image367,
        '5' : image368,
        '6' : image369,
        '7' : image372,
        '8' : image373,
        '9' : image374,
        '-' : image375,
        '+' : image376,
        '.' : image377,
        'e' : image378,
    }
    initial = 0
    minimum = -9999
    maximum = 99999

class Deaths_210(Counter):
    name = 'Deaths'
    frames = {
        '0' : image352,
        '1' : image353,
        '2' : image354,
        '3' : image365,
        '4' : image367,
        '5' : image368,
        '6' : image369,
        '7' : image372,
        '8' : image373,
        '9' : image374,
        '-' : image375,
        '+' : image376,
        '.' : image377,
        'e' : image378,
    }
    initial = 0
    minimum = 0
    maximum = 1000

class SkillCounter_211(Counter):
    name = 'Skill Counter'
    initial = 0
    minimum = 0
    maximum = 20

class MagicExplode3_212(Active):
    name = 'Magic Explode 3'
    animations = {
        'Disappearing' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image341, image344, image361, image362, image363, image364]
            },
        },
    }

class Active5_213(Active):
    name = 'Active 5'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image464, image467]
            },
        },
    }

class Active6_214(Active):
    name = 'Active 6'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image472]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image342]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image343]
            },
            12 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image360]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image549]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image516]
            },
        },
    }

class Gaswolke_215Movement(Ball):
    speed = 1
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 0

class Gaswolke_215(Active):
    name = 'Gaswolke'
    movement_class = Gaswolke_215Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image741, image740, image742]
            },
        },
        'Appearing' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image738, image733, image715, image741, image740]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image742, image743, image750, image747]
            },
        },
    }

class CheckKick_216(Text):
    name = 'Check Kick'
    is_global = True
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class ChangeMap_217(Text):
    name = 'Change Map'
    width = 757
    height = 30
    font = font11
    color = (255, 255, 255)
    text = 'Loading Map...'
    alignment = Qt.AlignHCenter | Qt.AlignTop

class ActiveObject1_218(Active):
    name = 'Active object 1'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 50,
                'back_to' : 15,
                'frames' : [image126, image127, image128, image129, image130, image131, image132, image133, image134, image135, image136, image137, image138, image139, image140, image141]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image768, image769]
            },
        },
    }

class Strafing_219Movement(Ball):
    speed = 7
    randomizer = 0
    angles = 0
    security = 100
    deceleration = 0

class Strafing_219(Active):
    name = 'Strafing'
    movement_class = Strafing_219Movement
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image294]
            },
        },
    }

class Strafing2_220Movement(Ball):
    speed = 7
    randomizer = 0
    angles = 0
    security = 100
    deceleration = 0

class Strafing2_220(Active):
    name = 'Strafing 2'
    movement_class = Strafing2_220Movement
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image294]
            },
        },
    }

class ExitCounter_221(Counter):
    name = 'exit counter'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Active9_222(Active):
    name = 'Active 9'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image749]
            },
        },
    }

class Mouse_224Movement(Mouse):
    x1 = -26
    y1 = -3
    x2 = 27
    y2 = 5

class Mouse_224(Active):
    name = 'mouse'
    movement_class = Mouse_224Movement
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image229]
            },
        },
    }

class Left_225(Active):
    name = 'left'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image210]
            },
        },
    }

class Right_226(Active):
    name = 'right'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image210]
            },
        },
    }

class Up_227(Active):
    name = 'Up'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image210]
            },
        },
    }

class Down_228(Active):
    name = 'Down'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image210]
            },
        },
    }

class Mouse2_229Movement(Mouse):
    x1 = -4
    y1 = -25
    x2 = 4
    y2 = 27

class Mouse2_229(Active):
    name = 'mouse 2'
    movement_class = Mouse2_229Movement
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image229]
            },
        },
    }

class ShotLatence_230(Counter):
    name = 'Shot Latence'
    initial = 0
    minimum = 0
    maximum = 5000

class ScoreBoard_231(ListControl):
    name = 'score-board'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class PingCounter_232(Counter):
    name = 'Ping Counter'
    initial = 0
    minimum = 0
    maximum = 999

class Ping_233(Counter):
    name = 'Ping'
    initial = 0
    minimum = 0
    maximum = 999

class ScoreBar_234(Active):
    name = 'score-bar'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image530]
            },
        },
    }

class NameScore_235(Text):
    name = 'name-score'
    width = 140
    height = 20
    font = font17
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class FragsScore_236(Text):
    name = 'frags-score'
    width = 69
    height = 20
    font = font17
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class IdScore_237(Text):
    name = 'id-score'
    width = 58
    height = 20
    font = font17
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class Accuracy_238(Counter):
    name = 'Accuracy'
    initial = 0
    minimum = 0
    maximum = 50

class Oben_239(Active):
    name = 'oben'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image636]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image561]
            },
        },
    }

class Unten_240(Active):
    name = 'unten'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image652]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image401]
            },
        },
    }

class Rechts_241(Active):
    name = 'rechts'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image638]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image565]
            },
        },
    }

class Links_242(Active):
    name = 'links'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image647]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image562]
            },
        },
    }

class Message4_243(Text):
    name = 'Message 4'
    width = 650
    height = 17
    font = font5
    color = (255, 251, 240)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class ErrorMsg_244(Text):
    name = 'Error-msg'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Unkown'
    alignment = Qt.AlignLeft | Qt.AlignTop

class DurchlaufChat_245(Counter):
    name = 'Durchlauf-Chat'
    initial = 0
    minimum = 0
    maximum = 3

class Counter3_246(Counter):
    name = 'Counter 3'
    initial = 0
    minimum = 0
    maximum = 45

class Exp_247(Active):
    name = 'Exp'
    animations = {
        'Disappearing' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image451, image453, image385, image382, image527, image573, image383, image588, image608, image609, image611]
            },
        },
    }

class Frantic_248Movement(Path):
    min_speed = 0
    max_speed = 60
    loop = False
    reposition = False
    reverse = False
    steps = [
        {'y': -16383, 'x': 1, 'pause': 0, 'name': None},
    ]

class Frantic_248(Active):
    name = 'frantic'
    movement_class = Frantic_248Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image217]
            },
        },
    }

class Daunting_249Movement(Path):
    min_speed = 0
    max_speed = 60
    loop = False
    reposition = False
    reverse = False
    steps = [
        {'y': 16383, 'x': -1, 'pause': 0, 'name': None},
    ]

class Daunting_249(Active):
    name = 'daunting'
    movement_class = Daunting_249Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image218]
            },
        },
    }

class Godlike_250Movement(Path):
    min_speed = 0
    max_speed = 60
    loop = False
    reposition = False
    reverse = False
    steps = [
        {'y': 0, 'x': 731, 'pause': 0, 'name': None},
    ]

class Godlike_250(Active):
    name = 'godlike'
    movement_class = Godlike_250Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image219]
            },
        },
    }

class FastMouse_252(Counter):
    name = 'fast mouse'
    initial = 0
    minimum = 0
    maximum = 200

class Blood3_253(Active):
    name = 'Blood 3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 70,
                'max_speed' : 70,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image714, image753, image754, image757, image767, image770, image773, image782, image783]
            },
            16 : {
                'min_speed' : 70,
                'max_speed' : 70,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image751, image554, image555, image556, image557, image558, image568, image629, image713]
            },
        },
    }

class Active2_254Movement(Ball):
    speed = 18
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 0

class Active2_254(Active):
    name = 'Active 2'
    movement_class = Active2_254Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image947]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image948]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image949]
            },
            12 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image950]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image951]
            },
            20 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image952]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image954]
            },
            28 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image953]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1011, image983, image1005, image1014]
            },
            4 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1071, image1043, image1065, image1074]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1130, image1102, image1124, image1133]
            },
            12 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image997, image966, image991, image1000]
            },
            16 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1061, image1032, image1055, image1064]
            },
            20 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1125, image1095, image1118, image1128]
            },
            24 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1186, image1158, image1180, image1189]
            },
            28 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1245, image1217, image1239, image1248]
            },
        },
    }

class Obj1Die_255(Active):
    name = '1 Die'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image460, image461, image465]
            },
            8 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image312, image311, image310]
            },
            16 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image305, image300, image309]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image465, image477, image519, image525]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image310, image633, image641, image646]
            },
            16 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image598, image597, image594, image589]
            },
        },
    }

class Grass_256(Active):
    name = 'Grass'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image380]
            },
        },
    }

class Desert_257(Active):
    name = 'desert'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image442]
            },
        },
    }

class Dust_258(Active):
    name = 'dust'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image564]
            },
        },
    }

class LoadMap_259(ListControl):
    name = 'Load Map'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class Tree_260(Active):
    name = 'tree'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image225]
            },
        },
    }

class BackgroundX_261(Counter):
    name = 'Background-X'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class BackgroundY_262(Counter):
    name = 'Background-Y'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Rock_264(Active):
    name = 'rock'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image306]
            },
        },
    }

class DeadTree_265(Active):
    name = 'dead tree'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image234]
            },
        },
    }

class GroundBackground_266(Active):
    name = 'Ground-background'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image400]
            },
        },
    }

class Stone_267(Active):
    name = 'stone'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image303]
            },
        },
    }

class TrackX_268(Counter):
    name = 'track x'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class TrackY_269(Counter):
    name = 'track y'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Track_270(Counter):
    name = 'track'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class House_271(Active):
    name = 'house'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image458]
            },
        },
    }

class Sidewalk_272(Active):
    name = 'Sidewalk'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image228]
            },
        },
    }

class BrokenSidewalk_273(Active):
    name = 'broken sidewalk'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image231]
            },
        },
    }

class Street_274(Active):
    name = 'street'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image414]
            },
        },
    }

class PoliceCar_275(Active):
    name = 'police car'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image459]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image394]
            },
        },
    }

class PoliceCar2_276(Active):
    name = 'police car 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image476]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image539]
            },
        },
    }

class Stone2_277(Active):
    name = 'stone 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image507]
            },
        },
    }

class Tree3_278(Active):
    name = 'tree 3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image508]
            },
        },
    }

class Street2_279(Active):
    name = 'street 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image480]
            },
        },
    }

class Sidewalk2_280(Active):
    name = 'Sidewalk 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image478]
            },
        },
    }

class Crossroad_281(Active):
    name = 'crossroad'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image559]
            },
        },
    }

class Rock3_282(Active):
    name = 'Rock 3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image601]
            },
        },
    }

class Rock3_283(Active):
    name = 'Rock3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image603]
            },
        },
    }

class Rock4_284(Active):
    name = 'Rock4'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image511]
            },
        },
    }

class Skeleton_285(Active):
    name = 'Skeleton'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image512]
            },
        },
    }

class Bush_286(Active):
    name = 'Bush'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image513]
            },
        },
    }

class Box_287(Active):
    name = 'Box'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image532]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class DestroyedBox_288(Active):
    name = 'Destroyed box'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image515]
            },
        },
    }

class Gate_289(Active):
    name = 'Gate'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image1]
            },
        },
    }

class Bush2_290(Active):
    name = 'Bush2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image537]
            },
        },
    }

class Boulders_291(Active):
    name = 'Boulders'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image227]
            },
        },
    }

class Cactus_292(Active):
    name = 'cactus'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image631]
            },
        },
    }

class SmallCactus_293(Active):
    name = 'small cactus'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image632]
            },
        },
    }

class Stone3_294(Active):
    name = 'Stone3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image533]
            },
        },
    }

class Tombstone_295(Active):
    name = 'Tombstone'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image514]
            },
        },
    }

class Floor_296(Active):
    name = 'floor'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image615]
            },
        },
    }

class Floor2_297(Active):
    name = 'floor2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image221]
            },
        },
    }

class WoodenFloor_298(Active):
    name = 'wooden floor'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image618]
            },
        },
    }

class StoneFloor_299(Active):
    name = 'stone floor'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image619]
            },
        },
    }

class Wall11_300(Active):
    name = 'wall11'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image316]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class Wall12_301(Active):
    name = 'wall12'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image314]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class Wall21_302(Active):
    name = 'wall21'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image622]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class Wall22_303(Active):
    name = 'wall22'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image623]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class Tree3_304(Active):
    name = 'tree3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image584]
            },
        },
    }

class Pond_305(Active):
    name = 'pond'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image560]
            },
        },
    }

class TestShoot_306(Active):
    name = 'test shoot'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image389]
            },
        },
    }

class IdPing_307(Text):
    name = 'id-ping'
    width = 58
    height = 20
    font = font17
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class Obj1Weapon_308(Active):
    name = '1. Weapon'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image510]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image606]
            },
        },
    }

class Obj2Weapon_309(Active):
    name = '2. weapon'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image605]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image634]
            },
        },
    }

class AmmoText_310(Active):
    name = 'ammo text'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image635]
            },
        },
    }

class AmmoCurrent_311(Counter):
    name = 'ammo current'
    frames = {
        '0' : image789,
        '1' : image802,
        '2' : image788,
        '3' : image791,
        '4' : image792,
        '5' : image794,
        '6' : image793,
        '7' : image795,
        '8' : image790,
        '9' : image798,
        '-' : image797,
        '+' : image799,
        '.' : image800,
        'e' : image801,
    }
    initial = 0
    minimum = 0
    maximum = 99

class AmmoFull_312(Counter):
    name = 'ammo full'
    frames = {
        '0' : image789,
        '1' : image802,
        '2' : image788,
        '3' : image791,
        '4' : image792,
        '5' : image794,
        '6' : image793,
        '7' : image795,
        '8' : image790,
        '9' : image798,
        '-' : image797,
        '+' : image799,
        '.' : image800,
        'e' : image801,
    }
    initial = 0
    minimum = 0
    maximum = 99

class _313(Active):
    name = '/'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image637]
            },
        },
    }

class Obj1WeaponList_314(Active):
    name = '1. weapon list'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image681]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image675]
            },
        },
    }

class Obj2WeaponList_315(Active):
    name = '2. weapon list'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image704]
            },
            2 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image872]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image786]
            },
            6 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image873]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image761]
            },
            10 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image813]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image726]
            },
            20 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image805]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image707]
            },
            28 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image803]
            },
            30 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image284]
            },
        },
    }

class PlOnlineText_316(Active):
    name = 'pl online text'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image702]
            },
        },
    }

class Players_317(Counter):
    name = 'Players'
    visible = False
    frames = {
        '0' : image789,
        '1' : image802,
        '2' : image788,
        '3' : image791,
        '4' : image792,
        '5' : image794,
        '6' : image793,
        '7' : image795,
        '8' : image790,
        '9' : image798,
        '-' : image797,
        '+' : image799,
        '.' : image800,
        'e' : image801,
    }
    initial = 1
    minimum = 0
    maximum = 99

class SecondWeapon_318(Counter):
    name = 'Second Weapon'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class AmmoTest_319(Active):
    name = 'Ammo-test'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image366]
            },
        },
    }

class WeaponList_320(ListControl):
    name = 'weapon list'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class Ammo1_321(Counter):
    name = 'Ammo1'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Ammo2_322(Counter):
    name = 'Ammo 2'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Reload2_323(Counter):
    name = 'Reload 2'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Sleep_324(Counter):
    name = 'sleep'
    initial = 0
    minimum = 0
    maximum = 5

class DetectMouseChange_325(Counter):
    name = 'detect mouse change'
    initial = 0
    minimum = -1
    maximum = 1

class SaveMouseChange_326(Counter):
    name = 'save mouse change'
    initial = 0
    minimum = -1
    maximum = 1

class Rubble_327(Active):
    name = 'rubble'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image12]
            },
        },
    }

class Skeleton2_328(Active):
    name = 'Skeleton2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image5]
            },
        },
    }

class Entrance_329(Active):
    name = 'entrance'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image6]
            },
        },
    }

class Lantern_330(Active):
    name = 'lantern'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image7]
            },
        },
    }

class BurningBox_331(Active):
    name = 'burning box'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image15, image16, image25]
            },
        },
    }

class MsgCounter_332(Counter):
    name = 'msg counter'
    initial = 0
    minimum = 0
    maximum = 10

class FlameDie_333(Active):
    name = 'flame die'
    animations = {
        'Disappearing' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image41, image52, image55, image56, image57, image58, image59, image60, image43, image44, image45]
            },
        },
    }

class Player_334(Active):
    name = 'Player'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image8]
            },
        },
    }

class MooSock_335(Socket):
    name = 'MooSock'

class Edit2_336(Edit):
    name = 'Edit 2'
    width = 185
    height = 123
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Obj3Die_338(Active):
    name = '3 Die'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image80, image86, image87]
            },
            8 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image89, image88, image90]
            },
            16 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image33, image32, image35]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image87, image479, image521, image587]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image90, image657, image678, image684]
            },
            16 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image35, image640, image639, image612]
            },
        },
    }

class Obj4Die_339(Active):
    name = '4 Die'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image99, image100, image101]
            },
            8 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image106, image102, image105]
            },
            16 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image37, image34, image36]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image101, image494, image524, image607]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image105, image709, image712, image723]
            },
            16 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image659, image658, image656, image645]
            },
        },
    }

class Obj5Die_340(Active):
    name = '5 Die'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image113, image114, image115]
            },
            8 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image143, image124, image142]
            },
            16 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image40, image38, image39]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image115, image520, image586, image642]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image142, image736, image739, image756]
            },
            16 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image711, image710, image708, image683]
            },
        },
    }

class Obj6Die_341(Active):
    name = '6 Die'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image147, image148, image150]
            },
            8 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image178, image163, image165]
            },
            16 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image47, image42, image46]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image150, image523, image602, image679]
            },
            8 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image165, image763, image781, image806]
            },
            16 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image46, image737, image724, image720]
            },
        },
    }

class Police_342(Text):
    name = 'police'
    visible = False
    width = 170
    height = 20
    font = font7
    color = (59, 107, 203)
    text = '1) Join police forces'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Terror_343(Text):
    name = 'terror'
    visible = False
    width = 142
    height = 20
    font = font7
    color = (255, 255, 255)
    text = '2) Join terrorists'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Mode_344(Counter):
    name = 'Mode'
    initial = 0
    minimum = 0
    maximum = 3

class PoliceSpawn_345(Active):
    name = 'police spawn'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image67]
            },
        },
    }

class TerrorSpawn_346(Active):
    name = 'terror spawn'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image68]
            },
        },
    }

class NameScore2_347(Text):
    name = 'name-score 2'
    width = 140
    height = 20
    font = font17
    color = (59, 107, 203)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class FragsScore2_348(Text):
    name = 'frags-score 2'
    width = 69
    height = 20
    font = font17
    color = (59, 107, 203)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class IdScore2_349(Text):
    name = 'id-score 2'
    width = 58
    height = 20
    font = font17
    color = (59, 107, 203)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class IdPing2_350(Text):
    name = 'id-ping 2'
    width = 58
    height = 20
    font = font17
    color = (59, 107, 203)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class NameScore3_351(Text):
    name = 'name-score 3'
    width = 140
    height = 20
    font = font17
    color = (128, 128, 128)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class FragsScore3_352(Text):
    name = 'frags-score 3'
    width = 69
    height = 20
    font = font17
    color = (128, 128, 128)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class IdScore3_353(Text):
    name = 'id-score 3'
    width = 58
    height = 20
    font = font17
    color = (128, 128, 128)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class IdPing3_354(Text):
    name = 'id-ping 3'
    width = 58
    height = 20
    font = font17
    color = (128, 128, 128)
    text = ''
    alignment = Qt.AlignHCenter | Qt.AlignTop

class Chatting_355(Active):
    name = 'chatting'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 40,
                'max_speed' : 40,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image112, image71, image76, image97, image76, image71]
            },
        },
    }

class ChattingPlayer_356(Active):
    name = 'chatting player'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 40,
                'max_speed' : 40,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image112, image71, image76, image97, image76, image71]
            },
        },
    }

class Police2_357(Counter):
    name = 'police 2'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class Terror2_358(Counter):
    name = 'terror 2'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class PoliceLeft_359(Counter):
    name = 'police left'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class TerrorLeft_360(Counter):
    name = 'terror left'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class RoundStart_361(Counter):
    name = 'Round start'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class PoliceWin_362(Active):
    name = 'police win'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image13]
            },
        },
    }

class TerrorWin_363(Active):
    name = 'terror win'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image14]
            },
        },
    }

class Cash_364(Active):
    name = 'cash'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image31]
            },
        },
    }

class _365(Active):
    name = '$'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image48]
            },
        },
    }

class Money_366(Counter):
    name = 'money'
    visible = False
    frames = {
        '0' : image789,
        '1' : image802,
        '2' : image788,
        '3' : image791,
        '4' : image792,
        '5' : image794,
        '6' : image793,
        '7' : image795,
        '8' : image790,
        '9' : image798,
        '-' : image797,
        '+' : image799,
        '.' : image800,
        'e' : image801,
    }
    initial = 0
    minimum = 0
    maximum = 6000

class Score_367(Active):
    name = 'score'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image26]
            },
        },
    }

class ScorePolice_368(Counter):
    name = 'score police'
    visible = False
    frames = {
        '0' : image98,
        '1' : image69,
        '2' : image70,
        '3' : image72,
        '4' : image73,
        '5' : image74,
        '6' : image75,
        '7' : image77,
        '8' : image78,
        '9' : image79,
        '-' : image797,
        '+' : image799,
        '.' : image800,
        'e' : image801,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class ScoreTerror_369(Counter):
    name = 'score terror'
    visible = False
    frames = {
        '0' : image260,
        '1' : image96,
        '2' : image107,
        '3' : image110,
        '4' : image144,
        '5' : image145,
        '6' : image146,
        '7' : image244,
        '8' : image256,
        '9' : image257,
        '-' : image797,
        '+' : image799,
        '.' : image800,
        'e' : image801,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class ShopList_370(Text):
    name = 'Shop list'
    width = 135
    height = 20
    font = font5
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class ShopListPrice_371(Text):
    name = 'Shop list price'
    width = 59
    height = 20
    font = font5
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignRight | Qt.AlignTop

class Shop1Blitter_372(TextBlitter):
    name = 'Shop1 blitter'
    visible = False

class Shop2Blitter_373(TextBlitter):
    name = 'Shop2 blitter'
    visible = False

class C4_374(Active):
    name = 'C4'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 10,
                'max_speed' : 10,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image27, image274, image282, image283]
            },
        },
    }

class Destroy_375(Active):
    name = 'Destroy'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image28]
            },
        },
    }

class WallDestroyed_376(Active):
    name = 'wall destroyed'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image227]
            },
        },
    }

class BoxDestroyed_377(Active):
    name = 'box destroyed'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image515]
            },
        },
    }

class OverlayRedux_378(OverlayRedux):
    name = 'Overlay Redux'

class Flashbang2_379(Active):
    name = 'flashbang 2'
    animations = {
        'Disappearing' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image439, image496, image502, image574, image613, image617, image644, image680, image682]
            },
        },
    }

class Flash_380(Active):
    name = 'flash'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image287]
            },
        },
    }

class FlashTime_381(Counter):
    name = 'flash time'
    initial = 0
    minimum = 0
    maximum = 500

class PlShadow_382(Active):
    name = 'pl shadow'
    animations = {
        'User defined 4' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image481]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image384]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image455]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image482]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image483]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image484]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image486]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image452]
            },
        },
    }

class PlShadow2_383(Active):
    name = 'pl shadow 2'
    animations = {
        'User defined 4' : {
            0 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image481]
            },
            4 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image384]
            },
            8 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image455]
            },
            12 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image482]
            },
            16 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image483]
            },
            20 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image484]
            },
            24 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image486]
            },
            28 : {
                'min_speed' : 1,
                'max_speed' : 1,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image452]
            },
        },
    }

class FlashScreen_384(ActivePicture):
    name = 'flash screen'
    width = 32
    height = 32
    filename = None

class Shop1Blitter2_385(TextBlitter):
    name = 'Shop1 blitter 2'
    visible = False

class Shop1Blitter3_386(TextBlitter):
    name = 'Shop1 blitter 3'
    visible = False

class CheckFlash_387(Counter):
    name = 'Check flash'
    frames = {
        '0' : image462,
        '1' : image473,
        '2' : image474,
        '3' : image475,
        '4' : image321,
        '5' : image322,
        '6' : image323,
        '7' : image324,
        '8' : image325,
        '9' : image326,
        '-' : image327,
        '+' : image328,
        '.' : image329,
        'e' : image330,
    }
    initial = 0
    minimum = -999999999
    maximum = 999999999

class InvincibleTime_388(Counter):
    name = 'Invincible time'
    initial = 0
    minimum = 0
    maximum = 12

class TurningSpeed_389(Counter):
    name = 'Turning speed'
    initial = 1
    minimum = 1
    maximum = 100

class RealName_390(Text):
    name = 'real name'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class ModMusic_391(Counter):
    name = 'ModMusic'
    initial = 0
    minimum = -127
    maximum = 127

class Respawntext_392(Text):
    name = 'respawntext'
    visible = False
    width = 294
    height = 24
    font = font12
    color = (255, 0, 0)
    text = 'Press space to respawn'
    alignment = Qt.AlignHCenter | Qt.AlignTop

class BanList_393(Text):
    name = 'Ban list'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = '0.0.0.0'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Checkip_395(Text):
    name = 'checkip'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Banid_396(Counter):
    name = 'banid'
    initial = 0
    minimum = 0
    maximum = 999999999

class Mapid_397(Text):
    name = 'mapid'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class GrenadeSpot_398(Active):
    name = 'grenade spot'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 4,
                'back_to' : 0,
                'frames' : [image64]
            },
        },
    }

class Shooting_399(Active):
    name = 'Shooting'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image29]
            },
        },
    }

class HP_400(Active):
    name = 'HP'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 5,
                'max_speed' : 5,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image627]
            },
        },
    }

class HealthText_401(Active):
    name = 'health text'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image63]
            },
        },
    }

class Hill_402(Active):
    name = 'hill'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image0]
            },
        },
    }

class Pipeline_403(Active):
    name = 'Pipeline'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image3]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class FenceHor_404(Active):
    name = 'fence hor'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image286]
            },
        },
    }

class FenceVert_405(Active):
    name = 'fence vert'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image298]
            },
        },
    }

class BrokenPipeline_406(Active):
    name = 'broken pipeline'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image213]
            },
        },
    }

class Wall13_407(Active):
    name = 'wall 13'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image315]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class Wall14_408(Active):
    name = 'wall 14'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image379]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class Wall23_409(Active):
    name = 'wall 23'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image258]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class Wall24_410(Active):
    name = 'wall 24'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image313]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image813]
            },
        },
    }

class PipelineDestroyed_411(Active):
    name = 'pipeline destroyed'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image213]
            },
        },
    }

class DM_412(Counter):
    name = 'DM'
    initial = 1
    minimum = 0
    maximum = 3

class Modestatus_413(Counter):
    name = 'modestatus'
    initial = 0
    minimum = 0
    maximum = 3

class Grass2_414(Active):
    name = 'Grass 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image168]
            },
        },
    }

class Desert2_415(Active):
    name = 'desert 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image246]
            },
        },
    }

class Dust2_416(Active):
    name = 'dust 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image564]
            },
        },
    }

class Mapcycle_417(ListControl):
    name = 'mapcycle'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class Up2_418(Active):
    name = 'up 2'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image212]
            },
        },
    }

class Right2_419(Active):
    name = 'right 2'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image215]
            },
        },
    }

class Down2_420(Active):
    name = 'down 2'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image212]
            },
        },
    }

class Left2_421(Active):
    name = 'left 2'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image215]
            },
        },
    }

class DarkGrass_422(Active):
    name = 'dark grass'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image214]
            },
        },
    }

class Water_423(Active):
    name = 'water'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image226]
            },
        },
    }

class VisibleId_424(Counter):
    name = 'Visible-id'
    initial = -1
    minimum = -1
    maximum = 99

class IdAllocation_425(Counter):
    name = 'id-allocation'
    initial = 2
    minimum = 2
    maximum = 100

class Reclist_426(ListControl):
    name = 'reclist'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class Msg_427(Text):
    name = 'msg'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Svrmotd_428(Text):
    name = 'svrmotd'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class NameTag2_429(ActiveBox):
    name = 'Name tag2'
    width = 150
    height = 20
    disabled = True
    fill = None
    font = Font('Arial', 9, True, False, False)
    text = 'User'

class NotID_430(Counter):
    name = 'notID'
    initial = 0
    minimum = 0
    maximum = 99

class Temp_431(Text):
    name = 'temp'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Csm_432(Counter):
    name = 'csm'
    initial = 0
    minimum = 0
    maximum = 9

class NameTag3_433(ActiveBox):
    name = 'Name tag3'
    width = 150
    height = 20
    disabled = True
    fill = None
    font = Font('Arial', 9, True, False, False)
    text = 'User'

class Counter_434(Counter):
    name = 'Counter'
    initial = 0
    minimum = 0
    maximum = 100

class Cp2_435Movement(Path):
    min_speed = 0
    max_speed = 10
    loop = False
    reposition = False
    reverse = False
    steps = [
        {'y': 16384, 'x': 0, 'pause': 0, 'name': None},
    ]

class Cp2_435(Active):
    name = 'cp2'
    movement_class = Cp2_435Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image29]
            },
        },
    }

class Cp2c_436(Counter):
    name = 'cp2c'
    initial = 0
    minimum = -999999999
    maximum = 999999999

class String31_437(Text):
    name = 'String 31'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Snipercounter_438(Counter):
    name = 'snipercounter'
    initial = 0
    minimum = 0
    maximum = 30

class Counter2_439(Counter):
    name = 'Counter 2'
    initial = 0
    minimum = 0
    maximum = 100

class Counter4_440(Counter):
    name = 'Counter 4'
    initial = 0
    minimum = 0
    maximum = 100

class Head_441(Active):
    name = 'Head'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image437]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image700]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image705]
            },
            12 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image748]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image752]
            },
            20 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image752]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image755]
            },
            28 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image437]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image758]
            },
            4 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image759]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image760]
            },
            12 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image764]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image765]
            },
            20 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image765]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image766]
            },
            28 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image758]
            },
        },
    }

class Follower_442(Active):
    name = 'follower'
    visible = False
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image9]
            },
        },
    }

class OverlayRedux2_443(OverlayRedux):
    name = 'Overlay Redux 2'

class Watersplosh_444(Active):
    name = 'watersplosh'
    animations = {
        'Disappearing' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image223, image620, image621, image661, image688, image697, image771]
            },
        },
    }

class Sall_446(Text):
    name = 'sall'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = ''
    alignment = Qt.AlignLeft | Qt.AlignTop

class Moo2_447(Socket):
    name = 'Moo2'

class Timeout1_448(ListControl):
    name = 'timeout1'
    width = 128
    height = 128
    font = Font('MS Sans Serif', 8, False, False, False)
    font_color = (0, 0, 0)
    background = (255, 255, 255)
    index_offset = -1
    lines = [
    ]

class Msg2_449(Text):
    name = 'msg2'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Molotov_450Movement(Ball):
    speed = 0
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 0

class Molotov_450(Active):
    name = 'molotov'
    movement_class = Molotov_450Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image815, image816, image817, image819, image820, image822, image823, image825, image827, image833, image834, image835]
            },
        },
    }

class Active17_451Movement(Ball):
    speed = 2
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 0

class Active17_451(Active):
    name = 'Active 17'
    movement_class = Active17_451Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image509, image772, image774, image779, image780, image784, image785, image796, image804]
            },
        },
    }

class P1_452(Active):
    name = 'P1'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image808, image809, image810, image837, image838, image839, image840, image843, image844]
            },
        },
    }

class Explode_453(Active):
    name = 'Explode'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 40,
                'max_speed' : 40,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image846, image847, image848, image849, image850, image851, image853, image854, image855, image856, image858, image859, image860, image861, image862, image864]
            },
        },
    }

class Temp2_454(Text):
    name = 'temp 2'
    width = 150
    height = 20
    font = font1
    color = (0, 0, 0)
    text = 'Text'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Dir_455(Counter):
    name = 'dir'
    initial = -1
    minimum = -1
    maximum = 32

class FlameDmg_456Movement(Ball):
    speed = 2
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 0

class FlameDmg_456(Active):
    name = 'flame dmg'
    movement_class = FlameDmg_456Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 30,
                'max_speed' : 30,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image245]
            },
        },
    }

class BigflameDmg_457(Active):
    name = 'bigflame dmg'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image911]
            },
        },
    }

class Nade_458Movement(Ball):
    speed = 0
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 0

class Nade_458(Active):
    name = 'nade'
    movement_class = Nade_458Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image155, image778, image812, image818, image832, image852, image863, image865, image866, image867, image868, image870, image871, image874, image875]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image877, image878, image879, image880, image881, image882, image883, image885, image886, image887, image888, image889, image890, image891, image892]
            },
        },
    }

class Nade2_459Movement(Ball):
    speed = 0
    randomizer = 0
    angles = 2
    security = 100
    deceleration = 9

class Nade2_459(Active):
    name = 'nade 2'
    movement_class = Nade2_459Movement
    animations = {
        'User defined 1' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image1003]
            },
        },
        'User defined 2' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image965, image990, image1003, image1038, image1049, image1057, image1068, image1079]
            },
        },
        'User defined 3' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image1023]
            },
        },
        'User defined 4' : {
            0 : {
                'min_speed' : 20,
                'max_speed' : 20,
                'repeat' : 0,
                'back_to' : 0,
                'frames' : [image543, image1012, image1023, image1024, image1025, image1026, image1030, image1027]
            },
        },
    }

class SmokeExp_460Movement(Ball):
    speed = 7
    randomizer = 20
    angles = 2
    security = 60
    deceleration = 9

class SmokeExp_460(Active):
    name = 'smoke exp'
    movement_class = SmokeExp_460Movement
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 30,
                'back_to' : 2,
                'frames' : [image893, image895, image896, image1028, image1029, image1028]
            },
        },
        'Disappearing' : {
            0 : {
                'min_speed' : 15,
                'max_speed' : 15,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image900, image901, image902, image903]
            },
        },
    }

class Edit_461(Edit):
    name = 'Edit'
    width = 200
    height = 70
    font = Font('MS Sans Serif', 8, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class Obj1_462(ActiveBox):
    name = '1'
    width = 52
    height = 16
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Up'

class Up_463(ActiveBox):
    name = 'Up'
    width = 76
    height = 16
    disabled = True
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, False, False, False)

class Obj2_464(ActiveBox):
    name = '2'
    width = 52
    height = 16
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Down'

class Obj3_465(ActiveBox):
    name = '3'
    width = 52
    height = 16
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Left'

class Obj4_466(ActiveBox):
    name = '4'
    width = 52
    height = 16
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Right'

class Down_467(ActiveBox):
    name = 'Down'
    width = 76
    height = 16
    disabled = True
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, False, False, False)

class Left_468(ActiveBox):
    name = 'Left'
    width = 76
    height = 16
    disabled = True
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, False, False, False)

class Right_469(ActiveBox):
    name = 'Right'
    width = 76
    height = 16
    disabled = True
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, False, False, False)

class Obj5_470(ActiveBox):
    name = ' 5'
    width = 52
    height = 16
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Reload'

class Obj6_471(ActiveBox):
    name = ' 6'
    width = 52
    height = 16
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Switch'

class Obj8_472(ActiveBox):
    name = '8'
    width = 52
    height = 16
    disabled = True
    fill = (160, 160, 160)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Shoot'

class Obj9_473(ActiveBox):
    name = '9'
    width = 52
    height = 16
    disabled = True
    fill = (160, 160, 160)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Grenade'

class Reload_474(ActiveBox):
    name = 'Reload'
    width = 76
    height = 16
    disabled = True
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, False, False, False)

class Switch_475(ActiveBox):
    name = 'Switch'
    width = 76
    height = 16
    disabled = True
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, False, False, False)

class Shoot_476(ActiveBox):
    name = 'shoot'
    width = 76
    height = 16
    disabled = True
    fill = (160, 160, 160)
    font = Font('MS Sans Serif', 8, False, False, False)
    text = 'Mouse1'

class Shoot2_477(ActiveBox):
    name = 'shoot 2'
    width = 76
    height = 16
    disabled = True
    fill = (160, 160, 160)
    font = Font('MS Sans Serif', 8, False, False, False)
    text = 'Mouse2'

class Music2_478(Text):
    name = 'Music 2'
    width = 39
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Music:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Rain3_479(Text):
    name = 'Rain 3'
    width = 48
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Graphics:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Rain5_480(Text):
    name = 'Rain 5'
    width = 77
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Turning Speed:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Obj1WeaponList_481(Active):
    name = '1. weapon list'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image2]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image4]
            },
        },
    }

class WaeponString_482(Text):
    name = 'waepon string'
    width = 77
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Start:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Skin_483(Active):
    name = 'skin'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image51]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image61]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image62]
            },
        },
    }

class Rain6_484(Text):
    name = 'Rain 6'
    width = 77
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Skin:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class WaeponString2_485(Text):
    name = 'waepon string 2'
    width = 77
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Music volume:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Active_486(Active):
    name = 'Active'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image220]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image317]
            },
            16 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image292]
            },
            24 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image285]
            },
        },
    }

class Active2_487(Active):
    name = 'Active 2'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image438]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image406]
            },
        },
    }

class Obj7_488(ActiveBox):
    name = '7'
    width = 52
    height = 16
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, True, False, False)
    text = 'Aim H.'

class Head_489(ActiveBox):
    name = 'Head'
    width = 76
    height = 16
    disabled = True
    fill = (240, 240, 240)
    font = Font('MS Sans Serif', 8, False, False, False)

class Rain7_490(Text):
    name = 'Rain 7'
    width = 110
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Points/Kills/Deaths:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Score_491(Text):
    name = 'score'
    width = 166
    height = 14
    font = font5
    color = (255, 255, 255)
    text = ''
    alignment = Qt.AlignRight | Qt.AlignTop

class Options_492(ActivePicture):
    name = 'options'
    width = 300
    height = 350
    filename = 'options.jpg'

class String2_493(Text):
    name = 'String 2'
    width = 150
    height = 20
    font = font5
    color = (255, 255, 255)
    text = 'Controls:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Ok_494(Active):
    name = 'ok'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image567]
            },
        },
        'User defined 1' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image616]
            },
        },
    }

class Ini_495(INI):
    name = 'Ini'
    filename = ''

class Rain4_496(Text):
    name = 'Rain 4'
    width = 48
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Footsteps:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Active3_497(Active):
    name = 'Active 3'
    animations = {
        'Stopped' : {
            0 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image438]
            },
            8 : {
                'min_speed' : 50,
                'max_speed' : 50,
                'repeat' : 1,
                'back_to' : 0,
                'frames' : [image406]
            },
        },
    }

class Connect_498(ActivePicture):
    name = 'connect'
    width = 300
    height = 250
    filename = 'connect.jpg'

class Rain5_499(Text):
    name = 'Rain 5'
    width = 77
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'IP:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class Rain6_500(Text):
    name = 'Rain 6'
    width = 77
    height = 14
    font = font1
    color = (255, 255, 255)
    text = 'Port:'
    alignment = Qt.AlignLeft | Qt.AlignTop

class JoinIp_501(Edit):
    name = 'join ip'
    width = 176
    height = 21
    font = Font('MS Sans Serif', 10, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

class JoinPort_502(Edit):
    name = 'join port'
    width = 67
    height = 21
    font = Font('MS Sans Serif', 10, False, False, False)
    foreground = (0, 0, 0)
    background = (255, 255, 255)
    transparent = False
    border = True

__all__ = ['String2_2', 'Object3', 'Title_4', 'Name_5',
    'GlobalName_6', 'Ini_7', 'CheckVersion_8', 'Ip2_9', 'Port2_10',
    'Connect_11', 'String2_12', 'MooSock_13', 'CheckUser_14',
    'StringParser_15', 'Msg_16', 'String11_17', 'Timeout_18', 'Edit_19',
    'RemoteIP_20', 'EigeneIP_21', 'ValidChar_22', 'ScreenshotNr_23',
    'Edit2_24', 'VerCheck_25', 'Version_26', 'IrcNick_27', 'Newid_28',
    'SvrKills_29', 'SvrDeaths_30', 'SvrPoints_31', 'SvrKills2_32',
    'SvrDeaths2_33', 'SvrPoints2_34', 'Channel1_36', 'String12_37',
    'BinaryObject_38', 'Zeilenumbruch_39', 'Lobby_40', 'Timeout_41',
    'String_42', 'StringParser_43', 'ServerIPs_44', 'StatusServer_45',
    'Ip_46', 'Port_47', 'SndKlein_48', 'Connect2_49', 'GetServerList_50',
    'HostAGame_51', 'ExitGame_52', 'Control_54', 'Ini_55', 'Counter4_56',
    'MooSock2_57', 'MessageOfDay_58', 'WeaponAllowed_59',
    'ServerError_60', 'ServerInfo_61', 'Edit2_62', 'Buffer_63',
    'SndKlein2_64', 'ClanTag_65', 'Counter5_66', 'StringParser2_67',
    'Edit3_68', 'Log_69', 'TextInputBox_70', 'InputBoxModifier_71',
    'MooSock_72', 'StingParserMotd_73', 'StringParse_74',
    'StringParser3_75', 'InputBoxHandler_76', 'List_77', 'UserList_78',
    'String2_79', 'String3_80', 'Nickname0_81', 'Server2_82', 'Flags_83',
    'Counter_84', 'ChatLog_87', 'IconListObject_88', 'Options_89',
    'JoinChat_90', 'SubApplication_91', 'Ctoip_92', 'SubApplication2_93',
    'Host_95', 'Serverinfo_96', 'Serverinfo2_97', 'Serverinfo3_98',
    'Map_99', 'ServerName_100', 'JoinMap_101', 'MaxPlayer_102',
    'String2_103', 'ServerName2_104', 'String4_105', 'String5_106',
    'MaxPl_107', 'String6_108', 'Button_109', 'String7_110',
    'String8_111', 'FF_112', 'StartMap_113', 'String9_114',
    'ScoreLimit_115', 'String10_116', 'TimeLimit_117', 'String11_118',
    'MapcycYesno_119', 'String12_120', 'Port3_121', 'Active2_122',
    'Active3_123', 'MapList_124', 'ChosedMap_125',
    'ChosedMapWithoutPath_126', 'Error_127', 'LoadMap_128',
    'UserKills_130', 'UserDeaths_131', 'GlobalPW_132', 'String13_133',
    'Motd_134', 'String14_135', 'DesertEagle_136', 'String15_137',
    'String16_138', 'M1_139', 'String17_140', 'String18_141', 'Mp5_142',
    'Ak47_143', 'String19_144', 'M5_145', 'String20_146', 'String21_147',
    'G3_148', 'Sniper_149', 'HostIP_150', 'Edit2_151', 'String23_152',
    'Pw_153', 'Enterpw_154', 'SvrPw_155', 'String24_156', 'Xm8_157',
    'String25_158', 'Uzi_159', 'String26_160', 'Sr60_161', 'String27_162',
    'Mapd_163', 'String28_164', 'GlobalValues_165', 'Obj2ndPort_166',
    'String29_167', 'Hideserver_168', 'Connecting_169', 'Status_170',
    'CheckMap_171', 'Info_173', 'VersionCheck_174', 'CurrentPlayer_175',
    'CheckDaMap_176', 'Edit_177', 'Enterpw_179', 'Rightpw_180', 'Moo_181',
    'XtraXtraCRC_182', 'Mapid_183', 'Mapid2_184', 'Sting_186',
    'Mapload_187', 'MapTileCounter_188', 'MapTileMax_189', 'Status2_190',
    'SpawnArea_192', 'Fusssoldat_193', 'Fusssoldat2_194', 'Active7_195',
    'Active8_196', 'Rauch_197', 'HitBack_198', 'Obj2Die_199',
    'String2_200', 'Respawn_201', 'Splitter_202', 'Killed_203',
    'Chat_204', 'Message1_205', 'Message2_206', 'Message3_207',
    'AmmoPack_208', 'Frags_209', 'Deaths_210', 'SkillCounter_211',
    'MagicExplode3_212', 'Active5_213', 'Active6_214', 'Gaswolke_215',
    'CheckKick_216', 'ChangeMap_217', 'ActiveObject1_218', 'Strafing_219',
    'Strafing2_220', 'ExitCounter_221', 'Active9_222', 'Mouse_224',
    'Left_225', 'Right_226', 'Up_227', 'Down_228', 'Mouse2_229',
    'ShotLatence_230', 'ScoreBoard_231', 'PingCounter_232', 'Ping_233',
    'ScoreBar_234', 'NameScore_235', 'FragsScore_236', 'IdScore_237',
    'Accuracy_238', 'Oben_239', 'Unten_240', 'Rechts_241', 'Links_242',
    'Message4_243', 'ErrorMsg_244', 'DurchlaufChat_245', 'Counter3_246',
    'Exp_247', 'Frantic_248', 'Daunting_249', 'Godlike_250',
    'FastMouse_252', 'Blood3_253', 'Active2_254', 'Obj1Die_255',
    'Grass_256', 'Desert_257', 'Dust_258', 'LoadMap_259', 'Tree_260',
    'BackgroundX_261', 'BackgroundY_262', 'Rock_264', 'DeadTree_265',
    'GroundBackground_266', 'Stone_267', 'TrackX_268', 'TrackY_269',
    'Track_270', 'House_271', 'Sidewalk_272', 'BrokenSidewalk_273',
    'Street_274', 'PoliceCar_275', 'PoliceCar2_276', 'Stone2_277',
    'Tree3_278', 'Street2_279', 'Sidewalk2_280', 'Crossroad_281',
    'Rock3_282', 'Rock3_283', 'Rock4_284', 'Skeleton_285', 'Bush_286',
    'Box_287', 'DestroyedBox_288', 'Gate_289', 'Bush2_290',
    'Boulders_291', 'Cactus_292', 'SmallCactus_293', 'Stone3_294',
    'Tombstone_295', 'Floor_296', 'Floor2_297', 'WoodenFloor_298',
    'StoneFloor_299', 'Wall11_300', 'Wall12_301', 'Wall21_302',
    'Wall22_303', 'Tree3_304', 'Pond_305', 'TestShoot_306', 'IdPing_307',
    'Obj1Weapon_308', 'Obj2Weapon_309', 'AmmoText_310', 'AmmoCurrent_311',
    'AmmoFull_312', '_313', 'Obj1WeaponList_314', 'Obj2WeaponList_315',
    'PlOnlineText_316', 'Players_317', 'SecondWeapon_318', 'AmmoTest_319',
    'WeaponList_320', 'Ammo1_321', 'Ammo2_322', 'Reload2_323',
    'Sleep_324', 'DetectMouseChange_325', 'SaveMouseChange_326',
    'Rubble_327', 'Skeleton2_328', 'Entrance_329', 'Lantern_330',
    'BurningBox_331', 'MsgCounter_332', 'FlameDie_333', 'Player_334',
    'MooSock_335', 'Edit2_336', 'Obj3Die_338', 'Obj4Die_339',
    'Obj5Die_340', 'Obj6Die_341', 'Police_342', 'Terror_343', 'Mode_344',
    'PoliceSpawn_345', 'TerrorSpawn_346', 'NameScore2_347',
    'FragsScore2_348', 'IdScore2_349', 'IdPing2_350', 'NameScore3_351',
    'FragsScore3_352', 'IdScore3_353', 'IdPing3_354', 'Chatting_355',
    'ChattingPlayer_356', 'Police2_357', 'Terror2_358', 'PoliceLeft_359',
    'TerrorLeft_360', 'RoundStart_361', 'PoliceWin_362', 'TerrorWin_363',
    'Cash_364', '_365', 'Money_366', 'Score_367', 'ScorePolice_368',
    'ScoreTerror_369', 'ShopList_370', 'ShopListPrice_371',
    'Shop1Blitter_372', 'Shop2Blitter_373', 'C4_374', 'Destroy_375',
    'WallDestroyed_376', 'BoxDestroyed_377', 'OverlayRedux_378',
    'Flashbang2_379', 'Flash_380', 'FlashTime_381', 'PlShadow_382',
    'PlShadow2_383', 'FlashScreen_384', 'Shop1Blitter2_385',
    'Shop1Blitter3_386', 'CheckFlash_387', 'InvincibleTime_388',
    'TurningSpeed_389', 'RealName_390', 'ModMusic_391', 'Respawntext_392',
    'BanList_393', 'Checkip_395', 'Banid_396', 'Mapid_397',
    'GrenadeSpot_398', 'Shooting_399', 'HP_400', 'HealthText_401',
    'Hill_402', 'Pipeline_403', 'FenceHor_404', 'FenceVert_405',
    'BrokenPipeline_406', 'Wall13_407', 'Wall14_408', 'Wall23_409',
    'Wall24_410', 'PipelineDestroyed_411', 'DM_412', 'Modestatus_413',
    'Grass2_414', 'Desert2_415', 'Dust2_416', 'Mapcycle_417', 'Up2_418',
    'Right2_419', 'Down2_420', 'Left2_421', 'DarkGrass_422', 'Water_423',
    'VisibleId_424', 'IdAllocation_425', 'Reclist_426', 'Msg_427',
    'Svrmotd_428', 'NameTag2_429', 'NotID_430', 'Temp_431', 'Csm_432',
    'NameTag3_433', 'Counter_434', 'Cp2_435', 'Cp2c_436', 'String31_437',
    'Snipercounter_438', 'Counter2_439', 'Counter4_440', 'Head_441',
    'Follower_442', 'OverlayRedux2_443', 'Watersplosh_444', 'Sall_446',
    'Moo2_447', 'Timeout1_448', 'Msg2_449', 'Molotov_450', 'Active17_451',
    'P1_452', 'Explode_453', 'Temp2_454', 'Dir_455', 'FlameDmg_456',
    'BigflameDmg_457', 'Nade_458', 'Nade2_459', 'SmokeExp_460',
    'Edit_461', 'Obj1_462', 'Up_463', 'Obj2_464', 'Obj3_465', 'Obj4_466',
    'Down_467', 'Left_468', 'Right_469', 'Obj5_470', 'Obj6_471',
    'Obj8_472', 'Obj9_473', 'Reload_474', 'Switch_475', 'Shoot_476',
    'Shoot2_477', 'Music2_478', 'Rain3_479', 'Rain5_480',
    'Obj1WeaponList_481', 'WaeponString_482', 'Skin_483', 'Rain6_484',
    'WaeponString2_485', 'Active_486', 'Active2_487', 'Obj7_488',
    'Head_489', 'Rain7_490', 'Score_491', 'Options_492', 'String2_493',
    'Ok_494', 'Ini_495', 'Rain4_496', 'Active3_497', 'Connect_498',
    'Rain5_499', 'Rain6_500', 'JoinIp_501', 'JoinPort_502']
