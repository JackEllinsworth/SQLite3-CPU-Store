import sqlite3
import menu

# Connects to the database
print("[DB] Loading...")

conn = sqlite3.connect('db/cpus.db')

# Creates TYPES table if not done already
print("[DB] Opened database successfully.")

conn.execute('''CREATE TABLE IF NOT EXISTS TYPES (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    CLOCK_SPEED REAL NOT NULL,
    CORES INTEGER NOT NULL,
    CACHE_SIZE INTEGER NOT NULL,
    PRICE REAL NOT NULL
);''')

# Starts menu
menu.send_menu(conn)
