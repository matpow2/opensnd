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

import ctypes
from ctypes import *
import sys
import atexit

if sys.platform == 'win32':
    openal_name = 'openal32'
    alure_name = 'alure32'
else:
    openal_name = 'openal'
    alure_name = 'alure'

openal_lib = ctypes.cdll.LoadLibrary(openal_name)
alure_lib = ctypes.cdll.LoadLibrary(alure_name)

ALboolean = c_int
ALchar = c_char
ALbyte = c_char
ALubyte = c_ubyte
ALshort = c_short
ALushort = c_ushort
ALint = c_int
ALuint = c_uint
ALsizei = c_int
ALenum = c_int
ALfloat = c_float
ALdouble = c_double
ALvoid = None
ALCchar = c_char
ALCint = c_int

alureInt64 = c_longlong
alureUInt64 = c_ulonglong

# OpenAL wrapper

alSourcef = openal_lib.alSourcef
alSourcef.restype = None
alSourcef.argtypes = [ALuint, ALenum, ALfloat]

alSourcei = openal_lib.alSourcei
alSourcei.restype = None
alSourcei.argtypes = [ALuint, ALenum, ALint]

alGetSourcef = openal_lib.alGetSourcef
alGetSourcef.restype = None
alGetSourcef.argtypes = [ALuint, ALenum, POINTER(ALfloat)]

alGetSource3f = openal_lib.alGetSource3f
alGetSource3f.restype = None
alGetSource3f.argtypes = [ALuint, ALenum, POINTER(ALfloat), POINTER(ALfloat),
    POINTER(ALfloat)]

alGenSources = openal_lib.alGenSources
alGenSources.restype = None
alGenSources.argtypes = [ALsizei, POINTER(ALuint)]


alDeleteSources = openal_lib.alDeleteSources
alDeleteSources.restype = None
alDeleteSources.argtypes = [ALsizei, POINTER(ALuint)]

alGetSource3f = openal_lib.alGetSource3f
alGetSource3f.restype = None
alGetSource3f.argtypes = [ALuint, ALenum, POINTER(ALfloat), POINTER(ALfloat),
    POINTER(ALfloat)]

alListenerf = openal_lib.alListenerf
alListenerf.restype = None
alListenerf.argtypes = [ALenum, ALfloat]

alListener3f = openal_lib.alListener3f
alListener3f.restype = None
alListener3f.argtypes = [ALenum, ALfloat, ALfloat, ALfloat]

alGetError = openal_lib.alGetError
alGetError.restype = ALenum
alGetError.argtypes = []

alIsExtensionPresent = openal_lib.alIsExtensionPresent
alIsExtensionPresent.restype = ALboolean
alIsExtensionPresent.argtypes = [POINTER(ALchar)]

# ALURE wrapper

class alureStream(Structure):
    pass

alureStream_p = POINTER(alureStream)

alureInitDevice = alure_lib.alureInitDevice
alureInitDevice.restype = ALboolean
alureInitDevice.argtypes = [POINTER(ALCchar), POINTER(ALCint)]

alureShutdownDevice = alure_lib.alureShutdownDevice
alureShutdownDevice.restype = ALboolean
alureShutdownDevice.argtypes = []

alureGetErrorString = alure_lib.alureGetErrorString
alureGetErrorString.restype = POINTER(ALchar)
alureGetErrorString.argtypes = []

alureResumeSource = alure_lib.alureResumeSource
alureResumeSource.restype = ALboolean
alureResumeSource.argtypes = [ALuint]

alureUpdateInterval = alure_lib.alureUpdateInterval
alureUpdateInterval.restype = ALboolean
alureUpdateInterval.argtypes = [ALfloat]

alurePauseSource = alure_lib.alurePauseSource
alurePauseSource.restype = ALboolean
alurePauseSource.argtypes = [ALuint]

alureStopSource = alure_lib.alureStopSource
alureStopSource.restype = ALboolean
alureStopSource.argtypes = [ALuint]

CALLBACK_FUNC = CFUNCTYPE(None, py_object, ALuint)

alurePlaySource = alure_lib.alurePlaySource
alurePlaySource.restype = ALboolean
alurePlaySource.argtypes = [ALuint, CALLBACK_FUNC, py_object]

alurePlaySourceStream = alure_lib.alurePlaySourceStream
alurePlaySourceStream.restype = ALboolean
alurePlaySourceStream.argtypes = [ALuint, alureStream_p, ALsizei, ALsizei, 
    CALLBACK_FUNC, py_object]

alureDestroyStream = alure_lib.alureDestroyStream
alureDestroyStream.restype = ALboolean
alureDestroyStream.argtypes = [alureStream_p, ALsizei, POINTER(ALuint)]

alureGetStreamLength = alure_lib.alureGetStreamLength
alureGetStreamLength.restype = alureInt64
alureGetStreamLength.argtypes = [alureStream_p]

alureSetStreamOrder = alure_lib.alureSetStreamOrder
alureSetStreamOrder.restype = ALboolean
alureSetStreamOrder.argtypes = [alureStream_p, ALsizei]

alureCreateStreamFromFile = alure_lib.alureCreateStreamFromFile
alureCreateStreamFromFile.restype = alureStream_p
alureCreateStreamFromFile.argtypes = [POINTER(ALchar), ALsizei, ALsizei,
    POINTER(ALuint)]

alureStreamSizeIsMicroSec = alure_lib.alureStreamSizeIsMicroSec
alureStreamSizeIsMicroSec.restype = ALboolean
alureStreamSizeIsMicroSec.argtypes = [ALboolean]

alureGetStreamFrequency = alure_lib.alureGetStreamFrequency
alureGetStreamFrequency.restype = ALsizei
alureGetStreamFrequency.argtypes = [alureStream_p]

alureSetStreamPatchset = alure_lib.alureSetStreamPatchset
alureSetStreamPatchset.restype = ALboolean
alureSetStreamPatchset.argtypes = [alureStream_p, POINTER(ALchar)]

# constants

AL_NO_ERROR = 0
AL_FALSE = 0
AL_TRUE = 1
AL_GAIN = 4106
AL_PITCH = 4099
AL_POSITION = 4100
AL_DIRECT_CHANNELS_SOFT = 0x1033

# Pythonic API

class AudioDevice(object):
    opened = False
    def __init__(self):
        self.sounds = []
        atexit.register(self.close)
    
    def open(self):
        if self.opened:
            return
        self.opened = True
        if not alureInitDevice(None, None):
            raise AudioError(
                'Failed to open OpenAL device: %s' % 
                alureGetErrorString())
        self.direct_channels = alIsExtensionPresent('AL_SOFT_direct_channels')
        alureStreamSizeIsMicroSec(AL_TRUE)
        alureUpdateInterval(0.125)
        
    def __del__(self):
        self.close()
    
    def close(self):
        if not self.opened:
            return
        self.opened = False
        for sound in self.sounds[:]:
            sound.close()
        self.sounds = []
        alureUpdateInterval(0)
        alureShutdownDevice()

audio_device = AudioDevice()
open = audio_device.open
close = audio_device.close

class AudioError(Exception):
    pass

CHUNK_LENGTH = 250000
NUM_BUFS = 3

def on_end_callback(sound, source):
    callback = sound.callback
    if callback is None:
        return
    func, arg, kw = callback
    func(*arg, **kw)

callback_pointer = CALLBACK_FUNC(on_end_callback)

class Sound(object):
    closed = True
    callback = None
    
    _paused = False
    _volume = 1.0
    _pitch = 1.0
    _x = _y = _z = 0.0

    def __init__(self, data = None, filename = None):
        if not audio_device.opened:
            raise AudioError('Audio device not initialized')
        self.source = ALuint()
        alGenSources(1, byref(self.source))
        if audio_device.direct_channels:
            alSourcei(self.source, AL_DIRECT_CHANNELS_SOFT, AL_TRUE)
        if data is not None:
            self.stream = alureCreateStreamFromStaticMemory(data, len(data), 
                CHUNK_LENGTH, 0, 0)
        elif filename is not None:
            self.stream = alureCreateStreamFromFile(filename, CHUNK_LENGTH, 0,
                None)
        else:
            raise AudioError('No input specified')
        if not self.stream:
            raise AudioError('Could not load sound')
        audio_device.sounds.append(self)
        self.closed = False
    
    def get_volume(self):
        return self._volume
    def set_volume(self, value):
        self._volume = value
        alSourcef(self.source, AL_GAIN, value)
    volume = property(get_volume, set_volume)

    def get_pitch(self):
        return self._pitch
    def set_pitch(self, value):
        self._pitch = value
        alSourcef(self.source, AL_PITCH, value)
    pitch = property(get_pitch, set_pitch)

    def get_rate(self):
        return alureGetStreamFrequency(self.stream)
    rate = property(get_rate)
    
    def get_frequency(self):
        return self._pitch * self.get_rate()
    def set_frequency(self, value):
        self.set_pitch(float(value) / self.get_rate())
    frequency = property(get_frequency, set_frequency)
    
    def get_pan(self):
        return self._x * 100.0
    def set_pan(self, pan):
        pan = max(-1.0, min(1.0, pan / 100.0))
        x = pan
        y = -math.sqrt(1.0 - pan**2)
        z = 0.0
        self.set_position(x, y, z)
    pan = property(get_pan, set_pan)
    
    def get_position(self):
        return self._x, self._y, self._z
    def set_position(self, (x, y, z)):
        self._x = x
        self._y = y
        self._z = z
        alSource3f(self.source, AL_POSITION, x, y, z)
    position = property(get_position, set_position)
    
    def get_duration(self):
        return alureGetStreamLength(self.stream)
    duration = property(get_duration)
    
    def get_paused(self):
        return self._paused
    def set_paused(self, value):
        if value == self._paused:
            return
        self._paused = value
        if value:
            alurePauseSource(self.source)
        else:
            alureResumeSource(self.source)
    paused = property(get_paused, set_paused)
                
    def play(self, loops = 1):
        loops -= 1
        if not alurePlaySourceStream(self.source, self.stream, NUM_BUFS, loops,
                                     callback_pointer, py_object(self)):
            raise AudioError('Could not play sound')
    
    def stop(self):
        alureStopSource(self.source, AL_FALSE)
    
    def close(self):
        if self.closed:
            return
        self.closed = True
        audio_device.sounds.remove(self)
        alureDestroyStream(self.stream, 0, None)
        alDeleteSources(1, byref(self.source))
    
    def set_soundfont(self, value):
        alureSetStreamPatchset(self.stream, value)
    
    def __del__(self):
        self.close()
    
    def set_callback(self, callback, *arg, **kw):
        self.callback = (callback, arg, kw)

class Listener(object):
    _volume = 1.0
    
    def get_volume(self):
        return self._volume
    def set_volume(self, value):
        self._volume = value
        alListenerf(AL_GAIN, value)
    volume = property(get_volume, set_volume)

listener = Listener()

if __name__ == '__main__':
    open()
    sound = Sound(filename = 'test.mod')
    sound.play()
    import time
    time.sleep(10.0)