import docker
from docker.utils import kwargs_from_env


def is_image_exist(name):
    """
    Check if an imag exist
    :param name: the name of the image
    :return: True if it works else False
    """
    client = docker.from_env()
    images_raws = client.images.list()
    images = [image.tags[0] for image in images_raws if image.tags != []]
    client.close()
    if name not in [image.split(":")[0] for image in images if image != ""]:
        return False
    return True


def clean_container(name):
    """
    Run the correponding container using the same image and container name
    :param client: the docker client
    :param api_client: the docker client api
    :param name_container: the container name
    :return: 0 if it works else -1
    """
    client = docker.from_env()
    kwargs = kwargs_from_env()
    api_client = docker.APIClient(**kwargs)
    try:
        # TODO stop current c_sai_daemon
        for c in client.containers.list():
            if c.__getattribute__("name") == name:#"c_sai_postgres":
                api_client.kill(name)#"c_sai_postgres")
        # TODO rm current c_sai_daemon
        for c in client.containers.list(all=True):
            if c.__getattribute__("name") == name:#"c_sai_postgres":
                api_client.remove_container(name)#"c_sai_postgres")
        client.close()
        api_client.close()
        return 0
    except Exception as e:
        print(e)
        client.close()
        api_client.close()
        return -1

