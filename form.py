from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL, Regexp
from flask_wtf import FlaskForm


class Format(FlaskForm):
    cafe_name = StringField("Cafe Name", validators=[DataRequired()],)
    location = StringField("Cafe location on Google MAPS", validators=[URL(message="Please Enter Valid URL"),Regexp(regex=r"https\://.*/maps", message="Enter Valid Google MAPS URL") ])
    open_time = StringField("Open Time e.g. 8AM", validators=[DataRequired()])
    close_time = StringField("Close Time e.g. 4PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

