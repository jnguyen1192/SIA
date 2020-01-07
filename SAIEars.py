import speech_recognition as sr
import pyautogui

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

    def create_actions_xml(self):
        """
        Create the file actions.xml using a predefine list
        :return: 0 if it works else -1
        """
        # TODO
        #   The files will have actions
        #   For each action, it can be:
        #       - name
        #       - param1 (optionnaly)
        #           . min
        #           . max
        #       - param2 (optionnaly)
        #           . min
        #           . max
        #       - param3 (optionnaly)
        #           . min
        #           . max
        actions = []
        # TODO action move
        move_width, move_height = pyautogui.size()
        actions.append(("move", (0, move_width), (0, move_height)))
        # TODO action left click
        actions.append(("left_click", ()))
        # TODO action hold left click
        actions.append(("hold_left_click", ()))
        # TODO action release left click
        actions.append(("release_left_click", ()))
        # TODO action right click
        actions.append(("right_click", ()))
        # TODO action hold right click
        actions.append(("hold_right_click", ()))
        # TODO action release right click
        actions.append(("release_right_click", ()))
        # TODO action sleep
        actions.append(("release_right_click", (1, self.TIME_TO_WAIT_MAX)))
        # TODO create the xml file with the list
        return -1

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
