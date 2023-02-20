from flask import Flask, url_for, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def lest(list):
    professions = ['инженер-исследователь',
                   'пилот',
                   'строитель',
                   'экзобиолог',
                   'врач',
                   'инженер по терраформированию',
                   'климатолог',
                   'специалист по радиационной защите',
                   'астрогеолог',
                   'гляциолог',
                   'инженер жизнеобеспечения',
                   'метеоролог',
                   'оператор марсохода',
                   'киберинженер',
                   'штурман',
                   'пилот дронов']
    return render_template('list_prof.html', list=list, professions=professions)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
