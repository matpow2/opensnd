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

class Frame1(Frame):
    name = 'Logo'
    index = 0
    width = 800
    height = 600
    background = (0, 0, 0)
    
    def initialize(self):
        self.create_object(Object3, 143, 86)
        self.create_object(String2_2, -172, 623)
        self.add_timed_call(self.on_timer_1, 0.5)
        self.add_timed_call(self.on_timer_2, 3.0)
        self.groups = {
        }
    
    def on_start(self):
        self.set_event_id(1)
        self.hide_cursor()
        self.set_event_id(2)
        if negate(os.path.isfile('data.ini')):
            open('data.ini', "wb").close()
            fp = open('data.ini', "ab")
            fp.write(self.get(String2_2).text)
            fp.close()
        pass
    
    def on_timer_1(self):
        self.set_event_id(3)
        self.load_mod('title.mod', 0, 0)
        self.load_mod('game1.mod', 1, 1)
        self.load_mod('game2.mod', 2, 2)
        self.load_mod('game3.mod', 3, 3)
        self.load_mod('game4.mod', 4, 4)
        pass
    
    def on_timer_2(self):
        self.set_event_id(4)
        self.next_frame()
        pass
    
    def update(self, dt):
        pass
    
