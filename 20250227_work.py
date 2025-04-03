# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:46:01 2025

@author: Admin
"""

import pymysql
import pandas as pd

host = 'localhost'
user = 'root'
password = 'lovekgh33'
db_name = 'test'

conn = pymysql.connect(host = host,
                       user = user,
                       password = password,
                       db = db_name,
                       charset = 'utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor)

query = 'select * from tmp3 union all select * from tmp4 union all select * from tmp5 union all select * from tmp6 union all select * from tmp7 union all select * from tmp8 union all select * from tmp9;'

cursor.execute(query)


execute_result = cursor.fetchall()


us = pd.DataFrame(execute_result)

print(execute_result)

execute_result.value_count()





















