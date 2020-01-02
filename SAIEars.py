import speech_recognition as sr


class SAIEars:
    """
    This class is used to microphone as an input
    """
    # TODO use test_speech_recognition.py

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
