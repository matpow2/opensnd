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
from config import FAST_CONNECT
from PySide.QtCore import Qt
import os

class Frame5(Frame):
    name = 'Connecting'
    index = 4
    width = 800
    height = 600
    background = (255, 255, 255)
    
    def initialize(self):
        if FAST_CONNECT:
            values = {0: 0, 1: 0, 2: 0, 3: 0, 4: 2, 5: 0, 6: 0, 8: 0, 9: 0, 10: 0,
                12: 1, 13: 44, 14: 0, 15: 0}
            strings = {0: u'127.0.0.1', 1: u'1203'}
            for k, v in values.iteritems():
                self.values[k] = v
            for k, v in strings.iteritems():
                self.strings[k] = v
            Ip_46.get_storage()['text'] = u'127.0.0.1'
            Port_47.get_storage()['text'] = u'1203'
            GlobalName_6.get_storage()['text'] = u'matpow2'
            Version_26.get_storage()['text'] = '1.44'
            add_encryption_key('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9')
            self.load_mod('title.mod', 0, 0)
            self.load_mod('game1.mod', 1, 1)
            self.load_mod('game2.mod', 2, 2)
            self.load_mod('game3.mod', 3, 3)
            self.load_mod('game4.mod', 4, 4)
        self.create_object(Zeilenumbruch_39, -10, -32)
        self.create_object(ChosedMapWithoutPath_126, 126, -86)
        self.create_object(Info_173, 286, -105)
        self.create_object(WeaponAllowed_59, 636, -43)
        self.create_object(MessageOfDay_58, 643, -69)
        self.create_object(VersionCheck_174, 605, -32)
        self.create_object(ServerError_60, 193, -131)
        self.create_object(CheckDaMap_176, 620, -65)
        self.create_object(ClanTag_65, 269, -134)
        self.create_object(Rightpw_180, 507, 669)
        self.create_object(Mapid_183, 195, -31)
        self.create_object(Mapid2_184, 194, -19)
        self.create_object(Sting_186, -175, 211)
        self.create_object(Connecting_169, 0, 0)
        self.create_object(Status2_190, 194, 275)
        self.create_object(Status_170, 193, 274)
        self.create_object(Ip_46, 23, -67)
        self.create_object(Port_47, 15, -46)
        self.create_object(StringParser_15, 534, -55)
        self.create_object(GlobalName_6, 124, -48)
        self.create_object(Version_26, 125, -113)
        self.create_object(MaxPlayer_102, 75, -81)
        self.create_object(CurrentPlayer_175, 39, -87)
        self.create_object(ScreenshotNr_23, 356, 674)
        self.create_object(GlobalValues_165, -69, 305)
        self.create_object(Moo_181, -73, 378)
        self.create_object(XtraXtraCRC_182, 309, -54)
        self.create_object(MapTileCounter_188, -172, 623)
        self.create_object(MapTileMax_189, -103, 623)
        self.create_object(CheckMap_171, 812, 245)
        self.create_object(Edit_177, 28, 619)
        self.create_object(Enterpw_179, 500, 637)
        self.create_object(Mapload_187, -231, 471)
        self.add_timed_call(self.on_timer_1, 1.0)
        self.add_timed_call(self.on_timer_2, 15.0)
        self.groups = {
            'Check connection' : False,
            'PW' : False,
            'Disc' : True,
        }
        # print self.values
        # print self.strings
        # for item in self.instances:
        #     klass = item.__class__
        #     if hasattr(klass, 'global_data'):
        #         print klass, klass.global_data
    
    def on_start(self):
        self.set_event_id(1)
        self.hide_cursor()
        self.get(Enterpw_179).limit_size(10)
        self.set_event_id(2)
        if self.get(ServerError_60).text != '':
            self.get(Status_170).set_value(self.get(ServerError_60).text)
            self.get(Status2_190).set_value(self.get(ServerError_60).text)
            self.get(Status_170).set_color((231, 0, 0))
        self.set_event_id(3)
        if self.get(ServerError_60).text == '':
            self.get(Status_170).set_value('Connecting to server ')
            self.get(StringParser_15).add_delimiter(',')
            self.get(Status2_190).set_value('Connecting to server ')
        pass
    
    def on_timer_1(self):
        self.set_event_id(4)
        if self.get(ServerError_60).text == '':
            self.get(Moo_181).connect(self.get(Ip_46).text, to_number(self.get(Port_47).text)+1)
        pass
    
    def on_timer_2(self):
        self.set_event_id(26)
        if (self.groups['Disc'] and
        self.get(ServerError_60).text == ''):
            self.get(Status_170).set_value('Could not connect to server')
            self.groups['PW'] = False
            self.get(Moo_181).disconnect()
            self.get(Status2_190).set_value('Could not connect to server')
            self.get(Status_170).set_color((231, 0, 0))
        pass
    
    def function_n(self, int_arg = None):
        self.set_event_id(15)
        self.get(Status_170).set_value('Server does not allow map downloads ('+self.get(ChosedMapWithoutPath_126).text+')')
        self.get(Status2_190).set_value('Server does not allow map downloads ('+self.get(ChosedMapWithoutPath_126).text+')')
        self.get(Status_170).set_color((231, 0, 0))
        pass
    
    def function_1(self, int_arg = None):
        self.set_event_id(10)
        self.get(StringParser_15).set_value(self.get(Info_173).text)
        self.get(ChosedMapWithoutPath_126).set_value(self.get(StringParser_15).get_element(-1 + 2)+'.sdo')
        self.get(Mapid_183).set_value(self.get(StringParser_15).get_element(-1 + 3))
        self.get(MessageOfDay_58).set_value(self.get(StringParser_15).get_element(-1 + 4))
        self.get(WeaponAllowed_59).set_value(self.get(StringParser_15).get_element(-1 + 5)+','+self.get(StringParser_15).get_element(-1 + 6)+','+self.get(StringParser_15).get_element(-1 + 7)+','+self.get(StringParser_15).get_element(-1 + 8)+','+self.get(StringParser_15).get_element(-1 + 9)+','+self.get(StringParser_15).get_element(-1 + 10)+','+self.get(StringParser_15).get_element(-1 + 11)+','+self.get(StringParser_15).get_element(-1 + 12)+','+self.get(StringParser_15).get_element(-1 + 13)+','+self.get(StringParser_15).get_element(-1 + 14))
        self.get(VersionCheck_174).set_value(self.get(StringParser_15).get_element(-1 + 15))
        self.get(CurrentPlayer_175).set_value(to_number(self.get(StringParser_15).get_element(-1 + 16)))
        self.get(MaxPlayer_102).set_value(to_number(self.get(StringParser_15).get_element(-1 + 17)))
        self.get(CheckDaMap_176).set_value(self.get(StringParser_15).get_element(-1 + 3))
        self.get(Rightpw_180).set_value(self.get(StringParser_15).get_element(-1 + 18))
        self.get(Sting_186).set_value(self.get(StringParser_15).get_element(-1 + 19))
        self.set_event_id(11)
        if self.get(Rightpw_180).text == ' ':
            self.groups['Check connection'] = True
            return
        self.set_event_id(12)
        if self.get_global_value(2) == 1:
            self.groups['Check connection'] = True
            return
        self.set_event_id(13)
        if (self.get(Rightpw_180).text != ' ' and
        self.get_global_value(2) == 0):
            self.values[2] = 1
            self.groups['PW'] = True
            self.get(Enterpw_179).set_focus(True)
            self.get(Moo_181).disconnect()
            return
        pass
    
    def function_0(self, int_arg = None):
        self.set_event_id(9)
        self.get(Status_170).set_color((231, 0, 0))
        self.get(Status_170).set_value('You were banned from this server')
        self.get(Status2_190).set_value('You were banned from this server')
        self.get(Moo_181).disconnect()
        pass
    
    def function_3(self, int_arg = None):
        self.set_event_id(17)
        if select(self.get(MapTileCounter_188).get_value() == self.get(MapTileMax_189).get_value()):
            self.get(Status_170).set_value(self.get(ChosedMapWithoutPath_126).text+' downloading...'+'\r\n'+'100%')
            self.get(Status2_190).set_value(self.get(ChosedMapWithoutPath_126).text+' downloading...'+'\r\n'+'100%')
            self.get(Mapload_187).add_line(right_string(self.get(Info_173).text, len(self.get(Info_173).text)-2))
            self.get(Mapload_187).ListSaveListFile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text)
            encrypt_file(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text, 8)
        self.set_event_id(18)
        if select(self.get(MapTileCounter_188).get_value() == self.get(MapTileMax_189).get_value()):
            return
            self.restart_frame()
        self.set_event_id(19)
        if (select(self.get(MapTileCounter_188).get_value() > 0) and
        select(self.get(MapTileCounter_188).get_value() != self.get(MapTileMax_189).get_value())):
            self.get(Mapload_187).add_line(right_string(self.get(Info_173).text, len(self.get(Info_173).text)-2))
            self.get(Status_170).set_value(self.get(ChosedMapWithoutPath_126).text+' downloading...'+'\r\n'+str(to_int(((self.get(MapTileCounter_188).get_value()*1.0)/(self.get(MapTileMax_189).get_value()*1.0)*100)))+'%')
            self.get(Status2_190).set_value(self.get(Status_170).text)
            self.get(MapTileCounter_188).add_value(1)
            self.get(Moo_181).send_line('002,'+str(self.get(MapTileCounter_188).get_value())+','+left_string(self.get(ChosedMapWithoutPath_126).text, len(self.get(ChosedMapWithoutPath_126).text)-4))
        self.set_event_id(20)
        if select(self.get(MapTileCounter_188).get_value() == 0):
            self.get(MapTileMax_189).set_value(to_number(right_string(self.get(Info_173).text, len(self.get(Info_173).text)-2)))
            self.get(Status_170).set_value(self.get(ChosedMapWithoutPath_126).text+' downloading...'+'\r\n'+'0%')
            self.get(Status2_190).set_value(self.get(ChosedMapWithoutPath_126).text+' downloading...'+'\r\n'+'0%')
            self.get(MapTileCounter_188).add_value(1)
            self.get(Moo_181).send_line('002,'+str(self.get(MapTileCounter_188).get_value())+','+left_string(self.get(ChosedMapWithoutPath_126).text, len(self.get(ChosedMapWithoutPath_126).text)-4))
        pass
    
    def function_2(self, int_arg = None):
        self.set_event_id(16)
        self.restart_frame()
        pass
    
    def function_y(self, int_arg = None):
        self.set_event_id(14)
        self.get(Status_170).set_value(self.get(ChosedMapWithoutPath_126).text+' downloading...')
        self.get(Status2_190).set_value(self.get(ChosedMapWithoutPath_126).text+' downloading...')
        self.groups['Disc'] = False
        self.get(Moo_181).send_line('002,0,'+left_string(self.get(ChosedMapWithoutPath_126).text, len(self.get(ChosedMapWithoutPath_126).text)-4))
        pass
    
    def function_rec(self, int_arg = None):
        self.set_event_id(7)
        self.get(Info_173).set_value(decrypt_string('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9', self.get(Info_173).text))
        self.set_event_id(8)
        self.get(StringParser_15).set_value(self.get(Info_173).text)
        getattr(self, "function_" + self.get(StringParser_15).get_element(0))()
        pass
    
    def on_sock_receive(self, instance):
        if type(instance) == Moo_181:
            self.set_event_id(6)
            self.get(Status_170).set_value('Receiving data...')
            self.get(Status2_190).set_value('Receiving data...')
            self.get(Info_173).set_value(self.get(Moo_181).get_line())
            self.function_rec()
        pass
    
    def on_sock_connect(self, instance):
        if type(instance) == Moo_181:
            self.set_event_id(5)
            self.get(Moo_181).send_line('000')
        pass
    
    def update(self, dt):
        self.set_event_id(21)
        if (Qt.Key_Escape in self.scene.key_presses and
        self.get_global_value(12) == 1):
            self.values[12] = 2
        self.set_event_id(22)
        if Qt.Key_Escape in self.scene.key_presses:
            self.get(ServerError_60).set_value('')
            self.set_frame(2)
        self.set_event_id(23)
        if (Qt.Key_F12 in self.scene.key_presses and
        self.get_global_value(12) == 1):
            self.values[12] = 2
        self.set_event_id(24)
        if Qt.Key_F12 in self.scene.key_presses:
            self.get(ServerError_60).set_value('')
            self.set_frame(2)
        if self.groups['Check connection']:
            self.set_event_id(29)
            if (self.check_once() and
            self.get(Version_26).text != self.get(VersionCheck_174).text and
            self.get(VersionCheck_174).text != ''):
                self.groups['Check connection'] = False
                self.get(Status_170).set_value('Incompatible version')
                self.get(Status2_190).set_value('Incompatible version')
                self.get(Status_170).set_color((231, 0, 0))
            self.set_event_id(30)
            if (self.check_once() and
            self.get(Version_26).text != self.get(VersionCheck_174).text and
            self.get(VersionCheck_174).text == ''):
                self.groups['Check connection'] = False
                self.get(Status_170).set_value("Can't receive information from server")
                self.get(Status2_190).set_value("Can't receive information from server")
                self.get(Status_170).set_color((231, 0, 0))
            self.set_event_id(31)
            if (self.check_once() and
            self.get(CurrentPlayer_175).get_value() >= self.get(MaxPlayer_102).get_value()):
                self.groups['Check connection'] = False
                self.get(Status_170).set_value('Server is full')
                self.get(Status2_190).set_value('Server is full')
                self.get(Status_170).set_color((231, 0, 0))
            self.set_event_id(32)
            if (self.check_once() and
            negate(os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text))):
                self.groups['Check connection'] = False
                self.get(Moo_181).send_line('001')
            self.set_event_id(33)
            if self.check_once():
                self.get(XtraXtraCRC_182).calculate(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text)
                self.get(Mapid2_184).set_value(str(self.get(XtraXtraCRC_182).get_crc()))
            self.set_event_id(34)
            if self.check_once():
                decrypt_file(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text, 8)
            self.set_event_id(35)
            if self.check_once():
                self.get(CheckMap_171).load(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text)
            self.set_event_id(36)
            if self.check_once():
                encrypt_file(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text, 8)
            self.set_event_id(37)
            if (self.check_once() and
            self.get(Mapid2_184).text != self.get(Mapid_183).text):
                self.get(Status_170).set_value('Map '+self.get(ChosedMapWithoutPath_126).text+' differs from server')
                self.groups['Check connection'] = False
                self.get(Status2_190).set_value('Map '+self.get(ChosedMapWithoutPath_126).text+' differs from server')
                self.get(Status_170).set_color((231, 0, 0))
            self.set_event_id(38)
            if (self.check_once() and
            to_number(self.get(CheckMap_171).get_line(3)) >= 1 and
            self.get(Mapid2_184).text == self.get(Mapid_183).text):
                self.values[2] = 0
                self.set_frame(5)
        if self.groups['PW']:
            self.set_event_id(41)
            if True:
                self.get(Status_170).set_value('Enter password:'+'\r\n'+self.get(Enterpw_179).get_value())
                self.get(Status2_190).set_value('Enter password:'+'\r\n'+self.get(Enterpw_179).get_value())
            self.set_event_id(42)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Enterpw_179).get_value() == self.get(Rightpw_180).text):
                self.groups['PW'] = False
                self.get(Status_170).set_value('Receiving data...')
                self.get(Status2_190).set_value('Receiving data...')
                self.restart_frame()
            self.set_event_id(43)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Enterpw_179).get_value() != self.get(Rightpw_180).text):
                self.get(Status_170).set_color((231, 0, 0))
                self.get(Status_170).set_value('Wrong password')
                self.get(Status2_190).set_value('Wrong password')
                self.groups['PW'] = False
                self.get(Moo_181).disconnect()
            self.set_event_id(44)
            if Qt.Key_Tab in self.scene.key_presses:
                self.get(Enterpw_179).set_focus(True)
        pass
    
