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

from config import *
import PySide
from common import get_time

import sys
import math
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtOpenGL import *

from OpenGL import GL

from sounds import *
from images import *
from fonts import *
from audio import AudioManager

import sys

class GraphicsView(QGraphicsView):
    def resizeEvent(self, event):
        scene = self.scene()
        if scene:
            scene.setSceneRect(QRect(QPoint(0, 0), event.size()))
        QGraphicsView.resizeEvent(self, event)

class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.application = app
        self.views = []
        self.scenes = []
        self.view = self.create_view()
        self.setWindowTitle(NAME)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    def create_view(self, parent_object = None):
        view = GraphicsView(self)
        self.views.append(view)
        view.setContentsMargins(QMargins())
        view.setViewport(QGLWidget())
        view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        scene = MainScene(self, view, parent_object)
        self.scenes.append(scene)
        view.setScene(scene)
        if parent_object is None:
            self.setCentralWidget(view)
        return view

class Player(object):
    def __init__(self, lives):
        self.lives = lives

    def set_ignore(self, value):
        self.ignore = value

class MainScene(QGraphicsScene):
    frame = None
    loop_count = 0
    parent_scene = None
    current_dt = 0.0
    next_frame = None
    def __init__(self, window, view, parent_object = None):
        QGraphicsScene.__init__(self, window)
        self.application = window.application
        self.window = window
        self.view = view
        self.parent_object = parent_object
        if parent_object is None:
            self.update_timer = QTimer(self)
            self.update_timer.timeout.connect(self.update_loop)
            # MMF 1.5 is 50 FPS
            self.update_timer.start((1 / 50.0) * 1000)
            self.values = {}
            self.strings = {}
            self.players = [Player(START_LIVES) for _ in xrange(4)]
            self.audio = AudioManager()
            start_index = 0
            if FAST_CONNECT:
                start_index = 4
            self.set_frame(start_index, True)
        else:
            scene = parent_object.scene
            self.values = scene.values
            self.strings = scene.strings
            self.players = scene.players
            self.audio = scene.audio
        self.key_presses = []
        self.key_downs = []
        self.mouse_downs = []
    
    def update_loop(self):
        try:
            if self.next_frame is not None:
                self.set_frame(self.next_frame, True)
                self.next_frame = None
                return
            self.loop_count += 1
            current_time = get_time()
            dt = current_time - self.current_time
            self.current_time = current_time
            self.audio.update(dt)
            self.make_update(dt)
        except:
            import traceback
            traceback.print_exc()
            self.exit()

    def make_update(self, dt):
        self.current_dt = dt
        self.frame.update(dt)
        for instance in self.frame.instances:
            instance.update(dt)
        self.update()
        self.key_presses = []

    def exit(self):
        if self.parent_object is not None:
            self.parent_object.on_exit(self)
            return
        self.audio.delete()
        self.application.quit()
    
    def set_frame(self, index, force = False):
        if not force:
            self.next_frame = index
            return
        if self.frame:
            self.frame.destroy()
        self.frame = FRAMES[index](self)
        self.current_time = get_time()
        
    def drawBackground(self, painter, rect):
        frame = self.frame
        painter.beginNativePainting()
        painter.setRenderHint(QPainter.Antialiasing)
        r, g, b = frame.background
        GL.glClearColor(r / 255.0, g / 255.0, b / 255.0, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        width, height = int(self.width()), int(self.height())
        GL.glViewport(0, 0, width, height)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(0, width, height, 0, -1, 1)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        frame.draw(painter)
        painter.endNativePainting()
    
    def get_mouse_position(self):
        p = self.view.mapToScene(self.view.mapFromGlobal(QCursor.pos()))
        return p.x(), p.y()
    
    def keyPressEvent(self, event):
        key = event.key()
        QGraphicsScene.keyPressEvent(self, event)
        self.key_presses.append(key)
        self.key_downs.append(key)
    
    def keyReleaseEvent(self, event):
        QGraphicsScene.keyReleaseEvent(self, event)
        self.key_downs.remove(event.key())
    
    def mousePressEvent(self, event):
        QGraphicsScene.mousePressEvent(self, event)
        pos = event.scenePos()
        button = event.button()
        self.frame.on_mouse_press(pos.x(), pos.y(), button)
        self.mouse_downs.append(button)

    def mouseDoubleClickEvent(self, event):
        QGraphicsScene.mouseDoubleClickEvent(self, event)
        self.mouse_downs.append(event.button())

    def mouseReleaseEvent(self, event):
        QGraphicsScene.mouseReleaseEvent(self, event)
        button = event.button()
        self.mouse_downs.remove(button)

    # def mouseMoveEvent(self, event):
        # pass

if __name__ == '__main__':
    if False:
        import sys
        trace_file = open('hey.trace', 'wb')
        def trace(frame, event, arg):
            trace_file.write(
                "%s, %s:%d\n" % (event, frame.f_code.co_filename, 
                frame.f_lineno))
            trace_file.flush()
            return trace
        sys.settrace(trace)

    # QGL.setPreferredPaintEngine(QPaintEngine.OpenGL)
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec_())