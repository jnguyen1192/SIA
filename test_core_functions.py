import unittest
import SAIEyes
import docker


class TestCoreFunctions(unittest.TestCase):
    def test_0(self):
        res = 0
        pred = 0
        assert(pred == res)

    def test_SAIEyes_get_screen(self):
        saie = SAIEyes.SAIEyes()
        print(saie.get_current_screen())

    def test_SAIEyes_locate_screen(self):
        saie = SAIEyes.SAIEyes()
        all_close_button = list(saie.get_pos_all_close_button())
        for close_button in all_close_button:
            x, y, width, height = close_button
            print(all_close_button[0])
            saie.move_to(x + width/2, y + height/2)

    def test_docker_ubuntu(self):
        client = docker.from_env()
        print(client)
        #client.images.pull('ubuntu')
        #for image in client.images.list():
        #    print(image.id)
        #print(client.containers.run("ubuntu", "echo hello world"))


if __name__ == '__main__':
    unittest.main()
