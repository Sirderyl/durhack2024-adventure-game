import sqlite3
import os

class Database:
    def __init__(self, file: str):
        exists = os.path.exists(file)

        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

        if not exists:
            with open("schema.sql") as f:
                self.cursor.executescript(f.read())

INSTANCE = Database("database.db")
