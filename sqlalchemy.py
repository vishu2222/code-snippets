from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
import pyodbc
import urllib


params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=tcp:serverName;"
                                 "DATABASE=databasename;"
                                 "UID=username;"
                                 "PWD=password")
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params),echo = True) # ?




# #create a Table
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)

meta.create_all(engine)


# Insert
conn = engine.connect()
result = conn.execute\
(students.insert(), [\
    {'name':'Rajiv', 'lastname' : 'Khanna'},\
    {'name':'Komal','lastname' : 'Bhandari'},\
    {'name':'Abdul','lastname' : 'Sattar'},\
    {'name':'Priya','lastname' : 'Rajhans'},]\
)


# Select
s = students.select()
conn = engine.connect()
result = conn.execute(s)

for row in result:
   print (row)



# Update
conn = engine.connect()
stmt=students.update().where(students.c.lastname=='Khanna').values(lastname='Kapoor')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()



# delete
conn = engine.connect()
stmt = students.delete().where(students.c.lastname == 'Khanna')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()

