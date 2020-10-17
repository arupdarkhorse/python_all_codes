import pandas as pd
import concurrent.futures as cf
import threading
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select

def create_csv(csv_num, comma_sep_table_header):
	""" create dyanmic csv file with column names as header
	:param :csv_num takes the total number of csv required in output file
	:type Integer
	:param comma_sep_table_header: comma separated column names
	:type string
	:rtype list
	:return list of csv file names
	"""
	csv_list = []
	for i in range(1, csv_num+1):
		filename = f"csv_partition_{i}.csv"		# you can choose a csv file name of your choice
		csv_list.append(filename)
		with open(filename, 'w') as writer:
			writer.write(f"{comma_sep_table_header}\n")

	return csv_list

def write_csv_partition(filename, partition_num, row_num_per_fetch):
	"""
	:param filename: csv file name
	:type String
	:param partition_num: the number of fetch for a csv file
	:type Integer
	:param row_num_per_fetch: the number of rows loaded to memory
	:type Integer
	:rtype None
	:return None
	"""
    for i in range(partition_num):
    	df = pd.DataFrame(complete_data.fetchmany(row_num_per_fetch))
    	df.to_csv(filename, mode = 'a', header=False, index=False)


if __name__ == "___main__":
	# this program is used to for for fetching bulk data from database 
	# using pandas since memory is a constraint
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
	header_str = ",".join(complete_data.keys())
	csv_list = create_csv(5, header_str)
	for i in csv_list:
		write_csv_partition(csv_list, 10, 20_000)


