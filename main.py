import os
from flask import Flask, render_template, url_for
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        pass
    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
