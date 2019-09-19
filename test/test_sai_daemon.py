import unittest
import SAIDaemon


class TestSAIDaemon(unittest.TestCase):

    def setUp(self):
        self.said = SAIDaemon.SAIDaemon()

    def test_SAIDaemon_build(self):
        assert (self.said.build('C:\\Users\\johdu\\PycharmProjects\\SAI') == 0)

    def test_SAIDaemon_build_test(self):
        assert(self.said.build() == 0)

    def test_SAIEnergy_hello_world(self):
        assert(self.said.hello_world() == "hello world")


if __name__ == '__main__':
    unittest.main()
