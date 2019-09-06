import unittest
import docker
import SpeedTest
import SAIEyes


class TestCoreFunctions(unittest.TestCase):
    def test_0(self):
        res = 0
        pred = 0
        assert (pred == res)

    def test_code_profiling(self):

        st = SpeedTest.SpeedTest()

        def t_s():
            se = SAIEyes.SAIEyes()
            se.get_current_screen()
        print(st.test_speed(t_s))

    def test_docker_ubuntu(self):
        client = docker.from_env()
        print(client)
        # client.images.pull('ubuntu')
        # for image in client.images.list():
        #    print(image.id)
        # print(client.containers.run("ubuntu", "echo hello world"))


    def test_temp(self):
        import wmi
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature':
                print(sensor.Name)
                print(sensor.Value)


if __name__ == '__main__':
    unittest.main()
