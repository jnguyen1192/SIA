import unittest
import tools.db_tools as dbt
import tools.sql_queries as sqt
import tools.docker_tools as dtt


class TestDb_tools(unittest.TestCase):

    # @source:http://stezz.blogspot.com/2011/04/calling-only-once-setup-in-unittest-in.html
    ClassIsSetup = False
    ClassIsTeardown = 1
    # TODO automaticly count the number of unittest
    ClassIsTeardownTotal = 6 # nb total of unittest

    def setUp(self):
        # TODO run db backup container
        if not self.ClassIsSetup:
            # run db container
            try:
                if not dtt.is_image_exist("c_sai_postgres"):
                    res = dbt.create_image_using_dockerfile("postgres")
                    if res == -1:
                        raise Exception("Image not created correctly")
                if not dtt.is_container_exist("c_sai_postgres"):
                    res = dbt.run_db()
                else:
                    res = 0
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
            pass#dtt.clean_container("c_sai_postgres")
        else:
            self.__class__.ClassIsTeardown = self.ClassIsTeardown + 1

    def test_db_tools_all_tables_created(self):
        """
        Test if all the tables are created
        """
        tables_name = ['Strategie', 'Action', 'Has_action']
        for name in tables_name:
            res = dbt.select_one_with_parameters(sqt.IS_TABLE_EXISTS, (name,))
            assert(res != -1)
            assert(res == True)

    def test_create_image_backup(self):
        """
        Test if the image for backup is correctly build
           1) Create the image
           2) Check using docker client if the image is correctly added
           3) Optionally: check if all library are in the container
               docker run -it --name c_sai_backup c_sai_backup dpkg -s postgresql
               docker rm c_sai_backup
               docker run -it --name c_sai_backup c_sai_backup dpkg -s postgresql-contrib
               docker rm c_sai_backup
               docker run -it --name c_sai_backup c_sai_backup dpkg -s postgresql-client
               docker rm c_sai_backup
                   Package: postgresql-contrib
                   Status: install ok installed
                   [...]
               We need to check the status for each package
        """
        # 1)
        assert dbt.create_image_using_dockerfile("backup") == 0
        # 2)
        assert dtt.is_image_exist("c_sai_backup")
        # 3)
        assert dtt.is_package_exist("postgresql", "backup")
        assert dtt.is_package_exist("postgresql-contrib", "backup")
        assert dtt.is_package_exist("postgresql-client", "backup")
        assert not dtt.is_package_exist("notexistpackage", "backup")

    def test_db_tools_new_backup(self):
        """
        Test function new_backup
        Configure docker-machine share folder to use this
        TODO need to optimize this procedure
        """
        # TODO  Create a backup using the corresponding container which need to be launch on Setup
        #       Check if the backup works:
        #           The correct date
        #           The correct tables
        #           The correct data

    def test_db_tools_run_db_case_nok(self):
        # TODO implement
        assert (-1)

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
