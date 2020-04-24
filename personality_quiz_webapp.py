from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
    return render_template("home.html")

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)