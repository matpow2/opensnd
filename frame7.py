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

class Frame7(Frame):
    name = 'Shut down'
    index = 6
    width = 800
    height = 600
    background = (0, 0, 0)
    
    def initialize(self):
        self.create_object(Newid_28, 146, -31)
        self.create_object(SvrKills_29, 215, -101)
        self.create_object(SvrDeaths_30, 213, -81)
        self.create_object(SvrPoints_31, 210, -62)
        self.create_object(SvrKills2_32, 266, -101)
        self.create_object(SvrDeaths2_33, 263, -79)
        self.create_object(SvrPoints2_34, 263, -60)
        self.create_object(MooSock_72, 384, -104)
        self.create_object(GlobalName_6, 146, -48)
        self.create_object(Edit_461, 426, -101)
        self.groups = {
        }
    
    def on_start(self):
        self.set_event_id(1)
        self.end_application()
        self.set_event_id(2)
        self.values[1] = 0
        self.hide_cursor()
        self.set_event_id(3)
        if select(self.get(SvrKills_29).get_value() != self.get(SvrKills2_32).get_value()):
            self.values[1] = 1
        self.set_event_id(4)
        if select(self.get(SvrDeaths_30).get_value() != self.get(SvrDeaths2_33).get_value()):
            self.values[1] = 1
        self.set_event_id(5)
        if select(self.get(SvrPoints_31).get_value() != self.get(SvrPoints2_34).get_value()):
            self.values[1] = 1
        self.set_event_id(6)
        if (self.get_global_value(1) == 1 and
        False):
            self.get(Edit_461).set_value('GET http://www.seekanddread.de/Server/svr_save.php?code='+str(randrange(9999))+'&uid='+self.get(Newid_28).text+'&name='+self.get(GlobalName_6).text+'&kills='+str(self.get(SvrKills2_32).get_value())+'&deaths='+str(self.get(SvrDeaths2_33).get_value())+'&points='+str(self.get(SvrPoints2_34).get_value()))
            self.get(Edit_461).set_value(self.get(Edit_461).get_value()+' HTTP/1.0'+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
            self.get(MooSock_72).connect('www.seekanddread.de', 80)
        self.set_event_id(7)
        if self.get_global_value(1) == 0:
            self.end_application()
        pass
    
    def on_sock_connect(self, instance):
        if type(instance) == MooSock_72:
            self.set_event_id(9)
            self.get(MooSock_72).send_text(self.get(Edit_461).get_value())
            self.get(MooSock_72).disconnect()
        pass
    
    def on_sock_disconnect(self, instance):
        if type(instance) == MooSock_72:
            self.set_event_id(10)
            self.end_application()
        pass
    
    def on_sock_connection(self, instance):
        if type(instance) == MooSock_72:
            self.set_event_id(8)
            self.get(MooSock_72).accept()
        pass
    
    def update(self, dt):
        pass
    
