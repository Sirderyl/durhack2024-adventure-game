import sqlite3
import os
import random

from stories import STORIES

from user import User

class Database:
    def __init__(self, file: str):
        exists = os.path.exists(file)

        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

        if not exists:
            with open("schema.sql") as f:
                self.cursor.executescript(f.read())

    def load_user(self, id: int) -> User:
        self.cursor.execute("SELECT * FROM user WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        story_id: str = row["story"]
        location: str = row["location"]
        active_quest: str = row["active_quest"]

        self.cursor.execute(
            "SELECT * FROM user_completed_quests WHERE user_id = ?",
            (id,)
        )


        story = STORIES[story_id]
        completed_quests = [story.quests[row["quest_name"]] for row in self.cursor.fetchall()]

        return User(
            token=id,
            story=story,
            location=story.locations[location],
            active_quest=story.quests[active_quest],
            completed_quests=completed_quests
        )

    def save_user(self, user: User):
        if user.token is None:
            # Generate some random text
            user.token = random.randint(0, 1000000000)

        self.cursor.execute(
            "DELETE FROM user_completed_quests WHERE user_id = ?",
            (user.token,)
        )
        self.cursor.execute(
            "DELETE FROM user WHERE id = ?",
            (user.token,)
        )

        self.cursor.execute("""
            INSERT INTO user (id, story, location, active_quest)
            VALUES (?, ?, ?, ?)
        """, (user.token, user.story, user.location, user.active_quest))

        for quest in user.completed_quests:
            self.cursor.execute("""
                INSERT INTO user_completed_quests (user_id, quest_name)
                VALUES (?, ?)
            """, (user.token, quest))


INSTANCE = Database("database.db")
