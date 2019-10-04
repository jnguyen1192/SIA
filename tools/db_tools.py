import psycopg2
import docker
from docker.utils import kwargs_from_env


# TODO create the container with its credentials
def run_db(port=5432):
    """
    Create the postgres container and run it
    :return: 0 if it works else -1
    """
    try:
        client = docker.from_env()
        #@source https://github.com/docker/for-win/issues/445
        #docker volume create --name postgres-data-volume -d local
        #volumes = {"/c/Users/johdu/PycharmProjects/SAI/data_postgres":
        # shared folder on oracle vm : C:\Users\johdu\PycharmProjects\SAI\data_postgres:/mnt/sda1/var/lib/docker/volumes/postgres-data-volume/_data
        volumes = {"postgres-data-volume":
                       {'bind': '/var/lib/postgresql/data/', 'mode': 'rw'}
                   }
        fo = open("C:/Users/johdu/PycharmProjects/SAI/Dockerfile.postgres", "r")
        #print("Image building...")
        #client.images.build(fileobj=fo, tag="postgres", custom_context=True)
        #print("Image builded")
        kwargs = kwargs_from_env()
        # @source : https://github.com/qazbnm456/tsaotun/blob/master/tsaotun/lib/docker_client.py
        api_client = docker.APIClient(**kwargs)
        # TODO stop current c_sai_daemon
        for c in client.containers.list():
            if c.__getattribute__("name") == "c_sai_postgres":
                api_client.kill("c_sai_postgres")
        # TODO rm current c_sai_daemon
        for c in client.containers.list(all=True):
            if c.__getattribute__("name") == "c_sai_postgres":
                api_client.remove_container("c_sai_postgres")
        #print("Before postgres run")
        # to test pg database https://www.enterprisedb.com/download-postgresql-binaries
        container = client.containers.run(image="c_sai_postgres",
                                    name="c_sai_postgres",
                                    pid_mode="host",
                                    volumes=volumes,
                                    ports={'5432/tcp': port},
                                    detach=True)

        print(container.logs().decode('utf8'))
        print("after postgres run")
        return 0
    except Exception as e:
        print(e)
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
                                      password="pass@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
        cursor = connection.cursor()


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
