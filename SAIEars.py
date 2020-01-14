import speech_recognition as sr
import pyautogui
import xml.etree.ElementTree as ET  # create xml file
from xml.dom import minidom  # pretty print on xml file

import pyaudio
import numpy


class SAIEars:
    """
    This class is used to microphone as an input
    """
    TIME_TO_WAIT_MAX = 10

    def __init__(self):
        # TODO implement
        # create actions.xml using a predefine list if it isn't correspondant
        pass
    # TODO use test_speech_recognition.py
    #       1) ask for a command and initiate the position
    #       2) do a random command
    #       3) ask for answer yes/no
    #       4) if yes stock on db command and random command
    #       loop to 1

    def create_actions_xml(self, file_name="actions.xml"):
        """
        Create the file actions.xml using a predefine list
        The files will have actions
        For each action, it can be:
           - name
           - param1 (optionnaly)
               . min
               . max
           - param2 (optionnaly)
               . min
               . max
           - param3 (optionnaly)
               . min
               . max
        :return: 0 if it works else -1
        """
        try:
            actions = []
            # action move
            move_width, move_height = pyautogui.size()
            actions.append(("move", ((0, move_width), (0, move_height))))
            # action left click
            actions.append(("left_click", ()))
            # action hold left click
            actions.append(("hold_left_click", ()))
            # action release left click
            actions.append(("release_left_click", ()))
            # action right click
            actions.append(("right_click", ()))
            # action hold right click
            actions.append(("hold_right_click", ()))
            # action release right click
            actions.append(("release_right_click", ()))
            # action sleep
            actions.append(("sleep", ((1, self.TIME_TO_WAIT_MAX), )))
            # create the xml file with the list
            # create the file structure
            actions_xml = ET.Element('actions')
            for action in actions:
                action_name, params = action
                cur_action = ET.SubElement(actions_xml, "action")
                cur_name = ET.SubElement(cur_action, "name")
                cur_name.set("value", action_name)
                for index, param in enumerate(params):
                    cur_param = ET.SubElement(cur_action, "param" + str(index+1))
                    min = ET.SubElement(cur_param, "min")
                    min.set("value", str(param[0])) #  convert to str for xml file
                    max = ET.SubElement(cur_param, "max")
                    max.set("value", str(param[1]))

            # create a new XML file with the results
            my_actions_xml = minidom.parseString(ET.tostring(actions_xml)).toprettyxml(indent="   ")

            actions_xml_file = open(file_name, "w")
            actions_xml_file.write(my_actions_xml)
            actions_xml_file.close()
            return 0
        except Exception as e:
            print(e)
            return -1

    def get_next_sound_detected(self, RATE=16000, RECORD_SECONDS=3600, CHUNKSIZE = 1024, MIN_VOLUME = 100):
        """
        Get the next sound detected from the microphone as a numpy array
        :param RATE: time resolution of the recording device (Hz)
        :param RECORD_SECONDS: number of seconds we want the detector will wait a sound (it can be infinite)
        :param CHUNKSIZE: width between each data from microphone input
        :param MIN_VOLUME: minimum volume of noise to start and end the sound detection
        :return: numpy array representing the detected sound
        """
        # initialize portaudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNKSIZE)

        # parse the microphone input in a numpy array
        begin = False
        frames = []  # A python-list of chunks(numpy.ndarray)
        for _ in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
            data = stream.read(CHUNKSIZE)
            frame = numpy.fromstring(data, dtype=numpy.int16)
            if max(frame) > MIN_VOLUME:
                begin = True
            # print(max(frame))
            if begin:
                frames.append(frame)
            if max(frame) < MIN_VOLUME and begin:
                break

        # Convert the list of numpy-arrays into a 1D array (column-wise)
        numpydata = numpy.hstack(frames)

        # close stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        return numpydata

    def get_command(self):
        """
        Get the microphone input
        :return: the input as a text or -1
        """
        # TODO implement
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            try:
                return r.recognize_sphinx(audio)
            except sr.UnknownValueError:
                return self.get_command()
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))
                return -1

    def is_listen(self, method):
        """
        Check if the sound is in one of the methods using the db
        :param method: the name of the method we want to check, it can be "reward" or "penalize"
        :return: True if it is else False
        """
        # TODO to implement
        return True
