import psycopg2
import docker
import time

from docker.utils import kwargs_from_env
import tools.sql_queries

import tools.docker_tools as dtt


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
        ports = {'5432/tcp': port}
        environment = ["POSTGRES_DB=postgres",
                       "POSTGRES_USER=postgres",
                       "POSTGRES_PASSWORD=postgres"]
       # fo = open("C:/Users/johdu/PycharmProjects/SAI/Dockerfile.postgres", "r")
        # docker build -f Dockerfile.postgres . -t c_sai_postgres
        #client.images.build(fileobj=fo, tag="c_sai_postgres", custom_context=True)
        #print("Image building...")
        #print("Image builded")
        kwargs = kwargs_from_env()
        # @source : https://github.com/qazbnm456/tsaotun/blob/master/tsaotun/lib/docker_client.py
        api_client = docker.APIClient(**kwargs)
        # restart a container
        dtt.clean_container("c_sai_postgres")

        # to test pg database https://www.enterprisedb.com/download-postgresql-binaries
        # to connect to the database enter the ip of docker
        container = client.containers.run(image="c_sai_postgres",
                                    name="c_sai_postgres",
                                    pid_mode="host",
                                    #volumes=volumes,
                                    ports=ports,
                                    environment=environment,
                                    detach=True)
        # TODO debug log here
        #print(container.logs().decode('utf8'))
        #print("after postgres run")
        return 0
    except Exception as e:
        print(e)
        return -1


# TODO Wait database connection
def wait_db_connection(nb_retry=10, time_sleep=60):
    """
    Wait the database connection
    :return: 0 if it works else -1
    """
    i = 0
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
            print("I wait", time_sleep, "seconds until try again,", nb_retry - i - 1, "remaining test cycle")
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
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")
