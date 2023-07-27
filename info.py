import os
from os import environ

#Client Authorization
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

#DataBase Authorization
DATABASE_URI = environ.get("DATABASE_URI")
DATABASE_NAME = environ.get("DATABASE_NAME")

#other
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
