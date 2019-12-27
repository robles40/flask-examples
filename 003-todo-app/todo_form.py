from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('new todo', validators=[DataRequired()])
