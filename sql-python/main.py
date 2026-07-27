import psycopg2


try:
    conn = psycopg2.connect(
        dbname="pb1_db",
        user="postgres",
        password="",
        host="localhost",      # or an IP address
        port="5433"            # default PostgreSQL port
    ) 

    with conn:
        # The cursor context manager automatically closes the cursor
        with conn.cursor() as curs:
            curs.execute("SELECT version();")
            db_version = curs.fetchone()
            print(f"Connected to PostgreSQL. Server version: {db_version}")


except Exception as error:
    print(f"Error connecting to database: {error}")


finally:
    # 3. Always close the main connection when finished to avoid leaks
    if 'conn' in locals() and conn:
        conn.close()
        print("Database connection closed.")
