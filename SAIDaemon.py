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

            from docker.utils import kwargs_from_env
            kwargs = kwargs_from_env()
            # @source : https://github.com/qazbnm456/tsaotun/blob/master/tsaotun/lib/docker_client.py
            api_client = docker.APIClient(**kwargs)
            print(api_client.version())

            print(os.getcwd())
            """
            print(api_client.create_container(image="sai_daemon", host_config=api_client.create_host_config(binds=[
                    os.getcwd() + ':/code/',
                ])).decode('utf8'))
            """

            #print(client.containers.run("sai_daemon").decode('utf8'))
            #print(img)

        except Exception as e:
            logging.error("Build function don't work because " + str(e))
            return -1
        # TODO the daemon has been correctly build
        return 0

    def hello_world(self):
        # TODO the daemon says hello world
        return "hello world"

