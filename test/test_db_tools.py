import unittest
import tools.db_tools as dbt
import tools.sql_queries as sqt
import tools.docker_tools as dtt

import docker
from docker.utils import kwargs_from_env


class Testdb_tools(unittest.TestCase):

    def setUp(self):
        # run db container
        res = -1
        try:
            res = dbt.run_db()
        except Exception as e:
            print(e)
            res = -1
        # todo wait database connection

        assert (res == 0)

    def tearDown(self):
        # stop and remove db container
        dtt.clean_container("c_sai_daemon")

    def test_db_tools_all_tables_created(self):
        """
        Test if all the tables are created
        :return:
        """
        tables_name = ['Strategie', 'Action', 'Has_action']
        for name in tables_name:
            assert(dbt.select_one_with_parameters(sqt.IS_TABLE_EXISTS, (name, )))

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
