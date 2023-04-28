from utils.database import create_connection

class User:
    def __init__(self, id, is_admin=False):
        self.id = id
        self.is_admin = is_admin

    @classmethod
    def get_or_create(cls, id):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        user = cursor.fetchone()

        if not user:
            cursor.execute("INSERT INTO users (id, is_admin) VALUES (?, 0)", (id,))
            conn.commit()
            user = (id, 0)

        conn.close()

        return cls(user[0], bool(user[1]))

    def is_admin(self):
        return self.is_admin

    def set_admin(self):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET is_admin=1 WHERE id=?", (self.id,))
        conn.commit()

        conn.close()
        self.is_admin = True
