import docker
import logging

class SAIDaemon:
    """
    The appearence of the SIA
    """
    def build(self):
        try:
            client = docker.from_env()
            print(client.containers.run("ubuntu", "echo hello world").decode('utf8'))

        except Exception as e:
            logging.error("Build function don't work because " + str(e))
            return -1
        # TODO the daemon has been correctly build
        return 0

    def hello_world(self):
        # TODO the daemon says hello world
        return "hello world"

