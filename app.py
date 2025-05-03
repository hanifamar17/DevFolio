from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)