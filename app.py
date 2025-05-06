from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
import os
import re


app = Flask(__name__)
secret_key = os.urandom(24)
app.secret_key = secret_key

# 🔹 Konfigurasi Gmail SMTP using GOOGLE APP PASSWORD
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

mail = Mail(app)

@app.route('/')
def index():
    projects = [
        {
            'title': 'CekLulus',
            'description': 'Aplikasi web sederhana untuk mengecek status kelulusan siswa MA Nurul Ummah secara online.',
            'tech': ['Flask', 'Python', 'SQLite', 'HTML', 'CSS'],
            'image': 'img/ceklulus.png',
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'RateJournee',
            'description': 'Track Your Day with Charts! View your daily ratings in bar and line charts.',
            'tech': ['Flask', 'Python', 'Chart.js', 'SQLAlchemy', 'Bootstrap'],
            'image': 'img/ratejournee.png',
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'Kasir',
            'description': 'Sistem kasir berbasis web yang dibangun menggunakan Django.',
            'tech': ['Django', 'Python', 'PostgreSQL', 'HTML', 'CSS'],
            'image': 'img/kasir.png',
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'AbsoluteYes',
            'description': 'Create and Display Yes-Only Questions using Flask.',
            'tech': ['Flask', 'Python', 'SQLite', 'Tailwind CSS'],
            'image': 'img/absoluteyes.png',
            'github': '#',
            'demo': '#'
        },
        {
            'title': 'Visitor-Log',
            'description': 'Easily record your visit with our web-based visitor log system using Flask.',
            'tech': ['Flask', 'Python', 'SQLAlchemy', 'HTML', 'CSS'],
            'image': 'img/visitorlog.png',
            'github': '#',
            'demo': '#'
        }
    ]
    
    skills = [
        {'name': 'Python', 'level': 90},
        {'name': 'Flask', 'level': 85},
        {'name': 'Django', 'level': 80},
        {'name': 'HTML/CSS', 'level': 90},
        {'name': 'JavaScript', 'level': 75},
        {'name': 'Tailwind CSS', 'level': 85},
        {'name': 'SQL', 'level': 80},
        {'name': 'Git', 'level': 75},
        {'name': 'RESTful API', 'level': 80},
    ]
    
    return render_template('index.html', projects=projects, skills=skills)

# 🔹 Route untuk menerima message dan mengirimkan email
@app.route("/send-message", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # Basic validation
    if not all([name, email, subject, message]):
        flash("❌ All fields are required.", "error")
        return redirect("/index#contact")

    # Optional: simple email format validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        flash("❌ Invalid email address.", "error")
        return redirect("/index#contact")

    try:
        msg = Message(
            subject=f"📩 DevFolio: {subject}",
            sender=email,
            recipients=[app.config["MAIL_USERNAME"]],
            html=f"""
                <h2 style="color: #4F46E5;">📬 You've got a new message!</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
                <p><strong>Subject:</strong> {subject}</p>
                <hr>
                <p style="white-space: pre-wrap;">{message}</p>
                <br>
                <small style="color: gray;">Sent from your DevFolio contact form</small>
            """
        )
        mail.send(msg)
        flash("✅ Your message has been sent successfully!", "success")
    except Exception as e:
        flash(f"❌ An error occurred while sending the message: {str(e)}", "error")

    # Redirect directly to contact section
    return redirect("/#contact")


if __name__ == '__main__':
    app.run(debug=True)