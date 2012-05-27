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

class Frame9(Frame):
    name = 'Connect to IP'
    index = 8
    width = 300
    height = 250
    background = (255, 255, 255)
    
    def initialize(self):
        self.create_object(Connect_498, 0, 0)
        self.create_object(Ok_494, 150, 219)
        self.create_object(Rain5_499, 42, 115)
        self.create_object(Rain6_500, 42, 166)
        self.create_object(JoinIp_501, 70, 112)
        self.create_object(JoinPort_502, 70, 163)
        self.groups = {
        }
    
    def on_start(self):
        self.set_event_id(6)
        self.get(JoinPort_502).set_value('1203')
        pass
    
    def on_mouse_press(self, x, y, button):
        if button == Qt.LeftButton:
            self.set_event_id(3)
            if (self.get(Ok_494).mouse_over() and
            len(self.get(JoinIp_501).get_value()) > 0 and
            self.get(JoinPort_502).get_number() > 0):
                self.strings[0] = self.get(JoinIp_501).get_value()
                self.strings[1] = self.get(JoinPort_502).get_value()
            self.set_event_id(4)
            if (self.get(Ok_494).mouse_over() and
            len(self.get(JoinIp_501).get_value()) > 0 and
            self.get(JoinPort_502).get_number() > 0):
                self.players[0].lives = 7
            self.set_event_id(5)
            if (self.get(Ok_494).mouse_over() and
            self.players[0].lives != 7):
                self.players[0].lives = 6
        pass
    
    def update(self, dt):
        self.set_event_id(1)
        if self.get(Ok_494).mouse_over():
            self.get(Ok_494).force_animation('User defined 1')
        self.set_event_id(2)
        if negate(self.get(Ok_494).mouse_over()):
            self.get(Ok_494).restore_animation()
        pass
    
