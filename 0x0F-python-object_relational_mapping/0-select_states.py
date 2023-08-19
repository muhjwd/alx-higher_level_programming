#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Extract MySQL username, password, and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute the query to select all states and order by states.id
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    
    # Fetch all results and display them
    results = cursor.fetchall()
    for row in results:
        print(row)
    
    # Close the cursor and the database connection
    cursor.close()
    db.close()
