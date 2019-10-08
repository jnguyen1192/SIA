import unittest
import tools.db_tools as dbt
import tools.sql_queries as sqt
import tools.docker_tools as dtt

import docker
from docker.utils import kwargs_from_env


class Testdb_tools(unittest.TestCase):

    # @source:http://stezz.blogspot.com/2011/04/calling-only-once-setup-in-unittest-in.html
    ClassIsSetup = False
    ClassIsTeardown = 1
    ClassIsTeardownTotal = 6 # nb total of unittest

    def setUp(self):
        if not self.ClassIsSetup:
            # run db container
            try:
                res = dbt.run_db()
            except Exception as e:
                print(e)
                res = -1
            # wait database connection
            dbt.wait_db_connection()
            assert (res == 0)
            self.__class__.ClassIsSetup = True

    def tearDown(self):
        if self.ClassIsTeardown == self.ClassIsTeardownTotal:  # the number of test case
            # stop and remove db container
            dtt.clean_container("c_sai_postgres")
        else:
            self.__class__.ClassIsTeardown = self.ClassIsTeardown + 1

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
