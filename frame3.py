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

class Frame3(Frame):
    name = 'Server-List'
    index = 2
    width = 800
    height = 600
    background = (255, 255, 255)
    
    def initialize(self):
        self.create_object(Zeilenumbruch_39, -183, -45)
        self.create_object(MessageOfDay_58, -162, 283)
        self.create_object(WeaponAllowed_59, -166, 312)
        self.create_object(ServerError_60, -161, 328)
        self.create_object(ServerInfo_61, 224, -117)
        self.create_object(Buffer_63, 164, 737)
        self.create_object(ClanTag_65, 232, -43)
        self.create_object(String2_79, 604, 636)
        self.create_object(String3_80, 604, 656)
        self.create_object(Nickname0_81, 604, 676)
        self.create_object(Channel1_36, 604, 696)
        self.create_object(Server2_82, 604, 716)
        self.create_object(IrcNick_27, 181, -75)
        self.create_object(GlobalName_6, -183, -22)
        self.create_object(Lobby_40, 0, 0)
        self.create_object(Timeout_41, 452, -61)
        self.create_object(String_42, 624, 115)
        self.create_object(StringParser_43, 539, -56)
        self.create_object(Version_26, -168, 35)
        self.create_object(Ip_46, -159, 13)
        self.create_object(Port_47, -186, -8)
        self.create_object(StatusServer_45, 24, 257)
        self.create_object(Ip2_9, -2, -64)
        self.create_object(Port2_10, 7, -40)
        self.create_object(EigeneIP_21, 842, 238)
        self.create_object(Connect2_49, 697, 145)
        self.create_object(GetServerList_50, 697, 185)
        self.create_object(HostAGame_51, 696, 245)
        self.create_object(ExitGame_52, 696, 265)
        self.create_object(Control_54, -48, -7)
        self.create_object(Counter4_56, 62, 647)
        self.create_object(MooSock2_57, 621, -59)
        self.create_object(RemoteIP_20, 842, 266)
        self.create_object(SndKlein2_64, 636, 64)
        self.create_object(SndKlein_48, 633, 62)
        self.create_object(Counter5_66, 68, 671)
        self.create_object(StringParser2_67, 581, -40)
        self.create_object(ScreenshotNr_23, 333, 654)
        self.create_object(MooSock_72, 121, 648)
        self.create_object(StingParserMotd_73, 263, 698)
        self.create_object(StringParse_74, 198, 704)
        self.create_object(StringParser3_75, 122, 690)
        self.create_object(InputBoxHandler_76, 239, 650)
        self.create_object(Flags_83, 505, 726)
        self.create_object(Counter_84, 492, 751)
        self.create_object(SvrKills_29, 108, -111)
        self.create_object(SvrDeaths_30, 106, -91)
        self.create_object(SvrPoints_31, 103, -72)
        self.create_object(SvrKills2_32, 159, -111)
        self.create_object(SvrDeaths2_33, 156, -89)
        self.create_object(SvrPoints2_34, 156, -70)
        self.create_object(Options_89, 695, 206)
        self.create_object(JoinChat_90, 694, 225)
        self.create_object(SubApplication_91, 250, 125)
        self.create_object(BinaryObject_38, 346, -103)
        self.create_object(Ctoip_92, 641, 158)
        self.create_object(SubApplication2_93, 250, 175)
        self.create_object(ServerIPs_44, -160, 76)
        self.create_object(Ini_55, 554, -99)
        self.create_object(Edit2_62, 832, 488)
        self.create_object(Edit3_68, 832, 373)
        self.create_object(Log_69, 393, 642)
        self.create_object(TextInputBox_70, 21, 550)
        self.create_object(InputBoxModifier_71, 394, 692)
        self.create_object(List_77, 729, 626)
        self.create_object(UserList_78, 612, 334)
        self.create_object(ChatLog_87, 15, 332)
        self.create_object(IconListObject_88, 20, 50)
        self.groups = {
            'userlist' : True,
            'Subapp' : True,
            'Menu' : True,
            'Buttons' : True,
            'receive' : True,
            'preset' : True,
            'Server Request' : True,
            'Subapp2' : True,
            'connecting' : True,
            'Connect' : True,
        }
    
    def on_start(self):
        self.set_event_id(1)
        self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
        self.get(Ini_55).set_group('Data')
        self.show_cursor()
        self.get(TextInputBox_70).set_focus(True)
        self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
        self.get(ChatLog_87).set_color((255, 0, 0))
        self.get(ChatLog_87).set_text('\r\n'+"Press 'join chat'!")
        self.players[0].lives = 0
        self.set_event_id(2)
        self.get(StringParser_43).add_delimiter(',')
        self.get(Connect2_49).set_transparency(70)
        self.get(HostAGame_51).set_transparency(70)
        self.get(Counter4_56).set_value(self.get(Ini_55).get_value_item('Turning'))
        self.values[0] = 0
        self.values[1] = 0
        self.values[2] = 0
        self.values[15] = 0
        self.values[5] = 0
        self.values[4] = 0
        self.values[8] = 0
        self.values[9] = 0
        self.values[13] = self.get(Ini_55).get_value_item('Turning')
        self.get(GetServerList_50).set_transparency(0)
        self.get(GetServerList_50).values[0] = 1
        self.get(Counter5_66).set_value(self.get(Ini_55).get_value_item('MusicVolume'))
        self.values[6] = 0
        self.get(StringParser2_67).add_delimiter('\n')
        self.get(Options_89).set_transparency(0)
        self.get(Options_89).values[0] = 1
        self.get(JoinChat_90).set_transparency(0)
        self.get(JoinChat_90).values[0] = 1
        self.get(Ctoip_92).values[0] = 1
        self.set_event_id(3)
        if self.get_global_value(12) == 2:
            self.values[12] = 1
            self.set_mod_volume(0, self.get(Counter5_66).get_value())
            self.set_mod_volume(1, self.get(Counter5_66).get_value())
            self.set_mod_volume(2, self.get(Counter5_66).get_value())
            self.set_mod_volume(3, self.get(Counter5_66).get_value())
            self.set_mod_volume(4, self.get(Counter5_66).get_value())
            self.cross_fade_mod(0, 0, 3000)
        self.set_event_id(4)
        if (self.get(Ini_55).get_value_item('Skin') != 0 and
        self.get(Ini_55).get_value_item('Skin') != 1 and
        self.get(Ini_55).get_value_item('Skin') != 2):
            self.values[4] = 0
            self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_55).set_group('Data')
            self.get(Ini_55).set_item_value('Skin', 0)
        self.set_event_id(5)
        if self.get(Ini_55).get_value_item('Skin') == 0:
            self.values[4] = 0
        self.set_event_id(6)
        if self.get(Ini_55).get_value_item('Skin') == 1:
            self.values[4] = 1
        self.set_event_id(7)
        if self.get(Ini_55).get_value_item('Skin') == 2:
            self.values[4] = 2
        self.set_event_id(8)
        if (self.get(Ini_55).get_value_item('Startweapon') != 0 and
        self.get(Ini_55).get_value_item('Startweapon') != 1):
            self.values[9] = 0
            self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_55).set_group('Data')
            self.get(Ini_55).set_item_value('Startweapon', 0)
        self.set_event_id(9)
        if self.get(Ini_55).get_value_item('Startweapon') == 0:
            self.values[9] = 0
        self.set_event_id(10)
        if self.get(Ini_55).get_value_item('Startweapon') == 1:
            self.values[9] = 1
        self.set_event_id(11)
        if self.get(Ini_55).get_value_item('Graphics') == 1:
            self.values[6] = 1
        self.set_event_id(12)
        if self.get(Ini_55).get_value_item('Graphics') == 2:
            self.values[6] = 2
        self.set_event_id(13)
        if self.get(Ini_55).get_value_item('Graphics') == 3:
            self.values[6] = 3
        self.set_event_id(14)
        if self.get(EigeneIP_21).text != '':
            self.get(HostAGame_51).set_transparency(0)
            self.get(HostAGame_51).values[0] = 1
        self.set_event_id(15)
        if select(self.get(Counter4_56).get_value() < 1):
            self.get(Counter4_56).set_value(25)
            self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_55).set_group('Data')
            self.get(Ini_55).set_item_value('Turning', self.get(Counter4_56).get_value())
            self.values[13] = self.get(Counter4_56).get_value()
        self.set_event_id(16)
        if select(self.get(Counter4_56).get_value() > 99):
            self.get(Counter4_56).set_value(25)
            self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_55).set_group('Data')
            self.get(Ini_55).set_item_value('Turning', self.get(Counter4_56).get_value())
            self.values[13] = self.get(Counter4_56).get_value()
        self.set_event_id(17)
        self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
        self.get(Ini_55).set_group('Data')
        self.set_event_id(19)
        if select(self.get(GetServerList_50).values.get(0, 0) == 1):
            self.get(Edit2_62).set_value('GET http://www.seekanddread.de/Game/svr_get.php HTTP/1.0'+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
            self.get(ServerIPs_44).reset()
            self.get(StatusServer_45).set_value('Searching...')
            self.get(GetServerList_50).set_transparency(70)
            self.get(GetServerList_50).values[0] = 0
            self.get(GetServerList_50).restore_animation()
            self.get(MooSock2_57).connect('www.seekanddread.de', 80)
            self.get(IconListObject_88).reset()
            self.get(IconListObject_88).set_line(-1)
        self.set_event_id(72)
        self.get(StringParse_74).add_delimiter(':')
        self.get(StringParse_74).add_delimiter(' ')
        self.get(StringParse_74).add_delimiter('!')
        self.set_event_id(73)
        self.get(StringParser3_75).add_delimiter(' ')
        self.get(Nickname0_81).set_value(self.get(IrcNick_27).text)
        self.get(Server2_82).set_value(self.get(Ip2_9).text)
        self.set_event_id(74)
        self.get(StingParserMotd_73).add_delimiter(':')
        pass
    
    def loop_get_server(self):
        self.set_event_id(27)
        self.get(BinaryObject_38).insert(self.get(StringParser2_67).get_element(-1 + (self.get_loop_index('Get Server')+1)), 0)
        self.set_event_id(28)
        self.get(BinaryObject_38).replace('-', '+')
        self.get(BinaryObject_38).replace('_', '/')
        self.get(BinaryObject_38).replace('.', '=')
        self.get(BinaryObject_38).replace('\n', '')
        self.get(BinaryObject_38).replace('\r', '')
        self.set_event_id(29)
        self.get(BinaryObject_38).decode_base64()
        self.set_event_id(30)
        self.get(StringParser_43).set_value(self.get(BinaryObject_38).get_string(0, self.get(BinaryObject_38).get_size()))
        self.set_event_id(31)
        self.get(BinaryObject_38).clear()
        self.set_event_id(32)
        if (self.groups['Server Request'] and
        self.get(StringParser_43).get_element(0) == 'Sndo'):
            self.get(ServerIPs_44).add_line(self.get(StringParser_43).get_element(-1 + 6)+','+self.get(StringParser_43).get_element(-1 + 7))
            self.get(IconListObject_88).add_line(self.get(StringParser_43).get_element(-1 + 2)+' - Map: '+self.get(StringParser_43).get_element(-1 + 3)+' - Players: '+self.get(StringParser_43).get_element(-1 + 4)+'/'+self.get(StringParser_43).get_element(-1 + 5)+' - Version: '+self.get(StringParser_43).get_element(-1 + 8), to_number(self.get(StringParser_43).get_element(-1 + 9)))
        self.set_event_id(33)
        if (self.groups['Server Request'] and
        self.get_loop_index('Get Server')+1 == self.get(StringParser2_67).get_count() and
        self.get(StatusServer_45).text == 'Searching...'):
            self.get(StatusServer_45).set_value('')
            self.get(GetServerList_50).set_transparency(0)
            self.get(GetServerList_50).values[0] = 1
            return False # 'Get Server'
        self.set_event_id(34)
        if (self.groups['Server Request'] and
        self.get_loop_index('Get Server')+1 == self.get(StringParser2_67).get_count() and
        self.get(StatusServer_45).text != 'Searching...'):
            self.get(GetServerList_50).set_transparency(0)
            self.get(GetServerList_50).values[0] = 1
            return False # 'Get Server'
        pass
    
    def on_mouse_press(self, x, y, button):
        if self.get(Connect2_49).is_over(x, y):
            self.set_event_id(48)
            if (self.groups['Connect'] and
            self.get(IconListObject_88).get_index() >= 0 and
            self.get(StatusServer_45).text != 'Connecting...' and
            select(self.get(Options_89).values.get(0, 0) == 1)):
                self.get(StringParser_43).set_value(self.get(ServerIPs_44).get_line(self.get(IconListObject_88).get_index()+1))
                self.get(StatusServer_45).set_value('Connecting...')
                self.get(Ip_46).set_value(self.get(StringParser_43).get_element(-1 + 1))
                self.get(Port_47).set_value(self.get(StringParser_43).get_element(-1 + 2))
                self.get(HostAGame_51).values[0] = 0
                self.get(HostAGame_51).set_transparency(70)
                self.get(Connect2_49).set_transparency(70)
                self.get(Connect2_49).values[0] = 0
                self.get(GetServerList_50).set_transparency(70)
                self.get(GetServerList_50).values[0] = 0
                self.get(Connect2_49).restore_animation()
                self.stop_mod(0, 3000) # with fade
                self.set_frame(4)
                self.get(IconListObject_88).set_focus(False)
                self.get(Ctoip_92).values[0] = 0
                self.get(Ctoip_92).set_transparency(70)
        if self.get(GetServerList_50).is_over(x, y):
            self.set_event_id(35)
            if (self.groups['Server Request'] and
            select(self.get(GetServerList_50).values.get(0, 0) == 1)):
                self.get(Edit2_62).set_value('GET http://www.seekanddread.de/Game/svr_get.php HTTP/1.0'+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
                self.get(ServerIPs_44).reset()
                self.get(StatusServer_45).set_value('Searching...')
                self.get(GetServerList_50).set_transparency(70)
                self.get(GetServerList_50).values[0] = 0
                self.get(GetServerList_50).restore_animation()
                self.get(MooSock2_57).connect('www.seekanddread.de', 80)
                self.get(IconListObject_88).reset()
                self.get(IconListObject_88).set_line(-1)
        if self.get(HostAGame_51).is_over(x, y):
            self.set_event_id(41)
            if (self.groups['Buttons'] and
            select(self.get(HostAGame_51).values.get(0, 0) == 1)):
                self.get(HostAGame_51).values[0] = 2
                self.set_frame(3)
        if self.get(ExitGame_52).is_over(x, y):
            self.set_event_id(42)
            self.get(ExitGame_52).set_transparency(70)
            self.get(ExitGame_52).values[0] = 0
            self.get(ExitGame_52).restore_animation()
            self.get(HostAGame_51).set_transparency(70)
            self.get(HostAGame_51).values[0] = 0
            self.get(GetServerList_50).set_transparency(70)
            self.get(GetServerList_50).values[0] = 0
            self.get(Connect2_49).set_transparency(70)
            self.get(Connect2_49).values[0] = 0
            self.set_frame(6)
            self.get(Ctoip_92).set_transparency(70)
            self.get(Ctoip_92).values[0] = 0
            self.get(Ctoip_92).restore_animation()
        if self.get(Options_89).is_over(x, y):
            self.set_event_id(43)
            if (self.groups['Buttons'] and
            select(self.get(Options_89).values.get(0, 0) == 1)):
                self.get(Options_89).set_transparency(70)
                self.get(Options_89).values[0] = 2
                self.get(Options_89).restore_animation()
                self.values[3] = self.get(SvrPoints2_34).get_value()
                self.values[14] = self.get(SvrKills2_32).get_value()
                self.values[15] = self.get(SvrDeaths2_33).get_value()
                self.get(SubApplication_91).set_visible(True)
                self.get(Ctoip_92).set_transparency(70)
                self.get(Ctoip_92).values[0] = 2
                self.get(Ctoip_92).restore_animation()
        if self.get(JoinChat_90).is_over(x, y):
            self.set_event_id(44)
            if (self.groups['Buttons'] and
            select(self.get(JoinChat_90).values.get(0, 0) == 1)):
                self.get(MooSock_72).connect(self.get(Server2_82).text, to_number(self.get(Port2_10).text))
                self.get(List_77).add_line('Connecting to '+self.get(Server2_82).text+' on port '+self.get(Port2_10).text)
                self.get(List_77).scroll_end()
                self.get(InputBoxHandler_76).add_delimiter(' ')
                self.get(JoinChat_90).set_transparency(70)
                self.get(JoinChat_90).values[0] = 2
                self.get(JoinChat_90).restore_animation()
        if self.get(Ctoip_92).is_over(x, y):
            self.set_event_id(45)
            if (self.groups['Buttons'] and
            select(self.get(Ctoip_92).values.get(0, 0) == 1)):
                self.get(Ctoip_92).set_transparency(70)
                self.get(Ctoip_92).values[0] = 2
                self.get(Ctoip_92).restore_animation()
                self.get(SubApplication2_93).set_visible(True)
                self.get(Options_89).set_transparency(70)
                self.get(Options_89).values[0] = 2
                self.get(Options_89).restore_animation()
        pass
    
    def on_sock_receive(self, instance):
        if type(instance) == MooSock2_57:
            self.set_event_id(23)
            self.get(Timeout_41).set_value(3)
            self.get(Edit3_68).set_value(self.get(MooSock2_57).get_bytes(2048))
        if type(instance) == MooSock_72:
            self.set_event_id(70)
            self.get(StringParse_74).set_value(self.get(MooSock_72).get_line())
        pass
    
    def on_sock_connect(self, instance):
        if type(instance) == MooSock2_57:
            self.set_event_id(21)
            self.get(MooSock2_57).send_text(self.get(Edit2_62).get_value())
        if type(instance) == MooSock_72:
            self.set_event_id(77)
            self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
            self.get(Log_69).set_value(self.get(Log_69).get_value()+'\r\nCONNECTED!')
            self.get(ChatLog_87).set_color((255, 0, 0))
            self.get(ChatLog_87).set_text('\r\n'+'* Connected to IRC server! Receiving MOTD...')
            self.get(List_77).add_line('Connected')
            self.get(Log_69).scroll_end()
            self.get(List_77).scroll_end()
        pass
    
    def on_sock_disconnect(self, instance):
        if type(instance) == MooSock2_57:
            self.set_event_id(24)
            self.get(GetServerList_50).flags[7] = False
        if type(instance) == MooSock_72:
            self.set_event_id(78)
            self.get(Log_69).set_value(self.get(Log_69).get_value()+'\r\nDISCONNECTED!')
            self.get(List_77).add_line('Disconnected')
            self.get(Log_69).scroll_end()
            self.get(List_77).scroll_end()
        pass
    
    def on_sock_connection(self, instance):
        if type(instance) == MooSock2_57:
            self.set_event_id(22)
            self.get(MooSock2_57).accept()
            self.get(GetServerList_50).flags[7] = True
        pass
    
    def on_IconListSelectionChanged(self, instance):
        if type(instance) == IconListObject_88:
            self.set_event_id(36)
            if (self.groups['Server Request'] and
            select(self.get(IconListObject_88).IconListSelectionChanged()) and
            False):
                self.get(StringParser_43).set_value(self.get(ServerIPs_44).get_line(self.get(IconListObject_88).get_index()+1))
                self.get(StatusServer_45).set_value(self.get(StringParser_43).get_element(-1 + 1)+':'+self.get(StringParser_43).get_element(-1 + 2))
        pass
    
    def on_RichLinkClicked(self, instance):
        if type(instance) == ChatLog_87:
            self.set_event_id(95)
            if (self.groups['connecting'] and
            select(self.get(ChatLog_87).RichLinkClicked())):
                OpenURL('self.get(ChatLog_87).RichGetLinkText')
        pass
    
    def on_IconListOnDoubleClick(self, instance):
        if type(instance) == IconListObject_88:
            self.set_event_id(49)
            if (self.groups['Connect'] and
            select(self.get(IconListObject_88).IconListOnDoubleClick()) and
            self.get(IconListObject_88).get_index() >= 0 and
            self.get(StatusServer_45).text != 'Connecting...' and
            select(self.get(Options_89).values.get(0, 0) == 1)):
                self.get(StringParser_43).set_value(self.get(ServerIPs_44).get_line(self.get(IconListObject_88).get_index()+1))
                self.get(StatusServer_45).set_value('Connecting...')
                self.get(Ip_46).set_value(self.get(StringParser_43).get_element(-1 + 1))
                self.get(Port_47).set_value(self.get(StringParser_43).get_element(-1 + 2))
                self.get(HostAGame_51).values[0] = 0
                self.get(HostAGame_51).set_transparency(70)
                self.get(Connect2_49).set_transparency(70)
                self.get(Connect2_49).values[0] = 0
                self.get(GetServerList_50).set_transparency(70)
                self.get(GetServerList_50).values[0] = 0
                self.get(Connect2_49).restore_animation()
                self.stop_mod(0, 3000) # with fade
                self.set_frame(4)
                self.get(IconListObject_88).set_focus(False)
                self.get(Ctoip_92).values[0] = 0
                self.get(Ctoip_92).set_transparency(70)
        pass
    
    def on_EndOfApplication(self, instance):
        self.set_event_id(37)
        if (self.groups['Server Request'] and
        EndOfApplication()):
            self.get(MooSock2_57).disconnect()
        pass
    
    def on_EndOfFrame(self, instance):
        self.set_event_id(38)
        if (self.groups['Server Request'] and
        EndOfFrame()):
            self.get(MooSock2_57).disconnect()
        pass
    
    def update(self, dt):
        self.set_event_id(18)
        if (select(self.get(Control_54).get_value() == 0) and
        self.is_active() and
        negate(Qt.Key_Control in self.scene.key_downs) and
        self.is_window_visible() and
        select(negate(self.get(SubApplication_91).visible)) and
        select(negate(self.get(SubApplication2_93).visible))):
            self.get(TextInputBox_70).set_focus(True)
        if self.groups['Server Request']:
            self.set_event_id(25)
            if select(self.get(Timeout_41).get_value() == 0):
                self.get(Timeout_41).set_value(-1)
                self.get(StringParser2_67).set_value(self.get(Edit3_68).get_value())
                for loop_index in xrange(self.get(StringParser2_67).get_count()):
                    self.loop_indexes['Get Server'] = loop_index
                    if self.loop_get_server() == False: break
            self.set_event_id(26)
            if (self.every(1.0) and
            select(self.get(Timeout_41).get_value() > 0)):
                self.get(Timeout_41).subtract_value(1)
        if self.groups['Menu']:
            self.set_event_id(52)
            if (self.get(Connect2_49).mouse_over() and
            select(self.get(Connect2_49).values.get(0, 0) == 1)):
                self.get(Connect2_49).force_animation('User defined 1')
            self.set_event_id(53)
            if negate(self.get(Connect2_49).mouse_over()):
                self.get(Connect2_49).restore_animation()
            self.set_event_id(54)
            if (self.get(Ctoip_92).mouse_over() and
            select(self.get(Ctoip_92).values.get(0, 0) == 1)):
                self.get(Ctoip_92).force_animation('User defined 1')
            self.set_event_id(55)
            if negate(self.get(Ctoip_92).mouse_over()):
                self.get(Ctoip_92).restore_animation()
            self.set_event_id(56)
            if (self.get(GetServerList_50).mouse_over() and
            select(self.get(GetServerList_50).values.get(0, 0) == 1)):
                self.get(GetServerList_50).force_animation('User defined 1')
            self.set_event_id(57)
            if negate(self.get(GetServerList_50).mouse_over()):
                self.get(GetServerList_50).restore_animation()
            self.set_event_id(58)
            if (self.get(HostAGame_51).mouse_over() and
            select(self.get(HostAGame_51).values.get(0, 0) == 1)):
                self.get(HostAGame_51).force_animation('User defined 1')
            self.set_event_id(59)
            if negate(self.get(HostAGame_51).mouse_over()):
                self.get(HostAGame_51).restore_animation()
            self.set_event_id(60)
            if self.get(ExitGame_52).mouse_over():
                self.get(ExitGame_52).force_animation('User defined 1')
            self.set_event_id(61)
            if negate(self.get(ExitGame_52).mouse_over()):
                self.get(ExitGame_52).restore_animation()
            self.set_event_id(62)
            if (self.get(Options_89).mouse_over() and
            select(self.get(Options_89).values.get(0, 0) == 1)):
                self.get(Options_89).force_animation('User defined 1')
            self.set_event_id(63)
            if negate(self.get(Options_89).mouse_over()):
                self.get(Options_89).restore_animation()
            self.set_event_id(64)
            if (self.get(JoinChat_90).mouse_over() and
            select(self.get(JoinChat_90).values.get(0, 0) == 1)):
                self.get(JoinChat_90).force_animation('User defined 1')
            self.set_event_id(65)
            if negate(self.get(JoinChat_90).mouse_over()):
                self.get(JoinChat_90).restore_animation()
            self.set_event_id(66)
            if (self.get(IconListObject_88).get_index() >= 0 and
            self.not_always()):
                self.get(Connect2_49).values[0] = 1
                self.get(Connect2_49).set_transparency(0)
            self.set_event_id(67)
            if (self.get(IconListObject_88).get_index() < 0 and
            self.not_always()):
                self.get(Connect2_49).values[0] = 0
                self.get(Connect2_49).restore_animation()
                self.get(Connect2_49).set_transparency(70)
        if self.groups['preset']:
            self.set_event_id(71)
            if self.get(StringParse_74).get_value() != '':
                self.get(Log_69).set_value(self.get(Log_69).get_value()+'\r\n'+self.get(StringParse_74).get_value())
                self.get(Log_69).scroll_end()
                self.get(List_77).add_line(self.get(StringParse_74).get_value())
                self.get(List_77).scroll_end()
        if self.groups['connecting']:
            self.set_event_id(79)
            if (Qt.Key_Return in self.scene.key_presses and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(InputBoxModifier_71).set_value(self.get(TextInputBox_70).get_value())
                self.get(InputBoxHandler_76).set_value(self.get(InputBoxModifier_71).get_value())
                self.get(InputBoxModifier_71).set_value('')
            self.set_event_id(80)
            if (left_string(self.get(InputBoxHandler_76).get_value(), 1) == '*' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('PRIVMSG '+self.get(Channel1_36).text+' :\x01ACTION meant: '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1)+'\x01')
                self.get(ChatLog_87).set_color((0, 0, 244))
                self.get(ChatLog_87).set_text('\r\n'+'*** '+self.get(Nickname0_81).text+' meant: '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1))
                self.get(List_77).add_line('   '+'PRIVMSG '+self.get(Channel1_36).text+' :\x01ACTION meant: '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1)+'\x01')
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(81)
            if (left_string(self.get(InputBoxHandler_76).get_value(), 1) == '#' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('PRIVMSG '+self.get(Channel1_36).text+' :\x01ACTION whispers: '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1)+'\x01')
                self.get(ChatLog_87).set_color((0, 0, 244))
                self.get(ChatLog_87).set_text('\r\n'+'*** '+self.get(Nickname0_81).text+' whispers: '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1))
                self.get(List_77).add_line('   '+'PRIVMSG '+self.get(Channel1_36).text+' :\x01ACTION whispers: '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1)+'\x01')
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(82)
            if (self.get(InputBoxHandler_76).get_element(0) == '/nick' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('NICK :'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-6))
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * Changing nickname....')
                self.get(List_77).add_line('   '+'NICK :'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-6))
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(83)
            if (self.get(InputBoxHandler_76).get_element(0) == '/join' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((255, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * No multiple rooms implemented...')
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(84)
            if (self.get(InputBoxHandler_76).get_element(0) == '/time' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('PRIVMSG '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-6)+' :\x01TIME\x01')
                self.get(ChatLog_87).set_color((100, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'-->'+self.get(Nickname0_81).text+'>'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-6)+'> Time?')
                self.get(List_77).add_line('   '+'PRIVMSG '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-6)+' :\x01TIME\x01')
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(85)
            if (self.get(InputBoxHandler_76).get_element(0) == '/version' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('PRIVMSG '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-9)+' :\x01VERSION\x01')
                self.get(ChatLog_87).set_color((100, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'-->'+self.get(Nickname0_81).text+'>'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-9)+'> Version?')
                self.get(List_77).add_line('   '+'PRIVMSG '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-9)+' :\x01VERSION\x01')
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(86)
            if (self.get(InputBoxHandler_76).get_element(0) == '/pm' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StringParse_74).set_value(self.get(TextInputBox_70).get_value())
                self.get(MooSock_72).send_line('PRIVMSG '+self.get(StringParse_74).get_element(-1 + 2)+' :'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(InputBoxHandler_76).get_value())-len(self.get(InputBoxHandler_76).get_element(-1 + 2))-5))
                self.get(ChatLog_87).set_color((100, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'-->'+self.get(Nickname0_81).text+'>'+self.get(StringParse_74).get_element(-1 + 2)+'> '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(InputBoxHandler_76).get_value())-len(self.get(InputBoxHandler_76).get_element(-1 + 2))-5))
                self.get(List_77).add_line('   '+'PRIVMSG '+self.get(StringParse_74).get_element(-1 + 2)+' :'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(InputBoxHandler_76).get_value())-len(self.get(InputBoxHandler_76).get_element(-1 + 2))-5))
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(87)
            if (self.get(InputBoxHandler_76).get_element(0) == '/quit' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('QUIT :'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-6))
                self.get(ChatLog_87).set_color((125, 0, 125))
                self.get(ChatLog_87).set_text('\r\n'+'* Disconnected.')
                self.get(List_77).add_line('   '+'QUIT :'+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-6))
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
                self.get(UserList_78).reset()
            self.set_event_id(88)
            if (self.get(InputBoxHandler_76).get_element(0) == '/me' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('PRIVMSG '+self.get(Channel1_36).text+' :\x01ACTION '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-4)+'\x01')
                self.get(ChatLog_87).set_color((0, 0, 244))
                self.get(ChatLog_87).set_text('\r\n'+'*** '+self.get(Nickname0_81).text+' '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-4))
                self.get(List_77).add_line('   '+'PRIVMSG '+self.get(Channel1_36).text+' :\x01ACTION '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-4)+'\x01')
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(89)
            if (left_string(self.get(InputBoxHandler_76).get_value(), 1) == '/' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(MooSock_72).send_line(right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1))
                self.get(List_77).add_line('   '+right_string(self.get(TextInputBox_70).get_value(), len(self.get(TextInputBox_70).get_value())-1))
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(90)
            if (self.get(InputBoxHandler_76).get_value() != '' and
            select(self.get(TextInputBox_70).has_focus())):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('PRIVMSG '+self.get(Channel1_36).text+' :'+self.get(TextInputBox_70).get_value())
                self.get(ChatLog_87).set_color((0, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'<'+self.get(Nickname0_81).text+'> '+self.get(TextInputBox_70).get_value())
                self.get(List_77).add_line('   '+'PRIVMSG '+self.get(Channel1_36).text+' :'+self.get(TextInputBox_70).get_value())
                self.get(List_77).scroll_end()
                self.get(TextInputBox_70).set_value('')
                self.get(InputBoxHandler_76).set_value('')
            self.set_event_id(91)
            if (select(self.get(MooSock_72).is_connected()) and
            select(self.get(Flags_83).flags[3] == False) and
            select(self.get(MooSock_72).has_bytes()) and
            self.get(StringParse_74).get_element(-1 + 2) == '376'):
                self.get(MooSock_72).send_line('JOIN '+self.get(Channel1_36).text)
                self.get(List_77).add_line('   '+'JOIN '+self.get(Channel1_36).text)
                self.get(List_77).scroll_end()
                self.get(Flags_83).flags[3] = True
            self.set_event_id(92)
            if (select(self.get(MooSock_72).is_connected()) and
            select(self.get(Flags_83).flags[2] == False)):
                self.get(MooSock_72).send_line('NICK '+self.get(Nickname0_81).text)
                self.get(List_77).add_line('   '+'NICK '+self.get(Nickname0_81).text)
                self.get(List_77).scroll_end()
                self.get(Flags_83).flags[2] = True
                self.get(StringParse_74).set_value('')
            self.set_event_id(93)
            if (select(self.get(MooSock_72).is_connected()) and
            select(self.get(Flags_83).flags[1] == False)):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(MooSock_72).send_line('USER '+self.get(Nickname0_81).text+' '+'"bla.bla"'+' "'+self.get(Server2_82).text+'"'+' :'+self.get(Nickname0_81).text)
                self.get(List_77).add_line('   USER '+self.get(Nickname0_81).text+' '+'"bla.bla"'+' "'+self.get(Server2_82).text+'"'+' :'+self.get(Nickname0_81).text)
                self.get(List_77).scroll_end()
                self.get(Flags_83).flags[1] = True
                self.get(ChatLog_87).set_color((255, 0, 0))
                self.get(StringParse_74).set_value('')
            self.set_event_id(94)
            if self.get(StringParse_74).get_element(-1 + 2) == '372':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 0, 50))
                self.get(ChatLog_87).set_text('\r\n'+right_string(self.get(StringParse_74).get_value(), len(self.get(StringParse_74).get_value())-len(self.get(StringParse_74).get_element(-1 + 1))-len(self.get(StringParse_74).get_element(-1 + 2))-len(self.get(StringParse_74).get_element(-1 + 3))-5))
                self.get(StringParse_74).set_value('')
        if self.groups['receive']:
            self.set_event_id(98)
            if (self.get(StringParse_74).get_element(-1 + 3) == 'JOIN' and
            select(self.get(Flags_83).flags[10] == False)):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * You joined channel '+self.get(Channel1_36).text)
                self.get(StringParse_74).set_value('')
                self.get(Flags_83).flags[10] = True
            self.set_event_id(99)
            if self.get(StringParse_74).get_element(-1 + 1) == 'PING':
                self.get(MooSock_72).send_line('PONG :'+self.get(StringParse_74).get_element(-1 + 2))
                self.get(List_77).add_line('   PONG :'+self.get(StringParse_74).get_element(-1 + 2))
                self.get(List_77).scroll_end()
                self.get(StringParse_74).set_value('')
            self.set_event_id(100)
            if self.get(StringParse_74).get_element(-1 + 5) == '\x01ACTION':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 0, 244))
                self.get(String2_79).set_value(right_string(self.get(StringParse_74).get_value(), (len(self.get(StringParse_74).get_value())-len(self.get(StringParse_74).get_element(-1 + 1))-len(self.get(StringParse_74).get_element(-1 + 2))-len(self.get(StringParse_74).get_element(-1 + 3))-len(self.get(StringParse_74).get_element(-1 + 4))-len(self.get(StringParse_74).get_element(-1 + 5))-7)))
                self.get(ChatLog_87).set_text('\r\n'+'*** '+self.get(StringParse_74).get_element(-1 + 1)+' '+left_string(self.get(String2_79).text, len(self.get(String2_79).text)-1))
                self.get(StringParse_74).set_value('')
            self.set_event_id(101)
            if self.get(StringParse_74).get_element(-1 + 5) == '\x01VERSION\x01':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((150, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'*** '+self.get(StringParse_74).get_element(-1 + 1)+' [VERSION]')
                self.get(MooSock_72).send_line('NOTICE '+self.get(StringParse_74).get_element(-1 + 1)+' :\x01VERSION Crirc by Megagun\x01')
                self.get(List_77).add_line('   NOTICE '+self.get(StringParse_74).get_element(-1 + 1)+' :\x01VERSION Crirc by Megagun\x01')
                self.get(List_77).scroll_end()
                self.get(StringParse_74).set_value('')
            self.set_event_id(102)
            if self.get(StringParse_74).get_element(-1 + 5) == '\x01TIME\x01':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((150, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'*** '+self.get(StringParse_74).get_element(-1 + 1)+' [TIME]')
                self.get(MooSock_72).send_line('NOTICE '+self.get(StringParse_74).get_element(-1 + 1)+' :\x01TIME 99:99\x01')
                self.get(List_77).add_line('   NOTICE '+self.get(StringParse_74).get_element(-1 + 1)+' :\x01TIME 99:99\x01')
                self.get(List_77).scroll_end()
                self.get(StringParse_74).set_value('')
            self.set_event_id(103)
            if self.get(StringParse_74).get_element(-1 + 5) == '\x01PING':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((150, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'*** '+self.get(StringParse_74).get_element(-1 + 1)+' [PING]')
                self.get(MooSock_72).send_line('NOTICE '+self.get(StringParse_74).get_element(-1 + 1)+' :\x01PING '+left_string(self.get(StringParse_74).get_element(-1 + 6), len(self.get(StringParse_74).get_element(-1 + 6))-1)+'\x01')
                self.get(List_77).add_line('   NOTICE '+self.get(StringParse_74).get_element(-1 + 1)+' :\x01PING '+left_string(self.get(StringParse_74).get_element(-1 + 6), len(self.get(StringParse_74).get_element(-1 + 6))-1)+'\x01')
                self.get(List_77).scroll_end()
                self.get(StringParse_74).set_value('')
            self.set_event_id(104)
            if (self.get(StringParse_74).get_element(-1 + 3) == 'PRIVMSG' and
            self.get(StringParse_74).get_element(-1 + 4) != self.get(Nickname0_81).text):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'<'+self.get(StringParse_74).get_element(-1 + 1)+'> '+right_string(self.get(StringParse_74).get_value(), (len(self.get(StringParse_74).get_value())-len(self.get(StringParse_74).get_element(-1 + 1))-len(self.get(StringParse_74).get_element(-1 + 2))-len(self.get(StringParse_74).get_element(-1 + 3))-len(self.get(StringParse_74).get_element(-1 + 4))-6)))
                self.get(StringParse_74).set_value('')
            self.set_event_id(105)
            if (self.get(StringParse_74).get_element(-1 + 3) == 'PRIVMSG' and
            self.get(StringParse_74).get_element(-1 + 4) == self.get(Nickname0_81).text):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((100, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'-->'+self.get(StringParse_74).get_element(-1 + 1)+'> '+right_string(self.get(StringParse_74).get_value(), (len(self.get(StringParse_74).get_value())-len(self.get(StringParse_74).get_element(-1 + 1))-len(self.get(StringParse_74).get_element(-1 + 2))-len(self.get(StringParse_74).get_element(-1 + 3))-len(self.get(StringParse_74).get_element(-1 + 4))-6)))
                self.get(StringParse_74).set_value('')
            self.set_event_id(106)
            if self.get(StringParse_74).get_element(-1 + 3) == 'NOTICE':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((150, 0, 0))
                self.get(ChatLog_87).set_text('\r\n'+'--'+self.get(StringParse_74).get_element(-1 + 1)+'-- '+right_string(self.get(StringParse_74).get_value(), (len(self.get(StringParse_74).get_value())-len(self.get(StringParse_74).get_element(-1 + 1))-len(self.get(StringParse_74).get_element(-1 + 2))-len(self.get(StringParse_74).get_element(-1 + 3))-len(self.get(StringParse_74).get_element(-1 + 4))-6)))
                self.get(StringParse_74).set_value('')
            self.set_event_id(107)
            if self.get(StringParse_74).get_element(-1 + 3) == 'QUIT':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((125, 0, 125))
                self.get(ChatLog_87).set_text('\r\n'+' * '+self.get(StringParse_74).get_element(-1 + 1)+' has quit IRC. Reason: < '+right_string(self.get(StringParse_74).get_value(), (len(self.get(StringParse_74).get_value())-len(self.get(StringParse_74).get_element(-1 + 1))-len(self.get(StringParse_74).get_element(-1 + 2))-len(self.get(StringParse_74).get_element(-1 + 3))-5))+' >')
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact(self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('@'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('+'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(StringParse_74).set_value('')
            self.set_event_id(108)
            if self.get(StringParse_74).get_element(-1 + 3) == 'PART':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((125, 0, 125))
                self.get(ChatLog_87).set_text('\r\n'+' *'+self.get(StringParse_74).get_element(-1 + 1)+' has quit IRC.')
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact(self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('@'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('+'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(StringParse_74).set_value('')
            self.set_event_id(109)
            if (self.get(StringParse_74).get_element(-1 + 3) == 'JOIN' and
            select(self.get(Flags_83).flags[10] == True)):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * '+self.get(StringParse_74).get_element(-1 + 1)+' has joined!')
                self.get(UserList_78).add_line(self.get(StringParse_74).get_element(-1 + 1))
                self.get(StringParse_74).set_value('')
            self.set_event_id(110)
            if (self.get(StringParse_74).get_element(-1 + 3) == 'NICK' and
            self.get(StringParse_74).get_element(0) != self.get(Nickname0_81).text):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * '+self.get(StringParse_74).get_element(-1 + 1)+' has changed nickname to '+self.get(StringParse_74).get_element(-1 + 4))
                self.get(UserList_78).add_line(self.get(StringParse_74).get_element(-1 + 4))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact(self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('@'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('+'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(StringParse_74).set_value('')
            self.set_event_id(111)
            if (self.get(StringParse_74).get_element(-1 + 3) == 'NICK' and
            self.get(StringParse_74).get_element(0) == self.get(Nickname0_81).text):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * '+self.get(StringParse_74).get_element(-1 + 1)+' has changed nickname to '+self.get(StringParse_74).get_element(-1 + 4))
                self.get(UserList_78).add_line(self.get(StringParse_74).get_element(-1 + 4))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact(self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('@'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(UserList_78).delete_line(self.get(UserList_78).find_exact('+'+self.get(StringParse_74).get_element(-1 + 1), 0))
                self.get(Nickname0_81).set_value(self.get(StringParse_74).get_element(-1 + 4))
                self.get(StringParse_74).set_value('')
            self.set_event_id(112)
            if self.get(StringParse_74).get_element(-1 + 2) == '353':
                self.get(String3_80).set_value(self.get(String3_80).text+' '+right_string(self.get(StringParse_74).get_value(), (len(self.get(StringParse_74).get_value())-7-len(self.get(StringParse_74).get_element(-1 + 1))-len(self.get(StringParse_74).get_element(-1 + 2))-len(self.get(StringParse_74).get_element(-1 + 3))-len(self.get(StringParse_74).get_element(-1 + 4))-len(self.get(StringParse_74).get_element(-1 + 5)))))
                self.get(StringParse_74).set_value('')
            self.set_event_id(113)
            if self.get(StringParse_74).get_element(-1 + 2) == '366':
                self.get(StringParse_74).set_value('')
                self.get(Flags_83).flags[30] = True
            self.set_event_id(114)
            if self.get(StringParse_74).get_element(-1 + 2) == '332':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StingParserMotd_73).set_value(self.get(StringParse_74).get_value())
                self.get(ChatLog_87).set_color((0, 200, 0))
                self.get(ChatLog_87).set_text('\r\n'+" * Topic is '"+self.get(StingParserMotd_73).get_element(-1)+"'")
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(115)
            if self.get(StringParse_74).get_element(-1 + 2) == '433':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StingParserMotd_73).set_value(self.get(StringParse_74).get_value())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+" * Nickname error:'"+self.get(StingParserMotd_73).get_element(-1)+"'")
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(116)
            if self.get(StringParse_74).get_element(-1 + 2) == '474':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StingParserMotd_73).set_value(self.get(StringParse_74).get_value())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+" * Error:'"+self.get(StingParserMotd_73).get_element(-1)+"'")
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(117)
            if self.get(StringParse_74).get_element(-1 + 2) == '421':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StingParserMotd_73).set_value(self.get(StringParse_74).get_value())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+" * Error:'"+self.get(StingParserMotd_73).get_element(-1)+"'")
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(118)
            if self.get(StringParse_74).get_element(-1 + 2) == '432':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StingParserMotd_73).set_value(self.get(StringParse_74).get_value())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * Erroneous nickname!')
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(119)
            if self.get(StringParse_74).get_element(-1 + 2) == '437':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StingParserMotd_73).set_value(self.get(StringParse_74).get_value())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * Nickname/channel is temporarily unavailable!')
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(120)
            if self.get(StringParse_74).get_element(-1 + 2) == '451':
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(StingParserMotd_73).set_value(self.get(StringParse_74).get_value())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * You should register ( /nick <username> ) first!')
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(121)
            if (self.get(StringParse_74).get_element(-1 + 2) == '001' and
            self.get(StringParse_74).get_element(-1 + 3) != self.get(Nickname0_81).text):
                self.get(ChatLog_87).go_to_character(self.get(ChatLog_87).get_character_count())
                self.get(ChatLog_87).set_color((0, 255, 0))
                self.get(ChatLog_87).set_text('\r\n'+' * Nickname error. Nickname now is: '+self.get(StringParse_74).get_element(-1 + 3))
                self.get(Nickname0_81).set_value(self.get(StringParse_74).get_element(-1 + 3))
                self.get(StringParse_74).set_value('')
                self.get(StingParserMotd_73).set_value('')
            self.set_event_id(122)
            if self.get(StringParse_74).get_value() != '':
                self.get(StringParse_74).set_value('')
        if self.groups['userlist']:
            self.set_event_id(125)
            if (self.get(String3_80).text != '' and
            select(self.get(Flags_83).flags[30] == True)):
                self.get(Flags_83).flags[5] = True
                self.get(StringParser3_75).set_value(self.get(String3_80).text)
                self.get(String3_80).set_value('.')
                self.get(Flags_83).flags[30] = False
            self.set_event_id(126)
            if self.get(StringParser3_75).get_element(-1 + self.get(Counter_84).get_value()) != '':
                self.get(UserList_78).add_line(self.get(StringParser3_75).get_element(-1 + self.get(Counter_84).get_value()))
                self.get(Counter_84).add_value(1)
        if self.groups['Subapp']:
            self.set_event_id(129)
            if self.players[0].lives == 4:
                self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_55).set_group('Data')
                self.get(Counter5_66).set_value(self.get(Ini_55).get_value_item('MusicVolume'))
                self.set_mod_volume(0, self.get(Counter5_66).get_value())
                self.set_mod_volume(1, self.get(Counter5_66).get_value())
                self.set_mod_volume(2, self.get(Counter5_66).get_value())
                self.set_mod_volume(3, self.get(Counter5_66).get_value())
                self.set_mod_volume(4, self.get(Counter5_66).get_value())
            self.set_event_id(130)
            if (self.players[0].lives == 4 and
            self.get_global_value(12) == 0 and
            self.is_mod_playing(0)):
                self.stop_mod(0, 3000) # with fade
            self.set_event_id(131)
            if (self.players[0].lives == 4 and
            self.get_global_value(12) == 1 and
            negate(self.is_mod_playing(0))):
                self.cross_fade_mod(0, 0, 3000)
            self.set_event_id(132)
            if self.players[0].lives == 4:
                self.get(SubApplication_91).set_visible(False)
                self.players[0].lives = 3
                self.get(Options_89).set_transparency(0)
                self.get(Options_89).values[0] = 1
                self.get(Ctoip_92).set_transparency(0)
                self.get(Ctoip_92).values[0] = 1
            self.set_event_id(133)
            if self.players[0].lives == 5:
                self.get(SubApplication_91).set_visible(False)
                self.players[0].lives = 3
                self.get(Options_89).set_transparency(0)
                self.get(Options_89).values[0] = 1
                self.get(Ctoip_92).set_transparency(0)
                self.get(Ctoip_92).values[0] = 1
        if self.groups['Subapp2']:
            self.set_event_id(136)
            if self.players[0].lives == 6:
                self.players[0].lives = 3
                self.get(Ctoip_92).set_transparency(0)
                self.get(Ctoip_92).values[0] = 1
                self.get(Options_89).set_transparency(0)
                self.get(Options_89).values[0] = 1
                self.get(SubApplication2_93).set_visible(False)
            self.set_event_id(137)
            if self.players[0].lives == 7:
                self.players[0].lives = 3
                self.get(SubApplication2_93).set_visible(False)
                self.set_frame(4)
                self.get(Ip_46).set_value(self.get_global_string(0))
                self.get(Port_47).set_value(self.get_global_string(1))
        pass
    
