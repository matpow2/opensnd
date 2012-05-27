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

class FrameProxy(object):
    def __init__(self, name, module = None):
        if module is None:
            module = name.lower()
        self.name = name
        self.module = module

    def __call__(self, *arg, **kw):
        return getattr(__import__(self.module), self.name)(*arg, **kw)

def get_frame(index):
    return FrameProxy('Frame%s' % (index + 1))

NAME = 'Seek & Dread Online'
COPYRIGHT = None
ABOUT = None
AUTHOR = 'Martin Ossowski'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BORDER_COLOR = (255, 255, 255)
START_LIVES = 4294967292L

FRAMES = [get_frame(i) for i in xrange(9)]
