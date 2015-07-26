import pymysql
import sys
import pythonScraper
pymysql.install_as_MySQLdb()

# Open database connection
db = pymysql.connect('localhost', 'testuser', 'test623', 'testdb')
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Execute the SQL command
# cursor.execute("INSERT INTO per36qf SELECT * FROM per36 WHERE MP > 500")
# cursor.execute("CREATE TABLE pg36 SELECT * FROM per36qf WHERE POS = 'PG' OR POS = 'PG-SG'")
cursor.execute("CREATE TABLE sg36 SELECT * FROM per36qf WHERE POS = 'SG' OR POS = 'SG-PG' OR POS = 'SG-SF'")
cursor.execute("CREATE TABLE sf36 SELECT * FROM per36qf WHERE POS = 'SF' OR POS = 'SF-SG' OR POS = 'SF-PF'")
cursor.execute("CREATE TABLE pf36 SELECT * FROM per36qf WHERE POS = 'PF' OR POS = 'PF-SF' OR POS = 'PF-C'")
cursor.execute("CREATE TABLE c36 SELECT * FROM per36qf WHERE POS = 'C' OR POS = 'C-PF'")
# Commit your changes in the database
db.commit()
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db.commit()
# except:
#     # Rollback in case there is any error
#     db.rollback()

# disconnect from server
db.close()