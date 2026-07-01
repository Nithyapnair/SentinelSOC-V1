from database.database import get_connection


def get_all_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username, role FROM users"
    )

    users = cursor.fetchall()

    conn.close()

    return users


def add_user(username, password, role):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(username, password, role)
        VALUES(?, ?, ?)
        """,
        (username, password, role)
    )

    conn.commit()
    conn.close()


def delete_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()


def login_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user