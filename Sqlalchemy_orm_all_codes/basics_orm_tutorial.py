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
ins = [{"id" : i, "name" : f"arup_{str(i)}"} for i in range(100000)]
conn.execute(arup_table.insert(), ins)

# selcting rows from table
    #temp = conn.execute(select[arup_table])
    #print(temp.fetchmany(10))

cnt = 0
while True:
    df = pd.DataFrame(conn.executemany(10000))
    if len(df)==0:
        cnt +=1
        break
    else:
        filename = f"arup_{str(cnt)}"
        df.to_csv(filename, index=False)