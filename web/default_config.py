# -*- coding: utf-8 -*-
"""
cdeweb.default_config
~~~~~~~~~~~~~~~~~~~~~

Default configuration. Should be overridden when deployed.

"""

import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
SECRET_KEY = '4ef582f317d50e0c0c36a512aa45282c9259f4c1ac634cf2'
SQLALCHEMY_DATABASE_URI = 'postgresql://cetm:cetm@localhost/cetm'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
CELERY_RESULT_BACKEND = 'db+postgresql://cetm:cetm@localhost:5432/cetm'
CELERYD_TASK_TIME_LIMIT = 1000

UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'html', 'htm', 'xml', 'nxml', 'zip'}

RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'full'

OPSIN_PATH = '/usr/local/bin/opsin'
