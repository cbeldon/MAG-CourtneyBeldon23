from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'training-23'

class InvestmentForm(FlaskForm):
    returned_amount = DecimalField('Returned Amount', validators=[DataRequired()])
    invested_amount = DecimalField('Invested Amount', validators=[DataRequired()])
    submit = SubmitField('Calculate')

@app.route('/', methods=['GET', 'POST'])
def form():
    form = InvestmentForm()
    if form.validate_on_submit():
        return redirect(url_for('result', 
                                returned_amount=form.returned_amount.data, 
                                invested_amount=form.invested_amount.data))
    return render_template('form.html', form=form)

@app.route('/result')
def result():
    returned_amount = float(request.args.get('returned_amount'))
    invested_amount = float(request.args.get('invested_amount'))
    gain = returned_amount - invested_amount
    roi = (gain / invested_amount) * 100
    return render_template('result.html', gain=gain, roi=roi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
