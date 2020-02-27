import smtplib
import time
import json

import requests
from bs4 import BeautifulSoup

with open('config.json') as config_file:
    config = json.load(config_file)
print(config)