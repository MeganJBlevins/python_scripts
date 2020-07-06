import mysql.connector

cnx = mysql.connector.connect(user='hlfdbadmin', password='M@rlinDB$ql!',
                              host='buildservmarlin\sqlexpress2012',
                              database='hlf_develop_catalog')
cnx.close()

