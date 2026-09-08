import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
def initialize_database():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS participants (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            education TEXT
        )
    """)
    conn.commit()
    conn.close()
def add_participant(name, age, gender, education):
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO participants
        (name, age, gender, education)
        VALUES (%s, %s, %s, %s)
        """, (name, age, gender, education)
    )
    conn.commit()
    conn.close()
def get_participants(search):
        conn = get_connection()
        if search:
            rows = conn.execute("""
                SELECT id, name, age, gender, education
                FROM participants
                WHERE name LIKE ?
                ORDER by id ASC
            """, (f"%{search}%",)).fetchall()
        else:
            rows = conn.execute("""
                SELECT id, name, age, gender, education
                FROM participants
                ORDER BY id ASC
            """).fetchall()
        conn.close()
        return rows
def delete_participant(participant_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM participants WHERE id = ?",
        (participant_id,)
    )

    conn.commit()
    conn.close()
