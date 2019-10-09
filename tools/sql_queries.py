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
"""
INSERT_ON_STRATEGIE = """"""