import pandas
from sqlalchemy import create_engine
hostname="127.0.0.1"
uname="root"
pwd=""
dbname="zipcodes1"
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
.format(host=hostname, db=dbname, user=uname, pw=pwd))
tables = pandas.read_csv(r"zip_code_database.csv")
connection=engine.connect()
tables.to_sql('zipcodes',con = engine, if_exists = 'replace')
connection.close()
print(tables)
