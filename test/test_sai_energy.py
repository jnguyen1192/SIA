import unittest
import SAIEnergy


class TestSAIEnergy(unittest.TestCase):
    def test_SAIEnergy_RAM_percent(self):
        saie = SAIEnergy.SAIEnergy()
        print(saie.get_current_RAM_percent())

    def test_SAIEnergy_is_RAM_almost_available(self):
        saie = SAIEnergy.SAIEnergy()
        assert(not saie.is_RAM_almost_full())


if __name__ == '__main__':
    unittest.main()
