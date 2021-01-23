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
    # labels2, values2 = scrape.get_co_occur(q)
    legend = "Description Words"
    # legend2 = "Web Page Words"
    labels = labels
    values = values
    # labels2 = labels2
    # values2 = values2
    # return render_template('chart.html', labels=labels, values=values, legend=legend, legend2=legend2, labels2=labels2, values2=values2)
    return render_template('chart.html', labels=labels, values=values, legend=legend)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
