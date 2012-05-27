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

import os
import sys
import time
import binascii
import random
import glob
import string
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtNetwork import QTcpSocket, QAbstractSocket
from ConfigParser import Error as ConfigError, RawConfigParser
from Crypto.Cipher import Blowfish
import urllib
import functools
import itertools
import operator
import zlib
from collections import defaultdict

if sys.platform == "win32":
    get_time = time.clock
else:
    get_time = time.time

def get_alpha(transparency):
    return 1.0 - transparency / 128.0

class Font(object):
    font = None
    def __init__(self, face, size, bold, italic, underline):
        self.face = face
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
    
    def load(self):
        if self.font is None:
            if self.bold:
                weight = QFont.Weight.Bold
            else:
                weight = QFont.Weight.Normal
            self.font = QFont(self.face, self.size, weight,
                self.italic)
            self.font.setUnderline(self.underline)
        return self.font

class Sound(object):
    def __init__(self, name):
        self.name = name

class Sprite(object):
    x = y = 0
    alpha = 1.0
    def __init__(self, image, pixmap, hotspot_x, hotspot_y):
        self.image = image
        self.pixmap = pixmap
        self.hotspot_x = hotspot_x
        self.hotspot_y = hotspot_y
    
    def set_position(self, x, y):
        self.x, self.y = x, y
        
    @property
    def width(self):
        return self.pixmap.width()

    @property
    def height(self):
        return self.pixmap.height()
    
    def copy(self):
        sprite = Sprite(self.image, self.pixmap, self.hotspot_x, self.hotspot_y)
        sprite.x = self.x
        sprite.y = self.y
        sprite.alpha = self.alpha
        return sprite

    def draw(self, painter):
        painter.save()
        painter.setOpacity(self.alpha)
        painter.translate(-self.hotspot_x, -self.hotspot_y)
        painter.drawPixmap(self.x, self.y, self.pixmap)
        painter.restore()
        
class Image(object):
    pixmap = None
    def __init__(self, name, hotspot_x, hotspot_y, action_x, action_y):
        self.name = name
        self.hotspot_x = hotspot_x
        self.hotspot_y = hotspot_y
        self.action_x = action_x
        self.action_y = action_y
    
    def load_icons(self, size):
        self.load_pixmap()
        icons = []
        for i in xrange(self.pixmap.width() / size):
            pixmap = self.pixmap.copy(i * size, 0, size, size)
            icon = QIcon(pixmap)
            icons.append(icon)
        return icons
    
    def load_pixmap(self):
        if self.pixmap is None:
            self.pixmap = QPixmap(os.path.join('images', self.name + '.png'))
        return self.pixmap
    
    def load(self, hotspot_x = None, hotspot_y = None):
        self.load_pixmap()
        if hotspot_x is None:
            hotspot_x = self.hotspot_x
        if hotspot_y is None:
            hotspot_y = self.hotspot_y
        return Sprite(self, self.pixmap, hotspot_x, hotspot_y)

def collides(a_x1, a_y1, a_x2, a_y2, b_x1, b_y1, b_x2, b_y2):
    if a_x2 <= b_x1 or a_y2 <= b_y1 or a_x1 >= b_x2 or a_y1 >= b_y2:
        return False
    return True

class CollisionBase(object):
    pass
    
class SpriteCollision(CollisionBase):
    def __init__(self, sprite):
        self.sprite = sprite
    
    def collides(self, ax1, ay1, ax2, ay2):
        sprite = self.sprite
        pixmap = sprite.pixmap
        x1 = sprite.x - sprite.hotspot_x
        y1 = sprite.y - sprite.hotspot_y
        x2 = x1 + sprite.width
        y2 = y1 + sprite.height
        return collides(x1, y1, x2, y2, ax1, ay1, ax2, ay2)

class BoundingBox(CollisionBase):
    def __init__(self, instance):
        self.instance = instance
    
    def collides(self, ax1, ay1, ax2, ay2):
        instance = self.instance
        if instance.width is None or instance.height is None:
            return False
        x1 = instance.x
        y1 = instance.y
        x2 = x1 + instance.width
        y2 = y1 + instance.height
        return collides(x1, y1, x2, y2, ax1, ay1, ax2, ay2)

class ObjectType(object):
    width = height = None
    x = y = 0
    collision = None
    visible = True
    is_global = False
    movement_class = None

    def __init__(self, parent):
        self.frame = parent
        self.scene = parent.scene
        self.values = {}
        self.flags = [False for _ in xrange(32)]
        self.initialize()
        if self.movement_class is not None:
            self.movement = self.movement_class(self)
    
    def set_position(self, x = None, y = None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        self.update_position()
    
    def update_position(self):
        pass
    
    def update_visible(self):
        pass
    
    def initialize(self):
        pass
    
    def update(self, dt):
        pass
    
    def draw(self, painter):
        pass
    
    def in_zone(self, (x1, y1, x2, y2)):
        return self.get_collision().collides(x1, y1, x2, y2)

    def is_over(self, x, y):
        return self.get_collision().collides(x, y, x, y)
    
    def mouse_over(self):
        return self.is_over(*self.scene.get_mouse_position())
    
    def get_collision(self):
        if self.collision is None:
            self.collision = BoundingBox(self)
        return self.collision
    
    def destroy(self):
        frame = self.frame
        frame.instances.remove(self)
        frame.object_types[type(self)].remove(self)
        self.on_destroy()

    def on_destroy(self):
        pass
    
    def set_visible(self, value):
        self.visible = value
        self.update_visible()

    def get_flag(self, index):
        return self.flags[index]
    
    @classmethod
    def get_storage(cls, *arg, **kw):
        if not hasattr(cls, 'global_data'):
            cls.global_data = {}
        return cls.global_data

class Text(ObjectType):
    def initialize(self):
        self.font = self.font.load()
        if self.is_global:
            self.text = self.get_storage().get('text', self.text)
    
    def set_color(self, value):
        self.color = value
    
    def draw(self, painter):
        painter.setPen(QColor(*self.color))
        painter.setFont(self.font)
        painter.drawText(QRect(self.x, self.y, self.width, self.height), 
            self.alignment, self.text)
    
    def set_value(self, value):
        self.text = value
    
    def on_destroy(self):
        if self.is_global:
            self.get_storage()['text'] = self.text

class Active(ObjectType):
    direction_value = 0
    frame_value = 0
    animation_value = None
    current_animation = None 
    original_animation = None
    current_direction = None
    current_frame = None
    sprite = None
    alpha = 1.0

    def initialize(self):
        self.set_animation('Stopped')
    
    def set_animation(self, name):
        self.animation_value = name
        try:
            self.current_animation = self.animations[name]
        except KeyError:
            self.current_animation = self.animations.values()[0]
        self.set_direction(self.direction_value)
    
    def force_animation(self, name):
        if self.original_animation is None:
            self.original_animation = self.animation_value
        self.set_animation(name)
    
    def restore_animation(self):
        self.set_animation(self.original_animation or 'Stopped')
        self.original_animation = None
    
    def set_direction(self, value):
        try:
            self.current_direction = self.current_animation[value]
        except KeyError:
            return
        self.direction_value = value
        self.set_frame(self.frame_value)
    
    def set_transparency(self, value):
        self.alpha = get_alpha(value)
        self.sprite.alpha = self.alpha
    
    def set_frame(self, value):
        self.frame_value = value
        self.current_frame = self.current_direction['frames'][value]
        self.sprite = self.current_frame.load()
        self.sprite.alpha = self.alpha
        self.collision = SpriteCollision(self.sprite)
        self.update_position()
    
    def update_position(self):
        if self.sprite is None:
            return
        self.sprite.set_position(self.x, self.y)
    
    def draw(self, painter):
        if self.sprite is None:
            return
        self.sprite.draw(painter)
    
    def get_collision(self):
        return self.collision

    def add_backdrop(self):
        self.frame.paste(self.sprite)

class Backdrop(ObjectType):
    def initialize(self):
        self.sprite = self.image.load(hotspot_x = 0, hotspot_y = 0)
    
    def update_position(self):
        self.sprite.set_position(self.x, self.y)
    
    def draw(self, painter):
        self.sprite.draw(painter)

class Counter(ObjectType):
    frames = None
    def initialize(self):
        self.set_value(self.initial)
    
    def set_value(self, value):
        self.current = max(self.minimum, min(self.maximum, value))
        if self.frames is None:
            return
        self.display = [self.frames[c].load_pixmap() for c in str(self.current)]

    def set_maximum(self, value):
        self.maximum = value
        self.set_value(self.current)

    def set_minimum(self, value):
        self.minimum = value
        self.set_value(self.current)
    
    def subtract_value(self, value):
        self.set_value(self.current - value)
        
    def add_value(self, value):
        self.set_value(self.current + value)
    
    def get_value(self):
        return self.current
    
    def draw(self, painter):
        if self.frames is None:
            return
        x = self.x
        y = self.y
        for frame in reversed(self.display):
            x -= frame.width()
            painter.drawPixmap(x, y - frame.height(), frame)

class ActivePicture(ObjectType):
    pixmap = None
    def initialize(self):
        if self.filename:
            self.set_filename(self.filename)
        
    def set_filename(self, value):
        self.filename = value
        self.pixmap = QPixmap(value)
    
    def draw(self, painter):
        if self.pixmap is None:
            return
        painter.drawPixmap(self.x, self.y, self.pixmap)

class StringParser(ObjectType):
    value = ''
    def initialize(self):
        self.delimiters = []
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def add_delimiter(self, value):
        self.delimiters.append(value)
    
    def load_filename(self, value):
        try:
            fp = open(value, 'rb')
        except (OSError, IOError):
            return
        self.value = fp.read()
        fp.close()
    
    def clear_delimiters(self):
        self.delimiters = []
    
    def get_count(self):
        return len(self.split())
    
    def get_element(self, index):
        try:
            return self.split()[index]
        except IndexError:
            return ''
    
    def get_last_element(self):
        return self.get_element(-1)
    
    def split(self):
        seps = self.delimiters
        res = [self.value]
        for sep in seps:
            s, res = res, []
            for seq in s:
                res += [item for item in seq.split(sep) if item]
        return res

class BinaryObject(ObjectType):
    data = ''

    def replace(self, a, b):
        self.data = self.data.replace(a, b)
    
    def insert(self, a, index):
        self.data = self.data[:index] + a + self.data[index:]
    
    def get_string(self, index, size):
        return self.data[index:index+size]
    
    def get_size(self):
        return len(self.data)
    
    def decode_base64(self):
        try:
            self.data = self.data.decode('base64')
        except binascii.Error:
            self.data = ''
    
    def clear(self):
        self.data = ''

class Edit(ObjectType):
    def initialize(self):
        self.font = self.font.load()
        self.edit = QLineEdit()
        self.edit.setFrame(self.border)
        self.edit.setFixedSize(self.width, self.height)
        self.edit.setFont(self.font)
        palette = self.edit.palette()
        if self.transparent:
            color = Qt.transparent
            self.edit.setAutoFillBackground(False)
        else:
            color = QColor(*self.background)
        palette.setColor(self.edit.backgroundRole(), color)
        palette.setColor(QPalette.Window, color)
        palette.setColor(self.edit.foregroundRole(), QColor(*self.foreground))
        self.edit.setPalette(palette)
        self.item = self.frame.add_widget(self.edit)
        if not self.visible:
            self.edit.setVisible(False)
    
    def get_value(self):
        return self.edit.text()
    
    def set_read_only(self, value):
        self.edit.setReadOnly(value)
    
    def load_file(self, filename):
        self.set_value(open(filename, 'rb').read())
    
    def set_value(self, value):
        self.edit.setText(value)
    
    def has_focus(self):
        return self.edit.hasFocus()
    
    def set_focus(self, value):
        return
        if value == self.has_focus():
            return
        if value:
            self.edit.setFocus()
        else:
            self.edit.clearFocus()

    def is_number(self):
        try:
            self.get_number(True)
            return True
        except ValueError:
            return False

    def get_number(self, exceptions = False):
        return to_number(self.get_value(), exceptions)
    
    def scroll_end(self):
        return
    
    def limit_size(self, size):
        self.edit.setMaxLength(size)
    
    def update_position(self):
        self.item.setPos(self.x, self.y)

    def disable(self):
        self.edit.setDisabled(True)

    def enable(self):
        self.edit.setDisabled(False)

    def is_modified(self):
        return self.edit.isModified()

    def on_destroy(self):
        self.edit.destroy()
        self.item.close()

class DisabledFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() in (QEvent.MouseButtonDblClick, 
                            QEvent.MouseButtonPress,
                            QEvent.MouseButtonRelease,
                            QEvent.MouseMove,
                            QEvent.KeyPress,
                            QEvent.KeyRelease):
            return True
        else:
            return QObject.eventFilter(self, obj, event)

class ActiveBox(ObjectType):
    text = None
    disabled = False
    def initialize(self):
        font = self.font.load()
        self.widget = QPushButton(self.text or '')
        self.widget.setFont(font)
        self.widget.setFixedSize(self.width, self.height)
        if self.disabled:
            self.filter = DisabledFilter()
            self.widget.installEventFilter(self.filter)
        if self.fill is not None:
            self.widget.setPalette(QPalette(QColor(*self.fill)))
        self.item = self.frame.add_widget(self.widget)
        self.widget.clicked.connect(self.on_press)

    def update_position(self):
        self.item.setPos(self.x, self.y)

    def get_text(self):
        return self.widget.text()

    def on_press(self):
        self.frame.on_box_click(self)

    def set_text(self, text):
        self.widget.setText(text)

    def on_destroy(self):
        self.widget.destroy()
        self.item.close()

class TextBlitter(ObjectType):
    def initialize(self):
        pass

class OverlayRedux(ObjectType):
    def initialize(self):
        pass

    def clear(self, r, g, b):
        print 'clearing:', r, g, b

    def set_transparency(sef, value):
        print 'set transparency:', value

class ListControl(ObjectType):
    def initialize(self):
        self.font = self.font.load()
        self.widget = QListWidget()
        # self.model = QStringListModel([])
        # self.view.setModel(self.model)
        # self.edit.setFrame(self.border)
        self.widget.setFixedSize(self.width, self.height)
        self.widget.setFont(self.font)
        # palette = self.edit.palette()
        # if self.transparent:
            # color = Qt.transparent
            # self.edit.setAutoFillBackground(False)
        # else:
            # color = QColor(*self.background)
        # palette.setColor(self.edit.backgroundRole(), color)
        # palette.setColor(QPalette.Window, color)
        # palette.setColor(self.edit.foregroundRole(), QColor(*self.foreground))
        # self.edit.setPalette(palette)
        self.item = self.frame.add_widget(self.widget)
        self.widget.itemSelectionChanged.connect(self.selection_changed)
    
    def add_line(self, value):
        QListWidgetItem(value, self.widget)

    def load(self, filename):
        lines = open(filename, 'rb').read().splitlines()
        for line in lines:
            self.add_line(line)
    
    def scroll_end(self):
        self.widget.scrollToBottom()
    
    def update_position(self):
        self.item.setPos(self.x, self.y)
    
    def reset(self):
        self.widget.clear()

    def get_count(self):
        return self.widget.count()

    def get_index(self):
        return self.widget.currentRow() - self.index_offset
    
    def load_file_list(self, path):
        for item in glob.glob(path):
            if os.path.isfile(item):
                self.add_line(os.path.split(item)[1])

    def set_focus(self, value):
        if value:
            self.widget.setFocus()
        else:
            self.widget.clearFocus()

    def get_line(self, index = None):
        if index is None:
            return self.widget.currentItem().text()
        else:
            item = self.widget.item(index + self.index_offset)
            if item is None:
                return ''
            return item.text()

    def selection_changed(self):
        self.frame.on_list_selection(self)

    def on_destroy(self):
        self.widget.destroy()
        self.item.close()

class IconList(ObjectType):
    def initialize(self):
        self.font = self.font.load()
        self.icons = self.image.load_icons(self.icon_size)
        self.widget = QListWidget()
        self.widget.setFixedSize(self.width, self.height)
        self.widget.setFont(self.font)
        self.item = self.frame.add_widget(self.widget)
    
    def reset(self):
        self.widget.clear()
    
    def set_line(self, index):
        if index == -1:
            # self.widget.clearSelection()
            return
        print 'set line:', index
        self.widget.setCurrentIndex(index)
    
    def add_line(self, value, icon):
        QListWidgetItem(self.icons[icon], value, self.widget)
    
    def get_index(self):
        return self.widget.currentRow()
    
    def update_position(self):
        self.item.setPos(self.x, self.y)

    def set_focus(self, value):
        return

    def on_destroy(self):
        self.widget.destroy()
        self.item.close()

class RichEdit(ObjectType):
    def initialize(self):
        self.font = self.font.load()
        self.edit = QTextBrowser()
        self.edit.setFixedSize(self.width, self.height)
        self.edit.setFont(self.font)
        self.edit.setReadOnly(self.read_only)
        self.item = self.frame.add_widget(self.edit)
    
    def set_color(self, value):
        self.edit.setTextColor(QColor(*value))
    
    def set_text(self, value):
        self.edit.append(value.replace('\r\n', ''))
    
    def go_to_character(self, index):
        size = self.get_character_count()
        index = max(0, min(self.get_character_count() - 1, index))
        cursor = self.edit.textCursor()
        cursor.clearSelection()
        cursor.setPosition(index)
        self.edit.setTextCursor(cursor)
    
    def get_character_count(self):
        return self.edit.document().characterCount()
        
    def update_position(self):
        self.item.setPos(self.x, self.y)

    def on_destroy(self):
        self.edit.destroy()
        self.item.close()

class SubApplication(ObjectType):
    def initialize(self):
        self.view = self.frame.window.create_view(self)
        self.view.setFixedSize(self.width, self.height)
        self.sub_scene = self.view.scene()
        self.sub_scene.set_frame(self.start_frame, True)
        self.update_visible()

    def update_position(self):
        self.view.move(self.x, self.y)

    def update_visible(self):
        self.view.setVisible(self.visible)

    def update(self, dt):
        self.sub_scene.make_update(dt)

    def draw(self, painter):
        pass

    def on_exit(self, subapp):
        print 'on exit:', subapp

    def on_destroy(self):
        self.view.destroy()

class ButtonControl(ObjectType):
    def initialize(self):
        if len(self.strings) > 1:
            print self.type, self.strings
            raise NotImplementedError('Multiple buttons not implemented')
        if self.type == 'Check':
            self.widget = QCheckBox()
        elif self.type == 'Text':
            self.widget = QPushButton(self.strings[0])
        else:
            raise NotImplementedError('button type %r' % self.type)
        self.widget.clicked.connect(self.on_press)
        self.item = self.frame.add_widget(self.widget)

    def update_position(self):
        self.item.setPos(self.x, self.y)

    def get_value(self):
        state = self.widget.checkState()
        if state == Qt.Checked:
            return True
        elif state == Qt.Unchecked:
            return False
        else:
            raise NotImplementedError('check state: %r' % state)

    def on_press(self):
        self.frame.on_button_click(self)

    def set_value(self, value):
        if value:
            state = Qt.Checked
        else:
            state = Qt.Unchecked
        self.widget.setCheckState(state)

    def disable(self):
        self.widget.setDisabled(True)

    def enable(self):
        self.widget.setDisabled(False)

    def on_destroy(self):
        self.widget.destroy()
        self.item.close()

class ChecksumCalculator(ObjectType):
    def initialize(self):
        pass

    def calculate(self, filename):
        data = open(filename, 'rb').read()
        self.checksum = zlib.crc32(data)

    def get_crc(self):
        return self.checksum
    
class INI(ObjectType):
    filename = None
    group = None
    item = None
    
    def initialize(self):
        if self.filename:
            self.set_filename(self.filename)
        else:
            self.config = RawConfigParser()
    
    def set_filename(self, name):
        self.filename = name
        self.config = RawConfigParser()
        self.config.read([name])
    
    def set_group(self, name):
        self.group = name
    
    def set_item(self, name):
        self.item = name
    
    def set(self, value, group = None, item = None):
        group = group or self.group
        item = item or self.item
        if not group or not item:
            return
        self.config.set(group, item, str(value))
        self.save()
    
    def set_group_item_value(self, group, item, value):
        self.set(value, group, item)
    
    def set_item_value(self, item, value):
        self.set(value, item = item)

    def set_item_string(self, item, value):
        self.set(value, item = item)
    
    def get(self, group = None, item = None):
        group = group or self.group
        item = item or self.item
        if not group or not item:
            return ''
        try:
            return self.config.get(group, item)
        except (ConfigError):
            return ''

    def get_int(self, group = None, item = None):
        group = group or self.group
        item = item or self.item
        if not group or not item:
            return 0
        try:
            return int(self.config.get(group, item))
        except (ConfigError, ValueError):
            return 0
    
    def get_string_item(self, item):
        return self.get(item = item)

    def get_value_item(self, item):
        return self.get_int(item = item)
    
    def save(self):
        if self.filename is None:
            return
        fp = open(self.filename, 'wb')
        self.config.write(fp)
        fp.close()

class Socket(ObjectType):
    socket = None
    server = None
    buffered_data = ''
    local_ip = ''
    def initialize(self):
        self.properties = {}
        self.connections = []
        self.free_ids = set()
        self.id_count = itertools.count(0)
    
    def connect(self, host, port):
        self.socket = QTcpSocket()
        self.socket.connectToHost(host, port)
        self.add_socket(self.socket)

    def add_socket(self, sock):
        self.socket = sock
        sock.connected.connect(self.on_connect)
        sock.disconnected.connect(self.on_disconnect)
        self.properties[sock] = {}
        self.connections.append(sock)

    def remove_socket(self, sock):
        del self.properties[sock]
        self.connections.remove(sock)

    def listen(self, port):
        self.server = QTcpServer()
        self.connections = []
        self.socket.newConnection.connect(self.on_connection)
    
    def is_connected(self):
        if self.socket is None:
            return False
        return self.socket.state() == QAbstractSocket.ConnectedState
    
    def update(self, dt):
        for socket in self.connections:
            self.socket = socket
            if not self.has_bytes():
                return
            self.frame.on_sock_receive(self)
    
    def get_bytes(self, size):
        ret = self.socket.read(size).data()
        return ret
    
    def get_line(self):
        while 1:
            ret = self.socket.readLine().data()
            if ret:
                if ret.endswith('\r\n'):
                    ret = ret[:-2]
                elif ret.endswith('\n'):
                    ret = ret[:-1]
                return ret
    
    def has_bytes(self):
        return self.socket.bytesAvailable()
    
    def send_text(self, data):
        if self.socket is None:
            return
        data = str(data)
        self.socket.writeData(data, len(data))
    
    def send_line(self, line):
        self.send_text(line + '\r\n')
    
    def on_connect(self):
        self.local_ip = self.socket.localAddress().toString()
        self.frame.on_sock_connect(self)

    def on_disconnect(self):
        self.remove_socket(self.socket)
        self.frame.on_sock_disconnect(self)

    def on_connection(self):
        self.frame.on_sock_connection(self)

    def accept(self):
        sock = self.socket.nextPendingConnection()
        if not sock:
            return
        self.add_socket(sock)
    
    def get_local_ip(self):
        return self.local_ip
    
    def disconnect(self):
        pass

    def get_property(self, name):
        return self.properties.get(self.socket, {}).get(name, '')

    def set_property(self, name, value):
        print 'set property:', name, value
        self.properties[self.socket][name] = value

    def select_property(self, name, value):
        print self.connections
        for socket in self.connections:
            self.socket = socket
            if self.get_property(name) == value:
                break
        else:
            print 'no such property:', name, value
            self.socket = None

    def select_socket(self, index):
        self.socket = self.connections[index - 1]

    def set_timeout(self, value):
        print 'SET TIMEOUT:', value / 1000.0

class MovementType(object):
    def __init__(self, instance):
        self.instance = instance
        print 'created movement', self, instance

    def stop(self):
        print 'stopped', self.instance

    def set_speed(self, value):
        print 'set speed:', value

class Ball(MovementType):
    pass

class Path(MovementType):
    pass

class Mouse(MovementType):
    pass

class InstanceList(object):
    def __init__(self, instances):
        object.__setattr__(self, 'instances', instances)

    def __getattribute__(self, name):
        object.__setattr__(self, 'attribute', name)
        instances = object.__getattribute__(self, 'instances')
        if not instances:
            return None
        return getattr(instances[0], name)

    def __setattr__(self, name, value):
        for instance in object.__getattribute__(self, 'instances'):
            setattr(instance, name, value)

class Frame(object):
    def __init__(self, parent, frame_widget = None):
        self.scene = parent
        self.window = parent.window
        self.values = parent.values
        self.strings = parent.strings
        self.players = parent.players
        self.frame_widget = frame_widget
        self.audio = parent.audio
        self.instances = []
        self.object_types = defaultdict(list)
        # event-related state
        self.loop_indexes = {}
        self.not_always_helpers = {}
        self.restrict_helpers = {}
        self.every_helpers = {}
        self.fire_once = set()
        self.timers = {}
        self.backdrops = []
        # initialization
        self.initialize()
        self.on_start()
    
    def on_start(self):
        pass
    
    def on_mouse_press(self, x, y, button):
        pass
    
    def update(self, dt):
        pass

    def draw(self, painter):
        for backdrop in self.backdrops:
            backdrop.draw(painter)
        for instance in self.instances:
            if not instance.visible:
                continue
            instance.draw(painter)
    
    def add_timed_call(self, func, seconds):
        QTimer.singleShot(seconds * 1000.0, func)
    
    def end_application(self):
        self.scene.exit()
    
    def set_frame(self, value):
        self.scene.set_frame(value)
    
    def next_frame(self):
        self.scene.set_frame(self.index + 1)
    
    def hide_cursor(self):
        self.window.setCursor(Qt.BlankCursor)
    
    def show_cursor(self):
        self.window.unsetCursor()
    
    def load_mod(self, filename, cache, track):
        self.audio.set_track_filename(filename, track)
    
    def set_mod_volume(self, track, volume):
        self.audio.set_track_volume(track, volume)

    def is_mod_playing(self, track):
        return self.audio.is_track_playing(track)
    
    def cross_fade_mod(self, src, dst, duration):
        self.audio.cross_fade_tracks(src, dst, duration)

    def stop_mod(self, track, fade_time = 0):
        self.audio.stop_track(track, fade_time)
    
    def add_widget(self, widget):
        item = self.scene.addWidget(widget)
        if self.frame_widget is not None:
            widget.setParent(self.frame_widget)
        return item

    def create_object(self, klass, x, y):
        item = klass(self)
        self.instances.append(item)
        self.object_types[klass].append(item)
        item.set_position(x, y)
        return item
    
    def initialize(self):
        pass
    
    def destroy(self):
        for instance in self.instances[:]:
            instance.destroy()
    
    # events

    def start_timer(self, index):
        self.timers[index] = 0.0

    def get_timer(self, index):
        return self.timers.get(index, 0.0)

    def stop_timer(self, index):
        del self.timers[index]
    
    def is_active(self):
        return bool(self.scene.application.activeWindow())
    
    def is_window_visible(self):
        return self.scene.view.isVisible()

    def get_loop_index(self, name):
        return self.loop_indexes[name]
    
    def get(self, objects, as_list = False):
        if type(objects) in (tuple, list):
            object_list = []
            for klass in objects:
                object_list.extend(self.object_types[klass])
        else:
            object_list = self.object_types[objects][:]
        if not as_list and len(object_list) != 1:
            raise ValueError('multiple instances of %s' % objects)
        if as_list:
            return object_list
        else:
            return object_list[0]

    def paste(self, sprite):
        self.backdrops.append(sprite.copy())
    
    def every(self, seconds):
        call_id = get_caller_id()
        if call_id not in self.every_helpers:
            self.every_helpers[call_id] = EveryHelper(seconds)
        return self.every_helpers[call_id].check(self.scene.current_dt)

    def not_always(self):
        call_id = get_caller_id()
        if call_id not in self.not_always_helpers:
            self.not_always_helpers[call_id] = NotAlwaysHelper(self.scene)
        return self.not_always_helpers[call_id].check()
    
    def check_once(self):
        call_id = get_caller_id()
        ret = call_id not in self.fire_once
        self.fire_once.add(call_id)
        return ret

    def restrict_for(self, seconds):
        call_id = get_caller_id()
        if call_id not in self.restrict_helpers:
            self.restrict_helpers[call_id] = RestrictHelper(seconds)
        return self.restrict_helpers[call_id].check(self.scene.current_dt)
    
    def get_global_string(self, index):
        return self.strings.get(index, '')
    
    def get_global_value(self, index):
        return self.values.get(index, 0)

    def set_event_id(self, global_id):
        self.selected = {}

    def mouse_in_zone(self, zone):
        x1, y1, x2, y2 = zone
        x, y = self.scene.get_mouse_position()
        return collides(x1, y1, x2, y2, x, y, x, y)

# event helper-functions

def cos(value):
    return math.cos(math.radians(value))

def sin(value):
    return math.sin(math.radians(value))

IMMEDIATE_OPERATORS = {
    '=' : operator.eq,
    '!' : operator.ne,
    '<>' : operator.ne,
    '>' : operator.gt,
    '>=' : operator.ge,
    '<' : operator.lt,
    '<=' : operator.le
}

def immediate_compare(a, op, b, true, false):
    if IMMEDIATE_OPERATORS.get(op, operator.eq)(a, b):
        return true
    else:
        return false

def get_caller_id():
    # this shit is so hacky, but it makes the code easier to read.
    # hacky friday. woo.
    return sys._getframe(2).f_lineno

def left_string(value, index):
    return value[:index]
    
def right_string(value, index):
    return value[-index:]

def mid_string(value, index1, index2):
    return value[index1:index1+index2]

VALID_NUMBER_CHARS = string.digits + '-+'

def to_number(value, exceptions = False):
    if not value:
        return 0
    i = 0
    for i, c in enumerate(value):
        if c not in VALID_NUMBER_CHARS:
            i -= 1
            break
    value = value[:i+1]
    if not value:
        return 0
    return int(value)

def to_int(value):
    try:
        return int(value)
    except ValueError:
        return 0

def negate(value):
    return not value

def select(value):
    return value

class EveryHelper(object):
    value = 0.0
    def __init__(self, seconds):
        self.seconds = seconds
    
    def check(self, dt):
        self.value += dt
        if self.value >= self.seconds:
            self.value -= self.seconds
            return True
        return False

class NotAlwaysHelper(object):
    loop_count = None
    def __init__(self, scene):
        self.scene = scene
    
    def check(self):
        loop_count = self.scene.loop_count
        old_count = self.loop_count
        self.loop_count = loop_count
        if old_count is None or loop_count+1 != old_count:
            return True
        return False

class RestrictHelper(object):
    value = 0.0
    def __init__(self, seconds):
        self.seconds = seconds
    
    def check(self, dt):
        self.value += dt
        if self.value >= self.seconds:
            self.value -= self.seconds
            return True
        return False

cipher_cache = {}

def add_encryption_key(key):
    cipher_cache[key] = MMFBlowfish(key)

def encrypt_string(key, value):
    return cipher_cache[key].encrypt(value)

def decrypt_string(key, value):
    return cipher_cache[key].decrypt(value)

def pad_data(data):
    pad_bytes = 8 - (len(data) % 8)
    return data + '\x00' * pad_bytes

def reverse_bytes(data):
    new_data = ''
    for i in xrange(len(data)/4):
        off = i * 4
        bytes = data[off:off+4]
        new_data += bytes[::-1]
    return new_data

class MMFBlowfish(object):
    def __init__(self, key, mode = Blowfish.MODE_ECB):
        self.cipher = Blowfish.new(key, mode)
    
    def encrypt(self, data):
        encrypt_data = reverse_bytes(pad_data(data))
        encrypted = reverse_bytes(self.cipher.encrypt(encrypt_data))
        filtered = urllib.quote(encrypted)
        return filtered
        
    def decrypt(self, data):
        decrypt_data = reverse_bytes(urllib.unquote(data))
        decrypted = reverse_bytes(self.cipher.decrypt(decrypt_data))
        return decrypted.replace('\x00', '')

def randrange(value):
    return random.randrange(0, value)

def key_string(value):
    return str(value)

def key_from_name(value):
    return 0

def encrypt_file(filename, shift):
    data = open(filename, 'rb').read()
    new_data = ''
    for c in data:
        new_data += chr((ord(c)+shift) % 256)
    open(filename, 'wb').write(new_data)
    
def decrypt_file(filename, shift):
    data = open(filename, 'rb').read()
    new_data = ''
    for c in data:
        new_data += chr((ord(c)-shift) % 256)
    open(filename, 'wb').write(new_data)

__all__ = ['Frame', 'Text', 'Active', 'Backdrop', 'Counter', 'ActivePicture',
           'StringParser', 'BinaryObject', 'Edit', 'INI', 'left_string',
           'add_encryption_key', 'EveryHelper', 'to_number', 'Socket',
           'mid_string', 'IconList', 'ListControl', 'RichEdit', 'SubApplication',
           'Font', 'right_string', 'randrange', 'ButtonControl', 'ActiveBox',
           'TextBlitter', 'OverlayRedux', 'ChecksumCalculator', 'Mouse', 'Path',
           'Ball', 'negate', 'to_int', 'select', 'key_string', 'encrypt_file',
           'decrypt_file', 'cos', 'sin', 'immediate_compare', 'encrypt_string',
           'decrypt_string', 'key_from_name']