import sqlite3
from Categories import Categories
from User import User
from PathGetter import PathGetter

class DataBaseManager:
    def __init__(self):
        self.db_path = PathGetter.get_database_path()
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def equal_users(self, user1: User, user2: User) -> bool:
        return user1.id == user2.id and user1.email == user2.email and user1.hour == user2.hour and user1.news_category.value == user2.news_category.value and user1.last_sent == user2.last_sent 
    
    def equal_lists(self, list1: list[User], list2: list[User]) -> bool:
        if len(list1) != len(list2):
            return False

        for i in range(len(list1)):
            if not self.equal_users(list1[i], list2[i]):
                return False
            
        return True

    def update_user_by_id(self, user: User) -> None:
        self.cursor.execute("""
            UPDATE users
            SET 
                email = ?,
                category = ?,
                hour = ?,
                last_sent = ?
            WHERE id = ?
        """, (
            user.email,
            user.news_category.value,
            user.hour,
            user.last_sent,
            user.id
        ))

        self.conn.commit()

    def load_users(self) -> list[User]:
        users: list[User] = []
        self.cursor.execute("SELECT * FROM users")
        for user in self.cursor.fetchall():
            id = user[0]
            email = user[1]
            hour = user[2]
            cat = Categories[user[3].upper()]
            last_sent = user[4]
            data = User(id, email, hour, cat)
            data.last_sent = last_sent
            users.append(data)
        return users

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            email TEXT,
            hour INTEGER,
            category TEXT,
            last_sent TEXT
        )
        """)

        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()