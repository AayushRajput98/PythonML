import pymysql as sql

db=sql.connect("localhost","root","","db")

cursor=db.cursor()

query='''INSERT INTO TAB(NAME)VALUES("AAYUSH")'''
try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()