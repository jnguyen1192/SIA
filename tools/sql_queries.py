IS_TABLE_EXISTS = """SELECT EXISTS (
   SELECT 1
   FROM   information_schema.tables 
   WHERE  table_name = %s
   );"""

""" TODO a request that will write:

For example :
 pos = 100,200
 move_cursor(pos)
 double_click(pos)
 
 The xml will be for the previous example :
 Action : move_cursor
<pos>100,200</pos>
 Action : double_click
<pos>100,200</pos>

"""
#TODO A test will need to be do to know if we need to wait each actions
INSERT_ON_STRATEGIE = """"""