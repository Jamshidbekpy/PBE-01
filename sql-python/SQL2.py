import psycopg2
from psycopg2 import sql

def get_connection():
    conn = psycopg2.connect(
        dbname="pb1_db",
        user="postgres",
        password="",
        host="localhost",      
        port="5433"  

    )
    return conn


# Create database

def create_database(db_name):
    """
    Connects to the default postgres server and safely creates a new database.
    """
    # 1. Establish a connection to the default administrative database
    conn = get_connection()
    
    # 2. CRITICAL: Turn on autocommit mode 
    # (PostgreSQL prohibits creating databases inside transaction blocks)
    conn.autocommit = True
    
    try:
        with conn.cursor() as curs:
            # 3. Check if the database already exists
            check_query = "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s;"
            curs.execute(check_query, (db_name,))
            
            if curs.fetchone():
                print(f"Database '{db_name}' already exists.")
                return False
                
            # 4. Safely inject the database name using sql.Identifier
            # sql.Identifier places proper quotation marks around the name automatically
            create_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
            curs.execute(create_query)
            
            print(f"Database '{db_name}' created successfully!")
            return True
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
        
    finally:
        # 5. Always close the connection
        conn.close()


conn = get_connection()

try:
    with conn.cursor() as curs:
        query = "INSERT INTO inventory (column1, column2) VALUES (%s, %s, %s) RETURNING id"
        curs.execute(query,(value1, valu2, value3))
        item_id = curs.fetchone()[0]
        print(f"Successfully inserted item with ID: {item_id}")
except Exception as e:
        print(f"An error occurred: {e}")
        
finally:
    conn.close()
  
        




