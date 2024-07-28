from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    wedding_date = datetime.datetime(2024, 11, 30, 16, 0)
    return render_template('index.html', wedding_date=wedding_date)

@app.route('/rsvp', methods=['POST'])
def rsvp():
    guest_name = request.form.get('name')
    guest_email = request.form.get('email')
    attending = request.form.get('attending')
    # Aquí podrías agregar el código para guardar la información en una base de datos.
    return "Gracias por confirmar tu asistencia."

if __name__ == '__main__':
    app.run(debug=True)
