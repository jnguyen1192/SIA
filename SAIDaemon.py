import os
import docker
import socket
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
            # TODO only if images changes
            #img = client.images.build(path=path_dockerfile, tag="sai_daemon")

            kwargs = kwargs_from_env()
            # @source : https://github.com/qazbnm456/tsaotun/blob/master/tsaotun/lib/docker_client.py
            api_client = docker.APIClient(**kwargs)
            print(api_client.version())
            print(os.getcwd()[2:])
            print("Docker run ---------->")
            #/Users/johdu/PycharmProjects/SAI/test
            # run container
            # TODO stop current c_sai_daemon
            for c in client.containers.list():
                if c.__getattribute__("name") == "c_sai_daemon":
                    api_client.kill("c_sai_daemon")
            # TODO rm current c_sai_daemon
            for c in client.containers.list(all=True):
                if c.__getattribute__("name") == "c_sai_daemon":
                    api_client.remove_container("c_sai_daemon")
            # @source : http://www.geo.mtu.edu/geoschem/docs/putty_install.html
            # @source : https://github.com/asweigart/pyautogui/issues/124
            # https://github.com/niranjanshr13/Automate_Linux_with_GAssistant probably use or not
            # TODO test if the ip is the real ip
            IPAddr = socket.gethostbyname_ex(socket.gethostname())[-1][-1]  # socket.gethostbyname(socket.gethostname())
            #print("other ", socket.gethostbyname_ex(socket.gethostname())[-1][-1])
            #print(socket.gethostname(), " with 99, it's a docker tools ip")
            print("Is is the real ip ?", IPAddr)


            #environment = {"DISPLAY": IPAddr + ':0.0'}
            environment = {"DISPLAY": '192.168.43.214:0.0'}
            volumes = {"/c/Users/johdu/PycharmProjects/SAI":
                           {'bind': '/code/', 'mode': 'rw'}
                       }
            # volume : src:dest
            print(client.containers.run(image="sai_daemon",
                                        name="c_sai_daemon",
                                        volumes=volumes,
                                        environment=environment).decode('utf8'))
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

