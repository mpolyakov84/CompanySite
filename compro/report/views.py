import os.path
from num2words import num2words
from babel.dates import format_date
from datetime import datetime, timedelta
from compro.report.forms import VacationForm
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from docxtpl import DocxTemplate
from compro.report.regex_handler import get_sub_address

report_bp = Blueprint('report', __name__, template_folder='templates')

@report_bp.route('/vacation', methods=['GET', 'POST'])
def vacation():
    form = VacationForm()

    if form.validate_on_submit():

        tpl_path = os.path.join(current_app.root_path, 'static\docs', 'vacation_tpl.docx')
        file_name = "Рапорт_відпуска_" + form.last_name.data + ".docx"
        gen_doc_path = os.path.join(current_app.root_path, 'static\docs\generated', file_name)
        fdoc = DocxTemplate(tpl_path)
        days_str = num2words(form.vacation_days.data, lang='uk')
        vacation_date_format = form.vacation_date.data.strftime('%d.%m.%Y')
        vacation_year = form.vacation_date.data.strftime('%Y')
        initials = form.last_name_mod.data.upper() + ' ' + form.first_name.data.upper()[0] +'.'\
                   + form.middle_name.data.upper()[0] + '.'
        if form.gender.data == 'male':
            gender = 'ий'
        else:
            gender = 'а'

        context = {'first_name': form.first_name.data.capitalize(), 'last_name': form.last_name.data.upper(), 'middle_name' : form.middle_name.data.capitalize(),
                   'initials': initials, 'vacation_date': vacation_date_format,
                   'vacation_days': form.vacation_days.data, 'day_for_trip': form.day_for_trip.data,
                   'address': form.address.data, 'telephone': form.telephone.data, 'days_str': days_str,
                   'vacation_year': vacation_year, 'gender': gender}
        fdoc.render(context)
        fdoc.save(gen_doc_path)

        # ticket
        tpl_ticket_path = os.path.join(current_app.root_path, 'static\docs', 'vacation_ticket_tpl.docx')
        ticket_file_name = 'Відпускний_квиток_' + form.last_name.data + '.docx'
        gen_ticket_doc_path = os.path.join(current_app.root_path, 'static\docs\generated', ticket_file_name)
        tdoc = DocxTemplate(tpl_ticket_path)

        sub_address = get_sub_address(form.address.data)
        vac_start_date = format_date(form.vacation_date.data,"dd MMMM YYYY", locale='uk_UA')

        if form.day_for_trip.data:
            shift_days = int(form.vacation_days.data) + 1
        else:
            shift_days = int(form.vacation_days.data)

        vac_end_date = format_date(form.vacation_date.data + timedelta(days=shift_days),"dd MMMM YYYY", locale='uk_UA')
        return_date = format_date(form.vacation_date.data + timedelta(days=shift_days+1),"dd MMMM YYYY", locale='uk_UA')

        initials_p = form.last_name.data.upper() + ' ' + form.first_name.data.upper()[0] + '.' \
                   + form.middle_name.data.upper()[0] + '.'

        ticket_context = {'first_name': form.first_name.data.capitalize(), 'last_name': form.last_name.data.upper(),
                          'middle_name': form.middle_name.data.capitalize(), 'vacation_days': form.vacation_days.data,
                          'initials': initials_p, 'vac_start_date': vac_start_date, 'vac_end_date': vac_end_date,
                          'return_date': return_date,'address': sub_address, 'telephone': form.telephone.data,
                          'days_str': days_str, 'vacation_year': vacation_year, 'gender': gender}
        tdoc.render(ticket_context)
        tdoc.save(gen_ticket_doc_path)

    return render_template('vacation_report.html', form=form)

