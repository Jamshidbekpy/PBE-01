import psycopg2


def get_connection():
    return psycopg2.connect(
            host="localhost",
            database="pb1_db1",
            user="postgres",
            password="",
            port="5433" 
        )
    


# try:
#     conn = get_connection()
#     print("Connection successful!")
#     cursor = conn.cursor()
    
#     # Example: Check the PostgreSQL server version
#     cursor.execute("SELECT version();")
#     db_version = cursor.fetchone()
#     print(f"PostgreSQL version: {db_version}")
    
# except psycopg2.Error as e:
#     print("Error connecting to the database:", e)
#     exit(1)
    
# finally:
#     if conn:
#         conn.close()
#         print("Connection closed.")



# try:
#     conn = get_connection()
#     print("Connection successful!")
#     cursor = conn.cursor()
    
#     try:
#         cursor.execute("SELECT * FROM playes;")
#         db_info = cursor.fetchall()
#         print(db_info, '###############################')

#     except psycopg2.Error as e:
#         print("query has mistake!", e)
#         exit(1)


    
    
# except psycopg2.Error as e:
#     print("Error connecting to the database:", e)
#     exit(1)
    
# finally:
#     if conn:
#         conn.close()
#         print("Connection closed.")



# try:
#     conn = get_connection()
#     print("Connection successful!")
#     cursor = conn.cursor()
    
#     try:
#         table_name = "table2"
#         cursor.execute(
#             f"CREATE TABLE {table_name} (" \
#             "employee_id INT PRIMARY KEY," \
#             "first_name VARCHAR(50) NOT NULL," \
#             "last_name VARCHAR(50) NOT NULL," \
#             "email VARCHAR(100) UNIQUE NOT NULL," \
#             "hire_date DATE NOT NULL," \
#             "salary DECIMAL(10, 2) NOT NULL" \
#             ");"
#         )
#         conn.commit()

#         get_tables_query = """
#             SELECT table_name 
#             FROM information_schema.tables 
#             WHERE table_schema = 'public' 
#             AND table_type = 'BASE TABLE';
#             """
#         cursor.execute(get_tables_query) # [('teams',), ('players',), ('table1',)]

#         tables = cursor.fetchall()
#         count = 0
#         for tablename in tables:
#             if tablename[0] == table_name:
#                 count+=1
#                 print("Our table created")
#             else:
#                 continue
#         if count==0:
#             print("Our table didn't create")

    
#         print(f"Tables in your database:{tables}")
        

            
    

#     except psycopg2.Error as e:
#         print("query has mistake!", e)
#         exit(1)


    
    
# except psycopg2.Error as e:
#     print("Error connecting to the database:", e)
#     exit(1)
    
# finally:
#     if conn:
#         conn.close()
#         print("Connection closed.")




# try:
#     conn = get_connection()
#     print("Connection successful!")
#     cursor = conn.cursor()
    
#     try:
#         cursor.execute(
#             "INSERT INTO teams (id, team, city) VALUES (%s, %s, %s)",
#             (7, "PORTUG","Por")
#         )

#         query = "SELECT * FROM teams ORDER BY id DESC;"

#         cursor.execute(query)
#         teams_info = cursor.fetchone()
        
    
#         print(f"Teams :{teams_info}")
        

            
    

#     except psycopg2.Error as e:
#         print("query has mistake!", e)
#         exit(1)


    
    
# except psycopg2.Error as e:
#     print("Error connecting to the database:", e)
#     exit(1)
    
# finally:
#     if conn:
#         conn.close()
#         print("Connection closed.")


