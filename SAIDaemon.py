import os
import docker
import logging

from docker.utils import kwargs_from_env


class SAIDaemon:
    """
    The appearence of the SIA
    """
    def build(self, path_dockerfile=''):
        if path_dockerfile == '':
            path_dockerfile = os.getcwd()
        client = None
        api_client = None
        try:
            client = docker.from_env()
            img = client.images.build(path=path_dockerfile, tag="sai_daemon")

            kwargs = kwargs_from_env()
            # @source : https://github.com/qazbnm456/tsaotun/blob/master/tsaotun/lib/docker_client.py
            api_client = docker.APIClient(**kwargs)
            print(api_client.version())
            print(os.getcwd()[2:])

            # run container
            print(client.containers.run(image="sai_daemon", name="c_sai_daemon", volumes={'/code/': {'bind': os.getcwd()[2:], 'mode': 'rw'}}).decode('utf8'))
            # create container
            """
            resp = api_client.create_container(image="sai_daemon", name="container_sai_daemon", host_config=api_client.create_host_config(binds=[
                    '/code/:' + os.getcwd()[2:],
                ]))
            container = client.containers.get(resp['Id'])
            container.start()
            """
            client.close()
            api_client.close()
            #print(client.containers.run("sai_daemon").decode('utf8'))
            #print(img)

        except Exception as e:
            logging.error("Build function don't work because " + str(e))
            client.close()
            api_client.close()
            return -1
        # TODO the daemon has been correctly build
        return 0

    def hello_world(self):
        # TODO the daemon says hello world
        return "hello world"

