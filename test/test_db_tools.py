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

    def generic_db_tools_all_tables_created(self, test=False):
        """
        Function to test if tables exist
        :return:
        """
        tables_name = ['Strategie', 'Action', 'Has_action']
        for name in tables_name:
            res = dbt.select_one_with_parameters(sqt.IS_TABLE_EXISTS, (name,), test)
            assert(res != -1)
            assert res

    def test_db_tools_all_tables_created(self):
        """
        Test if all the tables are created
        """
        self.generic_db_tools_all_tables_created()

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

    def test_get_last_backup(self):
        """
        Test function get_last_backup
        """
        # create a new backup
        file_name = dbt.new_backup()
        # get the last backup file name
        last_backup = dbt.get_last_backup()
        # remove the new backup
        dbt.remove_backup(file_name)
        # test the function
        assert file_name == last_backup

    def test_db_tools_new_backup(self):
        """
        Test function new_backup
        Configure docker-machine share folder to use this
          1) Create a backup using the corresponding container which need to be launch on Setup with new data
          2) Check if the backup works:
              2.1) The correct date
              2.2) The correct tables
              2.3) The correct data
        """
        # 1) create a backup with a new raw on table action
        # add a raw on table action prod
        new_raw_table = "test_new_backup"
        tmp_container_name = "tmp_postgres"
        assert dbt.query_with_parameters(sqt.INSERT_ON_ACTION, (new_raw_table,)) == 0
        file_name = dbt.new_backup()
        assert file_name != -1

        # 2) create a temporary database using a new postgres container with a different port (here 5433)
        if not dtt.is_image_exist("c_sai_postgres"):
            res = dbt.create_image_using_dockerfile("postgres")
            if res == -1:
                raise Exception("Image not created correctly")
        if not dtt.is_container_exist("c_sai_" + tmp_container_name):
            tmp_db_run = dbt.run_db(tmp_container_name, "postgres", 5433)
            # wait database connection
            dbt.wait_db_connection(True)
        else:
            tmp_db_run = 0
        assert tmp_db_run == 0
        # load the previous backup into the new db
        dbt.load_last_backup(tmp_container_name)
        # 2.1)  check if date is correct
        date = dbt.datetime.now().replace(microsecond=0).strftime("%Y%m%dT%H%M")  # without seconds
        assert date in file_name
        # 2.2) check if all the tables exists
        self.generic_db_tools_all_tables_created(True)
        # 2.3) check if the main data are presents (Actions ...)
        assert dbt.select_one_with_parameters(sqt.IS_RAW_EXISTS_ON_ACTION, (new_raw_table,), True)
        assert not dbt.select_one_with_parameters(sqt.IS_RAW_EXISTS_ON_ACTION, ("other",), True)
        assert dbt.remove_backup(file_name) == 0

        # clean the db, stop and remove the tmp_postgres container
        # delete the new raw on table action prod
        assert dbt.query_with_parameters(sqt.DELETE_ON_ACTION, (new_raw_table,)) == 0
        # stop and remove the tmp_postgres container
        assert dtt.clean_container("c_sai_" + tmp_container_name) == 0

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
