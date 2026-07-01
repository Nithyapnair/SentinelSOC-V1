from flask import Flask, render_template, request, redirect, url_for

from database.database import create_tables

from models.user import (
    login_user,
    get_all_users,
    add_user,
    delete_user
)

from models.alert import (
    get_all_alerts,
    add_alert,
    delete_alert
)

from models.incident import (
    get_all_incidents,
    add_incident,
    delete_incident
)

app = Flask(__name__)

# Create Database Tables
create_tables()


# ---------------- LOGIN ----------------

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = login_user(username, password)

        if user:
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Username or Password"

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- USERS ----------------

@app.route("/users")
def users():

    users = get_all_users()

    return render_template("users.html", users=users)


@app.route("/add_user", methods=["POST"])
def add_new_user():

    username = request.form["username"]
    password = request.form["password"]
    role = request.form["role"]

    add_user(username, password, role)

    return redirect(url_for("users"))


@app.route("/delete_user/<int:user_id>")
def remove_user(user_id):

    delete_user(user_id)

    return redirect(url_for("users"))


# ---------------- ALERTS ----------------

@app.route("/alerts")
def alerts():

    alerts = get_all_alerts()

    return render_template("alerts.html", alerts=alerts)


@app.route("/add_alert", methods=["POST"])
def create_alert():

    alert_name = request.form["alert_name"]
    severity = request.form["severity"]
    status = request.form["status"]

    add_alert(alert_name, severity, status)

    return redirect(url_for("alerts"))


@app.route("/delete_alert/<int:alert_id>")
def remove_alert(alert_id):

    delete_alert(alert_id)

    return redirect(url_for("alerts"))


# ---------------- INCIDENTS ----------------

@app.route("/incidents")
def incidents():

    incidents = get_all_incidents()

    return render_template(
        "incidents.html",
        incidents=incidents
    )


@app.route("/add_incident", methods=["POST"])
def create_incident():

    incident_name = request.form["incident_name"]
    priority = request.form["priority"]
    status = request.form["status"]
    assigned_to = request.form["assigned_to"]

    add_incident(
        incident_name,
        priority,
        status,
        assigned_to
    )

    return redirect(url_for("incidents"))


@app.route("/delete_incident/<int:incident_id>")
def remove_incident(incident_id):

    delete_incident(incident_id)

    return redirect(url_for("incidents"))


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)