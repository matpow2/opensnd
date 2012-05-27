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
from objects import *
from images import *
from fonts import *
from sounds import *
from PySide.QtCore import Qt
import os

class Frame4(Frame):
    name = 'Host a game'
    index = 3
    width = 800
    height = 600
    background = (255, 255, 255)
    
    def initialize(self):
        self.create_object(Zeilenumbruch_39, 88, -55)
        self.create_object(Serverinfo_96, 176, -70)
        self.create_object(Serverinfo2_97, 178, -57)
        self.create_object(Serverinfo3_98, 180, -41)
        self.create_object(ChosedMapWithoutPath_126, -176, 357)
        self.create_object(ChosedMap_125, -188, 332)
        self.create_object(MessageOfDay_58, -4, -92)
        self.create_object(WeaponAllowed_59, 42, -114)
        self.create_object(ClanTag_65, 333, -106)
        self.create_object(SvrPw_155, 46, 632)
        self.create_object(GlobalName_6, 7, -64)
        self.create_object(Host_95, 0, 0)
        self.create_object(String_42, 624, 121)
        self.create_object(Map_99, 412, -22)
        self.create_object(ServerName_100, -4, -40)
        self.create_object(JoinMap_101, 312, -21)
        self.create_object(MaxPlayer_102, 528, -27)
        self.create_object(String2_103, 31, 67)
        self.create_object(String4_105, 370, 67)
        self.create_object(String5_106, 31, 127)
        self.create_object(String7_110, -263, 512)
        self.create_object(String8_111, -263, 549)
        self.create_object(StartMap_113, 334, 656)
        self.create_object(Version_26, 391, -78)
        self.create_object(Ip_46, 76, -66)
        self.create_object(Port_47, 74, -40)
        self.create_object(String9_114, -283, 402)
        self.create_object(String6_108, -134, 402)
        self.create_object(String10_116, -283, 439)
        self.create_object(String6_108, -134, 439)
        self.create_object(String11_118, -263, 475)
        self.create_object(EigeneIP_21, 832, 272)
        self.create_object(String12_120, 31, 97)
        self.create_object(ExitGame_52, 694, 225)
        self.create_object(Active2_122, 694, 175)
        self.create_object(Active3_123, 694, 200)
        self.create_object(Error_127, 619, 239)
        self.create_object(UserKills_130, 583, -68)
        self.create_object(UserDeaths_131, 617, -68)
        self.create_object(MooSock_72, 609, -52)
        self.create_object(GlobalPW_132, 175, -93)
        self.create_object(String13_133, 31, 157)
        self.create_object(String14_135, 31, 187)
        self.create_object(String15_137, 31, 217)
        self.create_object(String16_138, 31, 247)
        self.create_object(String17_140, 31, 277)
        self.create_object(String18_141, 31, 307)
        self.create_object(String19_144, 217, 217)
        self.create_object(String20_146, 217, 247)
        self.create_object(String21_147, 217, 277)
        self.create_object(RemoteIP_20, 833, 297)
        self.create_object(HostIP_150, 831, 482)
        self.create_object(SndKlein2_64, 636, 64)
        self.create_object(SndKlein_48, 633, 62)
        self.create_object(String23_152, 31, 370)
        self.create_object(ScreenshotNr_23, 265, 640)
        self.create_object(String24_156, 31, 337)
        self.create_object(String25_158, 217, 307)
        self.create_object(String26_160, 217, 337)
        self.create_object(String27_162, 31, 400)
        self.create_object(String28_164, 31, 430)
        self.create_object(GlobalValues_165, -64, 180)
        self.create_object(Obj2ndPort_166, 182, 98)
        self.create_object(String29_167, 31, 460)
        self.create_object(ServerName2_104, 137, 66)
        self.create_object(MaxPl_107, 137, 126)
        self.create_object(Button_109, -117, 516)
        self.create_object(FF_112, -117, 553)
        self.create_object(ScoreLimit_115, -177, 401)
        self.create_object(TimeLimit_117, -177, 438)
        self.create_object(MapcycYesno_119, 153, 433)
        self.create_object(Port3_121, 137, 96)
        self.create_object(MapList_124, 413, 65)
        self.create_object(LoadMap_128, 839, 335)
        self.create_object(Motd_134, 137, 156)
        self.create_object(DesertEagle_136, 153, 220)
        self.create_object(M1_139, 153, 250)
        self.create_object(Mp5_142, 153, 280)
        self.create_object(Ak47_143, 153, 310)
        self.create_object(M5_145, 339, 220)
        self.create_object(G3_148, 339, 250)
        self.create_object(Sniper_149, 339, 280)
        self.create_object(Edit2_151, 418, 625)
        self.create_object(Pw_153, 153, 373)
        self.create_object(Enterpw_154, 189, 369)
        self.create_object(Xm8_157, 153, 340)
        self.create_object(Uzi_159, 339, 310)
        self.create_object(Sr60_161, 339, 340)
        self.create_object(Mapd_163, 153, 403)
        self.create_object(Hideserver_168, 153, 463)
        self.groups = {
            'Reactivate Forms' : False,
            'Check Name' : False,
            'Check motd' : False,
            'Check Server' : False,
            'Check pw' : False,
        }
    
    def on_start(self):
        self.set_event_id(1)
        self.values[0] = 0
        self.get(ServerName2_104).limit_size(20)
        self.get(ServerName2_104).set_value('Server'+str(randrange(9999)))
        self.get(MaxPl_107).set_value('8')
        self.get(Map_99).set_value(1)
        self.get(JoinMap_101).set_value(1)
        self.get(MaxPlayer_102).set_value(8)
        self.values[1] = 0
        self.values[2] = 0
        self.get(MaxPl_107).limit_size(2)
        self.values[15] = 0
        self.values[5] = 0
        self.get(ScoreLimit_115).set_value('0')
        self.get(ScoreLimit_115).limit_size(4)
        self.get(TimeLimit_117).set_value('0')
        self.get(TimeLimit_117).limit_size(3)
        self.values[8] = 0
        self.get(Port3_121).set_value('1203')
        self.get(Port3_121).limit_size(5)
        self.get(MapList_124).load_file_list(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\*.sdo')
        self.get(ChosedMap_125).set_value('No Map')
        self.get(Active2_122).values[0] = 0
        self.get(Motd_134).set_value('Welcome!')
        self.get(Motd_134).limit_size(70)
        self.get(DesertEagle_136).set_value(True)
        self.get(M1_139).set_value(True)
        self.get(Mp5_142).set_value(True)
        self.get(Ak47_143).set_value(True)
        self.get(M5_145).set_value(True)
        self.get(G3_148).set_value(True)
        self.get(Sniper_149).set_value(True)
        self.get(SvrPw_155).set_value(' ')
        self.get(Enterpw_154).set_value('Secret')
        self.get(Enterpw_154).limit_size(10)
        self.get(Enterpw_154).disable()
        self.values[5] = 1
        self.get(Xm8_157).set_value(True)
        self.get(Uzi_159).set_value(True)
        self.get(Sr60_161).set_value(True)
        self.get(GlobalValues_165).values[0] = 0
        self.get(Mapd_163).set_value(True)
        self.get(GlobalValues_165).values[3] = 1
        self.get(GlobalValues_165).values[4] = 0
        pass
    
    def loop_text2(self):
        self.set_event_id(48)
        if (self.groups['Check pw'] and
        mid_string(self.get(Enterpw_154).get_value(), self.get_loop_index('text2'), 1) == ','):
            return False # 'text2'
            self.get(Error_127).set_value(', is an invalid character')
            self.groups['Reactivate Forms'] = True
            self.groups['Check pw'] = False
        self.set_event_id(49)
        if (self.groups['Check pw'] and
        mid_string(self.get(Enterpw_154).get_value(), self.get_loop_index('text2'), 1) == ' '):
            return False # 'text2'
            self.get(Error_127).set_value('Space is an invalid character')
            self.groups['Reactivate Forms'] = True
            self.groups['Check pw'] = False
        self.set_event_id(50)
        if (self.groups['Check pw'] and
        self.get_loop_index('text2')+1 == len(self.get(Enterpw_154).get_value())):
            self.get(SvrPw_155).set_value(self.get(Enterpw_154).get_value())
            self.groups['Check Server'] = True
            self.groups['Check pw'] = False
        pass
    
    def loop_text(self):
        self.set_event_id(42)
        if (self.groups['Check motd'] and
        mid_string(self.get(Motd_134).get_value(), self.get_loop_index('text'), 1) == ','):
            return False # 'text'
            self.get(Error_127).set_value(', is an invalid character')
            self.groups['Reactivate Forms'] = True
            self.groups['Check motd'] = False
        self.set_event_id(43)
        if (self.groups['Check motd'] and
        self.get_loop_index('text')+1 == len(self.get(Motd_134).get_value()) and
        select(negate(self.get(Pw_153).get_value()))):
            self.groups['Check Server'] = True
            self.groups['Check motd'] = False
        self.set_event_id(44)
        if (self.groups['Check motd'] and
        self.get_loop_index('text')+1 == len(self.get(Motd_134).get_value()) and
        select(self.get(Pw_153).get_value())):
            self.groups['Check pw'] = True
            self.groups['Check motd'] = False
        pass
    
    def loop_name(self):
        self.set_event_id(36)
        if (self.groups['Check Name'] and
        mid_string(self.get(ServerName2_104).get_value(), self.get_loop_index('name'), 1) == ','):
            return False # 'name'
            self.get(Error_127).set_value(', is an invalid character')
            self.groups['Reactivate Forms'] = True
            self.groups['Check Name'] = False
        self.set_event_id(37)
        if (self.groups['Check Name'] and
        mid_string(self.get(ServerName2_104).get_value(), self.get_loop_index('name'), 1) == ' '):
            return False # 'name'
            self.get(Error_127).set_value('Space is an invalid character')
            self.groups['Reactivate Forms'] = True
            self.groups['Check Name'] = False
        self.set_event_id(38)
        if (self.groups['Check Name'] and
        self.get_loop_index('name')+1 == len(self.get(ServerName2_104).get_value())):
            self.groups['Check motd'] = True
            self.groups['Check Name'] = False
        pass
    
    def on_mouse_press(self, x, y, button):
        if self.get(Active2_122).is_over(x, y):
            self.set_event_id(14)
            if (negate(self.groups['Check Name']) and
            negate(self.groups['Check Server']) and
            negate(self.groups['Reactivate Forms']) and
            select(self.get(Active2_122).values.get(0, 0) == 0)):
                self.get(ServerName2_104).disable()
                self.get(MaxPl_107).disable()
                self.get(Port3_121).disable()
                self.get(MapList_124).set_focus(False)
                self.get(Motd_134).disable()
                self.get(DesertEagle_136).disable()
                self.get(M1_139).disable()
                self.get(Mp5_142).disable()
                self.get(Ak47_143).disable()
                self.get(M5_145).disable()
                self.get(G3_148).disable()
                self.get(Sniper_149).disable()
                self.get(Pw_153).disable()
                self.get(Xm8_157).disable()
                self.get(Uzi_159).disable()
                self.get(Sr60_161).disable()
                self.get(Enterpw_154).disable()
                self.groups['Check Name'] = True
        if self.get(Active3_123).is_over(x, y):
            self.set_event_id(3)
            if select(self.get(Active2_122).values.get(0, 0) == 0):
                self.set_frame(2)
        if self.get(ExitGame_52).is_over(x, y):
            self.set_event_id(4)
            if select(self.get(Active2_122).values.get(0, 0) == 0):
                self.get(Active2_122).values[0] = 1
                self.get(Active2_122).set_transparency(70)
                self.get(Active3_123).set_transparency(70)
                self.get(ExitGame_52).set_transparency(70)
                self.get(ExitGame_52).restore_animation()
                self.set_frame(6)
        pass
    
    def on_button_click(self, instance):
        if type(instance) == Pw_153:
            self.set_event_id(15)
            if select(negate(self.get(Pw_153).get_value())):
                self.get(Enterpw_154).disable()
        if type(instance) == Pw_153:
            self.set_event_id(16)
            if select(self.get(Pw_153).get_value()):
                self.get(Enterpw_154).enable()
        if type(instance) == Button_109:
            self.set_event_id(17)
            if select(negate(self.get(Button_109).get_value())):
                self.values[2] = 0
        if type(instance) == Button_109:
            self.set_event_id(18)
            if select(self.get(Button_109).get_value()):
                self.values[2] = 1
        if type(instance) == Mapd_163:
            self.set_event_id(19)
            if select(negate(self.get(Mapd_163).get_value())):
                self.get(GlobalValues_165).values[3] = 0
        if type(instance) == Mapd_163:
            self.set_event_id(20)
            if select(self.get(Mapd_163).get_value()):
                self.get(GlobalValues_165).values[3] = 1
        if type(instance) == Hideserver_168:
            self.set_event_id(21)
            if select(negate(self.get(Hideserver_168).get_value())):
                self.get(GlobalValues_165).values[4] = 0
        if type(instance) == Hideserver_168:
            self.set_event_id(22)
            if select(self.get(Hideserver_168).get_value()):
                self.get(GlobalValues_165).values[4] = 1
        pass
    
    def on_list_selection(self, instance):
        if type(instance) == MapList_124:
            self.set_event_id(2)
            self.get(ChosedMap_125).set_value(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(MapList_124).get_line(None))
            self.get(ChosedMapWithoutPath_126).set_value(left_string(self.get(MapList_124).get_line(None), len(self.get(MapList_124).get_line(None))-4))
        pass
    
    def update(self, dt):
        self.set_event_id(5)
        if select(self.get(MaxPl_107).is_number()):
            self.get(MaxPlayer_102).set_value(self.get(MaxPl_107).get_number())
        self.set_event_id(6)
        if select(negate(self.get(MaxPl_107).is_number())):
            self.get(MaxPl_107).set_value('8')
        self.set_event_id(7)
        if (select(self.get(MaxPl_107).is_modified()) and
        select(negate(self.get(MaxPl_107).is_number()))):
            self.get(MaxPl_107).set_value('8')
        self.set_event_id(8)
        if select(negate(self.get(ScoreLimit_115).is_number())):
            self.get(ScoreLimit_115).set_value('0')
        self.set_event_id(9)
        if (select(self.get(ScoreLimit_115).is_modified()) and
        select(negate(self.get(ScoreLimit_115).is_number()))):
            self.get(ScoreLimit_115).set_value('0')
        self.set_event_id(10)
        if select(negate(self.get(TimeLimit_117).is_number())):
            self.get(TimeLimit_117).set_value('0')
        self.set_event_id(11)
        if (select(self.get(TimeLimit_117).is_modified()) and
        select(negate(self.get(TimeLimit_117).is_number()))):
            self.get(TimeLimit_117).set_value('0')
        self.set_event_id(12)
        if select(negate(self.get(Port3_121).is_number())):
            self.get(Port3_121).set_value('1203')
        self.set_event_id(13)
        if (select(self.get(Port3_121).is_modified()) and
        select(negate(self.get(Port3_121).is_number()))):
            self.get(Port3_121).set_value('1203')
        self.set_event_id(23)
        if self.get(Active2_122).mouse_over():
            self.get(Active2_122).force_animation('User defined 1')
        self.set_event_id(24)
        if negate(self.get(Active2_122).mouse_over()):
            self.get(Active2_122).restore_animation()
        self.set_event_id(25)
        if self.get(Active3_123).mouse_over():
            self.get(Active3_123).force_animation('User defined 1')
        self.set_event_id(26)
        if negate(self.get(Active3_123).mouse_over()):
            self.get(Active3_123).restore_animation()
        self.set_event_id(27)
        if self.get(ExitGame_52).mouse_over():
            self.get(ExitGame_52).force_animation('User defined 1')
        self.set_event_id(28)
        if negate(self.get(ExitGame_52).mouse_over()):
            self.get(ExitGame_52).restore_animation()
        self.set_event_id(29)
        if select(self.get(Port3_121).is_modified()):
            self.get(Obj2ndPort_166).set_value('and '+str(self.get(Port3_121).get_number()+1))
        if self.groups['Check Name']:
            self.set_event_id(31)
            if self.get(ServerName2_104).get_value() == '':
                self.get(Error_127).set_value('Invalid server name')
                self.groups['Reactivate Forms'] = True
                self.groups['Check Name'] = False
            self.set_event_id(32)
            if len(self.get(ServerName2_104).get_value()) <= 5:
                self.get(Error_127).set_value('Invalid server name')
                self.groups['Reactivate Forms'] = True
                self.groups['Check Name'] = False
            self.set_event_id(33)
            if self.get(Motd_134).get_value() == '':
                self.get(Motd_134).set_value(' ')
            self.set_event_id(34)
            if (self.get(Enterpw_154).get_value() == '' and
            select(self.get(Pw_153).get_value())):
                self.get(Error_127).set_value('Password error')
                self.groups['Reactivate Forms'] = True
                self.groups['Check Name'] = False
            self.set_event_id(35)
            if True:
                for loop_index in xrange(len(self.get(ServerName2_104).get_value())):
                    self.loop_indexes['name'] = loop_index
                    if self.loop_name() == False: break
        if self.groups['Check motd']:
            self.set_event_id(41)
            if True:
                for loop_index in xrange(len(self.get(Motd_134).get_value())):
                    self.loop_indexes['text'] = loop_index
                    if self.loop_text() == False: break
        if self.groups['Check pw']:
            self.set_event_id(47)
            if True:
                for loop_index in xrange(len(self.get(Enterpw_154).get_value())):
                    self.loop_indexes['text2'] = loop_index
                    if self.loop_text2() == False: break
        if self.groups['Check Server']:
            self.set_event_id(53)
            if self.get(Port3_121).get_value() == '':
                self.get(Error_127).set_value("Can't host on that port")
                self.groups['Reactivate Forms'] = True
                self.groups['Check Server'] = False
            self.set_event_id(54)
            if select(negate(self.get(MaxPl_107).is_number())):
                self.get(Error_127).set_value("Can't host on that port")
                self.groups['Reactivate Forms'] = True
                self.groups['Check Server'] = False
            self.set_event_id(55)
            if to_number(self.get(Port3_121).get_value()) == 0:
                self.get(Error_127).set_value("Can't host on that port")
                self.groups['Reactivate Forms'] = True
                self.groups['Check Server'] = False
            self.set_event_id(56)
            if self.get(MaxPl_107).get_value() == '':
                self.get(Error_127).set_value('Max players error')
                self.groups['Reactivate Forms'] = True
                self.groups['Check Server'] = False
            self.set_event_id(57)
            if select(negate(self.get(MaxPl_107).is_number())):
                self.get(Error_127).set_value('Max players error')
                self.groups['Reactivate Forms'] = True
                self.groups['Check Server'] = False
            self.set_event_id(58)
            if to_number(self.get(MaxPl_107).get_value()) == 0:
                self.get(Error_127).set_value('Max players error')
                self.groups['Reactivate Forms'] = True
                self.groups['Check Server'] = False
            self.set_event_id(59)
            if (self.get(MapList_124).get_index() == 0 and
            select(negate(self.get(MapcycYesno_119).get_value()))):
                self.groups['Reactivate Forms'] = True
                self.groups['Check Server'] = False
                self.get(Error_127).set_value('Choose a map')
            self.set_event_id(60)
            if (self.check_once() and
            select(self.get(MapcycYesno_119).get_value())):
                self.get(GlobalValues_165).values[0] = 1
            self.set_event_id(61)
            if self.check_once():
                self.get(HostIP_150).set_value(self.get(RemoteIP_20).text)
            self.set_event_id(62)
            if self.check_once():
                self.values[1] = 1
                self.get(ServerName_100).set_value(self.get(ServerName2_104).get_value())
                self.get(Ip_46).set_value(self.get(EigeneIP_21).text)
                self.get(Port_47).set_value(self.get(Port3_121).get_value())
                self.get(MaxPlayer_102).set_value(self.get(MaxPl_107).get_number())
            self.set_event_id(63)
            if self.check_once():
                decrypt_file(self.get(ChosedMap_125).text, 8)
            self.set_event_id(64)
            if self.check_once():
                self.get(LoadMap_128).load(self.get(ChosedMap_125).text)
            self.set_event_id(65)
            if self.check_once():
                encrypt_file(self.get(ChosedMap_125).text, 8)
            self.set_event_id(66)
            if self.check_once():
                self.get(MessageOfDay_58).set_value(self.get(Motd_134).get_value())
            self.set_event_id(67)
            if select(self.get(DesertEagle_136).get_value()):
                self.get(WeaponAllowed_59).set_value('1')
            self.set_event_id(68)
            if select(negate(self.get(DesertEagle_136).get_value())):
                self.get(WeaponAllowed_59).set_value('0')
            self.set_event_id(69)
            if select(self.get(M1_139).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(70)
            if select(negate(self.get(M1_139).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(71)
            if select(self.get(Mp5_142).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(72)
            if select(negate(self.get(Mp5_142).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(73)
            if select(self.get(Ak47_143).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(74)
            if select(negate(self.get(Ak47_143).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(75)
            if select(self.get(M5_145).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(76)
            if select(negate(self.get(M5_145).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(77)
            if select(self.get(G3_148).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(78)
            if select(negate(self.get(G3_148).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(79)
            if select(self.get(Sniper_149).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(80)
            if select(negate(self.get(Sniper_149).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(81)
            if select(self.get(Uzi_159).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(82)
            if select(negate(self.get(Uzi_159).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(83)
            if select(self.get(Xm8_157).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
            self.set_event_id(84)
            if select(negate(self.get(Xm8_157).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
            self.set_event_id(85)
            if select(self.get(Sr60_161).get_value()):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',1')
                self.hide_cursor()
            self.set_event_id(86)
            if select(negate(self.get(Sr60_161).get_value())):
                self.get(WeaponAllowed_59).set_value(self.get(WeaponAllowed_59).text+',0')
                self.hide_cursor()
            self.set_event_id(87)
            if self.check_once():
                self.stop_mod(0)
                self.set_frame(5)
        if self.groups['Reactivate Forms']:
            self.set_event_id(90)
            if (True and
            select(negate(self.get(Pw_153).get_value()))):
                self.get(ServerName2_104).enable()
                self.get(MaxPl_107).enable()
                self.get(MapList_124).set_focus(True)
                self.get(Port3_121).enable()
                self.groups['Reactivate Forms'] = False
                self.get(Motd_134).enable()
                self.get(DesertEagle_136).enable()
                self.get(M1_139).enable()
                self.get(Mp5_142).enable()
                self.get(Ak47_143).enable()
                self.get(M5_145).enable()
                self.get(G3_148).enable()
                self.get(Sniper_149).enable()
                self.get(Pw_153).enable()
                self.get(Xm8_157).enable()
                self.get(Uzi_159).enable()
                self.get(Sr60_161).enable()
            self.set_event_id(91)
            if (True and
            select(self.get(Pw_153).get_value())):
                self.get(ServerName2_104).enable()
                self.get(MaxPl_107).enable()
                self.get(MapList_124).set_focus(True)
                self.get(Port3_121).enable()
                self.groups['Reactivate Forms'] = False
                self.get(Motd_134).enable()
                self.get(DesertEagle_136).enable()
                self.get(M1_139).enable()
                self.get(Mp5_142).enable()
                self.get(Ak47_143).enable()
                self.get(M5_145).enable()
                self.get(G3_148).enable()
                self.get(Sniper_149).enable()
                self.get(Pw_153).enable()
                self.get(Enterpw_154).enable()
                self.get(Xm8_157).enable()
                self.get(Uzi_159).enable()
                self.get(Sr60_161).enable()
        pass
    
