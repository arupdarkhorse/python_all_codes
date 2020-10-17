import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select
engine = create_engine("sqlite:///:memory:", echo= False)

meta = MetaData()
# Defining table schema
arup_table = Table('arup', meta,
                Column('id', Integer, primary_key= False),
                Column('name', String))
#creating table object
meta.create_all(engine)

#creating connnection
conn = engine.connect()

# insertind multiple rows to table
ins = [{"id" : i, "name" : f"arup_{str(i)}"} for i in range(10_00_000)]		#Here you mention the total number of rows in the table
conn.execute(arup_table.insert(), ins)


complete_data = conn.execute(select([arup_table]))
# cnt_csv will tract the total number of csv file to genereate and filename
cnt_csv = 0
# cnt_partion will tract the row number per csv
cnt_partition = 0


#row_num = 10
while True:
    df = pd.DataFrame(complete_data.fetchmany(1_00_000))
    if len(df)==0:
        break
    else:
        filename = f"arup_{str(cnt_csv)}.csv"     # Give the file nanme of your choice
        if cnt_partition == 0:
            df.to_csv(filename, index=False)
            cnt_partition +=1
        else:
            if cnt_partition == 2:
                cnt_csv += 1
                filename = f"arup_{str(cnt_csv)}.csv"
                df.to_csv(filename, index=False)
                cnt_partition = 1
            else:
                df.to_csv(filename, mode = 'a', header=False, index=False)
                cnt_partition +=1