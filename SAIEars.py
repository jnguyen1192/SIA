import speech_recognition as sr


class SAIEars:
    """
    This class is used to microphone as an input
    """
    # TODO use test_speech_recognition.py

    def get_command(self):
        """
        Get the microphone input
        :return: the input as a text
        """
        # TODO implement
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        return audio
