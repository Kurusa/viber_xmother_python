import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgres://uzmiexwrpreqbe:46e884adcb785718e34d01e736169f9114cdf51fa22d3e0e1279acfd875d1fbf@ec2-34-225-162-157.compute-1.amazonaws.com:5432/daj9o43t3rqafd' or \
        'sqlite:///' + os.path.join(basedir, 'data.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = 'pawloiwanov@gmail.com'
