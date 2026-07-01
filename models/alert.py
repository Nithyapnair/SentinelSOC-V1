from database.database import get_connection


def get_all_alerts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, alert_name, severity, status
        FROM alerts
        ORDER BY id DESC
    """)

    alerts = cursor.fetchall()

    conn.close()

    return alerts


def add_alert(alert_name, severity, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alerts(alert_name, severity, status)
        VALUES(?, ?, ?)
    """, (alert_name, severity, status))

    conn.commit()
    conn.close()


def delete_alert(alert_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM alerts WHERE id=?",
        (alert_id,)
    )

    conn.commit()
    conn.close()