import pymysql.cursors

userInput = input("Enter a student's first name: ")

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='sq8822nj',
                             password='Whyskar|3301',
                             db='sq8822nj_Assignment_Two',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * from Students WHERE First_Name = \"" + userInput + "\""
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # to save - connection.commit()
        

finally:
    connection.close()