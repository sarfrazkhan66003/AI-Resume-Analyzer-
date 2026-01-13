import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Sarfraz@0786',
        db='cv',
        port=3306
    )
    cursor = connection.cursor()
    
    # Check current columns to be safe (optional, but good practice)
    # But we'll just run the ALTER command directly since we know the issue.
    
    print("Altering table 'user_feedback' to increase 'comments' column size...")
    
    alter_sql = "ALTER TABLE user_feedback MODIFY comments VARCHAR(1000);"
    cursor.execute(alter_sql)
    connection.commit()
    
    print("Success! 'comments' column size increased to 1000 characters.")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
