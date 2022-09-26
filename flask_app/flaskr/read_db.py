import sys
import pandas as pd
#
import sqlite3
# ------------------------------------------------------------------
sys.stderr.write("*** 開始 ***\n")
#
file_sqlite3 = "./seven_data.db"
con = sqlite3.connect(file_sqlite3)
#
df=pd.read_sql_query('SELECT * FROM data LIMIT 3', con)
print(df)
# print(df.head())
#
con.close()
# df.to_csv("tmp001.csv",header=None,index=None)
sys.stderr.write("*** 終了 ***\n")