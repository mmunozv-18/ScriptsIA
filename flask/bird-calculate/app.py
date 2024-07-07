# app.py

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date1 = request.form.get('date1')
        date2 = request.form.get('date2')

        # Convertir las fechas a objetos datetime
        try:
            first_date = datetime.strptime(date1, '%Y-%m-%d')
            second_date = datetime.strptime(date2, '%Y-%m-%d')
            # Calcular la diferencia en días
            diff_days = abs((second_date - first_date).days)
            return render_template('index.html', difference=diff_days, date1=date1, date2=date2)
        except ValueError:
            return render_template('index.html', error='Por favor, ingresa fechas válidas.')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)