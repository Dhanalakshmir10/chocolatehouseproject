import sqlite3

def create_tables():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SeasonalFlavor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingredient (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity REAL NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CustomerSuggestion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_suggestion TEXT NOT NULL,
        allergy_concern TEXT
    )""")

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    create_tables()
