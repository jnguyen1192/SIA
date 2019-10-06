import unittest
import tools.db_tools as dbt

import docker
from docker.utils import kwargs_from_env


class Testdb_tools(unittest.TestCase):

    def test_db_tools_run_db_case_ok(self):
        """
        Test if the database is running
        :return:
        """
        res = -1
        try:
            res = dbt.run_db()

            client = docker.from_env()
            kwargs = kwargs_from_env()
            api_client = docker.APIClient(**kwargs)
            # TODO stop current c_sai_daemon
            # TODO test the connection
            #for c in client.containers.list():
            #    if c.__getattribute__("name") == "c_sai_postgres":
            #        api_client.kill("c_sai_postgres")
            # TODO rm current c_sai_daemon
            #for c in client.containers.list(all=True):
            #    if c.__getattribute__("name") == "c_sai_postgres":
            #        api_client.remove_container("c_sai_postgres")
        except Exception as e:
            print(e)
            res = -1

        assert (res==0)

    def test_db_tools_run_db_case_nok(self):
        # TODO implement
        assert (False == False)

    def test_db_tools_query_without_parameters_case_ok(self):
        # TODO implement
        assert (True == True)

    def test_db_tools_query_without_parameters_case_nok(self):
        # TODO implement
        assert (False == False)

    def test_db_tools_query_with_parameters_case_ok(self):
        # TODO implement
        assert (True==True)

    def test_db_tools_query_with_parameters_case_nok(self):
        # TODO implement
        assert (False==False)


if __name__ == '__main__':
    unittest.main()
