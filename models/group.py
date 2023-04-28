from utils.database import create_connection

class Group:
    def __init__(self, id):
        self.id = id

    @classmethod
    def get_or_create(cls, id):
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM groups WHERE id=?", (id,))
        group = cursor.fetchone()

        if not group:
            cursor.execute("INSERT INTO groups (id) VALUES (?)", (id,))
            conn.commit()

        conn.close()

        return cls(id)
