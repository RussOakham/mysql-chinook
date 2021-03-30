import os
import datetime
import pymysql

# Get username from GitPod workspace
username = os.getenv('RussOakham')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        list_of_names = ['jim', 'bob']
        # Prepare a string with same number of
        # placeholders as list_of_names len
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});"
                       .format(format_strings), list_of_names)
        connection.commit()
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
