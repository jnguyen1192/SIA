import psycopg2
import docker
import time
import subprocess
import os

import tools.docker_tools as dtt


def run_db(port=5432):
    """
    Create the postgres container and run it
    :return: 0 if it works else -1
    """
    client = docker.from_env()
    try:
        #@source https://github.com/docker/for-win/issues/445
        #docker volume create --name postgres-data-volume -d local
        #volumes = {"/c/Users/johdu/PycharmProjects/SAI/backup_postgres":
        # shared folder on oracle vm : C:\Users\johdu\PycharmProjects\SAI\backup_postgres:/mnt/sda1/var/lib/docker/volumes/postgres-data-volume/_data
        # Backup http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows
        volumes = {"postgres-data-volume":
                       {'bind': '/var/lib/postgresql/data/', 'mode': 'rw'}
                   }
        ports = {'5432/tcp': port}
        environment = ["POSTGRES_DB=postgres",
                       "POSTGRES_USER=postgres",
                       "POSTGRES_PASSWORD=postgres"]
       # fo = open("C:/Users/johdu/PycharmProjects/SAI/Dockerfile.postgres", "r")
        # docker build -f Dockerfile.postgres . -t c_sai_postgres
        #client.images.build(fileobj=fo, tag="c_sai_postgres", custom_context=True)
        #print("Image building...")
        #print("Image builded")
        # restart a container
        dtt.clean_container("c_sai_postgres")

        # to test pg database https://www.enterprisedb.com/download-postgresql-binaries
        # to connect to the database enter the ip of docker
        container = client.containers.run(image="c_sai_postgres",
                                    name="c_sai_postgres",
                                    pid_mode="host",
                                    volumes=volumes,
                                    ports=ports,
                                    environment=environment,
                                    detach=True)
        # TODO debug log here
        print("Création de l'image terminée")
        #print(container.logs().decode('utf8'))
        #print("after postgres run")
        client.close()
        return 0
    except Exception as e:
        print(e)
        client.close()
        return -1


def get_pwd():
    res = subprocess.run(['cmd', '/c', 'echo', '%cd%'], capture_output=True)
    pwd = res.stdout.decode('utf8')
    pwd_path = os.path.join(pwd)
    pwd_path_split = pwd_path.split("\\")
    if "test" in pwd_path_split[-1]:
        pwd = "\\".join(pwd_path_split[:-1])
    return pwd


def create_image_using_dockerfile(name):
    """
    Create the image to backup
    :return: 0 if it works else -1
    """
    client = docker.from_env()
    try:
        # TODO Option 1: need to use the correct folder to use this command in docker-machine
        #fo = open("C:/Users/johdu/PycharmProjects/SAI/Dockerfile.backup", "r")
        #print(fo)
        #
        #print("Before images build")
        # TODO Option 2 : use subprocess to use cmd from win
        # Prod way
        res = subprocess.run(["docker", "build", "-f", os.path.join(get_pwd(), "Dockerfile." + name), ".", "-t", "c_sai_"+ name],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res != 0:
            # Dev way
            res = subprocess.run(["docker", "build", "-f", "C:/Users/anthony/PycharmProjects/SAI/Dockerfile.backup", ".", "-t", "c_sai_"+ name])

        # docker build -f Dockerfile.backup . -t c_sai_backup
        #print(type(res.returncode), res.returncode)
        return res.returncode
        #client.images.build(fileobj=fo, tag="c_sai_backup", custom_context=True)
    except Exception as e:
        print(e)
        client.close()
        return -1


def run_backup():
    """
    Create the container which will backup the db on a windows share folder
    :return: 0 if it works else -1
    """

    client = docker.from_env()
    try:
        #@source https://github.com/docker/for-win/issues/445
        #docker volume create --name postgres-data-volume -d local
        #volumes = {"/c/Users/johdu/PycharmProjects/SAI/backup_postgres":
        # shared folder on oracle vm : C:\Users\johdu\PycharmProjects\SAI\backup_postgres:/mnt/sda1/var/lib/docker/volumes/postgres-data-volume/_data
        # Backup http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows
        volumes = {"postgres-data-volume":
                       {'bind': '/var/lib/postgresql/data/', 'mode': 'rw'}
                   }
        environment = ["POSTGRES_DB=postgres",
                       "POSTGRES_USER=postgres",
                       "POSTGRES_PASSWORD=postgres"]
        #print("Image building...")
        #print("Image builded")
        # restart a container
        dtt.clean_container("c_sai_backup")

        # to test pg database https://www.enterprisedb.com/download-postgresql-binaries
        # to connect to the database enter the ip of docker
        container = client.containers.run(image="c_sai_backup",
                                    name="c_sai_backup",
                                    pid_mode="host",
                                    volumes=volumes,
                                    environment=environment,
                                    detach=True)
        # TODO debug log here
        #print(container.logs().decode('utf8'))
        #print("after postgres run")
        client.close()
        return 0
    except Exception as e:
        print(e)
        client.close()
        return -1


def wait_db_connection(nb_retry=10, time_sleep=60):
    """
    Wait the database connection
    :return: 0 if it works else -1
    """
    i = 0
    time.sleep(40)
    while i < nb_retry:
        try:
            psycopg2.connect(user="postgres",
                              password="postgres",
                              host="192.168.99.100",
                              port="5432",
                              database="postgres")
            print("Connexion worked")
            return 0
        except Exception as e:
            #print(e)
            # TODO print all the functions called before
            print(wait_db_connection.__name__,": I wait", time_sleep, "seconds until try again,", nb_retry - i - 1, "remaining test cycle")
            time.sleep(time_sleep)
            i = i + 1
    return -1


# TODO connect to the database with the correct credentials and refactor


# TODO create function to use a query without parameters
def query_without_parameters(query_without_parameters):
    """
    Create a query on the database without parameters
    :return: 0 if it works else -1
    """
    connection = ""
    cursor = ""
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
        cursor = connection.cursor()


        cursor.execute(query_without_parameters)
        connection.commit()
        print("Query without parameters executed successfully in PostgreSQL ")
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while executing query in PostgreSQL", error)
        return -1
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# TODO create function to use a query with parameters
def query_with_parameters(query, parameters):
    """
    Create a query on the database without parameters
    :return: 0 if it works else -1
    """
    connection = ""
    cursor = ""
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="192.168.99.100",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        print(query)
        print(parameters)
        cursor.execute(query, parameters)
        connection.commit()
        print("Query with parameters executed successfully in PostgreSQL ")
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while executing query with parameters in PostgreSQL", error)
        return -1
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def select_one_with_parameters(query, parameters):
    """
    Select one result on the database with parameters
    :return: 0 if it works else -1
    """
    connection = ""
    cursor = ""
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="192.168.99.100",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        #print(query)
        #print(parameters)
        cursor.execute(query, parameters)
        res = cursor.fetchone()
        #print("Query with parameters executed successfully in PostgreSQL ")
        return res[0]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while executing query with parameters in PostgreSQL", error)
        return -1
    finally:
        if connection:
            # closing database connection.
            cursor.close()
            connection.close()

def new_backup():
    """
    Create a backup using the corresponding container
    :return: 0 if it works else -1
    """
    # TODO
    #   Use this command to connect to the DB on the container
    #       PGPASSWORD=postgres pgsql -h 192.168.99.100 -p 5432 -U postgres

    return 0
