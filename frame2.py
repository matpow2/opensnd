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

class Frame2(Frame):
    name = 'Login'
    index = 1
    width = 800
    height = 600
    background = (0, 0, 0)
    
    def initialize(self):
        self.create_object(ValidChar_22, 123, 620)
        self.create_object(Msg_16, 303, 699)
        self.create_object(VerCheck_25, 337, 712)
        self.create_object(IrcNick_27, 466, -94)
        self.create_object(Newid_28, -2, -66)
        self.create_object(Channel1_36, -232, 435)
        self.create_object(Title_4, 0, 0)
        self.create_object(GlobalName_6, 3, -48)
        self.create_object(CheckVersion_8, 180, -42)
        self.create_object(Ip2_9, 432, -109)
        self.create_object(Port2_10, 462, -72)
        self.create_object(Connect_11, 400, 455)
        self.create_object(String2_12, 9, 575)
        self.create_object(MooSock_13, 567, -65)
        self.create_object(CheckUser_14, 666, -34)
        self.create_object(StringParser_15, 700, -62)
        self.create_object(Timeout_18, 371, -24)
        self.create_object(RemoteIP_20, 155, -95)
        self.create_object(EigeneIP_21, 173, -121)
        self.create_object(ScreenshotNr_23, 588, 621)
        self.create_object(Version_26, 532, 659)
        self.create_object(SvrKills_29, 68, -112)
        self.create_object(SvrDeaths_30, 66, -92)
        self.create_object(SvrPoints_31, 63, -73)
        self.create_object(SvrKills2_32, 116, -112)
        self.create_object(SvrDeaths2_33, 113, -90)
        self.create_object(SvrPoints2_34, 113, -71)
        self.create_object(String12_37, 51, 515)
        self.create_object(String11_17, 50, 514)
        self.create_object(BinaryObject_38, 312, -123)
        self.create_object(Name_5, 280, 394)
        self.create_object(Ini_7, 150, -71)
        self.create_object(Edit_19, 31, 641)
        self.create_object(Edit2_24, 294, 655)
        self.groups = {
            'links' : True,
            'Check name' : False,
            'Get Info' : False,
            'Access' : False,
            'Check version' : False,
        }
    
    def on_start(self):
        self.set_event_id(1)
        self.get(Name_5).limit_size(15)
        self.get(Name_5).set_focus(True)
        self.get(Ini_7).set_filename((os.getcwd()+'\\')+'data.ini')
        self.get(Ini_7).set_group('Data')
        self.get(Ini_7).set_item('Name')
        self.get(Name_5).set_value(left_string(self.get(Ini_7).get(), 15))
        self.get(Ini_7).set_item('UID')
        self.get(Newid_28).set_value(self.get(Ini_7).get())
        self.values[10] = 0
        self.values[6] = 0
        self.get(Connect_11).values[0] = 0
        self.show_cursor()
        self.get(StringParser_15).add_delimiter('\r\n')
        self.get(Edit2_24).load_file('Screenshot.pak')
        add_encryption_key('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9')
        self.set_event_id(2)
        self.get(ScreenshotNr_23).set_value(self.get(Edit2_24).get_number())
        self.set_event_id(3)
        if self.get(Newid_28).text == '':
            self.get(Newid_28).set_value('0')
        self.set_event_id(4)
        if self.get(Ini_7).get_value_item('Footsteps') == 1:
            self.players[1].lives = 1
        self.set_event_id(5)
        if self.get(Ini_7).get_value_item('Footsteps') != 1:
            self.players[1].lives = 0
        self.set_event_id(6)
        if (self.get(Ini_7).get_value_item('Music') == 1 and
        self.get_global_value(0) == 0):
            self.values[0] = 1
            self.values[12] = 1
            self.set_mod_volume(0, self.get(Ini_7).get_value_item('MusicVolume'))
            self.set_mod_volume(1, self.get(Ini_7).get_value_item('MusicVolume'))
            self.set_mod_volume(2, self.get(Ini_7).get_value_item('MusicVolume'))
            self.set_mod_volume(3, self.get(Ini_7).get_value_item('MusicVolume'))
            self.set_mod_volume(4, self.get(Ini_7).get_value_item('MusicVolume'))
            self.cross_fade_mod(0, 0, 3000)
        self.set_event_id(7)
        if self.get(Name_5).get_value() == '':
            self.get(Name_5).set_value('Player')
        pass
    
    def loop_name(self):
        self.set_event_id(21)
        if (self.groups['Check name'] and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '[' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != ']' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '!' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '$' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '+' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '*' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != "'" and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '#' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '/' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '\\' and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != '|'):
            self.get(IrcNick_27).set_value(self.get(IrcNick_27).text+mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1))
        self.set_event_id(22)
        for loop_index in xrange(len(self.get(ValidChar_22).text)):
            self.loop_indexes['ValidChar'] = loop_index
            if self.loop_valid_char() == False: break
        pass
    
    def loop_valid_char(self):
        self.set_event_id(23)
        if (self.groups['Check name'] and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) == mid_string(self.get(ValidChar_22).text, self.get_loop_index('ValidChar'), 1)):
            return False # 'ValidChar'
        self.set_event_id(24)
        if (self.groups['Check name'] and
        self.get_loop_index('ValidChar') == len(self.get(ValidChar_22).text)-1 and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) == ' '):
            self.groups['Check name'] = False
            self.get(Connect_11).set_transparency(0)
            self.get(Connect_11).values[0] = 0
            self.get(String11_17).set_value('Space is an invalid character, use _ instead')
            self.get(CheckUser_14).set_value(0)
            self.get(Name_5).set_read_only(False)
            self.get(String12_37).set_value('Space is an invalid character, use _ instead')
        self.set_event_id(25)
        if (self.groups['Check name'] and
        self.get_loop_index('ValidChar') == len(self.get(ValidChar_22).text)-1 and
        mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1) != ' '):
            self.groups['Check name'] = False
            self.get(Connect_11).set_transparency(0)
            self.get(Connect_11).values[0] = 0
            self.get(String11_17).set_value(mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1)+' is an invalid character')
            self.get(CheckUser_14).set_value(0)
            self.get(Name_5).set_read_only(False)
            self.get(String12_37).set_value(mid_string(self.get(Name_5).get_value(), self.get_loop_index('Name'), 1)+' is an invalid character')
        pass
    
    def on_mouse_press(self, x, y, button):
        if self.get(Connect_11).is_over(x, y):
            self.set_event_id(9)
            if (select(self.get(CheckUser_14).get_value() == 0) and
            select(self.get(Connect_11).values.get(0, 0) == 0) and
            self.get(Name_5).get_value() != ''):
                self.get(String11_17).set_value('')
                self.get(Connect_11).values[0] = 1
                self.get(CheckUser_14).set_value(3)
                self.get(Connect_11).restore_animation()
                self.get(Connect_11).set_transparency(70)
                self.get(Edit_19).set_value('GET http://www.seekanddread.de/Game/login.php'+' HTTP/1.0'+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
                self.groups['Check name'] = True
                self.get(Name_5).set_read_only(True)
                self.get(IrcNick_27).set_value('')
                self.get(String12_37).set_value('')
            self.set_event_id(10)
            if (select(self.get(CheckUser_14).get_value() == 0) and
            select(self.get(Connect_11).values.get(0, 0) == 0) and
            self.get(Name_5).get_value() == ''):
                self.get(String11_17).set_value('Enter a name')
                self.get(String12_37).set_value('Enter a name')
        pass
    
    def on_sock_receive(self, instance):
        if type(instance) == MooSock_13:
            self.set_event_id(16)
            self.get(Edit_19).set_value(self.get(MooSock_13).get_bytes(1024))
            self.groups['Get Info'] = True
            self.get(Timeout_18).set_value(4)
        pass
    
    def on_sock_connect(self, instance):
        if type(instance) == MooSock_13:
            self.set_event_id(13)
            self.get(MooSock_13).send_text(self.get(Edit_19).get_value())
        pass
    
    def on_sock_disconnect(self, instance):
        if type(instance) == MooSock_13:
            self.set_event_id(15)
            self.get(Connect_11).flags[1] = False
        pass
    
    def on_sock_connection(self, instance):
        if type(instance) == MooSock_13:
            self.set_event_id(14)
            self.get(Connect_11).flags[1] = True
            self.get(MooSock_13).accept()
        pass
    
    def update(self, dt):
        self.set_event_id(8)
        if (Qt.Key_Escape in self.scene.key_presses and
        select(self.get(CheckUser_14).get_value() == 0)):
            self.end_application()
        self.set_event_id(11)
        if (self.every(1.0) and
        select(self.get(Timeout_18).get_value() > 0)):
            self.get(Timeout_18).subtract_value(1)
        self.set_event_id(12)
        if select(self.get(Timeout_18).get_value() == 0):
            self.get(Connect_11).set_transparency(0)
            self.get(Connect_11).values[0] = 0
            self.get(String11_17).set_value("Can't connect to server please try again later")
            self.get(Timeout_18).set_value(-1)
            self.get(MooSock_13).disconnect()
            self.get(CheckUser_14).set_value(0)
            self.get(String12_37).set_value("Can't connect to server please try again later")
        if self.groups['Check name']:
            self.set_event_id(18)
            if len(self.get(Name_5).get_value()) < 5:
                self.groups['Check name'] = False
                self.get(Connect_11).set_transparency(0)
                self.get(Connect_11).values[0] = 0
                self.get(String11_17).set_value('Your name must have at least 5 characters')
                self.get(CheckUser_14).set_value(0)
                self.get(Name_5).set_read_only(False)
                self.get(String12_37).set_value('Your name must have at least 5 characters')
            self.set_event_id(19)
            if self.get(Name_5).get_value() == 'Admin':
                self.groups['Check name'] = False
                self.get(Connect_11).set_transparency(0)
                self.get(Connect_11).values[0] = 0
                self.get(String11_17).set_value('Name is reserved')
                self.get(CheckUser_14).set_value(0)
                self.get(Name_5).set_read_only(False)
                self.get(String12_37).set_value('Name is reserved')
            self.set_event_id(20)
            if True:
                for loop_index in xrange(len(self.get(Name_5).get_value())):
                    self.loop_indexes['Name'] = loop_index
                    if self.loop_name() == False: break
            self.set_event_id(26)
            if True:
                self.get(MooSock_13).connect('www.seekanddread.de', 80)
                self.groups['Check name'] = False
                self.get(Timeout_18).set_value(10)
        if self.groups['links']:
            self.set_event_id(29)
            if (self.get(Connect_11).mouse_over() and
            select(self.get(Connect_11).values.get(0, 0) == 0)):
                self.get(Connect_11).force_animation('User defined 1')
            self.set_event_id(30)
            if (negate(self.get(Connect_11).mouse_over()) and
            select(self.get(Connect_11).values.get(0, 0) == 0)):
                self.get(Connect_11).restore_animation()
        if self.groups['Get Info']:
            self.set_event_id(33)
            if (self.every(1.0) and
            select(self.get(Timeout_18).get_value() > 1)):
                self.get(Timeout_18).subtract_value(1)
            self.set_event_id(34)
            if select(self.get(Timeout_18).get_value() == 1):
                self.get(StringParser_15).set_value(self.get(Edit_19).get_value())
                self.get(Msg_16).set_value(self.get(StringParser_15).get_element(-1))
                self.get(BinaryObject_38).insert(self.get(Msg_16).text, 0)
                self.get(BinaryObject_38).replace('-', '+')
                self.get(BinaryObject_38).replace('_', '/')
                self.get(BinaryObject_38).replace('.', '=')
                self.get(BinaryObject_38).replace('\n', '')
                self.get(BinaryObject_38).replace('\r', '')
                self.get(BinaryObject_38).decode_base64()
                self.get(Msg_16).set_value(self.get(BinaryObject_38).get_string(0, self.get(BinaryObject_38).get_size()))
                self.get(StringParser_15).clear_delimiters()
                self.get(StringParser_15).add_delimiter(',')
                self.get(StringParser_15).set_value(self.get(Msg_16).text)
                self.get(RemoteIP_20).set_value(self.get(StringParser_15).get_element(-1 + 1))
                self.get(Ip2_9).set_value(self.get(StringParser_15).get_element(-1 + 2))
                self.get(Port2_10).set_value(self.get(StringParser_15).get_element(-1 + 3))
                self.get(VerCheck_25).set_value(self.get(StringParser_15).get_element(-1 + 5))
                self.get(Ini_7).set_group_item_value('Data', 'UID', self.get(StringParser_15).get_element(-1 + 6))
                self.get(GlobalName_6).set_value(self.get(Name_5).get_value())
                self.get(EigeneIP_21).set_value(self.get(MooSock_13).get_local_ip())
                self.get(SvrKills_29).set_value(to_number(self.get(StringParser_15).get_element(-1 + 7)))
                self.get(SvrKills2_32).set_value(to_number(self.get(StringParser_15).get_element(-1 + 7)))
                self.get(SvrDeaths_30).set_value(to_number(self.get(StringParser_15).get_element(-1 + 8)))
                self.get(SvrDeaths2_33).set_value(to_number(self.get(StringParser_15).get_element(-1 + 8)))
                self.get(SvrPoints_31).set_value(to_number(self.get(StringParser_15).get_element(-1 + 9)))
                self.get(SvrPoints2_34).set_value(to_number(self.get(StringParser_15).get_element(-1 + 9)))
                self.get(Newid_28).set_value(self.get(StringParser_15).get_element(-1 + 6))
                self.get(Channel1_36).set_value(self.get(StringParser_15).get_element(-1 + 10))
                self.get(MooSock_13).disconnect()
                self.groups['Get Info'] = False
                self.groups['Check version'] = True
        if self.groups['Access']:
            self.set_event_id(37)
            if (self.every(1.0) and
            select(self.get(Timeout_18).get_value() > 1)):
                self.get(Timeout_18).subtract_value(1)
            self.set_event_id(38)
            if select(self.get(Timeout_18).get_value() == 1):
                self.values[3] = self.get(SvrKills2_32).get_value()
                self.values[14] = self.get(SvrDeaths2_33).get_value()
                self.values[15] = self.get(SvrPoints2_34).get_value()
                self.get(Ini_7).set_group_item_value('Data', 'Name', self.get(Name_5).get_value())
                self.set_frame(2)
        if self.groups['Check version']:
            self.set_event_id(41)
            if self.get(VerCheck_25).text == '1.44':
                self.groups['Access'] = True
                self.get(Timeout_18).set_value(4)
                self.get(String11_17).set_color((107, 199, 103))
                self.get(String11_17).set_value(self.get(StringParser_15).get_element(-1 + 4))
                self.groups['Check version'] = False
                self.get(String12_37).set_value(self.get(StringParser_15).get_element(-1 + 4))
            self.set_event_id(42)
            if self.get(VerCheck_25).text != '1.44':
                self.groups['Check version'] = False
                self.get(String11_17).set_color((255, 0, 0))
                self.get(String11_17).set_value("You don't have the latest version, download version "+self.get(StringParser_15).get_element(-1 + 5)+'  at http://www.seekanddread.de !')
                self.get(Timeout_18).set_value(-1)
                self.get(CheckUser_14).set_value(0)
                self.get(String12_37).set_value("You don't have the latest version, download version "+self.get(StringParser_15).get_element(-1 + 5)+'  at http://www.seekanddread.de !')
        pass
    
