from database.database import get_connection


def get_all_incidents():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               incident_name,
               priority,
               status,
               assigned_to
        FROM incidents
        ORDER BY id DESC
    """)

    incidents = cursor.fetchall()

    conn.close()

    return incidents


def add_incident(incident_name, priority, status, assigned_to):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO incidents
        (incident_name, priority, status, assigned_to)
        VALUES (?, ?, ?, ?)
    """, (incident_name, priority, status, assigned_to))

    conn.commit()
    conn.close()


def delete_incident(incident_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM incidents WHERE id=?",
        (incident_id,)
    )

    conn.commit()
    conn.close()