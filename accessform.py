from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AccessForm(FlaskForm):
    astronaut_id = StringField('ID астронавта', validators=[DataRequired(message='Необходимо выбрать значение')])
    astronaut_password = PasswordField('Пароль', validators=[DataRequired(message='Необходимо выбрать значение')])
    captain_id = StringField('ID капитана', validators=[DataRequired(message='Необходимо выбрать значение')])
    captain_password = PasswordField('Пароль', validators=[DataRequired(message='Необходимо выбрать значение')])
    submit = SubmitField('Доступ')
