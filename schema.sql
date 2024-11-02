CREATE TABLE user (
    id INTEGER NOT NULL PRIMARY KEY,
    story TEXT NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE user_completed_quests (
    user_id INT NOT NULL,
    quest_name TEXT NOT NULL
);
