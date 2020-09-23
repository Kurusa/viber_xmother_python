from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
import sched
import threading
import time
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
import sys

viber = Api(BotConfiguration(
    name='JuliasAssistant',
    avatar='https://i.ibb.co/vc2gJBZ/logo.jpg',
    auth_token='4ba564918267dcda-362581d3886b8e20-abfacb56f4b9717a'
))

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)

if not app.debug:
    if app.config['MAIL_SERVER']:
        """ auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Viber bot failure!!!',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler) """


def set_webhook(viber):
    try:
        viber.set_webhook("")
        time.sleep(1)
        url = 'https://limitless-river-20794.herokuapp.com/'
        viber.set_webhook(url)
    except:
        a = sys.exc_info()[1]
        if str(a) == 'failed with status: 999, message: DB Failure':
            pass
        else:
            raise


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(7, 1, set_webhook, (viber,))
t = threading.Thread(target=scheduler.run)
t.start()

from bot import model, views
