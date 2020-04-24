from flask import Flask, render_template, request
import personality_quiz

app = Flask(__name__)

global state
state = {
    "question":"None",
    "answers": [],
    "score": [0, 0],
    "count":0
}

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/quiz', methods=['GET', "POST"])
def quiz():
    global state
    if request.method == 'GET':
        question = personality_quiz.questions[state['count']]
        state['question'] = question['question']
        state['answers'] = [ans['answer'] for ans in question['answers']]
        return render_template('quiz.html', state=state)
    elif request.method == 'POST':
        response = request.form[str(state['count'])]
        question = personality_quiz.questions[state['count']]
        answer = [a for a in question['answers'] if a['answer'] == response]
        score = answer[0]['value']
        orientation = answer[0]['orientation']

        if orientation == "x":
            state['score'][0] += score
        elif orientation == "y":
            state['score'][1] += score
        
        state['count'] += 1

        if state['count'] == 2:
            return render_template('results.html', state=state)
        else:
            question = personality_quiz.questions[state['count']]
            state['question'] = question['question']
            state['answers'] = [ans['answer'] for ans in question['answers']]
            return render_template('quiz.html', state=state)

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)