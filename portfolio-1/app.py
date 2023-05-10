from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('homepage.html')

@app.route('/download/resume')
def download_resume():
    # Name of the file in the static directory
    filename = 'Harsha Putta.pdf'
    return send_from_directory(directory='static', filename=filename, as_attachment=True)