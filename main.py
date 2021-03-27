import os
import requests
from flask import Flask, render_template, url_for, flash, redirect
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
API_URL = os.environ.get('API_URL')

headers = {
    'Authorization': os.environ.get('AUTHORIZATION')
}


def send_message(name, email, message):
    api_params = {
        'message': {
            'nume': name,
            'email': email,
            'mesaj': message
        }
    }

    response = requests.post(url=API_URL, json=api_params, headers=headers)
    print(requests)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        send_message(form.name.data, form.email.data, form.message.data)
        flash('Your message has been sent!')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
