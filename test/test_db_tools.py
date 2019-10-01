import unittest
import tools.db_tools as dbt


class Testdb_tools(unittest.TestCase):

    def test_db_tools_run_db_case_ok(self):
        # TODO implement
        assert (dbt.run_db() == 0)

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
