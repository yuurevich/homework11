from flask import Flask, render_template
import utils
app = Flask(__name__)


@app.route('/')
def candidates():
    return render_template('list.html', candidates=utils.data)


@app.route('/candidate/<id>')
def index(id):
    return render_template('card.html', candidate=utils.get_candidate(id))


@app.route('/search/<name>')
def search(name):
    data = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=data, candidates_len=len(data))


@app.route('/skill/<skill>')
def skills(skill):
    data = utils.get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=data, skill=skill)


app.run()
