import pymysql as sql
def create_TABLE(cursor,query):
    cursor.execute(query)
def insert(cursor,name,values):
    query='''INSERT INTO '''+name+'''(NAME, LASTNAME)VALUES(+'''+values+''')'''
    cursor.execute(query)
def print_TABLE(cursor,name):
    query="SELECT *FROM "+name
    cursor.execute(query)
    result=cursor.fetchall()
    print(result)
def drop_TABLE(cursor,name):
    query='''DROP TABLE     '''+name
    cursor.execute(query)
db=sql.connect("localhost","root","","test")
cursor=db.cursor()
tableName=input("Enter the name of the table: ")
tableQuery=input("Enter the query to create the table with all string parameters: ")
create_TABLE(cursor,tableQuery)
db.commit()
values=input("Enter the values to be inserted in the table: ")
insert(cursor,tableName,values)
db.commit()
print()
print()
print("The values has been successfully entered in the table")
print_TABLE(cursor,tableName)
db.commit()
dropTABLE=input("Enter the table to be dropped")
drop_TABLE(cursor,dropTABLE)
db.commit()