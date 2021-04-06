from flask import Flask, render_template
from accessform import AccessForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    prof_list = [
        'Инженер-исследователь', 'Пилот', 'Строитель', 'Экзобиолог',
        'Врач', 'Инженер по терраформированию', 'Климатолог',
        'Специалист по радиационной защите', 'Астрогеолог', 'Гляциолог',
        'Инженер жизнеобеспечения', 'Метеоролог', 'Оператор марсохода',
        'Киберинженер', 'Штурман', 'Пилот дронов'
    ]
    return render_template('list_prof.html', list=list, prof_list=prof_list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {
        'title': 'Анкета',
        'surname': ('Фамилия:', 'Watny'),
        'name': ('Имя:', 'Mark'),
        'education': ('Образование:', 'выше среднего'),
        'profession': ('Профессия:', 'штурман марсохода'),
        'sex': ('Пол:', 'male'),
        'motivation': (
            'Мотивация:', 'Всегда мечтал застрять на Марсе!'
        ),
        'ready': ('Готовы остаться на Марсе?', 'True')
    }
    return render_template('auto_answer.html', param=param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AccessForm()
    if form.validate_on_submit():
        return "Доступ разрешен"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
