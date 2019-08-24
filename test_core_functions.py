import unittest
import SAIEyes
import SAIEnergy
import docker


class TestCoreFunctions(unittest.TestCase):
    def test_0(self):
        res = 0
        pred = 0
        assert (pred == res)

    def test_SAIEyes_get_screen(self):
        saie = SAIEyes.SAIEyes()
        print(saie.get_current_screen())

    def test_SAIEyes_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button = list(saie.get_pos_all_close_button())
        for close_button in all_close_button:
            x, y, width, height = close_button
            print(close_button)
            saie.move_to(x + width/2, y + height/2)

    def test_SAIEyes_crop_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button_generator = saie.get_pos_all_close_button()  # 0.052 s
        screen = saie.get_current_screen()  # 0.198 s
        try:
            x, y, w, h = next(all_close_button_generator)
            cropped_example = screen.crop((x, y, x+w, y+h))
            saie.save_image_court_term_memory(cropped_example)
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_rectangle_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button_generator = saie.get_pos_all_close_button()  # 0.052 s
        screen = saie.get_current_screen()  # 0.198 s
        try:
            saie.clean_ctm()
            x, y, w, h = next(all_close_button_generator)
            saie.save_image_with_rectangle_court_term_memory((x, y, x+w, y+h))
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_rectangles_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button_generator = saie.get_pos_all_close_button()  # 0.052 s
        screen = saie.get_current_screen()  # 0.198 s
        try:
            saie.clean_ctm()
            saie.save_image_with_rectangles_court_term_memory(all_close_button_generator)
        except Exception as e:
            print("No button found", e)

    def test_SAIEyes_clean_ctm(self):
        saie = SAIEyes.SAIEyes()
        saie.clean_ctm()
        assert saie.count_ctm_files() == 0

    def test_docker_ubuntu(self):
        client = docker.from_env()
        print(client)
        # client.images.pull('ubuntu')
        # for image in client.images.list():
        #    print(image.id)
        # print(client.containers.run("ubuntu", "echo hello world"))

    def test_cpu(self):
        # !/usr/bin/env python
        import psutil
        # gives a single float value
        print("psutil.cpu_percent()", psutil.cpu_percent())
        # gives an object with many fields
        print("psutil.virtual_memory().percent ", psutil.virtual_memory().percent)
        # you can convert that object to a dictionary
        #print(dict(psutil.virtual_memory()._asdict()))
        print("psutil.swap_memory().percent ", psutil.swap_memory().percent)
        # battery
        print("psutil.sensors_battery().percent ", psutil.sensors_battery().percent)
        # temperature
        #print("psutil.sensors_temperatures() ",  psutil.sensors_temperatures())
        print(psutil.__version__)

    def test_temp(self):
        import wmi
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature':
                print(sensor.Name)
                print(sensor.Value)

    def test_RAM_percent(self):
        saie = SAIEnergy.SAIEnergy()
        print(saie.get_current_RAM_percent())

    def test_is_RAM_almost_available(self):
        saie = SAIEnergy.SAIEnergy()
        assert(not saie.is_RAM_almost_full())



if __name__ == '__main__':
    unittest.main()
