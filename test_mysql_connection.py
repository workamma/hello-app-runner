#!/usr/bin/env python3
import os
import sys
import pymysql
import pymysql.cursors

def test_mysql_connection():
    """
    Test MySQL connection using environment variables.
    
    Required environment variables:
    - DB_HOST: MySQL server hostname
    - DB_USER: MySQL username
    - DB_PASSWORD: MySQL password
    - DB_PORT: MySQL server port (default: 3306)
    """
    print("Testing MySQL connection...")
    
    # Get connection parameters from environment variables
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = int(os.getenv('DB_PORT', '3306'))
    
    # Check if required environment variables are set
    if not host:
        print("Error: DB_HOST environment variable is not set")
        sys.exit(1)
    if not user:
        print("Error: DB_USER environment variable is not set")
        sys.exit(1)
    if not password:
        print("Error: DB_PASSWORD environment variable is not set")
        sys.exit(1)
    
    try:
        # Attempt to connect to MySQL
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        
        print(f"Successfully connected to MySQL server at {host}:{port}")
        
        # Get list of databases
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            
            print("\nAvailable databases:")
            for db in databases:
                print(f"- {db['Database']}")
        
        connection.close()
        print("\nConnection test completed successfully.")
        return True
        
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        return False

if __name__ == "__main__":
    test_mysql_connection()