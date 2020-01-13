import unittest
import SAIEars

import filecmp
import os


class TestSAIEars(unittest.TestCase):

    def setUp(self):
        self.saie = SAIEars.SAIEars()

    def test_SAIEars_analyse_microphone(self):
        # TODO
        #   Use those data to only record when there was a sound of a voice using dynamic deep reinforcement learning
        RATE = 16000
        numpydata = self.saie.get_next_sound_detected(RATE)


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

    def test_is_listen_reward(self):
        """
        Test if the sound listened is a reward
        """
        # TODO implement
        pass

    def test_is_listen_penalize(self):
        """
        Test if the sound listened is a penalize
        """
        # TODO implement
        pass

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
