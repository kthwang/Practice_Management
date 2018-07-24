from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config.update({"SECRET_KEY": "secret"})

class SearchForm(FlaskForm):
    search = StringField('검색', validators=[DataRequired()])


@app.route('/')
def base():
    return render_template('index.html')

@app.route('/<day>')
def fileName(day):
    return render_template(f'{day}.html')

@app.route('/search', methods=["post"])
def search():
    return render_template()

if __name__ == '__main__':
    app.run()
