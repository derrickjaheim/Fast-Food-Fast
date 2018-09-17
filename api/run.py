"""
This is the main module
"""
from flask import Flask
# from routes import GetUrls
from api.routes import GetUrls

APP = Flask(__name__)
APP.env = 'development'
APP.testing = True
GetUrls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)
