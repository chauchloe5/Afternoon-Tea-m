from flask import Flask, render_template, request
import personality_quiz

app = Flask(__name__)

global state
state = {
    "question":"None",
    "answers": [],
    "score": [0, 0],
    "count":0,
    "url":0
}

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/restart')
def new_quiz():
    state['count'] = 0
    state['score'] = [0, 0]
    state['url'] = ""
    return quiz()

@app.route('/quiz', methods=['GET', "POST"])
def quiz():
    global state
    if request.method == 'GET':
        if state['count'] == 10:
            return render_template('results.html', state=state)
        else:
            update_state()
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

        if state['count'] == 10:
            plot_results()
            return render_template('results.html', state=state)
        else:
            update_state()
            return render_template('quiz.html', state=state)

def plot_results():
    global state

    import matplotlib.pyplot as plt
    import matplotlib
    from datetime import datetime

    matplotlib.use('Agg')

    plt.figure()
    fig = plt.figure()
    plt.xlabel('Nerdy')
    plt.ylabel('Cute')
    plt.tick_params(length=0,labelleft=False, labelbottom=False, labelright=False, labeltop=False, right=False, top=False, left=False, bottom=False)
    ax = plt.axis([-10,10,-10,10])
    ax2 = plt.twinx()
    plt.ylabel('Mature')
    plt.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False, right=False, top=False, left=False, bottom=False)
    plt.axis([-10,10,-10,10])
    plt.twiny()
    plt.xlabel('Sexy')
    plt.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False, right=False, top=False, left=False, bottom=False)
    plt.axis([-10,10,-10,10])

    # Draw lines to split quadrants
    plt.plot([0,0],[-10,10], linewidth=4, color='#333333' )
    plt.plot([-10,10],[0,0], linewidth=4, color='#333333' )

    plt.plot(state['score'][0], state['score'][1], marker="o", color="#c60055")

    # current date and time
    now = datetime.now()
    timestamp = str(datetime.timestamp(now))
    path = "static/images/plot_" + timestamp + ".png"
    plt.savefig(path)
    state['url'] = path

def update_state():
    global state
    question = personality_quiz.questions[state['count']]
    state['question'] = question['question']
    state['answers'] = [ans['answer'] for ans in question['answers']]

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
