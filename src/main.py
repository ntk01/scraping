import flask
from flask import render_template
from flask import request
import describe
# import scrape


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/chart', methods=['GET', 'POST'])
def chart():
    q = request.form.get('keyword')

    labels, values = describe.get_word(q)
    legend = "Description Words"
    labels = labels
    values = values
    return render_template('chart.html', labels=labels, values=values, legend=legend)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
