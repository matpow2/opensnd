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

from chowaudio import (Sound, listener, open as open_audio, 
    close as close_audio, AudioError)
open_audio()

MUTED = False

if MUTED:
    listener.volume = 0.0

class Track(object):
    volume = 1.0
    volume_add = None
    sound = None
    def __init__(self, filename):
        self.filename = filename
    
    def set_volume(self, volume):
        self.volume = volume / 100.0
        if self.sound is not None:
            self.sound.volume = self.volume
    
    def play(self):
        if self.sound is not None:
            return
        self.sound = Sound(filename = self.filename)
        self.sound.volume = self.volume
        self.sound.play(0)

    def stop(self):
        if self.sound is None:
            return
        self.sound.close()
        self.sound = None
    
    def update(self, dt):
        if self.volume_add is None:
            return
        self.volume += self.volume_add
        self.sound.volume = self.volume
        if self.volume < 0.0 or self.volume > 1.0:
            self.volume = max(0.0, min(1.0, self.volume))
            self.volume_add = None
            self.stop()

    def is_playing(self):
        return self.sound is not None

class AudioManager(object):
    def __init__(self):
        self.track_filenames = {}
        self.tracks = {}
        self.track_volume = {}
    
    def update(self, dt):
        for track in self.tracks.values():
            track.update(dt)

    def set_default_directory(self, filename):
        self.sound_directory = filename
    
    def set_track_filename(self, name, track):
        self.tracks[track] = Track(name)
    
    def play_track(self, track):
        self.tracks[track].play()

    def is_track_playing(self, track):
        return self.tracks[track].is_playing()

    def stop_track(self, track, fade_time = 0):
        if fade_time:
            self.tracks[track].volume_add = -1.0 / fade_time
        else:
            self.tracks[track].stop()
    
    def set_track_volume(self, track, volume):
        self.tracks[track].set_volume(volume)
    
    def cross_fade_tracks(self, src, dst, duration):
        source_track = self.tracks[src]
        destination_track = self.tracks[dst]
        destination_track.play()
        if source_track.sound is None or src == dst:
            return
        source_track.volume_add = -1.0 / duration
        destination_track.volume_add = 1.0 / duration
    
    def delete(self):
        close_audio()
