#!/usr/bin/env python3
from flask import Flask, render_template, request, send_from_directory, flash, redirect
from werkzeug.exceptions import RequestEntityTooLarge
from time import time
from config import Config
from model import Model
from telegram import Bot
import os


app = Flask(__name__)
app.config.from_object(Config)
bot_owner_id = 275319916
bot_token = "925275676:AAG0SpykgoxkNu8O0YL28M8DVteAj9q_PU8"
bot = Bot(bot_token)


def clear(path) -> None:
    for item in os.listdir(path):
        p = f'{path}/{item}'
        now = time(); created = os.path.getmtime(p)
        if round(now - created) > 150: os.remove(p)


@app.route('/')
def index():
    return render_template('detector.html')


@app.route('/static/photos/out/<path:path>')
def send_image(path):
    return send_from_directory('static/photos/out', path)


@app.route('/', methods=['POST'])
def upload_file():
    try:
        f = request.files['file']
    except RequestEntityTooLarge:
        flash('File size too large.  Limit is 16 MB.')
        return redirect('/')
    model = Model()
    if f.filename != '':
        if f.content_type not in ('image/jpeg', 'image/jpg'):
            flash('Please resend the photo in the required format')
            return redirect('/')

        _, ext = os.path.splitext(f.filename)
        name = f'{round(time()*1000)}{ext}'
        path = f'static/photos/in/{name}'
        f.save(path)
        photo = open(f'static/photos/in/{name}', 'rb')
        caption = 'new detection from web app'
        bot.send_photo(bot_owner_id, photo, caption)
        res = model.getphoto(path)
        res.save('static/photos/out')
        for p in ['static/photos/in','static/photos/out']: clear(p)
        return render_template('detector.html', photo=name)

    return render_template('detector.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
