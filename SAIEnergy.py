import psutil

import logging


class SAIEnergy:
    def __init__(self, threshold_RAM=90, level=logging.INFO):
        self.threshold_RAM = threshold_RAM
        logging.basicConfig(level=level)

    def get_current_RAM_percent(self):
        # use psutil to get the RAM available
        return psutil.virtual_memory().percent

    def is_RAM_almost_full(self):
        return self.threshold_RAM < self.get_current_RAM_percent()
