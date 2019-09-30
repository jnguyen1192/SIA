import psycopg2
from psycopg2 import Error


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
        print("Query executed successfully in PostgreSQL ")
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
