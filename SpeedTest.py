import time
import unittest


class SpeedTest(unittest.TestCase):

    def test_speed_once(self, func, *args):
        beg = time.time()
        func(*args)
        end = time.time()
        return end - beg

    def test_speed_26_screenshot_in_one_second(self):
        """
        The goal is to mesurate how maximum can we take screen in less than a second
        """
        import threading
        import time
        from mss import mss
        import os

        import SAIEyes

        saie = SAIEyes.SAIEyes(eyes_dir="Speedtest", ctm_dir="Speedtest")

        def loop26():
            import d3dshot
            import os
            d = d3dshot.create()
            for i in range(26):
                name = "gross_"+str(i)
                print(name)
                # TODO find the best way
                # first way 9.029s => 2 img/s as a jpg 2.467s => 10 img/s
                #cs = saie.get_current_screen(name+".jpg")
                #saie.save_image_court_term_memory(cs, name + ".jpg")
                # second way 5.343s => 4 img/s as a jpg 2.68s => 10 img/s
                #import pyscreeze
                #pyscreeze._screenshot_win32(name+".png")
                # third way 4.658s => 5 img/s
                #with mss() as sct:
                #    print(sct.shot())
                    # rename monitor-1.png to name+".png"import os
                #    os.replace('monitor-1.png', name+".png")
                    #sct.save()
                # fourth way 4.909 => 5 img/s as a jpg 15 img/s
                d.screenshot_to_disk(directory=os.path.join("Speedtest", "CourtTermMemory"), file_name=name + ".jpg")

        my_thread = threading.Thread(target=loop26)
        my_thread.start()

        my_thread.join()

    def test_take_img_during_10_seconds(self):
        import time
        import d3dshot
        import os
        from datetime import datetime, timezone

        d = d3dshot.create()
        start = time.time()
        end = 0
        i = 0
        print("hello")
        # without current date 180 imgs => 18 img/s
        """while end - start < 10: 
            name = "gross_"+str(i)
            d.screenshot_to_disk(directory=os.path.join("Speedtest", "CourtTermMemory"), file_name=name + ".jpg")
            end = time.time()
            i += 1
        """
        # with current date and deleting on the directory 169 imgs => 16.9 imgs/s
        # with current date on the directory 183 imgs => 18 imgs/s
        while end - start < 10:
            d.screenshot_to_disk(directory=os.path.join("Speedtest", "CourtTermMemory"), file_name=datetime.today().strftime("%Y%m%d%H%M%S%f") + ".jpg")
            end = time.time()
            i += 1
        # TODO in one hour we get 18 Go of images to clean and we need to know how much we can extract different shape during this hour

    def test_take_img_during_one_hour(self):
        """
        Save one hour images
        """
        import time
        import d3dshot
        import os
        from datetime import datetime

        d = d3dshot.create()
        start = time.time()
        end = 0
        i = 0
        print("hello")
        # TODO How many images has been created ?
        while end - start < 3600:
            d.screenshot_to_disk(directory=os.path.join("Speedtest", "OneHour"), file_name=datetime.today().strftime("%Y%m%d%H%M%S%f") + ".jpg")
            end = time.time()
            i += 1

    def test_only_extract_shape_of_one_hour_images(self):
        """
        Extract the shape to one hour images to know what is the volume of the shape directory
        """
        # TODO for each images in directory Speedtest/OneHour
        # TODO      use class Shape to extract all the shape
        # TODO Get the size of the directory Speedtest/One_Hour_Shapes
        # TODO Optionnal 1: remove the duplicate shape
        # TODO Optionnal 2: remove the duplicate shape using a threshold

    def test_auto_click_and_move_during_taking_image_during_10_seconds(self):
        """
        This will test if SAI correctly save the inputs it use to do actions
        """
        # TODO Get a random action
        # TODO Start the saving in another thread during 10 seconds
        # TODO Do the random action during at least 3 seconds during 5 seconds

        # TODO Check if the database save the action
        # TODO Check if the directory contains images

    def test_auto_click_and_move_during_taking_image_during_1_minute(self):
        """
        This will test if SAI correctly save the inputs it use to do actions
        """
        # Implement the function create_db
        # Launch the db with SAIBrain
        # TODO Get a random action
        # Create a function random_point in the window in my_tools
        # TODO Start the saving in another thread during 60 seconds
        # Create a function Open in SAIEyes that will launch a thread that will save the images
        # TODO Do the random action during at least 3 seconds  during each 10 seconds
        # Use function move_mouse_to or left_click to do a random action and stock the action with the times
        # TODO Check if the database save the action
        # Select From action
        # TODO Check if the directory contains images
        # os.path.isfile() using Select From action, images

    def test_auto_click_and_move_during_taking_image_during_5_minute(self):
        """
        This will test if SAI correctly save the inputs it use to do actions
        """
        # TODO Get a random action
        # TODO Start the saving in another thread during 5 minutes
        # TODO Do the random action during at least 3 seconds  during each 30 seconds

        # TODO Check if the database save the action
        # TODO Check if the directory contains images

    def test_auto_click_and_move_during_taking_image_during_10_minute(self):
        """
        This will test if SAI correctly save the inputs it use to do actions
        """
        # TODO Get a random action
        # TODO Start the saving in another thread during 10 minutes
        # TODO Do the random action during at least 3 seconds during each 45 seconds

        # TODO Check if the database save the action
        # TODO Check if the directory contains images

    def test_auto_click_and_move_during_taking_image_during_30_minute(self):
        """
        This will test if SAI correctly save the inputs it use to do actions
        """
        # TODO Get a random action
        # TODO Start the saving in another thread during 30 minutes
        # TODO Do the random action during at least 3 seconds during each 45 seconds

        # TODO Check if the database save the action
        # TODO Check if the directory contains images

    def test_synthetisis_images_from_30_minutes_autoclick(self):
        """
        This will test if SAI correctly reduce images
        """
        # TODO Reduce the files as the shape
        # TODO                  as a new representation of the images less heavy

    def test_auto_click_and_move_during_taking_image_during_60_minute_with_syntethisis(self):
        """
        This will test if SAI correctly save the inputs it use to do actions
        """
        # TODO Get a random action
        # TODO Start the saving in another thread during 30 minutes
        # TODO Do the random action during at least 3 seconds during each 45 seconds

        # TODO Check if the database save the action
        # TODO Check if the directory contains images
        # TODO Then reduce the files as the shape
        # TODO                       as a new representation of the images less heavy




    def test_speed(self, func, *args, nb_test=10):
        sum = 0
        for i in range(nb_test):
            sum += self.test_speed_once(func, *args)
        return sum/nb_test


if __name__ == '__main__':
    unittest.main()