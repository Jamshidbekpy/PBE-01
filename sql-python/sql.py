import psycopg2
from psycopg2 import sql

def get_connection():
    """Establishes and returns a database connection."""
    return psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )

def setup_database():
    """1. CREATE: Creates the inventory table if it does not exist."""
    print("--- Creating Table ---")
    query = """
    CREATE TABLE IF NOT EXISTS inventory (
        id SERIAL PRIMARY KEY,
        item_name VARCHAR(100) NOT NULL,
        price NUMERIC(10, 2) NOT NULL,
        quantity INTEGER NOT NULL
    );
    """
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute(query)
                print("Table 'inventory' is ready.")
    finally:
        conn.close()

def create_item(name, price, qty):
    """2. INSERT: Adds a new item to the database."""
    print(f"\n--- Inserting Item: {name} ---")
    query = "INSERT INTO inventory (item_name, price, quantity) VALUES (%s, %s, %s) RETURNING id;"
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as curs:
                # Use parameterized queries (%s) to prevent SQL injection
                curs.execute(query, (name, price, qty))
                item_id = curs.fetchone()[0]
                print(f"Successfully inserted item with ID: {item_id}")
                return item_id
    finally:
        conn.close()

def retrieve_all_items():
    """3. RETRIEVE: Fetches and displays all items."""
    print("\n--- Retrieving All Items ---")
    query = "SELECT id, item_name, price, quantity FROM inventory;"
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute(query)
                items = curs.fetchall()
                for item in items:
                    print(f"ID: {item[0]} | Name: {item[1]} | Price: ${item[2]} | Stock: {item[3]}")
    finally:
        conn.close()

def update_item_price(item_id, new_price):
    """4. UPDATE: Changes the price of an existing item."""
    print(f"\n--- Updating Price for Item ID: {item_id} ---")
    query = "UPDATE inventory SET price = %s WHERE id = %s;"
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute(query, (new_price, item_id))
                print(f"Successfully updated price to ${new_price}.")
    finally:
        conn.close()

def delete_item(item_id):
    """5. DELETE: Removes an item from the database."""
    print(f"\n--- Deleting Item ID: {item_id} ---")
    query = "DELETE FROM inventory WHERE id = %s;"
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as curs:
                curs.execute(query, (item_id,))
                print(f"Successfully deleted item {item_id}.")
    finally:
        conn.close()

# --- Execution Workflow ---
if __name__ == "__main__":
    # Initialize the database structure
    setup_database()
    
    # Create two new items
    laptop_id = create_item("Laptop", 999.99, 10)
    phone_id = create_item("Smartphone", 499.99, 25)
    
    # Read the data
    retrieve_all_items()
    
    # Update the laptop price
    update_item_price(laptop_id, 949.99)
    
    # Delete the phone
    delete_item(phone_id)
    
    # Read data again to see final changes
    retrieve_all_items()
