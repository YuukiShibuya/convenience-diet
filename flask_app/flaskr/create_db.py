import sys
import pandas as pd
import json

import  sqlite3

sys.stderr.write("*** 開始 ***\n")
#
df = pd.read_json('../../data/seven_data_shaped20.json')
print(df)

file_sqlite3 = "./seven_data.db"
con = sqlite3.connect(file_sqlite3)

df.to_sql('data',con,if_exists='append',index=None)
#
con.close()
#
sys.stderr.write("*** 終了 ***\n")