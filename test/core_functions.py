import unittest

import docker
import os
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
        print(client.containers.run("ubuntu", "echo hello world"))

    def test_docker_dockerfile(self):
        client = docker.from_env()

        img = client.images.build(path=os.getcwd())


        print(img)
        from pprint import pprint
        client.images.prune(filters={'dangling': False})
        pprint(client.images.list())
        from datetime import datetime
        client.containers.prune(filters={'until': datetime.timestamp(datetime.now())})
        pprint(client.containers.list(all=True))

        pprint(client.containers.list())

    def test_temp(self):
        import wmi
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature':
                print(sensor.Name)
                print(sensor.Value)

    def test_ip(self):
        import socket
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(socket.gethostname())
        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is:" + IPAddr)


if __name__ == '__main__':
    unittest.main()
