import sqlite3
from pathlib import Path
from sqlite3 import Connection


# noinspection PyGlobalUndefined
def init():
    db_path = Path(__file__).parent.parent / "handlers.db"
    global db, cursor
    db: Connection = sqlite3.connect(db_path)
    cursor = db.cursor()


def create():
    cursor.execute(("""
        DROP TABLE IF EXISTS shop
    """))
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shop (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER
        )
    """)
    db.commit()


def populate():
    cursor.execute("""
        INSERT INTO shop (name, price) VALUES
        ('War and peace', '1300'),
        ('Invisible man', '1500')
    """)
    db.commit()


def get():
    cursor.execute("SELECT * FROM shop")
    return cursor.fetchall()


if __name__ == "__main__":
    init()
    create()
    populate()
    get()