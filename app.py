from flask import Flask, abort, render_template, redirect, request, flash
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

projects = [
    {
    'title': 'CekLulus',
    'description': 'Aplikasi web sederhana untuk mengecek status kelulusan siswa MA Nurul Ummah secara online. '
    'Siswa cukup memasukkan NISN dan tanggal lahir untuk mengetahui hasil kelulusan mereka. ',
    'tech': ['Flask', 'Python', 'Google Drive', 'HTML', 'TailwindCSS'],
    'image': 'img/ceklulus/ceklulus.png',
    'images': ['img/ceklulus/ceklulus.png', 'img/ceklulus/ceklulus1.png', 'img/ceklulus/ceklulus2.png', 'img/ceklulus/ceklulus3.png'],
    'github': 'https://github.com/example/ceklulus',
    'more': '/project/ceklulus',
    'slug': 'ceklulus',
    'features': [
        'Pencarian cepat berdasarkan NISN dan tanggal lahir',
        'Tampilan hasil kelulusan yang bersih, modern, dan responsif.',
        'Hak akses penggunaan sistem yang diatur oleh admin',
        'Pengelolaan data siswa dan kelulusan menggunakan Google Drive'
    ],
    },
    {
        'title': 'RateJournee',
        'description': 'Track Your Day with Charts! View your daily ratings in bar and line charts. Ratejournee is a simple app to record and reflect on your day. With anintuitive interface, you can easily rate your day, add notes, and track your mood trends.',
        'tech': ['Flask', 'Python', 'Chart.js', 'MySQL', 'TailwindCSS', 'FullCalendar', 'Alpine.js '],
        'image': 'img/ratejournee.png',
        'images' : ['img/ratejournee.png'],
        'github': '#',
        'more': '/project/ratejournee',
        'slug': 'ratejournee',
        'features': [
            'Give your day a rating and add a quick note.',
            'Interactive charts to visualize your mood trends.',
            'Takes just seconds to note down your day.',
        ],
    },
    {
        'title': 'Kasir',
        'description': 'Sistem kasir berbasis web yang dibangun menggunakan Django.',
        'tech': ['Django', 'Python', 'PostgreSQL', 'HTML', 'CSS'],
        'image': 'img/kasir.png',
        'images' : ['img/kasir.png'],
        'github': '#',
        'more': '/project/kasir',
        'slug': 'kasir',
        'features': [
            'Manajemen inventaris produk',
            'Sistem keranjang belanja',
            'Pembuatan struk dan invoice',
            'Laporan penjualan dan analitik'
        ],
    },
    {
        'title': 'AbsoluteYes',
        'description': 'Create and Display Yes-Only Questions using Flask.',
        'tech': ['Flask', 'Python', 'SQLite', 'Tailwind CSS'],
        'image': 'img/absoluteyes/absoluteyes.png',
        'images' : ['img/absoluteyes/absoluteyes.png', 'img/absoluteyes/absoluteyes1.png', 'img/absoluteyes/absoluteyes2.png', 'img/absoluteyes/absoluteyes3.png'],
        'github': '#',
        'more': '/project/absoluteyes',
        'slug': 'absoluteyes',  
        'features': [
            'Pembuatan pertanyaan khusus yes-only',
            'Berbagi pertanyaan via link',
            'Tampilan statistik jawaban',
            'Antarmuka yang minimalis dan user-friendly'
        ],
    },
    {
        'title': 'Visitor-Log',
        'description': 'Visitor-log are web-based system used to record student visits to library. The data, referred to as visitors is stored in an Excel file, along with visit records, which are also saved in the same Excel file.',
        'tech': ['Flask', 'Python', 'Google Drive', 'HTML', 'TailwindCSS'],
        'image': 'img/visilog/visilog.png',
        'images' : ['img/visilog/visilog.png', 'img/visilog/visilog1.png', 'img/visilog/visilog2.png'],
        'github': '#',
        'more': '/project/visitor-log',
        'slug': 'visitor-log',
        'features': [
            'Pencatatan kunjungan dengan form yang sederhana',
            'Dashboard admin untuk melihat semua kunjungan',
            'Ekspor data ke Excel atau CSV',
            'Sistem notifikasi untuk admin'
        ],
    }
    ]

@app.route('/')
def index():
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

@app.route('/project/<slug>')
def project_detail(slug):
    project = next((p for p in projects if p['slug'] == slug), None)
    if not project:
        return "Project not found", 404
    return render_template('projects/project_detail.html', project=project)

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