import psycopg2
import docker


# TODO create the container with its credentials
def run_db():
    """
    Create the postgres container and run it
    :return: 0 if it works else -1
    """
    try:
        client = docker.from_env()
        volumes = {"/c/Users/johdu/PycharmProjects/SAI/data_postgres":
                       {'bind': '/var/lib/postgresql/data/', 'mode': 'rw'}
                   }

        print(client.containers.run(image="postgres",
                                    name="c_sai_postgres",
                                    volumes=volumes).decode('utf8'))
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
