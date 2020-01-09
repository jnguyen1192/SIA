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
