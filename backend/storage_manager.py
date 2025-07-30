"""Storage manager for persisting scraped data."""

import sqlite3

DB_PATH = "data.sqlite3"


def store_items(items: list[dict]) -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL
        )
        """
    )
    for item in items:
        cur.execute(
            "INSERT INTO scraped_data (title, price) VALUES (?, ?)",
            (item.get("title"), item.get("price")),
        )
    conn.commit()
    conn.close()


def fetch_items() -> list[dict]:
    """Return all scraped items from the database."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT title, price FROM scraped_data")
    rows = cur.fetchall()
    conn.close()
    return [{"title": row[0], "price": row[1]} for row in rows]
