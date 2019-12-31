from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms import validators


class SearchForm(FlaskForm):
    type_field = SelectField('choose field', choices=[
        ('event_name', 'event_name'),
        ('event_date', 'event_date'),
    ])
    search_value = StringField("value: ", [validators.DataRequired('shouldnt be empty value')])

    submit = SubmitField("search")