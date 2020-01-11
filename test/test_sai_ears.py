import unittest
import SAIEars

import filecmp
import os


class TestSAIEars(unittest.TestCase):

    def setUp(self):
        self.saie = SAIEars.SAIEars()

    def test_SAIEars_analyse_microphone_1(self):
        """Show a text-mode spectrogram using live microphone data."""
        import argparse
        import math
        import shutil

        import numpy as np
        import sounddevice as sd

        usage_line = ' press <enter> to quit, +<enter> or -<enter> to change scaling '

        def int_or_str(text):
            """Helper function for argument parsing."""
            try:
                return int(text)
            except ValueError:
                return text

        try:
            columns, _ = shutil.get_terminal_size()
        except AttributeError:
            columns = 80

        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        args, remaining = parser.parse_known_args()
        if args.list_devices:
            print(sd.query_devices())
            parser.exit(0)
        __doc__ = "Show a text-mode spectrogram using live microphone dataShow a text-mode spectrogram using live microphone data"

        parser = argparse.ArgumentParser(
            description=__doc__ + '\n\nSupported keys:' + usage_line,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[parser])
        parser.add_argument(
            '-b', '--block-duration', type=float, metavar='DURATION', default=50,
            help='block size (default %(default)s milliseconds)')
        parser.add_argument(
            '-c', '--columns', type=int, default=columns,
            help='width of spectrogram')
        parser.add_argument(
            '-d', '--device', type=int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-g', '--gain', type=float, default=10,
            help='initial gain factor (default %(default)s)')
        parser.add_argument(
            '-r', '--range', type=float, nargs=2,
            metavar=('LOW', 'HIGH'), default=[100, 2000],
            help='frequency range (default %(default)s Hz)')
        args = parser.parse_args(remaining)
        low, high = args.range
        if high <= low:
            parser.error('HIGH must be greater than LOW')

        # Create a nice output gradient using ANSI escape sequences.
        # Stolen from https://gist.github.com/maurisvh/df919538bcef391bc89f
        colors = 30, 34, 35, 91, 93, 97
        chars = ' :%#\t#%:'
        gradient = []
        for bg, fg in zip(colors, colors[1:]):
            for char in chars:
                if char == '\t':
                    bg, fg = fg, bg
                else:
                    gradient.append('\x1b[{};{}m{}'.format(fg, bg + 10, char))

        try:
            samplerate = sd.query_devices(args.device, 'input')['default_samplerate']

            delta_f = (high - low) / (args.columns - 1)
            fftsize = math.ceil(samplerate / delta_f)
            low_bin = math.floor(low / delta_f)

            def callback(indata, frames, time, status):
                if status:
                    text = ' ' + str(status) + ' '
                    print('\x1b[34;40m', text.center(args.columns, '#'),
                          '\x1b[0m', sep='')
                if any(indata):
                    magnitude = np.abs(np.fft.rfft(indata[:, 0], n=fftsize))
                    magnitude *= args.gain / fftsize
                    line = (gradient[int(np.clip(x, 0, 1) * (len(gradient) - 1))]
                            for x in magnitude[low_bin:low_bin + args.columns])
                    print(*line, sep='', end='\x1b[0m\n')
                else:
                    print('no input')

            with sd.InputStream(device=args.device, channels=1, callback=callback,
                                blocksize=int(samplerate * args.block_duration / 1000),
                                samplerate=samplerate):
                while True:
                    response = input()
                    if response in ('', 'q', 'Q'):
                        break
                    for ch in response:
                        if ch == '+':
                            args.gain *= 2
                        elif ch == '-':
                            args.gain /= 2
                        else:
                            print('\x1b[31;40m', usage_line.center(args.columns, '#'),
                                  '\x1b[0m', sep='')
                            break
        except KeyboardInterrupt:
            parser.exit('Interrupted by user')
        except Exception as e:
            parser.exit(type(e).__name__ + ': ' + str(e))

        assert (True==True)

    def test_SAIEars_analyse_microphone_2(self):
        import pyaudio
        import struct
        import matplotlib.pyplot as plt
        import numpy as np
        from scipy import signal
        mic = pyaudio.PyAudio()
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 20000
        CHUNK = int(RATE / 20)
        stream = mic.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)

        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')

        while True:
            data = stream.read(CHUNK)
            data = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')
            f, t, Sxx = signal.spectrogram(data, fs=CHUNK)
            dBS = 10 * np.log10(Sxx)
            plt.pcolormesh(t, f, dBS)
            plt.pause(0.005)

    def test_SAIEars_analyse_microphone_3(self):
        import pyaudio
        import numpy as np
        import pylab
        import time

        RATE = 44100
        CHUNK = int(RATE / 20)  # RATE / number of updates per second

        def soundplot(stream):
            t1 = time.time()
            data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
            pylab.plot(data)
            pylab.title(i)
            pylab.grid()
            pylab.axis([0, len(data), -2 ** 16 / 2, 2 ** 16 / 2])
            pylab.savefig("03.png", dpi=50)
            pylab.close('all')
            print("took %.02f ms" % ((time.time() - t1) * 1000))

        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
        for i in range(int(20 * RATE / CHUNK)):  # do this for 10 seconds
            soundplot(stream)
        stream.stop_stream()
        stream.close()
        p.terminate()

    def test_SAIEars_analyse_microphone_4(self):
        """
        https://config9.com/linux/how-to-read-realtime-microphone-audio-volume-in-python-and-ffmpeg-or-similar/
        """
        import numpy as np
        import sounddevice as sd

        duration = 10 #in seconds

        def audio_callback(indata, frames, time, status):
           volume_norm = np.linalg.norm(indata) * 10
           print("|" * int(volume_norm))


        stream = sd.InputStream(callback=audio_callback)
        with stream:
           sd.sleep(duration * 1000)

    def test_SAIEars_analyse_microphone_5(self):
        """
        https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/
        """
        # TODO
        #   try to save data of recording as numpy
        #   try to load the data saved
        import pyaudio
        import time
        import pylab
        import numpy as np

        class SWHear(object):
            """
            The SWHear class is made to provide access to continuously recorded
            (and mathematically processed) microphone data.
            """

            def __init__(self, device=None, startStreaming=True):
                """fire up the SWHear class."""
                print(" -- initializing SWHear")

                self.chunk = 4096  # number of data points to read at a time
                self.rate = 44100  # time resolution of the recording device (Hz)

                # for tape recording (continuous "tape" of recent audio)
                self.tapeLength = 2  # seconds
                self.tape = np.empty(self.rate * self.tapeLength) * np.nan

                self.p = pyaudio.PyAudio()  # start the PyAudio class
                if startStreaming:
                    self.stream_start()

            ### LOWEST LEVEL AUDIO ACCESS
            # pure access to microphone and stream operations
            # keep math, plotting, FFT, etc out of here.

            def stream_read(self):
                """return values for a single chunk"""
                data = np.fromstring(self.stream.read(self.chunk), dtype=np.int16)
                # print(data)
                return data

            def stream_start(self):
                """connect to the audio device and start a stream"""
                print(" -- stream started")
                self.stream = self.p.open(format=pyaudio.paInt16, channels=1,
                                          rate=self.rate, input=True,
                                          frames_per_buffer=self.chunk)

            def stream_stop(self):
                """close the stream but keep the PyAudio instance alive."""
                if 'stream' in locals():
                    self.stream.stop_stream()
                    self.stream.close()
                print(" -- stream CLOSED")

            def close(self):
                """gently detach from things."""
                self.stream_stop()
                self.p.terminate()

            ### TAPE METHODS
            # tape is like a circular magnetic ribbon of tape that's continously
            # recorded and recorded over in a loop. self.tape contains this data.
            # the newest data is always at the end. Don't modify data on the type,
            # but rather do math on it (like FFT) as you read from it.

            def tape_add(self):
                """add a single chunk to the tape."""
                self.tape[:-self.chunk] = self.tape[self.chunk:]
                self.tape[-self.chunk:] = self.stream_read()

            def tape_flush(self):
                """completely fill tape with new data."""
                readsInTape = int(self.rate * self.tapeLength / self.chunk)
                print(" -- flushing %d s tape with %dx%.2f ms reads" % \
                      (self.tapeLength, readsInTape, self.chunk / self.rate))
                for i in range(readsInTape):
                    self.tape_add()

            def tape_forever(self, plotSec=.25):
                t1 = 0
                try:
                    while True:
                        self.tape_add()
                        if (time.time() - t1) > plotSec:
                            t1 = time.time()
                            self.tape_plot()
                except:
                    print(" ~~ exception (keyboard?)")
                    return

            def tape_plot(self, saveAs="03.png"):
                """plot what's in the tape."""
                pylab.plot(np.arange(len(self.tape)) / self.rate, self.tape)
                pylab.axis([0, self.tapeLength, -2 ** 16 / 2, 2 ** 16 / 2])
                if saveAs:
                    t1 = time.time()
                    pylab.savefig(saveAs, dpi=50)
                    print("plotting saving took %.02f ms" % ((time.time() - t1) * 1000))
                else:
                    pylab.show()
                    print()  # good for IPython
                pylab.close('all')

        ear = SWHear()
        ear.tape_forever()
        ear.close()
        print("DONE")

    def test_SAIEars_analyse_microphone_6(self):
        # TODO
        #   Use those data to only record when there was a sound of a voice using dynamic deep reinforcement learning
        import pyaudio
        import numpy

        RATE = 16000
        RECORD_SECONDS = 2.5
        CHUNKSIZE = 1024
        MIN_VOLUME = 50

        # initialize portaudio
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

        frames = []  # A python-list of chunks(numpy.ndarray)
        for _ in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
            data = stream.read(CHUNKSIZE)
            frame = numpy.fromstring(data, dtype=numpy.int16)
            print(max(frame))
            frames.append(frame)
            if max(frame) < MIN_VOLUME:
                break

        # Convert the list of numpy-arrays into a 1D array (column-wise)
        numpydata = numpy.hstack(frames)

        # close stream
        stream.stop_stream()
        stream.close()
        p.terminate()
        from pprint import pprint
        pprint(numpydata)
        import scipy.io.wavfile as wav
        wav.write('out.wav', RATE, numpydata)
        #pprint()
        import matplotlib.pyplot as plt
        plt.plot(wav.read('out.wav')[1])
        plt.ylabel('some numbers')
        plt.show()
        pprint(wav.read('out.wav')[1].shape)


    def test_create_actions_xml(self):
        """
        Test if the file action.xml is correctly created
        """
        new_file_name = "actions.xml"
        test_file_name = os.path.join("test_SAIEars", "test_xml_actions.xml")
        # create a sample file result
        assert self.saie.create_actions_xml() == 0
        # check if the new file correspond to the sample file result
        assert filecmp.cmp(new_file_name, test_file_name)
        # clean the file created
        if os.path.isfile(new_file_name):
            os.remove(new_file_name)


if __name__ == '__main__':
    unittest.main()
