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

qualifier_5 = (Obj1Weapon_308, Obj2Weapon_309, AmmoText_310, _313,
    Obj1WeaponList_314, Obj2WeaponList_315, PlOnlineText_316, Cash_364,
    _365, Score_367, HealthText_401, Obj1WeaponList_481, Skin_483)

class Frame8(Frame):
    name = 'Options'
    index = 7
    width = 300
    height = 350
    background = (255, 255, 255)
    
    def initialize(self):
        self.create_object(Options_492, 0, 0)
        self.create_object(Obj1_462, 19, 80)
        self.create_object(Up_463, 74, 80)
        self.create_object(Obj2_464, 19, 120)
        self.create_object(Obj3_465, 19, 100)
        self.create_object(Obj4_466, 19, 140)
        self.create_object(Down_467, 74, 120)
        self.create_object(Left_468, 74, 100)
        self.create_object(Right_469, 74, 140)
        self.create_object(Obj5_470, 155, 80)
        self.create_object(Obj6_471, 155, 100)
        self.create_object(Obj8_472, 155, 140)
        self.create_object(Obj9_473, 155, 160)
        self.create_object(Reload_474, 210, 80)
        self.create_object(Switch_475, 210, 100)
        self.create_object(Shoot_476, 210, 140)
        self.create_object(Shoot2_477, 210, 160)
        self.create_object(Counter4_56, 137, 255)
        self.create_object(Music2_478, 23, 200)
        self.create_object(Rain3_479, 23, 260)
        self.create_object(Rain5_480, 23, 240)
        self.create_object(Obj1WeaponList_481, 151, 220)
        self.create_object(WaeponString_482, 23, 220)
        self.create_object(Skin_483, 288, 220)
        self.create_object(Rain6_484, 158, 220)
        self.create_object(WaeponString2_485, 158, 200)
        self.create_object(Counter5_66, 279, 213)
        self.create_object(Active_486, 103, 266)
        self.create_object(Active2_487, 74, 200)
        self.create_object(Obj7_488, 155, 120)
        self.create_object(Head_489, 210, 120)
        self.create_object(Rain7_490, -92, 418)
        self.create_object(Score_491, 12, 414)
        self.create_object(String2_493, 17, 58)
        self.create_object(Ok_494, 150, 322)
        self.create_object(Control_54, -90, 180)
        self.create_object(Rain4_496, 23, 280)
        self.create_object(Active3_497, 80, 280)
        self.create_object(Ini_495, 268, 393)
        self.groups = {
            'Controls' : True,
        }
    
    def on_start(self):
        self.set_event_id(2)
        self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
        self.get(Ini_495).set_group('Data')
        self.get(Active2_487).set_direction(0)
        self.set_event_id(3)
        self.get(Counter4_56).set_value(self.get(Ini_495).get_value_item('Turning'))
        self.values[0] = 0
        self.values[1] = 0
        self.values[2] = 0
        self.values[15] = 0
        self.values[5] = 0
        self.values[4] = 0
        self.values[8] = 0
        self.values[9] = 0
        self.values[13] = self.get(Ini_495).get_value_item('Turning')
        self.get(Counter5_66).set_value(self.get(Ini_495).get_value_item('MusicVolume'))
        self.values[6] = 0
        self.set_event_id(4)
        if self.players[1].lives == 1:
            self.get(Active3_497).set_direction(8)
        self.set_event_id(5)
        if self.get_global_value(12) == 2:
            self.get(Active2_487).set_direction(8)
        self.set_event_id(6)
        if self.get_global_value(12) == 1:
            self.get(Active2_487).set_direction(8)
        self.set_event_id(7)
        if (self.get(Ini_495).get_value_item('Skin') != 0 and
        self.get(Ini_495).get_value_item('Skin') != 1 and
        self.get(Ini_495).get_value_item('Skin') != 2):
            self.values[4] = 0
            self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_495).set_group('Data')
            self.get(Ini_495).set_item_value('Startweapon', 0)
            self.get(Skin_483).set_direction(0)
        self.set_event_id(8)
        if self.get(Ini_495).get_value_item('Skin') == 0:
            self.get(Skin_483).set_direction(0)
            self.values[4] = 0
        self.set_event_id(9)
        if self.get(Ini_495).get_value_item('Skin') == 1:
            self.get(Skin_483).set_direction(24)
            self.values[4] = 1
        self.set_event_id(10)
        if self.get(Ini_495).get_value_item('Skin') == 2:
            self.get(Skin_483).set_direction(16)
            self.values[4] = 2
        self.set_event_id(11)
        if (self.get(Ini_495).get_value_item('Startweapon') != 0 and
        self.get(Ini_495).get_value_item('Startweapon') != 1):
            self.values[9] = 0
            self.get(Obj1WeaponList_481).set_direction(0)
            self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_495).set_group('Data')
            self.get(Ini_495).set_item_value('Startweapon', 0)
        self.set_event_id(12)
        if self.get(Ini_495).get_value_item('Startweapon') == 0:
            self.values[9] = 0
            self.get(Obj1WeaponList_481).set_direction(0)
        self.set_event_id(13)
        if self.get(Ini_495).get_value_item('Startweapon') == 1:
            self.values[9] = 1
            self.get(Obj1WeaponList_481).set_direction(24)
        self.set_event_id(14)
        if self.get(Ini_495).get_value_item('Graphics') == 1:
            self.values[6] = 1
            self.get(Active_486).set_direction(24)
        self.set_event_id(15)
        if self.get(Ini_495).get_value_item('Graphics') == 2:
            self.values[6] = 2
            self.get(Active_486).set_direction(16)
        self.set_event_id(16)
        if self.get(Ini_495).get_value_item('Graphics') == 3:
            self.values[6] = 3
            self.get(Active_486).set_direction(8)
        self.set_event_id(17)
        if select(self.get(Counter4_56).get_value() < 1):
            self.get(Counter4_56).set_value(25)
            self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_495).set_group('Data')
            self.get(Ini_495).set_item_value('Turning', self.get(Counter4_56).get_value())
            self.values[13] = self.get(Counter4_56).get_value()
        self.set_event_id(18)
        if select(self.get(Counter4_56).get_value() > 99):
            self.get(Counter4_56).set_value(25)
            self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
            self.get(Ini_495).set_group('Data')
            self.get(Ini_495).set_item_value('Turning', self.get(Counter4_56).get_value())
            self.values[13] = self.get(Counter4_56).get_value()
        self.set_event_id(19)
        self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
        self.get(Ini_495).set_group('Data')
        self.get(Up_463).set_text(self.get(Ini_495).get_string_item('Up'))
        self.get(Down_467).set_text(self.get(Ini_495).get_string_item('Down'))
        self.get(Left_468).set_text(self.get(Ini_495).get_string_item('Left'))
        self.get(Right_469).set_text(self.get(Ini_495).get_string_item('Right'))
        self.get(Reload_474).set_text(self.get(Ini_495).get_string_item('Reload'))
        self.get(Switch_475).set_text(self.get(Ini_495).get_string_item('Switch'))
        self.get(Head_489).set_text(self.get(Ini_495).get_string_item('AimH'))
        pass
    
    def on_mouse_press(self, x, y, button):
        if self.get(Active3_497).is_over(x, y):
            self.set_event_id(57)
            if (self.groups['Controls'] and
            self.players[1].lives == 0 and
            select(self.get(Active3_497).values.get(0, 0) == 0)):
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Footsteps', 1)
                self.players[1].lives = 1
                self.get(Active3_497).set_direction(8)
                self.get(Active3_497).values[0] = 2
            self.set_event_id(58)
            if (self.groups['Controls'] and
            self.players[1].lives == 1 and
            select(self.get(Active3_497).values.get(0, 0) == 0)):
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Footsteps', 0)
                self.players[1].lives = 0
                self.get(Active3_497).set_direction(0)
                self.get(Active3_497).values[0] = 2
        if self.get(Obj1WeaponList_481).is_over(x, y):
            self.set_event_id(24)
            if (self.groups['Controls'] and
            self.get_global_value(9) == 0):
                self.values[9] = 2
            self.set_event_id(26)
            if (self.groups['Controls'] and
            self.get_global_value(9) == 1):
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Startweapon', 0)
                self.get(Obj1WeaponList_481).set_direction(0)
                self.values[9] = 0
        if self.get(Skin_483).is_over(x, y):
            self.set_event_id(52)
            if (self.groups['Controls'] and
            self.get_global_value(4) == 2):
                self.values[4] = 3
            self.set_event_id(53)
            if (self.groups['Controls'] and
            self.get_global_value(4) == 1):
                self.values[4] = 2
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Skin', 2)
                self.get(Skin_483).set_direction(16)
            self.set_event_id(54)
            if (self.groups['Controls'] and
            self.get_global_value(4) == 0):
                self.values[4] = 1
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Skin', 1)
                self.get(Skin_483).set_direction(24)
        if self.get(Active_486).is_over(x, y):
            self.set_event_id(43)
            if (self.groups['Controls'] and
            select(self.get(Active_486).direction_value == 8)):
                self.values[6] = 4
            self.set_event_id(44)
            if (self.groups['Controls'] and
            select(self.get(Active_486).direction_value == 16)):
                self.values[6] = 3
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Graphics', self.get_global_value(6))
                self.get(Active_486).set_direction(8)
            self.set_event_id(45)
            if (self.groups['Controls'] and
            select(self.get(Active_486).direction_value == 24)):
                self.values[6] = 2
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Graphics', self.get_global_value(6))
                self.get(Active_486).set_direction(16)
            self.set_event_id(46)
            if (self.groups['Controls'] and
            select(self.get(Active_486).direction_value == 0)):
                self.values[6] = 1
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Graphics', self.get_global_value(6))
                self.get(Active_486).set_direction(24)
        if self.get(Active2_487).is_over(x, y):
            self.set_event_id(41)
            if (self.groups['Controls'] and
            self.get_global_value(12) == 0 and
            select(self.get(Active2_487).values.get(0, 0) == 0)):
                self.values[12] = 1
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Music', self.get_global_value(12))
                self.get(Active2_487).set_direction(8)
                self.get(Active2_487).values[0] = 2
            self.set_event_id(42)
            if (self.groups['Controls'] and
            self.get_global_value(12) == 1 and
            select(self.get(Active2_487).values.get(0, 0) == 0)):
                self.values[12] = 0
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Music', self.get_global_value(12))
                self.get(Active2_487).set_direction(0)
                self.get(Active2_487).values[0] = 2
        if button == Qt.LeftButton:
            self.set_event_id(22)
            if self.get(Ok_494).mouse_over():
                self.players[0].lives = 4
        pass
    
    def on_box_click(self, instance):
        if type(instance) == Obj1_462:
            self.set_event_id(27)
            if (self.groups['Controls'] and
            select(self.get(Control_54).get_value() == 0)):
                self.get(Up_463).set_text('Press a key')
                self.get(Control_54).set_value(1)
        if type(instance) == Obj2_464:
            self.set_event_id(28)
            if (self.groups['Controls'] and
            select(self.get(Control_54).get_value() == 0)):
                self.get(Control_54).set_value(2)
                self.get(Down_467).set_text('Press a key')
        if type(instance) == Obj3_465:
            self.set_event_id(29)
            if (self.groups['Controls'] and
            select(self.get(Control_54).get_value() == 0)):
                self.get(Control_54).set_value(3)
                self.get(Left_468).set_text('Press a key')
        if type(instance) == Obj4_466:
            self.set_event_id(30)
            if (self.groups['Controls'] and
            select(self.get(Control_54).get_value() == 0)):
                self.get(Control_54).set_value(4)
                self.get(Right_469).set_text('Press a key')
        if type(instance) == Obj5_470:
            self.set_event_id(31)
            if (self.groups['Controls'] and
            select(self.get(Control_54).get_value() == 0)):
                self.get(Control_54).set_value(5)
                self.get(Reload_474).set_text('Press a key')
        if type(instance) == Obj6_471:
            self.set_event_id(32)
            if (self.groups['Controls'] and
            select(self.get(Control_54).get_value() == 0)):
                self.get(Control_54).set_value(6)
                self.get(Switch_475).set_text('Press a key')
        if type(instance) == Obj7_488:
            self.set_event_id(33)
            if (self.groups['Controls'] and
            select(self.get(Control_54).get_value() == 0)):
                self.get(Control_54).set_value(7)
                self.get(Head_489).set_text('Press a key')
        pass
    
    def update(self, dt):
        self.set_event_id(1)
        if True:
            self.get(Score_491).set_value(str(self.get_global_value(3))+' / '+str(self.get_global_value(14))+' / '+str(self.get_global_value(15)))
        self.set_event_id(20)
        if self.get(Ok_494).mouse_over():
            self.get(Ok_494).force_animation('User defined 1')
        self.set_event_id(21)
        if negate(self.get(Ok_494).mouse_over()):
            self.get(Ok_494).restore_animation()
        if self.groups['Controls']:
            self.set_event_id(25)
            if (self.get_global_value(9) == 2 and
            self.not_always()):
                self.values[9] = 1
                self.get(Obj1WeaponList_481).set_direction(24)
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Startweapon', 1)
            self.set_event_id(34)
            if (len(self.scene.key_downs) > 1 and
            select(self.get(Control_54).get_value() == 1)):
                self.get(Up_463).set_text(key_string(self.scene.key_downs[-1]))
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_string('Up', self.get(Up_463).get_text())
                self.get(Control_54).set_value(0)
            self.set_event_id(35)
            if (len(self.scene.key_downs) > 1 and
            select(self.get(Control_54).get_value() == 2)):
                self.get(Down_467).set_text(key_string(self.scene.key_downs[-1]))
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_string('Down', self.get(Down_467).get_text())
                self.get(Control_54).set_value(0)
            self.set_event_id(36)
            if (len(self.scene.key_downs) > 1 and
            select(self.get(Control_54).get_value() == 3)):
                self.get(Left_468).set_text(key_string(self.scene.key_downs[-1]))
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_string('Left', self.get(Left_468).get_text())
                self.get(Control_54).set_value(0)
            self.set_event_id(37)
            if (len(self.scene.key_downs) > 1 and
            select(self.get(Control_54).get_value() == 4)):
                self.get(Right_469).set_text(key_string(self.scene.key_downs[-1]))
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_string('Right', self.get(Right_469).get_text())
                self.get(Control_54).set_value(0)
            self.set_event_id(38)
            if (len(self.scene.key_downs) > 1 and
            select(self.get(Control_54).get_value() == 5)):
                self.get(Reload_474).set_text(key_string(self.scene.key_downs[-1]))
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_string('Reload', self.get(Reload_474).get_text())
                self.get(Control_54).set_value(0)
            self.set_event_id(39)
            if (len(self.scene.key_downs) > 1 and
            select(self.get(Control_54).get_value() == 6)):
                self.get(Switch_475).set_text(key_string(self.scene.key_downs[-1]))
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_string('Switch', self.get(Switch_475).get_text())
                self.get(Control_54).set_value(0)
            self.set_event_id(40)
            if (len(self.scene.key_downs) > 1 and
            select(self.get(Control_54).get_value() == 7)):
                self.get(Head_489).set_text(key_string(self.scene.key_downs[-1]))
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_string('AimH', self.get(Head_489).get_text())
                self.get(Control_54).set_value(0)
            self.set_event_id(47)
            if self.get_global_value(6) == 4:
                self.values[6] = 0
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Graphics', self.get_global_value(6))
                self.get(Active_486).set_direction(0)
            self.set_event_id(48)
            if (Qt.LeftButton in self.scene.mouse_downs
             and
            self.mouse_in_zone((106, 239, 136, 256)) and
            self.restrict_for(0.1)):
                self.get(Counter4_56).add_value(1)
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Turning', self.get(Counter4_56).get_value())
                self.values[13] = self.get(Counter4_56).get_value()
            self.set_event_id(49)
            if (Qt.RightButton in self.scene.mouse_downs
             and
            self.mouse_in_zone((106, 239, 136, 256)) and
            self.restrict_for(0.1)):
                self.get(Counter4_56).subtract_value(1)
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Turning', self.get(Counter4_56).get_value())
                self.values[13] = self.get(Counter4_56).get_value()
            self.set_event_id(50)
            if (Qt.LeftButton in self.scene.mouse_downs
             and
            self.mouse_in_zone((235, 198, 279, 215))):
                self.get(Counter5_66).add_value(1)
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('MusicVolume', self.get(Counter5_66).get_value())
            self.set_event_id(51)
            if (Qt.RightButton in self.scene.mouse_downs
             and
            self.mouse_in_zone((235, 198, 279, 215))):
                self.get(Counter5_66).subtract_value(1)
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('MusicVolume', self.get(Counter5_66).get_value())
            self.set_event_id(55)
            if (self.get_global_value(4) == 3 and
            self.not_always()):
                self.values[4] = 0
                self.get(Ini_495).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
                self.get(Ini_495).set_group('Data')
                self.get(Ini_495).set_item_value('Skin', 0)
                self.get(Skin_483).set_direction(0)
            self.set_event_id(56)
            if select(self.get(Active2_487).values.get(0, 0) > 0):
                self.get(Active2_487).values[0] -= 1
            self.set_event_id(59)
            if select(self.get(Active3_497).values.get(0, 0) > 0):
                self.get(Active3_497).values[0] -= 1
        pass
    
