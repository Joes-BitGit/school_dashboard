from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def home():
    return render_template('index.html')

@app.route('/student/dash')
def student_dash():
    return render_template('student_dash.html')

@app.route('/professor/dash')
def professor_dash():
    return render_template('professor_dash.html')

@app.route('/student/class')
def student_class():
    return render_template('student_class.html')

@app.route('/professor/class')
def professor_class():
    return render_template('professor_class.html')

@app.route('/student/<username>')
def profile(username):
    return render_template('username.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
