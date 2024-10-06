from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class VacationForm(FlaskForm):

    first_name = StringField("Ім'я: ", validators=[DataRequired()])
    last_name = StringField('Прізвище: ',validators=[DataRequired()])
    middle_name = StringField('По батокові: ', validators=[DataRequired()])
    last_name_mod = StringField('Прізвище в родовому відмінку(приклад - ПЕТРОВА): ', validators=[DataRequired()])
    vacation_date = DateField('Дата з якої починається відпуска:', validators=[DataRequired()])
    vacation_days = StringField('Кількість днів відпуски: ', validators=[DataRequired()])
    day_for_trip = BooleanField('Додатковий день на дорогу:   ')

    address = StringField('Адреса проведення відпуски: ', validators=[DataRequired()])
    # region = StringField('Область (наприклад - Запорізька): ', validators=[DataRequired()])
    # area = StringField("Район (наприклад Кам'янський): ")
    # city = StringField('Місто: ')
    # village = StringField('Cело: ')
    # street = StringField('Вулиця, будинок:', validators=[DataRequired()])

    telephone = StringField('Телефон: ', validators=[DataRequired()])
    gender = SelectField('Стать: ', choices=[('male', 'чоловіча'), ('female', 'жіноча')], validators=[DataRequired()])
    submit = SubmitField('Згенерувати документи')