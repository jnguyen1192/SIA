import os
import docker
import logging


class SAIDaemon:
    """
    The appearence of the SIA
    """
    def build(self):
        try:
            client = docker.from_env()
            img = client.images.build(path=os.getcwd(), tag="sai_daemon")
            print(client.containers.run("sai_daemon").decode('utf8'))
            #print(img)

        except Exception as e:
            logging.error("Build function don't work because " + str(e))
            return -1
        # TODO the daemon has been correctly build
        return 0

    def hello_world(self):
        # TODO the daemon says hello world
        return "hello world"

