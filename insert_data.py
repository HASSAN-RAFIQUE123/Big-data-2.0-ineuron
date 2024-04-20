import MySQLdb
# import mysql.connector for connectin with sql.
import mysql.connector
# random for random value.
import random
import string
import time

# MySQL connection parameters
db_configration = {
    'user': 'root',
    'password': 'H0134440h.',
    'host': 'localhost',
    'database': 'kafka_sql'

}

# Define a function to generate random strings of specified length
def random_string(length):
    # add mix string to database.
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def random_number(length):
    # add mix number to database.
    return ''.join(random.choices(string.digits, k=length))
# Connect to MySQL database
cnx = mysql.connector.connect(**db_configration)
cursor = cnx.cursor()

# Run infinite loop to insert dummy records
while True:
    # Generate random data for the record
    name = random_string(10)
    email = random_string(10) + '@example.com'
    phone = random_number(8)
    


    # Construct SQL insert statement and execute it
    add_record = ("INSERT INTO input_data_02"
                  "(name, email, phone) "
                  "VALUES (%s, %s, %s)")
    data = (name, email, phone)
    cursor.execute(add_record, data)
    cursor.fetchall()
    cnx.commit()

    print("Inserted record: ", data)

    # Wait for 5 seconds before inserting next record
    time.sleep(2)

# Close MySQL connection
cursor.close()
cnx.close()
