import pymysql
import sys
import pythonScraper
pymysql.install_as_MySQLdb()

# Open database connection
db = pymysql.connect('localhost', 'testuser', 'test623', 'testdb')
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
##########################################################
names = pythonScraper.get_names()
d = pythonScraper.get_dict(names)
# add = 0
for name in names:
    sql = "INSERT INTO per36(NAME, POS, AGE, TM, G, GS, \
           MP, FGM, FGA, FGPERCENTAGE, 3PM, 3PA, 3PPERCENTAGE, \
           2PM, 2PA, 2PPERCENTAGE, \
           FTM, FTA, FTPERCENTAGE, ORB, DRB, TRB, \
           AST, STL, BLK, TOV, PF, PTS) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', \
           '%s', '%s', '%s', '%s', '%s', '%s', \
           '%s', '%s', '%s', '%s', \
           '%s', '%s', '%s', '%s', '%s', '%s', \
           '%s', '%s', '%s', '%s', '%s', '%s')"
    data = (d[name][1] + ' ' + d[name][2], d[name][3], d[name][4], d[name][5], \
            d[name][6], d[name][7], d[name][8], d[name][9], d[name][10], \
            d[name][11], d[name][12], d[name][13], d[name][14], d[name][15], \
            d[name][16], d[name][17], d[name][18], d[name][19], d[name][20], \
            d[name][21], d[name][22], d[name][23], d[name][24], d[name][25], \
            d[name][26], d[name][27], d[name][28], d[name][29])
    # cursor.execute(sql % data)
    # add += 1;
    # print(add)
    # # Commit your changes in the database
    # db.commit()
    try:
        # Execute the SQL command
        cursor.execute(sql % data)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        print(name)
        db.rollback()
###########################################################
# x = {'Ka':['0.5', '2.000'], 'FT':['1.2', '.457']}
# n = ['Ka', 'FT']
# t = "re'"
# for i in n:
#     sql = "INSERT INTO EXPERIMENT(str) \
#            VALUES ('%s')" % \
#            (t.replace("'", "''"))
#     # try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db.commit()
#     # except:
#     #     # Rollback in case there is any error
#     #     db.rollback()
#     #     print("Wrong")
###############################################################################################
# names = pythonScraper.get_names()
# d = pythonScraper.get_dict(names)
# q = d["Toure' Murry"]
# # try:
#     # Execute the SQL command
# cursor.execute("INSERT INTO per36(NAME, POS, AGE, TM, G, GS, \
#                 MP, FGM, FGA, FGPERCENTAGE, 3PM, 3PA, 3PPERCENTAGE, \
#                 2PM, 2PA, 2PPERCENTAGE, \
#                 FTM, FTA, FTPERCENTAGE, ORB, DRB, TRB, \
#                 AST, STL, BLK, TOV, PF, PTS) \
#                 VALUES ('%s', '%s', '%s', '%s', '%s', '%s', \
#                 '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
#                 '%s', '%s', '%s', '%s', \
#                 '%s', '%s', '%s', '%s', '%s', \
#                 '%s', '%s', '%s', '%s', '%s', '%s')" % \
#                (q[1] + " " + q[2], q[3], q[4], q[5], q[6], q[7], \
#                 q[8], q[9], q[10], q[11], q[12], q[13], q[14], \
#                 q[15], q[16], q[17], q[18], \
#                 q[19], q[20], q[21], q[22], q[23], q[24], \
#                 q[25], q[26], q[27], q[28], q[29]))
#     # Commit your changes in the database
# db.commit()
# # except:
# #    # Rollback in case there is any error
# #    db.rollback()

# # disconnect from server
# db.close()